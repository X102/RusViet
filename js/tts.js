/* ===== TTS: local voices (Web Speech) + ONLINE fallback (Google) for RU/ZH ===== */
(function(RG){
  const synth = window.speechSynthesis;
  let voices=[], curEl=null, defaulted=false, seqGen=0, curAudio=null;
  function load(){ if(!synth)return; voices=synth.getVoices()||[]; ensureDefault(); }
  if(synth){ load(); synth.onvoiceschanged=load; }

  function forSpeech(t){ return (t||'').replace(/[̀-ͯ]/g,'').replace(/[—–]/g,' '); }
  function isRu(v){ return /^ru\b|ru[-_]/i.test(v.lang)||/русск|russian/i.test(v.name); }
  function russianVoices(){ return voices.filter(isRu); }
  function primLang(){ return (window.SITE&&window.SITE.lang)||'ru'; }
  function zhVoices(){ return voices.filter(v=>/^zh\b|zh[-_]|cmn/i.test(v.lang)||/chinese|中文|普通话/i.test(v.name)); }
  function viVoices(){ return voices.filter(v=>/^vi\b|vi[-_]/i.test(v.lang)||/vietnam/i.test(v.name)); }
  function primaryVoices(){ return primLang()==='zh'?zhVoices():russianVoices(); }
  function localFor(lang){ return lang==='vi'?viVoices():lang==='zh'?zhVoices():russianVoices(); }
  function langOf(text){ return /[㐀-鿿豈-﫿]/.test(text)?'zh':/[А-Яа-яЁё]/.test(text)?'ru':(/[A-Za-zÀ-ỹ]/.test(text)?(primLang()==='zh'?'vi':'vi'):primLang()); }
  function ttsCode(lang){ return lang==='zh'?'zh-CN':lang==='vi'?'vi':'ru'; }
  function onlineEnabled(){ return RG.store.settings().onlineTTS!==false; }

  function score(v){ let s=0; const n=(v.name||'').toLowerCase();
    if(/natural/.test(n))s+=100; if(/online/.test(n))s+=60; if(/google/.test(n))s+=55;
    if(/(svetlana|dmitry|dariya|dariia|xiaoxiao|yunxi|xiaoyi|huihui|kangkang)/.test(n))s+=40;
    if(/(irina|pavel|milena|tatyana|maxim|elena)/.test(n))s+=30;
    if(/desktop/.test(n))s-=10; if(v.localService)s+=5; return s; }
  function bestPrimary(){ const rv=primaryVoices(); return rv.length?rv.slice().sort((a,b)=>score(b)-score(a))[0]:null; }
  function pick(){ const uri=RG.store.settings().voiceURI;
    if(uri){ const v=voices.find(v=>v.voiceURI===uri); if(v)return v; }
    return bestPrimary() || primaryVoices()[0] || null; }
  function ensureDefault(){ if(defaulted)return; const cur=RG.store.settings().voiceURI;
    if(!cur){ const b=bestPrimary(); if(b){RG.store.setSetting('voiceURI',b.voiceURI);defaulted=true;} } else defaulted=true; }

  function stopAudio(){ if(curAudio){ try{curAudio.pause();}catch(e){} curAudio=null; } }
  // Phát âm online (Google translate_tts) — dùng khi máy không có giọng nội bộ cho ngôn ngữ đó
  function audioSpeak(text, lang, done){
    let fired=false; const fin=()=>{ if(fired)return; fired=true; done&&done(); };
    try{
      stopAudio();
      const q=forSpeech(text).slice(0,200);
      const a=new Audio('https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl='+ttsCode(lang)+'&q='+encodeURIComponent(q));
      curAudio=a;
      let r=RG.store.settings().ttsRate||1; a.playbackRate=Math.max(0.6,Math.min(1.4,r));
      a.onended=()=>{ if(curAudio===a)curAudio=null; fin(); };
      a.onerror=()=>{ if(curAudio===a)curAudio=null; fin(); };
      const pr=a.play(); if(pr&&pr.catch) pr.catch(()=>fin());
    }catch(e){ fin(); }
  }
  function synthSpeak(text, lang, voice, done, el){
    const u=new SpeechSynthesisUtterance(forSpeech(text));
    if(voice){ u.voice=voice; u.lang=voice.lang; } else u.lang=ttsCode(lang)==='vi'?'vi-VN':ttsCode(lang)==='zh-CN'?'zh-CN':'ru-RU';
    u.rate=RG.store.settings().ttsRate||0.95; u.pitch=1;
    let fired=false; const fin=()=>{ if(fired)return; fired=true; if(el)el.classList.remove('speaking'); done&&done(); };
    u.onend=fin; u.onerror=fin;
    if(el) el.classList.add('speaking');
    try{ synth.speak(u); }catch(e){ fin(); }
  }

  const TTS = RG.tts = {
    get available(){ return !!synth || true; },           // luôn có thể đọc (online)
    get hasRussian(){ return primaryVoices().length>0; },
    voices(){ return voices; },
    russian(){ return primaryVoices().slice().sort((a,b)=>score(b)-score(a)); },
    best:bestPrimary,
    quality(v){ const s=score(v); return s>=100?'natural':s>=55?'tốt':'cơ bản'; },
    useBest(){ const b=bestPrimary(); if(b){RG.store.setSetting('voiceURI',b.voiceURI);return b;} return null; },
    hasVi(){ return viVoices().length>0 || onlineEnabled(); },   // online cũng đọc được tiếng Việt
    viVoice(){ return viVoices()[0]||null; },
    // đọc 1 đoạn theo ngôn ngữ ('ru'|'zh'|'vi'); gọi done() khi xong
    speakAs(text, lang, done){
      if(!text||!text.trim()){ done&&done(); return; }
      lang=lang||'ru';
      const local=localFor(lang);
      if((!local.length || !synth) && onlineEnabled()) return audioSpeak(text, lang, done);
      if(!synth){ done&&done(); return; }
      synthSpeak(text, lang, local[0]||(lang==='ru'?pick():null), done);
    },
    speakSeq(text, lang){
      seqGen++; const my=seqGen; if(!text) return; this.stop();
      const zh=lang==='zh'; 
      const pieces=text.split(zh?/(?<=[。！？；])/:/(?<=[.;!?…])\s+|\s+(?=\d{1,2}\.\s)/).map(x=>x.trim()).filter(Boolean);
      let i=0; const step=()=>{ if(my!==seqGen||i>=pieces.length)return;
        TTS.speakAs(pieces[i++], lang||'ru', ()=>{ if(my===seqGen) setTimeout(step,360); }); };
      seqGen=my; step();
    },
    speak(text, el){
      this.stop();
      if(!text) return;
      const lang=langOf(text);
      const local=localFor(lang);
      if(el){ curEl=el; el.classList.add('speaking'); }
      const done=()=>{ if(el){el.classList.remove('speaking'); if(curEl===el)curEl=null;} };
      if((!local.length || !synth) && onlineEnabled()){ return audioSpeak(text, lang, done); }
      if(!synth){ done(); return; }
      synthSpeak(text, lang, local[0]||pick(), done, el);
    },
    stop(){ seqGen++; if(synth)synth.cancel(); stopAudio(); if(curEl){curEl.classList.remove('speaking');curEl=null;} }
  };
})(window.RG);
