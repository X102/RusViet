/* ===== Data access: prefer preloaded RG_DATA (static <script> tags), fall back to injection ===== */
(function(RG){
  RG.BOOK='grammar-morphology';
  const base='data/';
  const path={
    library: base+'library.js',
    book: id=>base+'books/'+id+'/book.js',
    glossary: id=>base+'books/'+id+'/glossary.js',
    answers: id=>base+'books/'+id+'/answers.js',
    unit: (book,unit)=>base+'books/'+book+'/units/'+unit+'.js'
  };
  window.RG_DATA=window.RG_DATA||{};
  const cache={};
  function inject(key,file){
    if(window.RG_DATA[key]) return Promise.resolve(window.RG_DATA[key]);
    if(!file) return Promise.reject(new Error('Thiếu đường dẫn dữ liệu: '+key));
    if(cache[key]) return cache[key];
    cache[key]=new Promise((res,rej)=>{
      const s=document.createElement('script'); s.src=file;
      s.onload=()=>window.RG_DATA[key]?res(window.RG_DATA[key]):rej(new Error('empty '+file));
      s.onerror=()=>rej(new Error('Không tải được '+file));
      document.head.appendChild(s);
    });
    return cache[key];
  }
  function get(key,file){
    if(window.RG_DATA[key]) return Promise.resolve(window.RG_DATA[key]); // preloaded
    return inject(key,file);                                            // hosted/lazy fallback
  }
  RG.data={
    library:()=>get('library',path.library),
    book:(id=RG.BOOK)=>get('book:'+id,path.book(id)),
    glossary:(id=RG.BOOK)=>get('glossary:'+id,path.glossary(id)),
    unit:(unit,book=RG.BOOK)=>get('unit:'+unit,path.unit(book,unit)),
    answers:(id=RG.BOOK)=>get('answers:'+id,path.answers(id)),
  };
})(window.RG);
