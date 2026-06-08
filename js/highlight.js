/* ===== Highlighting (cross-node) + selection toolbar ===== */
(function(RG){
  const {el}=RG.util;
  const COLORS=['yellow','green','pink','blue'];

  function textNodes(root){
    const out=[],w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,{
      acceptNode(n){
        if(!n.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        let p=n.parentNode;
        while(p&&p!==root){ if(p.nodeName==='BUTTON'||p.nodeName==='MARK') return NodeFilter.FILTER_REJECT; p=p.parentNode; }
        return NodeFilter.FILTER_ACCEPT;
      }});
    let n; while((n=w.nextNode())) out.push(n); return out;
  }
  // wrap first un-highlighted occurrence of `needle` inside root
  function wrapOnce(root, needle, color){
    needle=needle.replace(/\s+/g,' ').trim(); if(!needle) return false;
    const nodes=textNodes(root); let hay='',map=[];
    nodes.forEach(node=>{ const t=node.nodeValue; for(let i=0;i<t.length;i++){ map.push([node,i]); }
      hay+=t; });
    // normalize whitespace while keeping index map
    let normHay='',nmap=[];
    for(let i=0;i<hay.length;i++){ const c=hay[i];
      if(/\s/.test(c)){ if(normHay.endsWith(' '))continue; normHay+=' '; nmap.push(map[i]); }
      else { normHay+=c; nmap.push(map[i]); } }
    const idx=normHay.indexOf(needle); if(idx<0) return false;
    const startRef=nmap[idx], endRef=nmap[idx+needle.length-1];
    if(!startRef||!endRef) return false;
    const range=document.createRange();
    range.setStart(startRef[0],startRef[1]); range.setEnd(endRef[0],endRef[1]+1);
    // wrap each fully/partly covered text node
    const affected=[];
    const tw=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,null);
    let node; while((node=tw.nextNode())){ if(range.intersectsNode(node)) affected.push(node); }
    affected.forEach(tn=>{
      let s=0,e=tn.nodeValue.length;
      if(tn===range.startContainer) s=range.startOffset;
      if(tn===range.endContainer) e=range.endOffset;
      if(s>=e) return;
      const r2=document.createRange(); r2.setStart(tn,s); r2.setEnd(tn,e);
      const mk=el('mark',{class:'hl hl-'+color}); try{ r2.surroundContents(mk); }catch(err){}
    });
    return true;
  }

  const HL=RG.hl={
    apply(root,sid){ (RG.store.getHL(sid)||[]).forEach(h=>wrapOnce(root,h.text,h.color)); },
    clear(root,sid){
      RG.store.setHL(sid,[]);
      RG.util.$$('mark.hl',root).forEach(m=>{ const p=m.parentNode; while(m.firstChild)p.insertBefore(m.firstChild,m); p.removeChild(m); p.normalize&&p.normalize(); });
      RG.util.toast('Đã xoá tô màu');
    },
    attach(root,sid){
      HL.apply(root,sid);
      let bar=null;
      const close=()=>{ if(bar){bar.remove();bar=null;} };
      root.addEventListener('mouseup',e=>{
        setTimeout(()=>{
          const sel=window.getSelection(); if(!sel||sel.isCollapsed){close();return;}
          const text=sel.toString().trim(); if(text.length<2||!root.contains(sel.anchorNode)){close();return;}
          close();
          const rect=sel.getRangeAt(0).getBoundingClientRect();
          bar=el('div',{class:'sel-bar'});
          COLORS.forEach(c=>bar.appendChild(el('div',{class:'swatch sw-'+c,title:'Tô '+c,
            onmousedown:ev=>{ev.preventDefault();
              const arr=RG.store.getHL(sid); arr.push({text,color:c}); RG.store.setHL(sid,arr);
              wrapOnce(root,text,c); sel.removeAllRanges(); close(); RG.util.toast('Đã tô màu & lưu');}})));
          bar.appendChild(el('div',{class:'sep'}));
          RG.dict.externals(text).forEach(l=>bar.appendChild(el('button',{class:'plink',title:'Tra '+l.label,
            onmousedown:ev=>{ev.preventDefault();RG.dict.open(l.url);close();}}, l.icon)));
          document.body.appendChild(bar);
          bar.style.left=Math.max(8,window.scrollX+rect.left)+'px';
          bar.style.top=(window.scrollY+rect.top-bar.offsetHeight-8)+'px';
        },1);
      });
      document.addEventListener('mousedown',e=>{ if(bar&&!bar.contains(e.target)) close(); });
    }
  };
})(window.RG);
