/* Odyssey & Orbit: app shell logic (router, Explorers cards, NASA Archive search, story frame) */
/* ---------- settings ---------- */
const GITHUB_URL='https://github.com/odysseyorbit10-prog/Odyssey_Orbit';   /* the team's GitHub repository */
const MACHINES=[
 {id:'surveyor3',name:'SURVEYOR 3',yr:'1967',world:'moon',page:'stories/surveyor3.html'},
 {id:'lrv',name:'APOLLO 17 LRV',yr:'1972',world:'moon',page:'stories/apollo17-lrv.html'},
 {id:'opportunity',name:'OPPORTUNITY',yr:'2004',world:'mars',page:'stories/opportunity.html'},
 {id:'ingenuity',name:'INGENUITY',yr:'2021',world:'mars',page:'stories/ingenuity.html'}];
const ORDER=MACHINES.map(m=>m.id);
const $=i=>document.getElementById(i);
$('gh').href=GITHUB_URL;

$('logo').src='assets/images/brand/logo-home.png';$('heroImg').src='assets/images/characters/mascot-rover.png';
/* the new team logo is used on every page (Home shows it larger) */
const LOGO_HOME='assets/images/brand/logo-home.png';let LOGO_DEFAULT=LOGO_HOME;
const HAS3D=typeof THREE!=='undefined'&&typeof MASCOT!=='undefined';
/* the stories speak through this window (it has the visitor's click), so start loading the voices now */
try{speechSynthesis.getVoices()}catch(e){}

/* ---------- twinkling stars + decorative planets ---------- */
const sc=$('stars'),sx=sc.getContext('2d');let ST=[];
function rsz(){sc.width=innerWidth;sc.height=innerHeight;ST=Array.from({length:Math.round(innerWidth*innerHeight/9000)},()=>({x:Math.random()*innerWidth,y:Math.random()*innerHeight*.8,r:.6+Math.random()*1.6,p:Math.random()*6.28,s:.6+Math.random()*1.8}))}
addEventListener('resize',rsz);rsz();
(function tw(t){requestAnimationFrame(tw);if(document.hidden||$('story').classList.contains('on'))return;sx.clearRect(0,0,sc.width,sc.height);
ST.forEach(s=>{const a=.35+.65*Math.abs(Math.sin(t/1000*s.s+s.p));sx.globalAlpha=a;sx.fillStyle='#fff';sx.beginPath();sx.arc(s.x,s.y,s.r,0,7);sx.fill();if(s.r>1.9){sx.globalAlpha=a*.5;sx.fillRect(s.x-s.r*3,s.y-.4,s.r*6,.8);sx.fillRect(s.x-.4,s.y-s.r*3,.8,s.r*6)}});sx.globalAlpha=1})(0);
function planets(view){const P=$('planets');P.innerHTML='';const add=(css,inner)=>{const d=document.createElement('div');d.className='planet';d.style.cssText=css;d.innerHTML=inner||'';P.appendChild(d)};
P.style.cssText='position:fixed;inset:0;z-index:2;pointer-events:none';
/* Home and Machine Selection pages: no extra planets (only the space background art) */
}

