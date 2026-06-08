/* ===== Persistent state (localStorage) ===== */
(function(RG){
  const KEY='rusviet.v1';
  const def={
    settings:{theme:'light',ttsRate:.9,voiceURI:'',fontSize:17,showStress:true,autoplay:false,readVi:true,autoOnline:true},
    progress:{}, highlights:{}, notes:{}, srs:{}, recent:[], lastSeen:{}
  };
  let state;
  try{ state=Object.assign({},def,JSON.parse(localStorage.getItem(KEY)||'{}')); }
  catch(e){ state={...def}; }
  for(const k in def) if(state[k]==null) state[k]=def[k];

  let timer;
  function persist(){ clearTimeout(timer); timer=setTimeout(()=>{
    try{ localStorage.setItem(KEY,JSON.stringify(state)); }catch(e){}
  },120); }

  const S = RG.store = {
    get state(){return state;},
    settings(){return state.settings;},
    setSetting(k,v){state.settings[k]=v;persist();},
    // progress
    isDone(id){return !!(state.progress[id]&&state.progress[id].done);},
    isBookmarked(id){return !!(state.progress[id]&&state.progress[id].bm);},
    toggleDone(id){const p=state.progress[id]||(state.progress[id]={});p.done=!p.done;persist();return p.done;},
    toggleBookmark(id){const p=state.progress[id]||(state.progress[id]={});p.bm=!p.bm;persist();return p.bm;},
    doneCount(prefix){return Object.keys(state.progress).filter(k=>k.startsWith(prefix)&&state.progress[k].done).length;},
    bookmarks(){return Object.keys(state.progress).filter(k=>state.progress[k].bm);},
    // highlights
    getHL(id){return state.highlights[id]||[];},
    setHL(id,arr){state.highlights[id]=arr;persist();},
    allHL(){return state.highlights;},
    // notes
    getNote(id){return state.notes[id]||'';},
    setNote(id,v){if(v) state.notes[id]=v; else delete state.notes[id];persist();},
    notedSections(){return Object.keys(state.notes);},
    // SRS (Leitner-lite) box 0..5, due timestamp
    srs(){return state.srs;},
    grade(word,ok){const s=state.srs[word]||(state.srs[word]={box:0,due:0});
      s.box=ok?Math.min(5,s.box+1):0;
      const days=[0,1,2,4,8,16][s.box]||16; s.due=Date.now()+days*864e5; persist();},
    dueWords(){const n=Date.now();return Object.keys(state.srs).filter(w=>state.srs[w].due<=n);},
    // recent
    pushRecent(item){state.recent=[item,...state.recent.filter(r=>r.id!==item.id)].slice(0,12);persist();},
    setLastSeen(unitId,secId){state.lastSeen[unitId]=secId;persist();},
    lastSeen(unitId){return state.lastSeen[unitId];},
    // export / reset
    export(){return JSON.stringify(state,null,2);},
    reset(){state=JSON.parse(JSON.stringify(def));persist();}
  };
})(window.RG);
