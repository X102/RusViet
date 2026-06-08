/* ===== Flashcards / spaced-repetition review ===== */
(function(RG){
  const {el,stripStress,normRu}=RG.util;
  function shuffle(a){for(let i=a.length-1;i>0;i--){const j=Math.random()*(i+1)|0;[a[i],a[j]]=[a[j],a[i]];}return a;}

  RG.fc={
    render(view, bookId){
      bookId=bookId||RG.app.bookId;
      view.innerHTML='';
      view.appendChild(el('h1',{class:'page-title'},'🃏 Flashcard ôn từ'));
      view.appendChild(el('p',{class:'page-sub'},'Lật thẻ, nghe phát âm và tự đánh giá. Hệ thống lặp lại ngắt quãng sẽ ưu tiên những từ bạn chưa thuộc.'));
      const stage=el('div',{class:'fc-stage'}); view.appendChild(stage);
      stage.appendChild(el('div',{class:'empty'},el('div',{class:'e'},'⏳'),'Đang tải từ vựng…'));
      RG.data.glossary(bookId).then(g=>{
        const entries=g.entries||[]; const byKey=new Map(entries.map(e=>[normRu(e.ru),e]));
        const due=RG.store.dueWords().map(w=>byKey.get(w)).filter(Boolean);
        const seen=new Set(Object.keys(RG.store.srs()));
        const fresh=shuffle(entries.filter(e=>!seen.has(normRu(e.ru)))).slice(0,30);
        let deck=shuffle([...due, ...fresh]).slice(0,20);
        if(!deck.length) deck=shuffle(entries.slice()).slice(0,20);
        run(stage,deck);
      }).catch(()=>stage.innerHTML='<div class="empty">Không tải được từ vựng.</div>');
    }
  };
  function run(stage,deck){
    let i=0,right=0;
    function draw(){
      stage.innerHTML='';
      if(i>=deck.length){
        stage.appendChild(el('div',{class:'empty'},el('div',{class:'e'},'🎉'),
          el('h2',{},'Hoàn thành phiên ôn!'),
          el('p',{class:'muted'},`Bạn nhớ ${right}/${deck.length} thẻ.`),
          el('button',{class:'btn primary',style:'margin-top:14px',onclick:()=>RG.fc.render(RG.util.$('#view'),RG.app.bookId)},'🔁 Ôn tiếp')));
        return;
      }
      const e=deck[i];
      stage.appendChild(el('div',{class:'fc-progress'},`Thẻ ${i+1} / ${deck.length}`));
      const card=el('div',{class:'flashcard'});
      const inner=el('div',{class:'inner'});
      const front=el('div',{class:'face'},
        el('div',{class:'big ru-text'}, e.ru),
        el('button',{class:'btn sm',onclick:ev=>{ev.stopPropagation();RG.tts.speak(stripStress(e.ru));}},'🔊 Nghe'),
        el('div',{class:'muted',style:'font-size:13px'},'Bấm để lật'));
      const back=el('div',{class:'face back'},
        el('div',{class:'mean'}, e.vi),
        el('div',{class:'big ru-text',style:'font-size:24px'}, e.ru),
        el('button',{class:'btn sm',onclick:ev=>{ev.stopPropagation();RG.tts.speak(stripStress(e.ru));}},'🔊'));
      inner.appendChild(front); inner.appendChild(back); card.appendChild(inner);
      card.addEventListener('click',()=>card.classList.toggle('flip'));
      stage.appendChild(card);
      if(RG.store.settings().autoplay) setTimeout(()=>RG.tts.speak(stripStress(e.ru)),250);
      const act=el('div',{class:'fc-actions'},
        el('button',{class:'btn',onclick:()=>{RG.store.grade(normRu(e.ru),false);i++;draw();}},'😕 Chưa thuộc'),
        el('button',{class:'btn ok',onclick:()=>{RG.store.grade(normRu(e.ru),true);right++;i++;draw();}},'😄 Đã thuộc'));
      stage.appendChild(act);
    }
    draw();
  }
})(window.RG);
