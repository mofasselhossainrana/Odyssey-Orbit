# Packs the whole app (shell + 4 story pages + styles + scripts + images) into ONE html file that can be
# downloaded and shared, and opened with a double-click. Run from the project folder:  python tools/bundle.py
# Output: share/Odyssey-Orbit.html (git-ignored)
import base64, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
rd = lambda p: open(p, encoding='utf-8').read()
b64 = lambda p, mime: 'data:' + mime + ';base64,' + base64.b64encode(open(p, 'rb').read()).decode()
IMG = 'assets/images/'

def must(s, old, new):
    if old not in s: sys.exit('MISSING: ' + old[:100])
    return s.replace(old, new)

def script(code): return '<script>' + code.replace('</script', '<\\/script') + '</script>'

# shared scripts, referenced from index.html as assets/js/... and from the story pages as ../assets/js/...
JS = {name: rd('assets/js/' + name) for name in ('mascots.js', 'moon.js')}
def inline_js(html, prefix):
    for name, code in JS.items():
        tag = '<script src="' + prefix + 'assets/js/' + name + '"></script>'
        if tag in html: html = html.replace(tag, script(code))
    return html

STORIES = ('surveyor3.html', 'apollo17-lrv.html', 'opportunity.html', 'ingenuity.html')
PAGES = {'stories/' + p: inline_js(rd('stories/' + p), '../') for p in STORIES}   # keys match MACHINES[].page

s = inline_js(rd('index.html'), '')
# the app shell's own stylesheet and script go inline
css = must(rd('assets/css/main.css'), 'url(../images/backgrounds/space-bg.webp)', 'url(' + b64(IMG + 'backgrounds/space-bg.webp', 'image/webp') + ')')
s = must(s, '<link rel="stylesheet" href="assets/css/main.css">', '<style>\n' + css + '</style>')
s = must(s, '<script src="assets/js/app.js"></script>', script(rd('assets/js/app.js')))

masc = b64(IMG + 'characters/mascot-rover.png', 'image/png')
s = must(s, 'src="' + IMG + 'brand/logo-explorers.png"', 'src="' + b64(IMG + 'brand/logo-explorers.png', 'image/png') + '"')
s = must(s, "$('logo').src='" + IMG + "brand/logo-home.png';$('heroImg').src='" + IMG + "characters/mascot-rover.png';",
         "const MASCOT_PNG='" + masc + "';$('heroImg').src=MASCOT_PNG;")
s = must(s, "const LOGO_HOME='" + IMG + "brand/logo-home.png';",
         "const LOGO_HOME='" + b64(IMG + 'brand/logo-home.png', 'image/png') + "';")
s = s.replace("'" + IMG + "characters/mascot-rover.png'", 'MASCOT_PNG')
# story pages travel inside this file and open in the frame with srcdoc; their two images reuse the
# (already embedded) images of the Home page instead of being embedded a second time
s = must(s, 'frame.src=m.page}', "frame.removeAttribute('src');frame.srcdoc=STORY_PAGES[m.page].split('../" + IMG + "brand/title.png').join(document.querySelector('.titleimg img').src).split('../" + IMG + "brand/nasa-badge.webp').join(document.querySelector('.nasabadge img').src)}")
s = must(s, "if(curStory){frame.src='about:blank';curStory=''}", "if(curStory){frame.removeAttribute('srcdoc');frame.src='about:blank';curStory=''}")
s = must(s, 'src="' + IMG + 'brand/nasa-badge.webp"', 'src="' + b64(IMG + 'brand/nasa-badge.webp', 'image/webp') + '"')
# About section: the five team photos
for f, mime in (('team-1.webp', 'image/webp'), ('team-2.jpg', 'image/jpeg'), ('team-3.jpg', 'image/jpeg'),
                ('team-4.jpg', 'image/jpeg'), ('team-5.jpg', 'image/jpeg')):
    s = must(s, 'src="' + IMG + 'team/' + f + '"', 'src="' + b64(IMG + 'team/' + f, mime) + '"')
s = must(s, 'src="' + IMG + 'brand/title.png"', 'src="' + b64(IMG + 'brand/title.png', 'image/png') + '"')
pages_js = 'const STORY_PAGES=' + json.dumps(PAGES, ensure_ascii=False).replace('</', '<\\/') + ';'
s = must(s, '/* ---------- settings ---------- */', pages_js + '\n/* ---------- settings ---------- */')
os.makedirs('share', exist_ok=True)
out = 'share/Odyssey-Orbit.html'
open(out, 'w', encoding='utf-8', newline='\n').write(s)
print(out, round(len(s.encode('utf-8')) / 1048576, 2), 'MB')
