/* ===== Dictionary: per-book glossary + SITE-WIDE fallback + shared dict + popover ===== */
(function(RG){
  const {el,stripStress,normRu}=RG.util;
  const deacc=s=>(s||'').normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
  let maps={}, loading={}, curBook=null, curMap=null, globalMap=null, allCache=null, initCache=null;
  const GENDER={m:'giống đực (м.р.)',f:'giống cái (ж.р.)',n:'giống trung (с.р.)'};
  const isZh=s=>/[㐀-鿿豈-﫿]/.test(s||'');

  function ensure(id){
    id=id||curBook;
    if(!id) return Promise.resolve(curMap||new Map());
    if(maps[id]){ curMap=maps[id]; return Promise.resolve(maps[id]); }
    if(loading[id]) return loading[id];
    loading[id]=RG.data.glossary(id).then(g=>{
      const m=new Map(); (g.entries||[]).forEach(e=>{ const k=normRu(e.ru); if(!m.has(k))m.set(k,e); });
      maps[id]=m; if(id===curBook)curMap=m; return m;
    }).catch(()=>{ maps[id]=new Map(); if(id===curBook)curMap=maps[id]; return maps[id]; });
    return loading[id];
  }
  // merge ALL loaded book glossaries + the shared Chinese-Vietnamese dict (built once, lazily)
  function buildGlobal(){
    if(globalMap) return globalMap;
    globalMap=new Map();
    const D=window.RG_DATA||{};
    for(const k in D){
      if(k.lastIndexOf('glossary:',0)===0 && D[k] && D[k].entries)
        D[k].entries.forEach(e=>{ const kk=normRu(e.ru); if(kk&&!globalMap.has(kk)) globalMap.set(kk,e); });
    }
    for(const dk in D){
      if(dk.lastIndexOf('dict:',0)!==0) continue;
      const big=D[dk], dn=dk.slice(5);
      for(const w in big){ const kk=normRu(w);
        if(!globalMap.has(kk)){ const p=String(big[w]).split('\t');
          globalMap.set(kk,{ru:w,ruPlain:w,py:p[0]||'',hv:p[1]||'',vi:(p.length>=3?p[2]:p[0])||'',ref:(p[3]||''),shared:true,dict:dn}); } }
    }
    return globalMap;
  }
  // resolve: current book -> all books -> shared dict -> per-character compose (Chinese)
  function resolve(word){
    const k=normRu(word);
    let e=(curMap&&curMap.get(k)); if(e) return Object.assign({src:'sách này'},e);
    e=buildGlobal().get(k); if(e){ const lbl=e.dict==='ru-vi'?'từ điển Nga–Việt':e.dict==='zh-vi'?'từ điển Trung–Việt':'từ điển'; return Object.assign({src:e.shared?lbl:'sách khác'},e); }
    if(isZh(word) && word.length>=2){
      const G=buildGlobal(); const parts=[], pys=[]; let i=0, hit=0;
      while(i<word.length){
        let m=null;
        for(let l=Math.min(6,word.length-i); l>=1; l--){ const sub=word.substr(i,l); const c=G.get(normRu(sub)); if(c){m={w:sub,c:c,l:l};break;} }
        if(m){ hit++; parts.push(m.w+' '+((m.c.vi||'').split(/[|;]/)[0].trim()||'?')); if(m.c.py)pys.push(m.c.py); i+=m.l; }
        else { parts.push(word[i]+' ?'); i+=1; }
      }
      if(hit) return {ru:word,ruPlain:word,py:pys.join(' '),vi:parts.join(' · '),src:'tách từ',composed:true};
    }
    return null;
  }
  function externals(term){
    const t=stripStress(term).trim(); const w=encodeURIComponent(t);
    if(isZh(t)){
      const qz=encodeURIComponent('nghĩa, pinyin và cách dùng của từ "'+t+'" trong tiếng Trung');
      return [{label:'Google',icon:'🔍',url:'https://www.google.com/search?q='+qz},
        {label:'Hanzii',icon:'📕',url:'https://hanzii.net/search/word/'+w+'?hl=vi'},
        {label:'Wiktionary',icon:'📘',url:'https://en.wiktionary.org/wiki/'+w},
        {label:'YouGlish',icon:'🎬',url:'https://youglish.com/pronounce/'+w+'/chinese'}];
    }
    const q=encodeURIComponent('nghĩa và cách dùng của từ "'+t+'" trong tiếng Nga');
    return [{label:'Google',icon:'🔍',url:'https://www.google.com/search?q='+q},
      {label:'Wiktionary',icon:'📘',url:'https://ru.wiktionary.org/wiki/'+w},
      {label:'Nga–Việt',icon:'🇷🇺',url:'https://vtudien.com/nga-viet/dictionary/nghia-cua-tu-'+w},
      {label:'YouGlish',icon:'🎬',url:'https://youglish.com/pronounce/'+w+'/russian'}];
  }
  function open(url){ try{ window.open(url,'_blank','noopener'); }catch(e){ location.href=url; } }
  function linkRow(term, after){
    const row=el('div',{class:'plinks'});
    externals(term).forEach(l=>row.appendChild(el('button',{class:'plink',title:l.label,
      onclick:e=>{e.stopPropagation();open(l.url);after&&after();}}, l.icon+' '+l.label)));
    return row;
  }
  // Tra tự động online (CORS) cho từ không có trong từ điển: Google Dịch -> MyMemory, có cache
  async function online(term){
    term=stripStress(term).trim(); if(!term) return null;
    const lang=isZh(term)?'zh-CN':'ru';
    const ck='rg.tr.'+lang+'.'+term;
    try{ const c=localStorage.getItem(ck); if(c) return JSON.parse(c); }catch(e){}
    let res=null;
    try{
      const u='https://translate.googleapis.com/translate_a/single?client=gtx&sl='+lang+'&tl=vi&dt=t&q='+encodeURIComponent(term);
      const r=await fetch(u); if(r.ok){ const j=await r.json(); const t=((j[0]||[]).map(x=>x&&x[0]).filter(Boolean).join('')).trim(); if(t && t.toLowerCase()!==term.toLowerCase()) res={vi:t,src:'Google Dịch'}; }
    }catch(e){}
    if(!res){ try{
      const u='https://api.mymemory.translated.net/get?q='+encodeURIComponent(term)+'&langpair='+lang+'|vi';
      const r=await fetch(u); if(r.ok){ const j=await r.json(); const t=j&&j.responseData&&j.responseData.translatedText; if(t) res={vi:t.trim(),src:'MyMemory'}; }
    }catch(e){} }
    if(res){ try{ localStorage.setItem(ck,JSON.stringify(res)); }catch(e){} }
    return res;
  }
  RG.dict={
    setBook(id){ curBook=id; if(maps[id])curMap=maps[id]; else ensure(id); },
    ready(){ return ensure(curBook); },
    map:()=>curMap, externals, linkRow, open, resolve, online,
    resetGlobal(){ globalMap=null; allCache=null; initCache=null; },
    dictCount(){ return buildGlobal().size; },
    initials(){ if(initCache) return initCache; const set=new Set();
      for(const e of RG.dict.allEntries()) set.add(RG.dict.initial(e));
      initCache=Array.from(set).sort((a,b)=>a==='#'?1:b==='#'?-1:(a<b?-1:1)); return initCache; },
    allEntries(){ if(allCache) return allCache; const G=buildGlobal(); allCache=Array.from(G.values());
      allCache.sort((a,b)=>{ const ka=deacc(a.py)||a.ru||'', kb=deacc(b.py)||b.ru||''; return ka<kb?-1:ka>kb?1:0; }); return allCache; },
    initial(e){ const k=deacc(e.py)||(e.ru||'').toLowerCase(); const c=(k[0]||''); return /[a-zа-яё]/.test(c)?c:'#'; },
    searchAll(query, limit){ limit=limit||400; const q=normRu(query); const out=[]; if(!q) return out;
      const G=buildGlobal();
      for(const e of G.values()){ if(normRu(e.ru).indexOf(q)>=0 || (e.vi&&e.vi.toLowerCase().indexOf(query.toLowerCase())>=0)){ out.push(e); if(out.length>=limit) break; } }
      return out; },
    lookup(word){ const e=(curMap&&curMap.get(normRu(word))); return e||buildGlobal().get(normRu(word))||null; },
    showFor(word, anchor){
      ensure(curBook).then(()=>{
        hide();
        const k=normRu(word), e=resolve(word);
        const say=(e&&stripStress(e.ru))||stripStress(word);
        const pop=el('div',{class:'popover',id:'rg-pop'});
        pop.appendChild(el('div',{class:'pw'},
          el('span',{class:isZh(word)?'zh':'ru-text'}, (e&&e.ru)||word),
          el('button',{class:'play',title:'Nghe',onclick:ev=>{ev.stopPropagation();RG.tts.speak(say);}},'🔊')));
        if(e){
          const sub=e.py || (e.g?GENDER[e.g]:'');
          if(sub) pop.appendChild(el('div',{class:'px'}, sub));
          pop.appendChild(el('div',{class:'pm'}, e.vi||''));
          if(e.hv) pop.appendChild(el('div',{class:'px'}, 'Hán Việt: '+e.hv));
          if(e.ref && e.shared && !/-s\d/.test(e.ref) && RG.util.normRu(e.ref)!==k){ const rf=el('div',{class:'dref'},'↔ Liên quan: ');
            const a=el('span',{class:(isZh(e.ref)?'zh':'ru-text'),style:'cursor:pointer;color:var(--ru);font-weight:600'}, e.ref);
            a.addEventListener('click',ev=>{ev.stopPropagation();RG.dict.showFor(e.ref,anchor);});
            rf.appendChild(a); pop.appendChild(rf); }
          if(e.src) pop.appendChild(el('div',{class:'dsrc'}, '· '+e.src));
        }
        const row=el('div',{class:'row'},
          el('button',{class:'btn sm',onclick:ev=>{ev.stopPropagation();RG.tts.speak(say);}},'🔊 Nghe'),
          el('button',{class:'btn sm',onclick:ev=>{ev.stopPropagation();RG.store.grade(k,true);RG.util.toast('Đã thêm vào flashcard');}},'➕ Lưu thẻ'));
        if(RG.hanzi && isZh(word)) row.appendChild(el('button',{class:'btn sm primary',onclick:ev=>{ev.stopPropagation();hide();RG.hanzi.show(word);}},'✍️ Cách viết'));
        pop.appendChild(row);
        if(!e || e.composed || !e.vi){
          const od=el('div',{class:'donline'}); pop.appendChild(od);
          const run=()=>{ od.innerHTML=''; od.appendChild(el('div',{class:'px'},'🌐 Đang tra online…'));
            online(word).then(r=>{ od.innerHTML='';
              if(r){ od.appendChild(el('div',{class:'pm'}, (e&&e.composed?'Cả cụm: ':'')+r.vi));
                     od.appendChild(el('div',{class:'dsrc'}, '· '+r.src+' (tự động online)')); }
              else if(!e) od.appendChild(el('div',{class:'miss'},'Chưa có trong từ điển; chưa tra được online (cần mạng) — dùng nguồn dưới.')); });
          };
          if(RG.store.settings().autoOnline!==false) run();
          else od.appendChild(el('button',{class:'btn sm',onclick:ev=>{ev.stopPropagation();run();}},'🌐 Tra nghĩa online'));
        }
        pop.appendChild(linkRow((e&&e.ru)||word, hide));
        document.body.appendChild(pop); position(pop, anchor);
        setTimeout(()=>document.addEventListener('mousedown',outside),0);
      });
    },
    hide
  };
  function position(pop, anchor){
    const r=anchor.getBoundingClientRect(), pw=pop.offsetWidth, ph=pop.offsetHeight;
    let x=window.scrollX+r.left, y=window.scrollY+r.bottom+8;
    if(x+pw>window.scrollX+innerWidth-12) x=window.scrollX+innerWidth-pw-12;
    if(r.bottom+ph+12>innerHeight) y=window.scrollY+r.top-ph-8;
    pop.style.left=Math.max(8,x)+'px'; pop.style.top=y+'px';
  }
  function hide(){ const p=document.getElementById('rg-pop'); if(p)p.remove(); document.removeEventListener('mousedown',outside); }
  function outside(e){ const p=document.getElementById('rg-pop'); if(p&&!p.contains(e.target)&&!e.target.classList.contains('ru')&&!e.target.classList.contains('zh')) hide(); }
})(window.RG);
