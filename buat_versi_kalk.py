# Jana 2 versi kalkulator Orang Minyak: slider.html & kalkulator.html (anggaran sahaja, harga tepat via WhatsApp)
# Jalankan dalam folder orang-minyak: python ../buat_versi_kalk.py
import re
src = open('index.html', encoding='utf-8').read()


def R(s, a, b, n=1):
    c = s.count(a)
    assert c == n, (c, a[:80])
    return s.replace(a, b)


EN_BARU = {
    'Minimum 30 kg': 'Minimum 30 kg', 'Tong disediakan': 'Drums provided', 'Volum besar': 'Large volume',
    'Ini anggaran sahaja. Harga sebenar ikut pasaran semasa dan timbangan di tempat.':
        'This is an estimate only. The actual price follows the current market and on-site weighing.',
    'Dapatkan harga tepat di WhatsApp': 'Get an exact price on WhatsApp', 'seminggu': 'a week',
    'Berapa bekas minyak terpakai anda seminggu?': 'How many containers of used oil do you fill a week?',
    'Botol 1.5 L': '1.5 L bottle', 'Jerikan 5 L': '5 L jerrycan', 'Jerikan 20 L': '20 L jerrycan',
    'Tong 200 L': '200 L drum', 'Jumlah anggaran': 'Estimated total',
}


def umum(s):
    s = R(s, '<small>RM2.50/kg</small>', '<small data-i>Minimum 30 kg</small>')
    s = R(s, '<small>RM2.60/kg*</small>', '<small data-i>Tong disediakan</small>')
    s = R(s, '<small data-i>Ikut volum*</small>', '<small data-i>Volum besar</small>')
    s = R(s, '<div class="out-big">RM<span id="oYear">', '<div class="out-big">≈ RM<span id="oYear">')
    s = R(s, '        <button type="button" class="btn btn-primary js-book" data-i>Tempah kutipan pertama</button>\n',
          '        <p class="out-note" data-i>Ini anggaran sahaja. Harga sebenar ikut pasaran semasa dan timbangan di tempat.</p>\n'
          '        <div class="out-btns"><a class="btn btn-primary" id="waHarga" href="https://wa.me/60178899786" target="_blank" rel="noopener" data-i>Dapatkan harga tepat di WhatsApp</a>\n'
          '        <button type="button" class="btn btn-line-lt js-book" data-i>Tempah kutipan pertama</button></div>\n')
    s = R(s, 'Anggaran ini menggunakan RM2.60/kg.*', 'WhatsApp kami untuk harga tepat.')
    s = R(s, 'This estimate uses RM2.60/kg.*', 'WhatsApp us for an exact price.')
    s = R(s, "  msgOnce:'One-off collection.",
          "  msgHarga:(k,f)=>'Hello Orang Minyak. I would like an exact price. My estimate: '+k+' kg a week ('+f+').',\n"
          "  fq:{once:'one-off',week:'weekly',corp:'large volume'},\n  msgOnce:'One-off collection.")
    s = R(s, "  msgOnce:'Kutipan sekali sahaja.",
          "  msgHarga:(k,f)=>'Salam Orang Minyak. Saya nak harga tepat. Anggaran saya: '+k+' kg seminggu ('+f+').',\n"
          "  fq:{once:'sekali sahaja',week:'setiap minggu',corp:'volum besar'},\n  msgOnce:'Kutipan sekali sahaja.")
    s = R(s, "$('oMsg').textContent=msg;\n", "$('oMsg').textContent=msg;\n  $('waHarga').href=waLink(D().msgHarga(kg,D().fq[freq]));\n")
    pairs = ''.join(f"'{a}':'{b}'," for a, b in EN_BARU.items())
    s = R(s, "'Kalkulator':'Calculator',", "'Kalkulator':'Calculator'," + pairs)
    css = ('.out-note{font-size:.82rem;color:var(--deep-muted);border-left:3px solid var(--oil);padding-left:10px}\n'
           '.out-btns{display:grid;gap:10px}\n'
           '.btn-line-lt{background:transparent;border:1.5px solid #3a5446;color:var(--deep-ink)}\n')
    s = R(s, '@media (max-width:860px){.calc-grid', css + '@media (max-width:860px){.calc-grid')
    return s


blok = re.search(r'          <div class="rangerow">.*?\n          </div>\n', src, re.S).group(0)
SETKG = "function setKg(v){kg=Math.max(1,Math.min(5000,Math.round(+v)||1));$('kgR').value=Math.min(kg,400);$('kgN').value=kg;calc();}"
INPUTS = "$('kgR').oninput=e=>setKg(e.target.value);\n$('kgN').oninput=e=>{if(e.target.value!=='')setKg(e.target.value)};"

# ---------- Versi SLIDER ----------
sl = umum(src)
sl = R(sl, blok,
       '          <div class="kgbig"><span id="kgShow">60</span><em>kg</em><small data-i>seminggu</small></div>\n'
       '          <input type="range" class="bigrange" id="kgR" min="5" max="400" step="5" value="60" aria-labelledby="kgLbl">\n'
       '          <div class="ticks" aria-hidden="true"><span>5</span><span>100</span><span>200</span><span>300</span><span>400+</span></div>\n'
       '          <input type="hidden" id="kgN" value="60">\n')
