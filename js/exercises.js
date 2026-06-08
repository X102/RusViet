/* ===== Exercise self-test enhancements ===== */
(function(RG){
  const {el,$$}=RG.util;
  RG.ex={
    // returns a control button that toggles "hide meanings" quiz mode for a container
    quizToggle(container){
      const btn=el('button',{class:'btn sm',onclick:()=>{
        const on=container.classList.toggle('quiz');
        btn.classList.toggle('toggle-on',on);
        btn.firstChild.textContent = on?'👀 Hiện nghĩa':'🙈 Ẩn nghĩa (tự kiểm tra)';
        if(on){ RG.util.toast('Bấm vào ô mờ để hiện nghĩa'); }
      }},'🙈 Ẩn nghĩa (tự kiểm tra)');
      // reveal individual meaning on click
      container.addEventListener('click',e=>{
        if(container.classList.contains('quiz')&&e.target.classList.contains('m'))
          e.target.classList.toggle('show');
      });
      return btn;
    }
  };
})(window.RG);
