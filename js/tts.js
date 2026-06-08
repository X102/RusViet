/* ===== Text-to-speech (Russian) via Web Speech API, with smart voice picking ===== */
(function(RG){
  const synth = window.speechSynthesis;
  let voices=[], curEl=null, defaulted=false, seqGen=0;
  function load(){ if(!synth)return; voices=synth.getVoices()||[]; ensureDefault(); }
  if(synth){ load(); synth.onvoiceschanged=load; }

  function forSpeech(t){ return (t||'').replace(/[̀-ͯ]/g,'').replace(/[—–]/g,' '); }
  function isRu(v){ return /^ru\b|ru[-_]/i.test(v.lang)||/русск|russian/i.test(v.name); }
  function russianVoices(){ return voices.filter(isRu); }
  function primLang(){ return (window.SITE&&window.SITE.lang)||'ru'; }
  function primaryVoices(){ return primLang()==='zh'?zhVoices():russianVoices(); }
  function zhVoices(){ return voices.filter(v=>/^zh\b|zh[-_]|cmn/i.test(v.lang)||/chinese|中文|普通话/i.test(v.name)); }
  function viVoices(){ return voices.filter(v=>/^vi\b|vi[-_]/i.test(v.lang)||/vietnam/i.test(v.name)); }
  // higher = better
  function score(v){
    let s=0; const n=(v.name||'').toLowerCase();
    if(/natural/.test(n)) s+=100;          // Edge "Online (Natural)" — best free
    if(/online/.test(n)) s+=60;
    if(/google/.test(n)) s+=55;            // Chrome "Google русский"
    if(/(svetlana|dmitry|dariya|dariia|xiaoxiao|yunxi|xiaoyi|huihui|kangkang)/.test(n)) s+=40;
    if(/(irina|pavel|milena|tatyana|maxim|elena)/.test(n)) s+=30;
    if(/desktop/.test(n)) s-=10;           // older robotic desktop voices
    if(v.localService) s+=5;               // works offline
    return s;
  }
  function bestRussian(){
    const rv=primaryVoices(); if(!rv.length) return null;
    return rv.slice().sort((a,b)=>score(b)-score(a))[0];
  }
  function pick(){
    const uri=RG.store.settings().voiceURI;
    if(uri){ const v=voices.find(v=>v.voiceURI===uri); if(v)return v; }
    return bestRussian() || voices.find(v=>primLang()==='zh'?/zh|cmn/i.test(v.lang):/ru/i.test(v.lang)) || null;
  }
  // On first load, remember the best Russian voice so the picker shows it selected
  function ensureDefault(){
    if(defaulted) return;
    const cur=RG.store.settings().voiceURI;
    if(!cur){ const b=bestRussian(); if(b){ RG.store.setSetting('voiceURI',b.voiceURI); defaulted=true; } }
    else defaulted=true;
  }

  const TTS = RG.tts = {
    get available(){ return !!synth; },
    get hasRussian(){ return primaryVoices().length>0; },
    voices(){ return voices; },
    russian(){ return primaryVoices().slice().sort((a,b)=>score(b)-score(a)); },
    best:bestRussian,
    quality(v){ const s=score(v); return s>=100?'natural':s>=55?'tốt':'cơ bản'; },
    useBest(){ const b=bestRussian(); if(b){RG.store.setSetting('voiceURI',b.voiceURI);return b;} return null; },
    hasVi(){ return viVoices().length>0; },
    viVoice(){ return viVoices()[0]||null; },
    // speak one chunk in a given language ('ru'|'vi'); calls done() once when finished
    speakAs(text, lang, done){
      if(!synth||!text||!text.trim()){ done&&done(); return; }
      const u=new SpeechSynthesisUtterance(forSpeech(text));
      let v=null;
      if(lang==='vi'){ v=viVoices()[0]; u.lang='vi-VN'; }
      else if(lang==='zh'){ v=zhVoices()[0]; u.lang='zh-CN'; }
      else { v=pick(); u.lang=v?v.lang:'ru-RU'; }
      if(v) u.voice=v;
      u.rate=RG.store.settings().ttsRate||0.95; u.pitch=1;
      let fired=false; const fin=()=>{ if(fired)return; fired=true; done&&done(); };
      u.onend=fin; u.onerror=fin;
      try{ synth.speak(u); }catch(e){ fin(); }
    },
    // read a longer text sentence-by-sentence with clear pauses
    speakSeq(text, lang){
      seqGen++; const my=seqGen;
      if(!synth||!text) return;
      synth.cancel();
      const pieces=text.split(/(?<=[.;!?…])\s+|\s+(?=\d{1,2}\.\s)/).map(x=>x.trim()).filter(Boolean);
      let i=0;
      const step=()=>{ if(my!==seqGen||i>=pieces.length) return;
        TTS.speakAs(pieces[i++], lang||'ru', ()=>{ if(my===seqGen) setTimeout(step, 420); }); };
      step();
    },
    speak(text, el){
      seqGen++;
      if(!synth||!text) return;
      synth.cancel();
      if(curEl){ curEl.classList.remove('speaking'); curEl=null; }
      const u=new SpeechSynthesisUtterance(forSpeech(text));
      let v=null;
      if(/[\u4E00-\u9FFF\u3400-\u4DBF]/.test(text)){ v=zhVoices()[0]||null; u.lang='zh-CN'; }
      else { v=pick(); u.lang=v?v.lang:'ru-RU'; }
      if(v) u.voice=v;
      u.rate=RG.store.settings().ttsRate||0.9; u.pitch=1;
      if(el){ curEl=el; el.classList.add('speaking');
        u.onend=u.onerror=()=>{el.classList.remove('speaking');if(curEl===el)curEl=null;}; }
      try{ synth.speak(u); }catch(e){}
    },
    stop(){ seqGen++; if(synth)synth.cancel(); if(curEl){curEl.classList.remove('speaking');curEl=null;} }
  };
})(window.RG);
