/* ===== RG namespace + DOM/util helpers ===== */
window.RG = window.RG || {};
(function(RG){
  const U = RG.util = {};
  U.$  = (s,r=document)=>r.querySelector(s);
  U.$$ = (s,r=document)=>Array.from(r.querySelectorAll(s));
  U.el = (tag, attrs={}, ...kids)=>{
    const e=document.createElement(tag);
    for(const k in attrs){
      if(k==='class') e.className=attrs[k];
      else if(k==='html') e.innerHTML=attrs[k];
      else if(k.startsWith('on')&&typeof attrs[k]==='function') e.addEventListener(k.slice(2),attrs[k]);
      else if(attrs[k]!=null) e.setAttribute(k,attrs[k]);
    }
    for(const kid of kids.flat()){
      if(kid==null||kid===false||kid===true)continue;
      e.appendChild(kid&&kid.nodeType?kid:document.createTextNode(String(kid)));
    }
    return e;
  };
  U.esc = s => (s||'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  U.debounce=(fn,ms=200)=>{let t;return(...a)=>{clearTimeout(t);t=setTimeout(()=>fn(...a),ms)};};

  // Cyrillic helpers
  const CYR=/[Ѐ-ӿ]/;
  U.hasCyr = s => CYR.test(s||'');
  U.hasZh = s => /[\u4E00-\u9FFF\u3400-\u4DBF]/.test(s||'');
  U.stripStress = s => (s||'').replace(/[̀-ͯ]/g,'');
  U.normRu = s => U.stripStress(s).trim().toLowerCase().replace(/ё/g,'е');
  // Split a string into [{ru:bool,text}] tokens (Cyrillic runs vs the rest)
  U.tokenize = s => {
    const out=[]; const re=/[Ѐ-ӿ̀-ͯ]+(?:[-'’][Ѐ-ӿ̀-ͯ]+)*|[\u4E00-\u9FFF\u3400-\u4DBF]+/g;
    let last=0,m;
    while((m=re.exec(s))){
      if(m.index>last) out.push({ru:false,text:s.slice(last,m.index)});
      const t=m[0];
      if(/[\u4E00-\u9FFF\u3400-\u4DBF]/.test(t)) out.push({ru:false,zh:true,text:t});
      else out.push({ru:true,text:t});
      last=re.lastIndex;
    }
    if(last<s.length) out.push({ru:false,text:s.slice(last)});
    return out;
  };
  U.toast=(msg)=>{const t=U.$('#toast');t.textContent=msg;t.classList.add('show');
    clearTimeout(U._tt);U._tt=setTimeout(()=>t.classList.remove('show'),1900);};
})(window.RG);