sl = R(sl, '<label for="kgR" id="kgLbl" data-i>', '<label for="kgR" id="kgLbl" data-i>')
sl = R(sl, SETKG,
       "function setKg(v){kg=Math.max(1,Math.min(5000,Math.round(+v)||1));const r=$('kgR');r.value=Math.min(kg,400);$('kgN').value=kg;"
       "$('kgShow').textContent=kg>=400?'400+':kg;r.style.setProperty('--p',((r.value-r.min)/(r.max-r.min)*100)+'%');calc();}")
sl = R(sl, INPUTS, "$('kgR').oninput=e=>setKg(e.target.value);\nsetKg(60);")
sl = R(sl, '.out-note{',
       '.kgbig{display:flex;align-items:baseline;gap:8px;font-family:var(--f-disp);font-weight:800;line-height:1}\n'
       '.kgbig span{font-size:clamp(3.4rem,9vw,4.6rem);color:var(--ink);font-variation-settings:"wdth" 75}\n'
       '.kgbig em{font-style:normal;font-size:1.6rem;color:var(--green-2)}\n'
       '.kgbig small{font:500 .9rem var(--f-body);color:var(--muted)}\n'
       '.bigrange{-webkit-appearance:none;appearance:none;width:100%;height:44px;background:transparent;cursor:pointer;--p:14%}\n'
       '.bigrange::-webkit-slider-runnable-track{height:12px;border-radius:99px;background:linear-gradient(90deg,var(--green-2) var(--p),var(--line) var(--p))}\n'
       '.bigrange::-moz-range-track{height:12px;border-radius:99px;background:var(--line)}\n'
       '.bigrange::-moz-range-progress{height:12px;border-radius:99px;background:var(--green-2)}\n'
       '.bigrange::-webkit-slider-thumb{-webkit-appearance:none;width:34px;height:34px;margin-top:-11px;border-radius:50%;background:var(--oil);border:4px solid var(--bg);box-shadow:0 0 0 2px var(--oil),0 4px 14px rgba(0,0,0,.4)}\n'
       '.bigrange::-moz-range-thumb{width:28px;height:28px;border-radius:50%;background:var(--oil);border:4px solid var(--bg)}\n'
       '.ticks{display:flex;justify-content:space-between;font:500 .74rem var(--f-mono);color:var(--muted);margin-top:-4px}\n'
       '.out-note{')
open('slider.html', 'w', encoding='utf-8', newline='\n').write(sl)

# ---------- Versi KALKULATOR (kira bekas) ----------
B = [('b15', 'Botol 1.5 L', 1.5, 0), ('j5', 'Jerikan 5 L', 5, 0), ('j20', 'Jerikan 20 L', 20, 3), ('t200', 'Tong 200 L', 200, 0)]
kk = umum(src)
kk = R(kk, '<label for="kgR" id="kgLbl" data-i>Anggaran minyak terpakai seminggu (kg)</label>',
       '<span class="lbl" id="kgLbl" data-i>Berapa bekas minyak terpakai anda seminggu?</span>')
rows = ''.join(
    f'            <div class="bk"><span data-i>{n}</span><div class="step">'
    f'<button type="button" aria-label="Kurang {n}" data-b="{k}" data-d="-1">&minus;</button>'
    f'<output id="c_{k}">{c}</output>'
    f'<button type="button" aria-label="Tambah {n}" data-b="{k}" data-d="1">+</button></div></div>\n'
    for k, n, l, c in B)
kk = R(kk, blok,
       '          <div class="bekas" role="group" aria-labelledby="kgLbl">\n' + rows + '          </div>\n'
       '          <div class="bk-tot"><span data-i>Jumlah anggaran</span><b><span id="kgShow">54</span> kg</b></div>\n')
kk = R(kk, "let lang='ms', seg='r', freq='week', kg=60;", "let lang='ms', seg='r', freq='week', kg=54;")
kk = R(kk, SETKG, "")
kk = R(kk, INPUTS,
       "const BK={" + ','.join(f"{k}:{{l:{l},n:{c}}}" for k, n, l, c in B) + "};\n"
       "function bekasKg(){let L=0;for(const k in BK)L+=BK[k].l*BK[k].n;kg=Math.max(1,Math.round(L*0.9));$('kgShow').textContent=kg;calc();}\n"
       "document.querySelectorAll('.step button').forEach(b=>b.onclick=()=>{const o=BK[b.dataset.b];o.n=Math.max(0,Math.min(99,o.n+(+b.dataset.d)));$('c_'+b.dataset.b).textContent=o.n;bekasKg();});\n"
       "bekasKg();")
kk = R(kk, '.out-note{',
       '.bekas{display:grid;gap:8px}\n'
       '.bk{display:flex;align-items:center;justify-content:space-between;gap:12px;border:1.5px solid var(--line);background:var(--paper);border-radius:12px;padding:8px 8px 8px 14px;font-weight:600}\n'
       '.step{display:flex;align-items:center;gap:4px}\n'
       '.step button{width:44px;height:44px;border-radius:10px;border:1.5px solid var(--line);background:var(--bg);color:var(--ink);font:700 1.3rem var(--f-body);cursor:pointer}\n'
       '.step button:active{background:var(--green-soft)}\n'
       '.step output{min-width:34px;text-align:center;font:600 1.15rem var(--f-mono)}\n'
       '.bk-tot{display:flex;justify-content:space-between;align-items:baseline;border-top:1px dashed var(--line);padding-top:12px;color:var(--muted);font-size:.9rem}\n'
       '.bk-tot b{font:800 1.6rem var(--f-disp);color:var(--ink)}\n'
       '.out-note{')
open('kalkulator.html', 'w', encoding='utf-8', newline='\n').write(kk)
print('ok')
