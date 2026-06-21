/* ===== Content renderer: JSON blocks -> interactive DOM ===== */
(function(RG){
  const {el,hasCyr,stripStress,tokenize}=RG.util;

  function speakRu(text){
    const ru=tokenize(text).filter(t=>t.ru).map(t=>t.text).join(' ');
    if(ru) return RG.tts.speakSeq(ru,'ru');
    const zh=tokenize(text).filter(t=>t.zh).map(t=>t.text).join('。');
    if(zh) RG.tts.speakSeq(zh,'zh');
  }
  // string -> fragment with clickable Russian tokens
  function rich(text){
    const frag=document.createDocumentFragment();
    const showStress=RG.store.settings().showStress;
    tokenize(text).forEach(tok=>{
      if(tok.ru){
        const span=el('span',{class:'ru'}, showStress?tok.text:stripStress(tok.text));
        span.addEventListener('click',e=>{e.stopPropagation();RG.dict.showFor(tok.text,span);});
        frag.appendChild(span);
      } else if(tok.zh){
        const span=el('span',{class:'zh'}, tok.text);
        span.addEventListener('click',e=>{e.stopPropagation();RG.dict.showFor(tok.text,span);});
        frag.appendChild(span);
      } else {
        tok.text.split(/(\([^)]*\))/).forEach(pt=>{ if(!pt) return;
          if(pt.charAt(0)==='(') frag.appendChild(el('span',{class:'gloss'}, pt));
          else frag.appendChild(document.createTextNode(pt)); });
      }
    });
    return frag;
  }
  RG.render={ rich, speakRu };

  function lineSpeaker(text){
    return el('button',{class:'play',title:'Nghe câu',style:'margin-left:6px',
      onclick:e=>{e.stopPropagation();speakRu(text);}},'🔊');
  }
  function splitNum(text){
    const parts=text.split(/\s+(?=\d{1,2}\.\s)/);
    return parts.length>1?parts:null;
  }
  function para(cls,text,withSpeak){
    const p=el('div',{class:'block '+cls});
    const items=splitNum(text);
    if(items){ items.forEach(it=>{ const ln=el('div',{class:'line'}); ln.appendChild(rich(it.trim())); p.appendChild(ln); }); }
    else p.appendChild(rich(text));
    if(withSpeak&&(hasCyr(text)||RG.util.hasZh(text))) p.appendChild(lineSpeaker(text));
    return p;
  }
  function vocabItem(b){
    const v=el('div',{class:'vocab'});
    if(b.g) v.appendChild(el('div',{class:'g g-'+b.g}, b.g.toUpperCase()));
    const w=el('div',{class:'w'});
    const r=el('div',{class:'r'}); r.appendChild(rich(b.ru));
    r.addEventListener('click',e=>{e.stopPropagation();RG.dict.showFor(b.ru,r);});
    w.appendChild(r);
    if(b.py) w.appendChild(el('div',{class:'py'}, b.py));
    w.appendChild(el('div',{class:'m'}, b.vi));
    v.appendChild(w);
    v.appendChild(el('button',{class:'play',title:'Nghe',
      onclick:e=>{e.stopPropagation();RG.tts.speak(stripStress(b.ru));}},'🔊'));
    return v;
  }
  function table(b){
    const wrap=el('div',{class:'tbl-wrap'}); const t=el('table',{class:'gt'});
    b.rows.forEach(row=>{ const tr=el('tr');
      row.forEach(c=>{ const td=el('td'); td.appendChild(rich(c)); tr.appendChild(td); });
      t.appendChild(tr); });
    wrap.appendChild(t); return wrap;
  }

  // Render an array of blocks into container (groups consecutive vocab)
  RG.render.blocks=function(blocks, container){
    let i=0;
    while(i<blocks.length){
      const b=blocks[i];
      if(b.t==='vocab'){
        const list=el('div',{class:'vocab-list'});
        while(i<blocks.length&&blocks[i].t==='vocab'){ list.appendChild(vocabItem(blocks[i])); i++; }
        container.appendChild(list); continue;
      }
      switch(b.t){
        case 'instruction': container.appendChild(para('b-instruction',b.text.replace(/^Yêu cầu:\s*/i,''),true)); break;
        case 'goal':        container.appendChild(para('b-goal',b.text)); break;
        case 'note':        container.appendChild(para('b-note',b.text.replace(/^Lưu ý[^:]*:\s*/i,''),true)); break;
        case 'model':       container.appendChild(para('b-model',b.text.replace(/^M(ẫu|ô hình)[^:]*:\s*/i,''),true)); break;
        case 'example':     container.appendChild(para('b-example',b.text.replace(/^Ví dụ:\s*/i,''),true)); break;
        case 'subhead':     container.appendChild(el('div',{class:'block b-subhead'},rich(b.text))); break;
        case 'table':       container.appendChild(table(b)); break;
        case 'audio': {
          const w=el('div',{class:'block b-audio'});
          if(b.label) w.appendChild(el('div',{class:'alab'},'🎧 '+b.label));
          w.appendChild(el('audio',{controls:'',preload:'none',src:b.src}));
          container.appendChild(w); break; }
        default:            container.appendChild(para('b-para',b.text,true));
      }
      i++;
    }
  };
})(window.RG);
