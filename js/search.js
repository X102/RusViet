/* ===== Global search (current book): glossary + section titles + optional full-text ===== */
(function(RG){
  const {el,esc,normRu,stripStress}=RG.util;
  function hl(text,q){ if(!q)return esc(text);
    const i=text.toLowerCase().indexOf(q.toLowerCase()); if(i<0)return esc(text);
    return esc(text.slice(0,i))+'<mark class="q">'+esc(text.slice(i,i+q.length))+'</mark>'+esc(text.slice(i+q.length)); }

  RG.search={
    render(view, bookId){
      bookId=bookId||RG.app.bookId;
      view.innerHTML='';
      view.appendChild(el('h1',{class:'page-title'},'🔎 Tìm kiếm'));
      view.appendChild(el('p',{class:'page-sub'},'Tìm từ vựng và tên bài trong '+(RG.app.book?RG.app.book.title:'sách')+'. Bấm “Tìm sâu” để quét toàn bộ nội dung.'));
      const box=el('div',{class:'search-box'}, el('span',{},'🔎'),
        el('input',{type:'search',placeholder:'Nhập từ tiếng Nga hoặc tiếng Việt…',autofocus:'true'}));
      view.appendChild(box);
      const deepBtn=el('button',{class:'btn sm',style:'margin:12px 0'},'🌊 Tìm sâu trong toàn bộ nội dung'); view.appendChild(deepBtn);
      const out=el('div',{}); view.appendChild(out);
      const input=box.querySelector('input');
      let deep=false, deepData=null;
      input.addEventListener('input',RG.util.debounce(render,150));
      deepBtn.addEventListener('click',()=>{ deep=true; deepBtn.textContent='⏳ Đang tải…';
        RG.data.book(bookId).then(b=>Promise.all(b.parts.map(p=>RG.data.unit(p.id))))
          .then(units=>{deepData=units;deepBtn.textContent='✅ Đã bật tìm sâu';render();}); });
      function render(){
        const q=input.value.trim(); out.innerHTML=''; if(!q) return;
        RG.dict.ready().then(()=>{
          const m=RG.dict.map(); const qn=normRu(q), ql=q.toLowerCase();
          const vres=[]; if(m) m.forEach(e=>{ if(normRu(e.ru).includes(qn)||e.vi.toLowerCase().includes(ql)) vres.push(e); });
          if(vres.length){ out.appendChild(el('h2',{class:'sec'},`Từ vựng (${vres.length})`));
            vres.slice(0,40).forEach(e=>{ const r=el('div',{class:'result'});
              r.innerHTML=`<div class="ru-text" style="color:var(--ru);font-size:17px;font-weight:600">${hl(e.ru,q)}</div><div>${hl(e.vi,q)}</div>`;
              r.addEventListener('click',()=>RG.tts.speak(stripStress(e.ru))); out.appendChild(r); }); }
          RG.data.book(bookId).then(b=>{
            const tres=b.parts.filter(p=>p.vi.toLowerCase().includes(ql)||(p.ru||'').toLowerCase().includes(ql));
            if(tres.length){ out.appendChild(el('h2',{class:'sec'},'Chương'));
              tres.forEach(p=>{ const r=el('div',{class:'result',html:hl(p.vi,q)});
                r.addEventListener('click',()=>location.hash='#/unit/'+bookId+'/'+p.id); out.appendChild(r); }); }
            if(deep&&deepData){
              const dres=[];
              deepData.forEach(u=>u.sections.forEach(s=>{
                if(s.title.toLowerCase().includes(ql)) dres.push({u,s,snip:s.title});
                else for(const blk of s.blocks){ const tx=blk.text||(blk.ru?blk.ru+' '+blk.vi:'');
                  if(tx&&tx.toLowerCase().includes(ql)){ dres.push({u,s,snip:tx}); break; } } }));
              if(dres.length){ out.appendChild(el('h2',{class:'sec'},`Trong nội dung (${dres.length})`));
                dres.slice(0,60).forEach(x=>{ const r=el('div',{class:'result'});
                  r.innerHTML=`<div>${hl(x.snip.slice(0,140),q)}</div><div class="where">${esc(x.u.vi)} · ${esc(x.s.title)}</div>`;
                  r.addEventListener('click',()=>location.hash='#/section/'+bookId+'/'+x.u.id+'/'+x.s.id); out.appendChild(r); }); } }
            if(!out.children.length) out.appendChild(el('div',{class:'empty'},el('div',{class:'e'},'🤔'),'Không tìm thấy.'));
          });
        });
      }
    }
  };
})(window.RG);