/* ---------- Explorers cards: each machine drawn as a 3D cartoon on its world ---------- */
function sceneArt(cv,world,seed){const x=cv.getContext('2d'),W=cv.width,H=cv.height;let s=seed;const r=()=>(s=(s*16807)%2147483647)/2147483647;
let g=x.createLinearGradient(0,0,0,H);if(world==='moon'){g.addColorStop(0,'#0c0f4a');g.addColorStop(.6,'#3a2a9a');g.addColorStop(1,'#6a4fc0')}else{g.addColorStop(0,'#7a1e14');g.addColorStop(.55,'#e2602a');g.addColorStop(1,'#ffae6a')}x.fillStyle=g;x.fillRect(0,0,W,H);
for(let i=0;i<70;i++){x.fillStyle='rgba(255,255,255,'+(world==='moon'?.4+r()*.6:.15+r()*.3)+')';x.beginPath();x.arc(r()*W,r()*H*.6,.6+r()*1.6,0,7);x.fill()}
if(world==='moon'){x.fillStyle='#4f8fff';x.beginPath();x.arc(W*.82,H*.16,W*.08,0,7);x.fill();x.fillStyle='#3fae5a';x.beginPath();x.arc(W*.8,H*.15,W*.03,0,7);x.fill()}
else{x.fillStyle='rgba(255,220,180,.85)';x.beginPath();x.arc(W*.8,H*.17,W*.07,0,7);x.fill()}
x.fillStyle=world==='moon'?'#4a3a8e':'#a8401e';x.beginPath();x.moveTo(0,H*.62);for(let i=0;i<=12;i++)x.lineTo(i*W/12,H*.56-Math.abs(Math.sin(i*1.3+seed))*H*.08);x.lineTo(W,H);x.lineTo(0,H);x.fill();
g=x.createLinearGradient(0,H*.6,0,H);if(world==='moon'){g.addColorStop(0,'#a59ad8');g.addColorStop(1,'#5c4ea6')}else{g.addColorStop(0,'#e88a52');g.addColorStop(1,'#9a3e1e')}x.fillStyle=g;x.beginPath();x.moveTo(0,H*.7);x.quadraticCurveTo(W*.5,H*.6,W,H*.7);x.lineTo(W,H);x.lineTo(0,H);x.fill();
for(let i=0;i<9;i++){const cx=r()*W,cy=H*.74+r()*H*.22,rr=4+r()*12;x.fillStyle=world==='moon'?'rgba(60,40,120,.55)':'rgba(110,40,15,.5)';x.beginPath();x.ellipse(cx,cy,rr*1.6,rr*.6,0,0,7);x.fill()}}
function buildCards(){[['moon','moonCards'],['mars','marsCards']].forEach(([w,id])=>{const box=$(id);box.innerHTML='';MACHINES.filter(m=>m.world===w).forEach((m,k)=>{
const b=document.createElement('button');b.className='card';b.setAttribute('aria-label','Explore '+m.name);
b.innerHTML='<canvas class="scene" width="300" height="384"></canvas><img alt=""><span class="yr">'+m.yr+'</span><span class="nm">'+m.name+'</span>';
sceneArt(b.querySelector('canvas'),w,7+k*31+(w==='mars'?100:0));
try{if(HAS3D)b.querySelector('img').src=MASCOT.snapshot(m.id,420,{mood:'happy',wave:1,t:.62,pad:m.id==='lrv'?1.34:undefined});else b.querySelector('img').src='assets/images/characters/mascot-rover.png'}catch(e){console.warn(e);b.querySelector('img').src='assets/images/characters/mascot-rover.png'}
b.onclick=()=>go('#/story/'+m.id);box.appendChild(b)})})}

