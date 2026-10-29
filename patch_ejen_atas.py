# Orang Minyak: jalur "Jadi Ejen" di paling atas + pautan menu + id #ejen pada kad Program Ejen
p = 'index.html'
s = open(p, encoding='utf-8').read()


def R(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:80])
    s = s.replace(a, b)


R('<header class="top">',
  '<a class="ejen-bar js-wa" data-msg="msgEjen" href="https://wa.me/60178899786" target="_blank" rel="noopener">'
  '<span class="eb-tag" data-i>Jadi Ejen Kami</span>'
  '<span class="eb-txt" data-i>Kenalkan sebuah restoran atau kantin, dapat <b>RM30</b> setiap premis</span>'
  '<span class="eb-go" data-i>Daftar &rarr;</span></a>\n<header class="top">')
R('      <a href="#soalan" data-i>Soalan</a>\n    </nav>',
  '      <a href="#soalan" data-i>Soalan</a>\n      <a class="nav-ejen js-wa" data-msg="msgEjen" href="https://wa.me/60178899786" target="_blank" rel="noopener" data-i>Jadi ejen</a>\n    </nav>')
R('<section class="block">\n  <div class="wrap">\n    <div class="duo">',
  '<section class="block" id="ejen">\n  <div class="wrap">\n    <div class="duo">')
R('@media (max-width:980px){nav.links{display:none}}',
  '@media (max-width:980px){nav.links{display:none}}\n'
  '.ejen-bar{display:flex;align-items:center;justify-content:center;gap:12px;flex-wrap:wrap;padding:9px 16px;background:var(--oil);color:#1A1204;text-decoration:none;font-size:.9rem;line-height:1.3;text-align:center}\n'
  '.ejen-bar .eb-tag{font-family:var(--f-mono);font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;background:#1A1204;color:var(--oil);padding:3px 9px;border-radius:99px;white-space:nowrap}\n'
  '.ejen-bar .eb-go{font-weight:700;text-decoration:underline;text-underline-offset:3px;white-space:nowrap}\n'
  '.ejen-bar:hover .eb-go{text-decoration-thickness:2px}\n'
  'nav.links a.nav-ejen{color:var(--oil);font-weight:600}\n'
  '@media (max-width:560px){.ejen-bar{gap:6px 10px;font-size:.84rem}}')
R("'Kalkulator':'Calculator',",
  "'Kalkulator':'Calculator','Jadi Ejen Kami':'Become Our Agent',"
  "'Kenalkan sebuah restoran atau kantin, dapat <b>RM30</b> setiap premis':'Refer a restaurant or canteen, earn <b>RM30</b> per business',"
  "'Daftar &rarr;':'Join &rarr;','Jadi ejen':'Become an agent',")
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok')
