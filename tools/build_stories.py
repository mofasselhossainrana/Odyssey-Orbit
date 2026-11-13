# Builds the Moon story pages (stories/surveyor3.html, stories/apollo17-lrv.html) from the shared story
# template (tools/story-template.html, a pristine copy of stories/ingenuity.html) and wires every story's
# end screen (Recap / Next) into the app.
# Run from the project folder:  python tools/build_stories.py
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
from moon_content import SURVEYOR, LRV, COMMON  # noqa: E402

import shutil
TEMPLATE = 'tools/story-template.html'
if not os.path.exists(TEMPLATE):                    # pristine copy of the template, taken once
    shutil.copy('stories/ingenuity.html', TEMPLATE)
BASE = open(TEMPLATE, encoding='utf-8').read()

class Page:
    def __init__(self, s): self.s = s
    def rep(self, old, new, all_=False):
        if old not in self.s: sys.exit('MISSING: ' + old[:120])
        self.s = self.s.replace(old, new) if all_ else self.s.replace(old, new, 1)
    def region(self, a, b, new):
        i = self.s.find(a)
        if i < 0: sys.exit('MISSING region start: ' + a[:120])
        j = self.s.find(b, i)
        if j < 0: sys.exit('MISSING region end: ' + b[:120])
        self.s = self.s[:i] + new + self.s[j + len(b):]
    def line(self, prefix, new):
        i = self.s.find('\n' + prefix)
        if i < 0: sys.exit('MISSING line: ' + prefix[:120])
        i += 1; j = self.s.find('\n', i)
        self.s = self.s[:i] + new + self.s[j:]

