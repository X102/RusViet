/* ===== App: multi-book router, navigation, views ===== */
(function(RG){
  const {$,$$,el,esc}=RG.util;
  const A=RG.app={lib:null, book:null, bookId:null};
  const SITE=Object.assign({lang:'ru',name:'RusViet',sub:'Học tiếng Nga',logo:'Я',
    langName:'tiếng Nga',langShort:'Nga',title:null,test:'Здравствуйте! Я говорю по-русски.'}, window.SITE||{});

  function applyTheme(){ document.documentElement.setAttribute('data-theme',RG.store.settings().theme); }
  function go(hash){ location.hash=hash; }
  function loadBook(id){
    return RG.data.book(id).then(b=>{ A.bookId=id; A.book=b; RG.dict.setBook&&RG.dict.setBook(id); return b; });
  }
  function partProgress(p){ const done=RG.store.doneCount(p.sectionPrefix||(String(p.num).padStart(2,'0')+'-s'));
    return {done, total:p.sectionCount, pct:p.sectionCount?Math.round(done/p.sectionCount*100):0}; }

  /* ---------- sidebar ---------- */
  function buildSidebar(bookId){
    const sb=$('#sidebar'); sb.innerHTML='';
    sb.appendChild(el('div',{class:'brand',onclick:()=>go('#/')},
      el('div',{class:'logo'},SITE.logo),
      el('div',{}, el('b',{},SITE.name), el('span',{},SITE.sub))));
    const h=location.hash;
    const nav=(icon,label,hash,active,count)=>el('div',{class:'nav-item'+(active?' active':''),onclick:()=>go(hash)},
      el('div',{class:'ic'},icon), el('div',{},label), count!=null?el('div',{class:'count'},count):null);

    if(!bookId || !A.book){
      sb.appendChild(el('div',{class:'nav-group-title'},'Thư viện'));
      sb.appendChild(nav('🏠','Trang chủ','#/', h===''||h==='#/'));
      (A.lib?A.lib.books:[]).forEach(b=>sb.appendChild(nav(b.cover||'📘', b.title, '#/book/'+b.id, h.includes('/'+b.id))));
      return;
    }
    const b=A.book;
    sb.appendChild(el('div',{class:'nav-item',onclick:()=>go('#/')},
      el('div',{class:'ic'},'📚'), el('div',{},'Thư viện')));
    sb.appendChild(el('div',{class:'nav-group-title'}, b.title));
    sb.appendChild(nav(b.cover||'📖','Tổng quan sách','#/book/'+bookId, h==='#/book/'+bookId));
    let lastGroup=null;
    b.parts.forEach(p=>{
      if(p.group && p.group!==lastGroup){ sb.appendChild(el('div',{class:'nav-group-title'},p.group)); lastGroup=p.group; }
      const pr=partProgress(p);
      sb.appendChild(nav(p.icon, p.vi, '#/unit/'+bookId+'/'+p.id,
        h.includes('/'+bookId+'/'+p.id), `${pr.done}/${pr.total}`));
    });
    sb.appendChild(el('div',{class:'nav-group-title'},'Công cụ'));
    sb.appendChild(nav('🃏','Flashcard','#/flashcards/'+bookId, h==='#/flashcards/'+bookId));
    sb.appendChild(nav('📚','Từ điển','#/dictionary/'+bookId, h==='#/dictionary/'+bookId));
    sb.appendChild(nav('🔎','Tìm kiếm','#/search/'+bookId, h==='#/search/'+bookId));
    sb.appendChild(nav('⭐','Đã lưu','#/bookmarks/'+bookId, h==='#/bookmarks/'+bookId));
  }

  /* ---------- topbar ---------- */
  let curTitle='';
  function buildTopbar(title){
    curTitle=title||''; const tb=$('#topbar'); tb.innerHTML='';
    tb.appendChild(el('button',{class:'btn icon menu-btn',onclick:()=>{$('#sidebar').classList.toggle('open');$('#scrim').classList.toggle('show');}},'☰'));
    tb.appendChild(el('div',{style:'font-weight:700;font-size:15px'},title||''));
    tb.appendChild(el('div',{class:'spacer'}));
    if(!RG.tts.hasRussian) tb.appendChild(el('button',{class:'btn sm ghost',title:'Chưa có giọng tiếng Nga',onclick:openDrawer},'🔈 Giọng '+SITE.langShort+'?'));
    tb.appendChild(el('button',{class:'btn icon',title:'Sáng/Tối',onclick:()=>{
      const s=RG.store.settings(); RG.store.setSetting('theme',s.theme==='dark'?'light':'dark'); applyTheme(); buildTopbar(curTitle);
    }}, RG.store.settings().theme==='dark'?'☀️':'🌙'));
    tb.appendChild(el('button',{class:'btn icon',title:'Cài đặt',onclick:openDrawer},'⚙️'));
  }
  function statCard(n,l){ return el('div',{class:'stat'},el('div',{class:'n'},String(n)),el('div',{class:'l'},l)); }

  /* ---------- LIBRARY (home) ---------- */
  function viewLibrary(view){
    buildTopbar('Thư viện'); view.innerHTML='';
    const hero=el('div',{class:'card',style:'cursor:default;background:linear-gradient(135deg,var(--brand),var(--accent));color:#fff;border:none'});
    hero.appendChild(el('div',{class:'emoji'},'📚'));
    hero.appendChild(el('h3',{style:'font-size:22px;color:#fff'}, A.lib?A.lib.title:'Thư viện tiếng Nga'));
    hero.appendChild(el('p',{style:'color:#ffffffdd'},'Chọn một cuốn sách để bắt đầu. Mọi từ tiếng Nga đều bấm được để nghe và tra nghĩa.'));
    view.appendChild(hero);

    const recent=RG.store.state.recent;
    if(recent&&recent.length){
      view.appendChild(el('h2',{class:'sec'},'⏩ Học tiếp'));
      const g=el('div',{class:'grid cols'});
      recent.slice(0,3).forEach(r=>{ const c=el('div',{class:'card',onclick:()=>go(r.hash)});
        c.appendChild(el('div',{class:'tag'}, r.bookVi||r.partVi||'Bài'));
        c.appendChild(el('h3',{},r.title)); g.appendChild(c); });
      view.appendChild(g);
    }

    const books=A.lib?A.lib.books:[];
    const GROUPS=[['grammar','📚 Giáo trình & Ngữ pháp'],['textbook','📚 Giáo trình & Ngữ pháp'],['reader','📖 Truyện & Văn học']];
    const order=[['grammar','textbook'],['reader'],['__other__']];
    const labels={g0:'📚 Giáo trình & Ngữ pháp', g1:'📖 Truyện & Văn học', g2:'📦 Khác'};
    const holders={};
    order.forEach((types,gi)=>{ const h=el('h2',{class:'sec'}, labels['g'+gi]); const g=el('div',{class:'grid cols'});
      view.appendChild(h); view.appendChild(g); holders[gi]={h,g,n:0}; });
    function bucket(t){ if(t==='grammar'||t==='textbook')return 0; if(t==='reader')return 1; return 2; }
    Promise.all(books.map(b=>RG.data.book(b.id).catch(()=>null))).then(loaded=>{
      books.forEach((meta,i)=>{
        const b=loaded[i]; const bi=bucket(meta.type);
        const c=el('div',{class:'card book',onclick:()=>go('#/book/'+meta.id)});
        c.appendChild(el('div',{class:'cover'}, meta.cover||'📘'));
        c.appendChild(el('h3',{}, meta.title));
        c.appendChild(el('p',{}, meta.subtitle||''));
        if(meta.level||(b&&b.level)) c.appendChild(el('span',{class:'tag'}, meta.level||b.level));
        if(b){
          const total=b.parts.reduce((s,p)=>s+p.sectionCount,0);
          const done=b.parts.reduce((s,p)=>s+RG.store.doneCount(p.sectionPrefix||(String(p.num).padStart(2,'0')+'-s')),0);
          c.appendChild(el('div',{class:'muted',style:'font-size:12.5px;margin-top:8px'},
            `${b.parts.length} chương · ${total} bài`));
          const bar=el('div',{class:'bar'}); bar.appendChild(el('i',{style:`width:${total?Math.round(done/total*100):0}%`})); c.appendChild(bar);
        }
        holders[bi].g.appendChild(c); holders[bi].n++;
      });
      Object.values(holders).forEach(o=>{ if(!o.n){ o.h.remove(); o.g.remove(); } });
    });

    if(A.lib&&A.lib.comingSoon){
      view.appendChild(el('h2',{class:'sec'},'🚀 Sắp ra mắt'));
      const g2=el('div',{class:'grid cols'});
      A.lib.comingSoon.forEach(s=>{ const c=el('div',{class:'card soon'});
        c.appendChild(el('div',{class:'emoji'},s.cover)); c.appendChild(el('h3',{},s.title));
        c.appendChild(el('span',{class:'tag soon'},'Sắp có')); g2.appendChild(c); });
      view.appendChild(g2);
    }
  }

  /* ---------- BOOK overview ---------- */
  function viewBook(view, bookId){
    const b=A.book; buildTopbar(b.title); view.innerHTML='';
    view.appendChild(el('div',{class:'crumb'}, el('b',{onclick:()=>go('#/')},'Thư viện'),' / '+b.title));
    view.appendChild(el('h1',{class:'page-title'}, `${b.cover||'📘'} ${b.title}`));
    view.appendChild(el('p',{class:'page-sub'}, b.description||b.subtitle||''));
    const total=b.parts.reduce((s,p)=>s+p.sectionCount,0);
    const done=b.parts.reduce((s,p)=>s+RG.store.doneCount(p.sectionPrefix||(String(p.num).padStart(2,'0')+'-s')),0);
    view.appendChild(el('div',{class:'stats'},
      statCard(b.parts.length,'Chương'), statCard(total,'Bài học'),
      statCard(done,'Đã hoàn thành'), statCard(Object.keys(RG.store.srs()).length,'Thẻ ôn')));
    view.appendChild(el('h2',{class:'sec'},'📖 Mục lục'));
    let lastG=null, grid=null;
    b.parts.forEach(p=>{
      if((p.group||'')!==lastG){ lastG=p.group||'';
        if(lastG) view.appendChild(el('div',{class:'group-head'}, lastG));
        grid=el('div',{class:'grid cols'}); view.appendChild(grid); }
      const pr=partProgress(p);
      const c=el('div',{class:'card unit',onclick:()=>go('#/unit/'+bookId+'/'+p.id)});
      c.appendChild(el('div',{class:'stripe',style:`background:${p.color}`}));
      c.appendChild(el('div',{class:'emoji'},p.icon));
      c.appendChild(el('h3',{}, p.vi));
      c.appendChild(el('p',{}, (p.ru||'')+(p.exerciseCount?(' · '+p.exerciseCount+' bài tập'):'')));
      const bar=el('div',{class:'bar'}); bar.appendChild(el('i',{style:`width:${pr.pct}%`})); c.appendChild(bar);
      grid.appendChild(c);
    });
  }

  /* ---------- UNIT (section list) ---------- */
  function viewUnit(view, bookId, unitId){
    const part=A.book.parts.find(p=>p.id===unitId);
    if(!part){ go('#/book/'+bookId); return; }
    buildTopbar(part.vi); view.innerHTML='';
    view.appendChild(el('div',{class:'crumb'},
      el('b',{onclick:()=>go('#/')},'Thư viện'),' / ',
      el('b',{onclick:()=>go('#/book/'+bookId)},A.book.title),' / '+part.vi));
    view.appendChild(el('h1',{class:'page-title'},`${part.icon} ${part.vi}`));
    view.appendChild(el('p',{class:'page-sub'},`${part.ru} — ${part.sectionCount} mục (${part.exerciseCount} bài tập)`));
    view.appendChild(el('div',{class:'empty'},el('div',{class:'e'},'⏳'),'Đang tải…'));
    RG.data.unit(unitId,bookId).then(u=>{
      view.querySelector('.empty').remove();
      const list=el('div',{class:'sec-list'}); view.appendChild(list);
      u.sections.forEach(s=>{
        const isEx=s.type==='exercise';
        const done=RG.store.isDone(s.id), bm=RG.store.isBookmarked(s.id);
        const row=el('div',{class:'sec-row '+(isEx?'':'grammar'),onclick:()=>go('#/section/'+bookId+'/'+unitId+'/'+s.id)});
        row.appendChild(el('div',{class:'num'}, isEx?(s.num||'•'):'📘'));
        const ti=el('div',{class:'ti'}); ti.appendChild(el('b',{},s.title));
        ti.appendChild(el('small',{}, isEx?'Bài tập':'Lý thuyết / ghi chú'));
        row.appendChild(ti);
        row.appendChild(el('div',{class:'state'}, (bm?'⭐':'')+(done?' ✅':'')));
        list.appendChild(row);
      });
    });
  }

  /* ---------- SECTION (reader) ---------- */
  function viewSection(view, bookId, unitId, secId){
    RG.data.unit(unitId,bookId).then(u=>{
      const part=A.book.parts.find(p=>p.id===unitId);
      const idx=u.sections.findIndex(s=>s.id===secId); const s=u.sections[idx];
      if(!s){ go('#/unit/'+bookId+'/'+unitId); return; }
      buildTopbar(part.vi);
      RG.store.pushRecent({id:secId,hash:'#/section/'+bookId+'/'+unitId+'/'+secId,title:s.title,partVi:part.vi,bookVi:A.book.title});
      view.innerHTML='';
      view.appendChild(el('div',{class:'crumb'},
        el('b',{onclick:()=>go('#/')},'Thư viện'),' / ',
        el('b',{onclick:()=>go('#/book/'+bookId)},A.book.title),' / ',
        el('b',{onclick:()=>go('#/unit/'+bookId+'/'+unitId)},part.vi),' / '+s.title.split('(')[0]));
      view.appendChild(el('div',{class:'reader-head'},
        el('span',{class:'badge'}, s.type==='exercise'?('Bài '+(s.num||'')):'Ngữ pháp'),
        el('h1',{class:'page-title',style:'margin:0'}, s.title)));

      const tools=el('div',{class:'reader-tools'});
      const doneBtn=el('button',{class:'btn sm'+(RG.store.isDone(s.id)?' ok':''),onclick:()=>{
        const d=RG.store.toggleDone(s.id); doneBtn.classList.toggle('ok',d);
        doneBtn.firstChild.textContent=d?'✅ Đã hoàn thành':'☑️ Đánh dấu hoàn thành'; buildSidebar(bookId);
      }}, RG.store.isDone(s.id)?'✅ Đã hoàn thành':'☑️ Đánh dấu hoàn thành');
      const bmBtn=el('button',{class:'btn sm'+(RG.store.isBookmarked(s.id)?' toggle-on':''),onclick:()=>{
        const v=RG.store.toggleBookmark(s.id); bmBtn.classList.toggle('toggle-on',v);
        bmBtn.firstChild.textContent=v?'⭐ Đã lưu':'☆ Lưu'; }}, RG.store.isBookmarked(s.id)?'⭐ Đã lưu':'☆ Lưu');
      tools.appendChild(doneBtn); tools.appendChild(bmBtn);
      const body=el('div',{class:'sec-body'}); body.style.fontSize=(RG.store.settings().fontSize||17)+'px';
      tools.appendChild(el('button',{class:'btn sm primary',onclick:()=>RG.player.start(body)},'🎧 Nghe cả bài'));
      if(s.type==='exercise') tools.appendChild(RG.ex.quizToggle(body));
      tools.appendChild(el('button',{class:'btn sm',onclick:()=>{RG.tts.stop();RG.player.stop&&RG.player.stop();}},'⏹ Dừng đọc'));
      tools.appendChild(el('button',{class:'btn sm',onclick:()=>RG.hl.clear(body,s.id)},'🧽 Xoá tô màu'));
      view.appendChild(tools);

      RG.dict.ready();
      RG.render.blocks(s.blocks, body); view.appendChild(body);
      RG.hl.attach(body,s.id);
      if(s.type==='exercise'){
        const panel=el('div',{class:'study'}); view.appendChild(panel);
        let theory=null; for(let i=idx-1;i>=0;i--){ if(u.sections[i].type!=='exercise'){ theory=u.sections[i]; break; } }
        if(theory) panel.appendChild(el('button',{class:'btn sm',onclick:()=>go('#/section/'+bookId+'/'+unitId+'/'+theory.id)},'📖 Lý thuyết & giải thích'));
        RG.data.answers(bookId).then(map=>{
          const a=(map&&map.answers&&s.num)?map.answers[s.num]:null;
          if(a){ const ab=el('div',{class:'answer-body'}); ab.appendChild(RG.render.rich(trimAnswer(a, exItemCount(s))));
            const btn=el('button',{class:'btn sm',onclick:()=>{const open=ab.classList.toggle('show');btn.firstChild.textContent=open?'🙈 Ẩn đáp án':'🔑 Xem đáp án';}},'🔑 Xem đáp án');
            panel.appendChild(btn); panel.appendChild(ab);
          } else note();
        }).catch(note);
        function note(){ if(!panel.querySelector('.study-note')) panel.appendChild(el('div',{class:'study-note'},'💡 Đây là bài giải mẫu — đáp án và giải nghĩa nằm ngay trong nội dung phía trên. Hãy tự làm rồi đối chiếu.')); }
      }

      const notes=el('div',{class:'notes'});
      notes.appendChild(el('label',{style:'font-weight:700;display:block;margin-bottom:8px'},'📝 Ghi chú của bạn'));
      const ta=el('textarea',{placeholder:'Viết ghi chú, mẹo nhớ…'}); ta.value=RG.store.getNote(s.id);
      ta.addEventListener('input',RG.util.debounce(()=>RG.store.setNote(s.id,ta.value.trim()),400));
      notes.appendChild(ta); view.appendChild(notes);

      const pager=el('div',{class:'pager'});
      pager.appendChild(idx>0?el('button',{class:'btn',onclick:()=>go('#/section/'+bookId+'/'+unitId+'/'+u.sections[idx-1].id)},'← Bài trước'):el('span'));
      pager.appendChild(idx<u.sections.length-1?el('button',{class:'btn primary',onclick:()=>go('#/section/'+bookId+'/'+unitId+'/'+u.sections[idx+1].id)},'Bài tiếp →'):el('span'));
      view.appendChild(pager);
      window.scrollTo(0,0);
    });
  }

  /* ---------- DICTIONARY ---------- */
  function viewDictionary(view, bookId){
    buildTopbar('Từ điển'); view.innerHTML='';
    view.appendChild(el('h1',{class:'page-title'},'📚 Từ điển'));
    const dc=(RG.dict.dictCount&&RG.dict.dictCount())||0;
    view.appendChild(el('p',{class:'page-sub'},'Đọc từ điển cũng là cách học từ. Chuyển nguồn, lọc theo chữ cái hoặc gõ tìm; bấm 🔊 để nghe, bấm từ để xem chi tiết.'));
    const box=el('div',{class:'search-box'},el('span',{},'🔎'),el('input',{type:'search',placeholder:(SITE.lang==='zh'?'Tìm theo chữ Hán, pinyin hoặc nghĩa tiếng Việt…':'Tìm theo từ tiếng Nga hoặc nghĩa tiếng Việt…')}));
    view.appendChild(box);
    const chips=el('div',{class:'chips'}); view.appendChild(chips);
    const az=el('div',{class:'chips',style:'gap:6px'}); view.appendChild(az);
    const out=el('div',{style:'margin-top:8px'}); view.appendChild(out);
    const more=el('div',{style:'text-align:center;margin:16px 0'}); view.appendChild(more);
    let mode=(dc>0?'all':'book'), letter='', shown=0; const PAGE=200;
    RG.data.glossary(bookId).then(g=>{
      const bookE=g.entries||[];
      function curList(){
        const raw=box.querySelector('input').value.trim();
        if(raw) return RG.dict.searchAll? (mode==='book'
            ? bookE.filter(e=>RG.util.normRu(e.ru).includes(RG.util.normRu(raw))||(e.vi||'').toLowerCase().includes(raw.toLowerCase()))
            : RG.dict.searchAll(raw,5000)) : bookE;
        let arr = mode==='book'? bookE : RG.dict.allEntries();
        if(mode==='all'&&letter) arr=arr.filter(e=>RG.dict.initial(e)===letter);
        return arr;
      }
      function card(e){ const v=el('div',{class:'vocab'});
        if(e.g) v.appendChild(el('div',{class:'g g-'+e.g},e.g.toUpperCase()));
        const w=el('div',{class:'w'}); const r=el('div',{class:(RG.util.hasZh(e.ru)?'r zh':'r ru-text')},e.ru);
        r.addEventListener('click',()=>RG.dict.showFor(e.ru,r));
        w.appendChild(r); if(e.py) w.appendChild(el('div',{class:'py'},e.py)); w.appendChild(el('div',{class:'m'},e.vi||'')); v.appendChild(w);
        v.appendChild(el('button',{class:'play',onclick:()=>RG.tts.speak(RG.util.stripStress(e.ru))},'🔊')); return v; }
      function paint(reset){
        const list=curList();
        if(reset){ shown=0; out.innerHTML=''; out._grid=null;
          out.appendChild(el('div',{class:'muted',style:'margin-bottom:10px'}, list.length.toLocaleString('vi')+' từ'+(mode==='all'&&!box.querySelector('input').value?' · toàn bộ từ điển':' trong nguồn này'))); }
        let grid=out._grid; if(!grid){ grid=el('div',{class:'vocab-list'}); out.appendChild(grid); out._grid=grid; }
        const next=list.slice(shown,shown+PAGE); next.forEach(e=>grid.appendChild(card(e))); shown+=next.length;
        more.innerHTML='';
        if(shown<list.length) more.appendChild(el('button',{class:'btn',onclick:()=>paint(false)},'Tải thêm ('+(list.length-shown).toLocaleString('vi')+' từ nữa)'));
      }
      function rebuildChips(){
        chips.innerHTML='';
        chips.appendChild(el('div',{class:'chip'+(mode==='book'?' on':''),onclick:()=>{mode='book';letter='';rebuildChips();paint(true);}},'📕 '+A.book.title));
        if(dc>0) chips.appendChild(el('div',{class:'chip'+(mode==='all'?' on':''),onclick:()=>{mode='all';rebuildChips();paint(true);}},'🌐 Toàn bộ từ điển ('+dc.toLocaleString('vi')+')'));
        az.style.display = mode==='all' ? 'flex':'none';
        if(mode==='all'&&!az.childNodes.length){
          (RG.dict.initials?RG.dict.initials():['#']).forEach(L=>az.appendChild(
            el('div',{class:'chip',style:'padding:5px 9px',onclick:()=>{letter=(letter===L?'':L);
              [...az.children].forEach(c=>c.classList.toggle('on',c.textContent===L&&letter===L)); box.querySelector('input').value=''; paint(true);}}, L.toUpperCase())));
        }
      }
      box.querySelector('input').addEventListener('input',RG.util.debounce(()=>{letter='';[...az.children].forEach(c=>c.classList.remove('on'));paint(true);},180));
      rebuildChips(); paint(true);
    });
  }
  function viewBookmarks(view, bookId){
    buildTopbar('Đã lưu'); view.innerHTML='';
    view.appendChild(el('h1',{class:'page-title'},'⭐ Đã lưu & Ghi chú'));
    view.appendChild(el('p',{class:'page-sub'},'Trong sách: '+A.book.title));
    Promise.all(A.book.parts.map(p=>RG.data.unit(p.id,bookId))).then(units=>{
      const find=id=>{ for(const u of units){ const s=u.sections.find(x=>x.id===id); if(s)return{u,s}; } return null; };
      const ids=Array.from(new Set([...RG.store.bookmarks(),...RG.store.notedSections()]));
      const mine=ids.map(find).filter(Boolean);
      if(!mine.length){ view.appendChild(el('div',{class:'empty'},el('div',{class:'e'},'⭐'),'Chưa có gì được lưu trong sách này.')); return; }
      const list=el('div',{class:'sec-list'});
      mine.forEach(f=>{ const row=el('div',{class:'sec-row',onclick:()=>go('#/section/'+bookId+'/'+f.u.id+'/'+f.s.id)});
        row.appendChild(el('div',{class:'num'},f.u.icon));
        const ti=el('div',{class:'ti'}); ti.appendChild(el('b',{},f.s.title));
        ti.appendChild(el('small',{}, f.u.vi+(RG.store.getNote(f.s.id)?' · có ghi chú 📝':'')));
        row.appendChild(ti);
        row.appendChild(el('div',{class:'state'}, (RG.store.isBookmarked(f.s.id)?'⭐':'')+(RG.store.isDone(f.s.id)?' ✅':'')));
        list.appendChild(row); });
      view.appendChild(list);
    });
  }

  /* ---------- settings drawer ---------- */
  function field(label,ctrl){ return el('div',{class:'field'},el('label',{},label),ctrl); }
  function toggle(label,key){ const s=RG.store.settings(); const seg=el('div',{class:'seg'});
    seg.appendChild(el('button',{class:s[key]?'on':'',onclick:()=>{RG.store.setSetting(key,true);openDrawer();}},'Bật'));
    seg.appendChild(el('button',{class:!s[key]?'on':'',onclick:()=>{RG.store.setSetting(key,false);openDrawer();}},'Tắt'));
    return field(label,seg); }
  function exportData(){ const blob=new Blob([RG.store.export()],{type:'application/json'});
    const a=el('a',{href:URL.createObjectURL(blob),download:'rusviet-tien-do.json'}); a.click(); RG.util.toast('Đã xuất tiến độ'); }
  function openDrawer(){
    const d=$('#drawer'); const s=RG.store.settings(); d.innerHTML='';
    d.appendChild(el('div',{style:'display:flex;align-items:center'},
      el('h3',{style:'flex:1'},'⚙️ Cài đặt'), el('button',{class:'btn icon',onclick:()=>d.classList.remove('open')},'✕')));
    const seg=el('div',{class:'seg'});
    ['light','dark'].forEach(t=>seg.appendChild(el('button',{class:s.theme===t?'on':'',
      onclick:()=>{RG.store.setSetting('theme',t);applyTheme();openDrawer();buildTopbar(curTitle);}}, t==='light'?'☀️ Sáng':'🌙 Tối')));
    d.appendChild(field('Giao diện',seg));
    const fs=el('input',{type:'range',min:14,max:24,step:1,value:s.fontSize});
    fs.addEventListener('input',()=>{RG.store.setSetting('fontSize',+fs.value); const b=$('.sec-body'); if(b)b.style.fontSize=fs.value+'px';});
    d.appendChild(field('Cỡ chữ bài đọc: '+s.fontSize+'px',fs));
    const rate=el('input',{type:'range',min:.5,max:1.2,step:.05,value:s.ttsRate});
    rate.addEventListener('input',()=>RG.store.setSetting('ttsRate',+rate.value));
    d.appendChild(field('Tốc độ đọc',rate));
    const ru=RG.tts.russian(); const allv=RG.tts.voices(); const other=allv.filter(v=>ru.indexOf(v)<0);
    const sel=el('select');
    if(ru.length){ const g=document.createElement('optgroup'); g.label='Giọng '+SITE.langName;
      ru.forEach((v,i)=>{ const o=el('option',{value:v.voiceURI}, `${v.name}${i===0?' ⭐ khuyên dùng':''} · ${RG.tts.quality(v)}`);
        if(v.voiceURI===s.voiceURI)o.selected=true; g.appendChild(o); }); sel.appendChild(g); }
    if(other.length){ const g=document.createElement('optgroup'); g.label='Giọng khác';
      other.forEach(v=>{ const o=el('option',{value:v.voiceURI}, `${v.name} (${v.lang})`); if(v.voiceURI===s.voiceURI)o.selected=true; g.appendChild(o); }); sel.appendChild(g); }
    if(!allv.length) sel.appendChild(el('option',{value:''},'(Chưa tải được giọng)'));
    sel.addEventListener('change',()=>RG.store.setSetting('voiceURI',sel.value));
    const test=el('button',{class:'btn sm',onclick:()=>RG.tts.speak(SITE.test)},'🔊 Nghe thử');
    const useBest=el('button',{class:'btn sm',onclick:()=>{const b=RG.tts.useBest(); if(b){openDrawer();RG.util.toast('Đã chọn: '+b.name);}else RG.util.toast('Máy chưa có giọng Nga');}},'✨ Giọng Nga tốt nhất');
    const hint=el('div',{class:'muted',style:'font-size:12.5px;margin-top:8px;line-height:1.5'});
    hint.innerHTML = RG.tts.hasRussian ? 'Mẹo: mở bằng <b>Microsoft Edge</b> để có giọng “Online (Natural)” hay nhất.'
      : '⚠️ Chưa có giọng '+SITE.langName+'. Mở bằng <b>Edge</b>, hoặc <b>Windows → Cài đặt → Thời gian & ngôn ngữ → Giọng nói → Thêm giọng</b>.';
    d.appendChild(field('Giọng đọc '+SITE.langName+(RG.tts.hasRussian?'':' ⚠️'),
      el('div',{}, sel, el('div',{style:'display:flex;gap:8px;margin-top:8px;flex-wrap:wrap'}, test, useBest), hint)));
    d.appendChild(toggle('Hiện dấu nhấn (а́)','showStress'));
    d.appendChild(toggle('Tự đọc khi lật flashcard','autoplay'));
    d.appendChild(toggle('Đọc cả tiếng Việt khi “Nghe cả bài”','readVi'));
    d.appendChild(toggle('Tự động tra online khi thiếu từ (cần mạng)','autoOnline'));
    d.appendChild(toggle('Đọc ngoại ngữ bằng giọng online khi máy thiếu giọng','onlineTTS'));
    d.appendChild(el('div',{class:'field'}, el('label',{},'Dữ liệu học tập'),
      el('button',{class:'btn sm',style:'margin-right:8px',onclick:exportData},'⬇️ Xuất tiến độ'),
      el('button',{class:'btn sm',onclick:()=>{ if(confirm('Xoá toàn bộ tiến độ, highlight và ghi chú?')){RG.store.reset();location.reload();} }},'🗑 Đặt lại')));
    d.classList.add('open');
  }

  /* ---------- router ---------- */
  function exItemCount(sec){
    let txt=''; (sec.blocks||[]).forEach(b=>{ if(b.t==='para'||b.t==='example') txt+=' '+(b.text||''); });
    const nums=(txt.match(/(?:^|\s)(\d{1,2})\.\s/g)||[]).map(x=>parseInt(x.trim(),10)).filter(n=>!isNaN(n));
    return nums.length?Math.max.apply(null,nums):0;
  }
  function trimAnswer(ans, limit){
    if(!limit) return ans;
    const re=/(\d{1,2})\.\s/g; const idx=[]; let m;
    while((m=re.exec(ans))) idx.push({n:+m[1], at:m.index});
    if(!idx.length) return ans;
    const kept=[];
    for(let i=0;i<idx.length;i++){ const end=i+1<idx.length?idx[i+1].at:ans.length;
      if(idx[i].n<=limit) kept.push(ans.slice(idx[i].at,end).trim()); }
    return kept.join(' ');
  }
  function showErr(err){ console.error(err); $('#view').innerHTML='<div class="empty"><div class="e">⚠️</div>Lỗi: '+esc(err&&err.message||'')+'</div>'; }
  function route(){
    const view=$('#view'); $('#sidebar').classList.remove('open'); $('#scrim').classList.remove('show');
    RG.dict.hide&&RG.dict.hide(); RG.tts.stop&&RG.tts.stop(); RG.player&&RG.player.stop&&RG.player.stop();
    const parts=location.hash.replace(/^#\/?/,'').split('/').filter(Boolean);
    try{
      if(!parts.length){ buildSidebar(null); return viewLibrary(view); }
      const v=parts[0], a=parts[1], b=parts[2], c=parts[3];
      const withBook=(fn)=>loadBook(a).then(()=>{ buildSidebar(a); fn(); }).catch(showErr);
      switch(v){
        case 'book':       return withBook(()=>viewBook(view,a));
        case 'unit':       return withBook(()=>viewUnit(view,a,b));
        case 'section':    return withBook(()=>viewSection(view,a,b,c));
        case 'flashcards': return withBook(()=>{buildTopbar('Flashcard');RG.fc.render(view,a);});
        case 'search':     return withBook(()=>{buildTopbar('Tìm kiếm');RG.search.render(view,a);});
        case 'dictionary': return withBook(()=>viewDictionary(view,a));
        case 'bookmarks':  return withBook(()=>viewBookmarks(view,a));
        default: buildSidebar(null); return viewLibrary(view);
      }
    }catch(err){ showErr(err); }
  }

  /* ---------- boot ---------- */
  function boot(){
    applyTheme();
    if(SITE.title) document.title=SITE.title;
    $('#scrim').addEventListener('click',()=>{$('#sidebar').classList.remove('open');$('#scrim').classList.remove('show');});
    window.addEventListener('hashchange',route);
    $('#view').innerHTML='<div class="empty"><div class="e">📚</div>Đang tải…</div>';
    RG.data.library().then(lib=>{ A.lib=lib;
      // Tự nạp dữ liệu mọi sách liệt kê trong library.json (không cần thẻ <script> riêng cho từng sách/bài)
      return Promise.all((lib.books||[]).map(b=>Promise.all([
        RG.data.book(b.id).catch(()=>null),
        RG.data.glossary(b.id).catch(()=>null),
        RG.data.answers(b.id).catch(()=>null)
      ]))).then(()=>{ RG.dict.resetGlobal&&RG.dict.resetGlobal(); });
    }).then(()=>route())
      .catch(err=>{ $('#view').innerHTML='<div class="empty"><div class="e">⚠️</div>Không tải được thư viện.<br><small>'+esc(err&&err.message)+'</small></div>'; });
    if(window.speechSynthesis&&window.speechSynthesis.addEventListener)
      window.speechSynthesis.addEventListener('voiceschanged',()=>buildTopbar(curTitle));
  }
  if(document.readyState!=='loading') boot(); else document.addEventListener('DOMContentLoaded',boot);
})(window.RG);