/* ---------- router: the nav works from anywhere ---------- */
const frame=$('frame');let curStory='';
function toast(t){const e=$('toast');e.textContent=t;e.classList.add('on');clearTimeout(toast.k);toast.k=setTimeout(()=>e.classList.remove('on'),2200)}
function go(h){if(location.hash===h)route();else location.hash=h}
let lastView='',cameFromHome=false;
/* Back on the Machine Selection page: step back in browser history when we came from Home, otherwise open Home */
$('exBack').onclick=()=>{if(cameFromHome&&history.length>1)history.back();else go('#/')};
/* ---------- About: its own page (#/about); only that page scrolls, and its parts fade in as they come into view ---------- */
const ABW=document.querySelector('#about .abw');
if('IntersectionObserver' in window){const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{root:ABW,threshold:.12});document.querySelectorAll('.ab-rv').forEach(e=>io.observe(e))}
else document.querySelectorAll('.ab-rv').forEach(e=>e.classList.add('in'));
function route(){const h=location.hash||'#/',parts=h.replace(/^#\/?/,'').split('/');let v=parts[0]||'home';
if(!['home','about','explorers','archive','story'].includes(v))v='home';
const fd=$('fade'),newStory=v==='story'&&curStory!==((MACHINES.find(q=>q.id===parts[1])||MACHINES[0]).id),same=$(v).classList.contains('on')&&!newStory;
const apply=()=>{document.querySelectorAll('.view').forEach(e=>e.classList.toggle('on',e.id===v));
document.body.classList.toggle('ex',v==='explorers');document.body.classList.toggle('soft',v==='about'||v==='archive');document.body.classList.toggle('home',v==='home');cameFromHome=v==='explorers'&&lastView==='home'?true:v==='explorers'?cameFromHome:false;lastView=v;
document.querySelectorAll('.nl[data-r]').forEach(a=>a.classList.toggle('on',a.dataset.r===(v==='story'?'explorers':v)));
$('nav').classList.toggle('solid',v==='story');$('logo').src=v==='home'?LOGO_HOME:LOGO_DEFAULT;$('logo').classList.toggle('home',v==='home');$('stars').style.display=$('bg').style.display=v==='story'?'none':'';planets(v==='story'?'':v);
if(v==='story'){const m=MACHINES.find(q=>q.id===parts[1])||MACHINES[0];if(curStory!==m.id){curStory=m.id;frame.src=m.page}document.title=m.name+' — Odyssey & Orbit'}
else{if(curStory){frame.src='about:blank';curStory=''}document.title='Odyssey & Orbit — Abandoned, But Not Forgotten'}
if(v==='explorers'&&!$('moonCards').children.length)buildCards();
if(v==='archive')arOpen();
if(v==='about'&&!same)ABW.scrollTop=0};
if(same){apply();return}
fd.classList.add('on');setTimeout(()=>{apply();if(newStory)frameReady().then(()=>fd.classList.remove('on'));else fd.classList.remove('on')},180)}
/* resolves when the story page in the iframe has its document ready (max 5 s), plus a moment for its first frame */
function frameReady(){const t0=Date.now(),want=frame.getAttribute('src')||'';return new Promise(r=>{(function chk(){let ok=false;try{const d=frame.contentDocument;ok=!!d&&d.readyState!=='loading'&&frame.contentWindow.location.href.indexOf(want)>=0&&want!=='about:blank'}catch(e){ok=true}
 if(ok||Date.now()-t0>5000)setTimeout(r,ok?250:0);else setTimeout(chk,80)})()})}
addEventListener('hashchange',route);
$('brand').onclick=()=>go('#/');$('go').onclick=()=>go('#/explorers');

/* ---------- NASA Archive: live search of NASA's Image and Video Library API (images-api.nasa.gov) ---------- */
const AR={q:'',page:1,shown:0,total:0,busy:false,want:'',seq:0};
const AR_FOR={surveyor3:'Surveyor 3',lrv:'Apollo 17 Lunar Roving Vehicle',opportunity:'Opportunity rover',ingenuity:'Ingenuity helicopter'};
const AR_PAGE=24;
function arText(html){try{return (new DOMParser().parseFromString(String(html||''),'text/html').body.textContent||'').replace(/\s+/g,' ').trim()}catch(e){return String(html||'')}}
function arDate(s){const d=new Date(s);return isNaN(d)?'':d.toLocaleDateString('en-GB',{day:'numeric',month:'short',year:'numeric'})}
function arEl(tag,cls,txt){const e=document.createElement(tag);if(cls)e.className=cls;if(txt!=null)e.textContent=txt;return e}
function arMsg(em,txt,retry){const m=arEl('div','arc-msg');m.appendChild(arEl('span','em',em));m.appendChild(document.createTextNode(txt));
 if(retry){const b=arEl('button','arc-more','Try again');b.type='button';b.style.margin='16px auto 0';b.onclick=retry;m.appendChild(b)}$('arGrid').appendChild(m)}
function arCard(it){const d=(it.data&&it.data[0])||{},links=it.links||[];const pv=(links.find(l=>l.rel==='preview')||links[0]||{}).href;
 const a=arEl('a','arc-card');a.href='https://images.nasa.gov/details/'+encodeURIComponent(d.nasa_id||'');a.target='_blank';a.rel='noopener noreferrer';
 a.title=(d.title||'NASA photo')+' — opens on NASA\'s website';
 const ph=arEl('div','ph');if(pv){const im=arEl('img');im.loading='lazy';im.alt=d.title||'NASA photo';im.src=pv.replace(/^http:/,'https:');im.onerror=()=>{im.remove();ph.appendChild(arEl('span','noimg','🛰️'))};ph.appendChild(im)}else ph.appendChild(arEl('span','noimg','🛰️'));
 if(d.nasa_id)ph.appendChild(arEl('span','id',d.nasa_id));a.appendChild(ph);
 const bd=arEl('div','bd');bd.appendChild(arEl('h3','',d.title||'Untitled NASA photo'));
 const mt=[arDate(d.date_created),d.center].filter(Boolean).join(' · ');if(mt)bd.appendChild(arEl('div','mt',mt));
 const ds=arText(d.description||d.description_508);if(ds)bd.appendChild(arEl('p','',ds));
 bd.appendChild(arEl('span','op','Open on NASA ↗'));a.appendChild(bd);return a}
async function arSearch(q,more){q=String(q||'').trim();if(!q){$('arQ').focus();return}
 const seq=++AR.seq,grid=$('arGrid'),st=$('arStatus'),mb=$('arMore');
 if(!more){AR.q=q;AR.page=1;AR.shown=0;AR.total=0;$('arQ').value=q;grid.innerHTML='';for(let i=0;i<8;i++)grid.appendChild(arEl('div','arc-skel'));st.textContent='Searching NASA for "'+q+'"…';mb.hidden=true}
 else{AR.page++;mb.disabled=true;mb.textContent='Loading…'}
 AR.busy=true;
 try{const r=await fetch('https://images-api.nasa.gov/search?media_type=image&page_size='+AR_PAGE+'&page='+AR.page+'&q='+encodeURIComponent(q));
  if(!r.ok)throw new Error('HTTP '+r.status);const j=await r.json();if(seq!==AR.seq)return;
  const items=((j.collection||{}).items||[]).filter(it=>it.data&&it.data[0]);AR.total=((j.collection||{}).metadata||{}).total_hits||items.length;
  if(!more)grid.innerHTML='';items.forEach(it=>grid.appendChild(arCard(it)));AR.shown+=items.length;
  if(!AR.shown){st.textContent='';arMsg('🔭','No NASA photos found for "'+q+'". Try another name, like "Apollo 17", "Mars rover" or "Moon".')}
  else{st.innerHTML='';st.append('Showing ',arEl('b','',String(AR.shown)),' of '+AR.total.toLocaleString('en')+' NASA photos for ',arEl('b','','"'+q+'"'))}
  const hasNext=((j.collection||{}).links||[]).some(l=>l.rel==='next');mb.hidden=!(hasNext&&AR.shown<AR.total&&items.length);mb.disabled=false;mb.textContent='Show more photos'}
 catch(e){if(seq!==AR.seq)return;console.warn(e);if(more){AR.page--;mb.disabled=false;mb.textContent='Show more photos';toast('Could not load more photos. Please try again.')}
  else{grid.innerHTML='';st.textContent='';arMsg('📡','We could not reach NASA\'s photo library. Please check your internet connection and try again.',()=>arSearch(q))}}
 finally{if(seq===AR.seq)AR.busy=false}}
$('arForm').onsubmit=e=>{e.preventDefault();arSearch($('arQ').value)};
$('arChips').querySelectorAll('button').forEach(b=>b.onclick=()=>arSearch(b.dataset.q));
$('arMore').onclick=()=>{if(!AR.busy)arSearch(AR.q,true)};
/* called by the router each time the archive opens: first visit shows Surveyor 3 (or the machine whose story just ended) */
function arOpen(){const q=AR.want||(!AR.q?'Surveyor 3':'');AR.want='';if(q&&q!==AR.q)arSearch(q)}

/* messages from the story pages: "next" after a story's end screen, or "archive" after the last one */
addEventListener('message',e=>{const d=e.data||{};if(e.source!==frame.contentWindow)return;
if(d.type==='next'){const i=ORDER.indexOf(d.from);if(i>=0&&i<ORDER.length-1)go('#/story/'+ORDER[i+1]);else{AR.want=AR_FOR[d.from]||'';go('#/archive')}}
else if(d.type==='archive'){AR.want=AR_FOR[d.from]||'';go('#/archive')}
else if(d.type==='home')go('#/');});
route();