def moon_page(c):
    p = Page(BASE)
    p.rep('<title>Ingenuity — Abandoned but not Forgotten</title>', '<title>' + c['title'] + '</title>')
    p.rep('#8a4326,#1d0c12', '#4a5a9a,#0b0f26', all_=True)
    p.rep('overflow:hidden;background:#2a140c}', 'overflow:hidden;background:#15151c}')
    p.line('<div id="ov">', c['ov'])
    p.rep('<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>',
          '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>\n<script src="../assets/js/mascots.js"></script>\n<script src="../assets/js/moon.js"></script>')
    p.region('function mkLRO(){', "$('hero').style.display='none'}})();", c['mascot'])
    p.rep("who.textContent=w==='LRO'?'Ingenuity':w;", "who.textContent=w==='LRO'?'" + c['who'] + "':w;")
    p.line('const IMG_C=', 'const MOONIMG=MOONMAP(),IMG_C=MOONIMG.c,IMG_H=MOONIMG.h;/* stylized Moon maps made in assets/js/moon.js */')
    p.rep('new THREE.PointsMaterial({size:1.6,sizeAttenuation:false})', 'new THREE.PointsMaterial({size:1.6,sizeAttenuation:false,fog:false})')
    p.rep('new THREE.MeshBasicMaterial({map:t,side:THREE.BackSide,transparent:true,blending:THREE.AdditiveBlending,depthWrite:false})',
          'new THREE.MeshBasicMaterial({map:t,side:THREE.BackSide,transparent:true,blending:THREE.AdditiveBlending,depthWrite:false,fog:false})')
    p.region('const ING_SRC=', '];\nlet HD=null;', c['sites'] + '\nlet HD=null;')
    p.rep("/* Perseverance landed at the same spot: its pin shares Ingenuity's place, so only one marker is drawn */\npins[1].m.visible=false;pins[1].ring.visible=false;", c['pinhide'])
    p.region('const STOPS=[', '\nconst rmE=', c['stops'] + COMMON['wl'] + '\nconst rmE=')
    p.region('function rmDraw(){', '\nfunction rmShow(', COMMON['rmdraw'] + '\nfunction rmShow(')
    p.rep('const OPP_SRC=ING_SRC,OPP_MAP=ING_MAP;', c['srcconst'])
    p.rep('">Flight map ↗</a>', '">' + c['maplabel'] + ' ↗</a>')
    p.rep('°E (Mars)</small>', '°E (Moon)</small>')
    p.rep("$('t1').textContent='Ingenuity'", "$('t1').textContent='" + c['who'] + "'")
    p.rep('(like the delta layers in Jezero)', '(hidden on the Moon)')
    p.rep('/* no hematite "blueberries" in Jezero crater */', '/* no hematite "blueberries" on the Moon */')
    p.rep('Data: NASA/JPL-Caltech · Mars globe: stylized illustration', 'Data: NASA · Moon globe: stylized illustration')
    p.rep('bumpScale:2,displacementMap:th,displacementScale:.32,displacementBias:-.16', 'bumpScale:.7,displacementMap:th,displacementScale:.14,displacementBias:-.07')
    p.rep('5+hAtV(s.lat,s.lon)*.32-.16+.04', '5+hAtV(s.lat,s.lon)*.14-.07+.04')
    p.rep('mesh(tg,M(0xb86a3e,{roughness:1,map:regT})', 'mesh(tg,M(0x8e8b86,{roughness:1,map:regT})')
    p.rep('M(0x6e4330,{roughness:1})', 'M(0x5f5c58,{roughness:1})')
    p.line('{const tm=new THREE.MeshBasicMaterial', c['tracks'])
    p.region('/* Perseverance (a simplified model', 'let heliFly=1;', COMMON['lmd'] + c['models'])
    p.region('function setSurf(m){', 'HALO.position.copy(SUNM.position)}', COMMON['setsurf'])
    p.line('const sky=on=>', COMMON['sky'])
    p.line('if(heliFly&&HELI.userData.base)', "if(typeof surfTick==='function')surfTick(t);SUNM.position.copy(sun.position).normalize().multiplyScalar(360);HALO.position.copy(SUNM.position)}")
    p.rep('color:0xffd9b0,transparent:true,opacity:.7', 'color:0xe8ecff,transparent:true,opacity:.6')
    p.region('const FB=[', '\n];\nconst FBIMG={};', c['fb'] + '\nconst FBIMG={};')
    p.line('const PIAU=', COMMON['piau'])
    p.region('/* illustration for the launch slide', "return c.toDataURL('image/jpeg',.88)}", COMMON['illus'])
    p.rep('im.src=drawLaunch()', 'im.src=drawIllus(f.draw)')
    p.rep("'https://photojournal.jpl.nasa.gov/catalog/'+f.pia", 'PIAPAGE(f.pia)', all_=True)
    # the data-card "Photo" link: Apollo photos live on images.nasa.gov (IDs are case-sensitive there)
    p.rep("href=\"https://photojournal.jpl.nasa.gov/catalog/'+f.pia+'\"", "href=\"'+PIAPAGE(f.pia)+'\"", all_=True)
    p.rep('NASA · Ingenuity Mars Helicopter ↗', c['srcname'] + ' ↗')
    p.region('/* top-down aerial views', 'for(let y=0;y<H;y+=3)', c['pics'] + 'for(let y=0;y<H;y+=3)')
    p.rep("x.fillText('INGENUITY · '+(k===1?'NAVCAM (B&W)':'COLOR CAMERA')+' · FRAME '+String(1000+k*173),12,H-12)}", c['stamp'])
    p.line('const PICS=', c['picnames'])
    p.rep("My pick: ⭐ Séítah, where I flew over sand the rover could not cross!", c['pick'])
    p.rep("(i===3?' ⭐':'')", "(i===" + str(c['picki']) + "?' ⭐':'')")
    p.rep("' · ★ FIRST FLIGHT':i===STOPS.length-1?' · ✕ LAST FLIGHT'", c['tags'])
    p.rep('<span class="bd">P</span>', '<span class="bd">' + c['twinletter'] + '</span>')
    p.region("b.querySelector('.tg').textContent='MY PARTNER · LANDED 18 FEB 2021';", "b.querySelector('em').textContent='Jezero crater · carried me to Mars';", c['twin'])
    p.region('async function tour(again){', "await say(\"Now it's your turn! Pick any card to explore.\",4.5)}", c['tour'])
    p.region('const ACH=[', '\n];\nconst AP=', c['ach'] + '\nconst AP=')
    p.rep("pg='https://photojournal.jpl.nasa.gov/catalog/'+a.pia", 'pg=PIAPAGE(a.pia)')
    p.rep('const urls=[AIMG(a.pia,1280),AIMG2(a.pia),AIMG3(a.pia)];', 'const urls=PIAU(a.pia,1280);')
    p.rep('/* Ingenuity rests at "Valinor Hills"; Perseverance photographed it there on 4 Feb 2024 (PIA26236). */', c['fincomment'])
    p.region('const yrs=new Date().getFullYear()-2021;', 'abandoned, but not forgotten.",6);', c['finale'])
    p.rep("mood='happy';await say(\"I'm Ingenuity, NASA's little Mars helicopter! I was the first aircraft ever to fly on another planet.\",5.5);mood='';", c['intro'])
    p.rep("Want to know how I got to Mars? Let's go back in time!", c['q'])
    p.rep("That's how I got to Mars! Now let me show you where I flew.", c['after'])
    p.rep('<button id="frp" class="yl">↺ Replay</button><button id="fnx" class="pu">Next ➜</button>', c['endbtns'])
    p.line("$('fnx').onclick=", c['fnx'])
    for bad in ('Ingenuity', 'Perseverance', 'Jezero', 'HELI', 'heliFly'):
        if bad in p.s and bad not in c.get('allow', ()):
            n = p.s.count(bad); print('  note:', c['file'], 'still mentions', bad, n, 'x')
    out = 'stories/' + c['file']
    open(out, 'w', encoding='utf-8', newline='\n').write(p.s)
    print('built', out, len(p.s) // 1024, 'KB')

moon_page(SURVEYOR)
moon_page(LRV)

# ---- end screens of the two Mars pages ----
def patch(fn, fnx, endbtns):
    s = open(fn, encoding='utf-8').read()
    old = '<button id="frp" class="yl">↺ Replay</button><button id="fnx" class="pu">Next ➜</button>'
    if old in s: s = s.replace(old, endbtns)
    # replace the existing "goNext + Next button" code wherever it sits (it may share a line with other code)
    k = s.find("$('fnx').onclick=")
    if k < 0: sys.exit('MISSING fnx handler in ' + fn)
    i = s.rfind("const STORY_ID=", 0, k); i = k if i < 0 else i
    j = s.find('};', k) + 2
    s = s[:i] + fnx + s[j:]
    open(fn, 'w', encoding='utf-8', newline='\n').write(s); print('patched', fn)

patch('stories/opportunity.html', COMMON['gonext']('opportunity', 'ingenuity.html') +
      "$('fnx').onclick=()=>{const b=$('fnx');b.classList.remove('pop');void b.offsetWidth;b.classList.add('pop');setTimeout(()=>goNext('next'),350)};",
      '<button id="frp" class="yl">↺ Recap</button><button id="fnx" class="pu">Next ➜</button>')
patch('stories/ingenuity.html', COMMON['gonext']('ingenuity', '../index.html#/archive') +
      "$('fnx').onclick=()=>{const b=$('fnx');b.classList.remove('pop');void b.offsetWidth;b.classList.add('pop');setTimeout(()=>goNext('archive'),350)};",
      '<button id="frp" class="yl">↺ Recap</button><button id="fnx" class="pu"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" style="width:1.05em;height:1.05em;flex:none"><path d="M3 3h18v5H3zm1 6h16v12H4zm5 3v2h6v-2z"/></svg>NASA Archive</button>')
