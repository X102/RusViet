/* ===== Passive listening: read a lesson aloud (RU + VI), sequential, with pauses ===== */
(function(RG){
  const {el,$,$$}=RG.util;
  let queue=[], bi=0, gen=0, paused=false, bar=null;

  // ordered [{lang,text}] segments, split further into sentences/numbered items
  function segment(text){
    const segs=[]; let buf='', mode=null;
    const flush=()=>{ if(buf.trim()&&mode&&/[А-Яа-яЁёA-Za-zÀ-ỹ0-9]/.test(buf)){
      // split a run into sentence-sized pieces for natural pauses
      buf.split(mode==='zh'?/(?<=[。！？；])/:/(?<=[.;!?…])\s+|\s+(?=\d{1,2}\.\s)/).forEach(piece=>{
        if(piece.trim()) segs.push({lang:mode,text:piece.trim()}); });
    } buf=''; };
    RG.util.tokenize(text).forEach(tok=>{
      const m2=tok.ru?'ru':(tok.zh?'zh':(/[A-Za-zÀ-ỹ]/.test(tok.text)?'vi':null));
      if(m2){ if(mode&&mode!==m2)flush(); mode=m2; buf+=tok.text; }
      else buf+=tok.text;
    });
    flush();
    return segs;
  }
  function build(body){
    queue=[];
    $$('.block, .vocab', body).forEach(elm=>{
      const lines=$$('.line', elm);
      const targets=lines.length?lines:[elm];
      targets.forEach(t=>{ const txt=(t.textContent||'').replace(/🔊/g,'').trim();
        if(!txt) return; const segs=segment(txt); if(segs.length) queue.push({el:t, segs}); });
    });
  }
  function setBar(){
    if(bar) bar.remove();
    bar=el('div',{class:'player-bar'},
      el('button',{class:'btn icon',title:'Dòng trước',onclick:()=>jump(-1)},'⏮'),
      el('button',{class:'btn icon',id:'pp',title:'Tạm dừng/Tiếp',onclick:toggle},'⏸'),
      el('button',{class:'btn icon',title:'Dòng sau',onclick:()=>jump(1)},'⏭'),
      el('button',{class:'btn icon',title:'Dừng',onclick:stop},'⏹'),
      el('div',{class:'pinfo',id:'pinfo'},''));
    document.body.appendChild(bar);
  }
  function info(){ const p=$('#pinfo'); if(p)p.textContent=`Đang đọc ${Math.min(bi+1,queue.length)}/${queue.length}`; }
  function highlight(){
    $$('.reading').forEach(e=>e.classList.remove('reading'));
    const it=queue[bi]; if(it&&it.el){ it.el.classList.add('reading'); it.el.scrollIntoView({behavior:'smooth',block:'center'}); }
  }
  function playBlock(){
    const my=gen;
    if(paused||my!==gen) return;
    if(bi>=queue.length){ stop(); RG.util.toast('Đã đọc xong bài'); return; }
    highlight(); info();
    const segs=queue[bi].segs.slice();
    const readVi=RG.store.settings().readVi!==false && RG.tts.hasVi();
    (function next(){
      if(my!==gen||paused) return;
      if(!segs.length){ bi++; setTimeout(()=>{ if(my===gen&&!paused) playBlock(); }, 550); return; }
      const seg=segs.shift();
      if(seg.lang==='vi' && !readVi){ return next(); }
      const gap = seg.lang==='vi' ? 480 : 380; // pause after each piece
      RG.tts.speakAs(seg.text, seg.lang, ()=>{ if(my===gen&&!paused) setTimeout(()=>{ if(my===gen&&!paused) next(); }, gap); });
    })();
  }
  function toggle(){
    if(!queue.length) return;
    paused=!paused; const b=$('#pp'); if(b)b.textContent=paused?'▶':'⏸';
    if(paused){ gen++; RG.tts.stop(); } else { playBlock(); }
  }
  function jump(d){ gen++; RG.tts.stop(); bi=Math.max(0,Math.min(queue.length-1,bi+d)); paused=false; const b=$('#pp'); if(b)b.textContent='⏸'; playBlock(); }
  function stop(){ gen++; RG.tts.stop(); paused=false; $$('.reading').forEach(e=>e.classList.remove('reading')); if(bar){bar.remove();bar=null;} }
  RG.player={
    start(body){
      stop(); build(body);
      if(!queue.length){ RG.util.toast('Không có nội dung để đọc'); return; }
      if(!RG.tts.available){ RG.util.toast('Trình duyệt không hỗ trợ đọc'); return; }
      bi=0; paused=false; gen++; setBar(); playBlock();
      if(!RG.tts.hasVi()) RG.util.toast('Chưa có giọng tiếng Việt — chỉ đọc tiếng Nga. Mở bằng Edge để có giọng Việt.');
    },
    stop, playing(){ return !!bar; }, _segment:segment
  };
})(window.RG);
