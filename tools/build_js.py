import json, os
ROOT="/sessions/sleepy-epic-wozniak/mnt/outputs/site/data"
def emit(key, jsonpath):
    obj=json.load(open(jsonpath,encoding='utf-8'))
    jspath=jsonpath[:-5]+".js"
    payload=json.dumps(obj,ensure_ascii=False,separators=(',',':'))
    with open(jspath,"w",encoding="utf-8") as f:
        f.write('window.RG_DATA=window.RG_DATA||{};\n')
        f.write('window.RG_DATA[%s]=%s;\n'%(json.dumps(key),payload))
    return jspath, len(payload)
items=[("library", f"{ROOT}/library.json"),
       ("book:grammar-morphology", f"{ROOT}/books/grammar-morphology/book.json"),
       ("glossary:grammar-morphology", f"{ROOT}/books/grammar-morphology/glossary.json")]
for fn in sorted(os.listdir(f"{ROOT}/books/grammar-morphology/units")):
    if fn.endswith('.json'):
        items.append(("unit:"+fn[:-5], f"{ROOT}/books/grammar-morphology/units/{fn}"))
for key,jp in items:
    p,n=emit(key,jp); print(f"{key:32s} -> {os.path.basename(p):20s} {n:>9,} bytes")
