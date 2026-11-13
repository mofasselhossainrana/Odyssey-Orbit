# Story content + scene code for the two Moon machines. Used by build_stories.py.
# Facts: NASA mission pages, NASA Image and Video Library captions, Guinness World Records (lunar speed record).
# Photo IDs starting with "PIA" load from NASA Photojournal, the others from images.nasa.gov.

def gonext(story_id, next_page):
    return ("const STORY_ID='" + story_id + "',NEXT_PAGE='" + next_page + "';"
            "function goNext(type){type=type||'next';if(window.parent!==window)window.parent.postMessage({type,from:STORY_ID},'*');"
            "else location.href=type==='archive'?'../index.html#/archive':NEXT_PAGE}")

COMMON = {'gonext': gonext}

COMMON['wl'] = r"""
const WL=[0];for(let i=1;i<WP.length;i++)WL.push(WL[i-1]+Math.hypot(WP[i][0]-WP[i-1][0],WP[i][1]-WP[i-1][1]));
const progAt=k=>WL[STOPI[k]]/WL[WL.length-1];
const ptAt=p=>{const d=p*WL[WL.length-1];let i=1;while(i<WL.length-1&&WL[i]<d)i++;const t=Math.max(0,Math.min(1,(d-WL[i-1])/(WL[i]-WL[i-1]||1)));return[WP[i-1][0]+(WP[i][0]-WP[i-1][0])*t,WP[i-1][1]+(WP[i][1]-WP[i-1][1])*t]};"""

COMMON['rmdraw'] = r"""function rmDraw(){const x=rmC.getContext('2d'),W=rmC.width,H=rmC.height,K=17.1,ox=60,oy=84,px=a=>ox+(a+4)*K,py=b=>oy+(3-b)*K;
if(!rmBG){rmBG=document.createElement('canvas');rmBG.width=W;rmBG.height=H;const b=rmBG.getContext('2d'),g=b.createLinearGradient(0,0,W,H);g.addColorStop(0,MAP.bg[0]);g.addColorStop(1,MAP.bg[1]);b.fillStyle=g;b.fillRect(0,0,W,H);
const r=mkRng(77);for(let i=0;i<2600;i++){b.fillStyle=r()<.5?'rgba(235,235,245,'+(r()*.06)+')':'rgba(5,5,10,'+(r()*.14)+')';b.fillRect(r()*W,r()*H,1+r()*3,1+r()*3)}
for(let i=0;i<46;i++){const cx=r()*W,cy=90+r()*(H-130),rr=4+Math.pow(r(),2)*20;b.strokeStyle='rgba(230,230,240,.10)';b.lineWidth=1.5;b.beginPath();b.arc(cx,cy,rr,0,7);b.stroke();b.fillStyle='rgba(0,0,0,.12)';b.beginPath();b.arc(cx+1,cy+1,rr*.85,0,7);b.fill()}
b.strokeStyle='rgba(230,230,255,.08)';b.lineWidth=1;for(let q=0;q<=30;q+=5){b.beginPath();b.moveTo(px(q),oy-20);b.lineTo(px(q),H-40);b.stroke()}for(let q=0;q>=-30;q-=5){b.beginPath();b.moveTo(ox-30,py(q));b.lineTo(W-20,py(q));b.stroke()}}
x.clearRect(0,0,W,H);x.drawImage(rmBG,0,0);x.save();MAP.feat(x,px,py,K);x.restore();
const tot=WL[WL.length-1],d=rmP*tot;
x.lineCap='round';x.lineJoin='round';x.setLineDash([2,9]);x.strokeStyle='rgba(235,235,255,.55)';x.lineWidth=3;x.beginPath();WP.forEach((p,i)=>(i&&!JUMP.has(i))?x.lineTo(px(p[0]),py(p[1])):x.moveTo(px(p[0]),py(p[1])));x.stroke();x.setLineDash([]);
x.save();x.strokeStyle='#ffd24a';x.lineWidth=5;x.shadowColor='rgba(255,190,60,.9)';x.shadowBlur=12;x.beginPath();x.moveTo(px(WP[0][0]),py(WP[0][1]));
for(let i=1;i<WP.length;i++){const jm=JUMP.has(i);if(WL[i]<=d){jm?x.moveTo(px(WP[i][0]),py(WP[i][1])):x.lineTo(px(WP[i][0]),py(WP[i][1]))}else{if(!jm){const t=(d-WL[i-1])/(WL[i]-WL[i-1]),a=WP[i-1][0]+(WP[i][0]-WP[i-1][0])*t,b=WP[i-1][1]+(WP[i][1]-WP[i-1][1])*t;x.lineTo(px(a),py(b))}break}}x.stroke();x.restore();
STOPS.forEach((s,k)=>{const[a,b]=WP[STOPI[k]],X=px(a),Y=py(b),on=WL[STOPI[k]]<=d+.001,hi=k===rmH,last=k===STOPS.length-1,R=hi?17:12;
x.globalAlpha=on?1:.32;if(hi){x.beginPath();x.arc(X,Y,R+8,0,7);x.fillStyle='rgba(255,210,80,.28)';x.fill()}
x.beginPath();x.arc(X,Y,R,0,7);x.fillStyle=last?'#ff5a4d':'#ffc94d';x.fill();x.lineWidth=3;x.strokeStyle='#fff';x.stroke();
x.fillStyle=last?'#fff':'#2a1700';x.font='800 '+(hi?18:15)+'px Fredoka,Arial,sans-serif';x.textAlign='center';x.textBaseline='middle';x.fillText(String(k+1),X,Y+1);
const f1='700 '+(hi?17:15)+'px Fredoka,Arial,sans-serif';x.font=f1;const w1=x.measureText(s.n).width;x.font='600 12px Arial,sans-serif';const w2=x.measureText(s.yr).width,bw=Math.max(w1,w2)+18,bh=hi?44:40,lo=LBO[k],rt=LSIDE[k]>0,bx=(rt?X+R+8:X-R-8-bw)+lo[0],by=Y-bh/2+lo[1];if(Math.abs(lo[1])>20){x.strokeStyle='rgba(255,255,255,.4)';x.lineWidth=1.5;x.beginPath();x.moveTo(X,Y-R);x.lineTo(bx+(rt?10:bw-10),by+(lo[1]<0?bh:0));x.stroke()}
x.fillStyle='rgba(12,12,26,.86)';x.strokeStyle=hi?'#ffd24a':'rgba(255,255,255,.35)';x.lineWidth=hi?2.5:1.5;x.beginPath();if(x.roundRect)x.roundRect(bx,by,bw,bh,10);else x.rect(bx,by,bw,bh);x.fill();x.stroke();
x.textAlign='left';x.textBaseline='alphabetic';x.fillStyle='#fff';x.font=f1;x.fillText(s.n,bx+9,by+18);x.fillStyle='#ffd24a';x.font='600 12px Arial,sans-serif';x.fillText(s.yr,bx+9,by+34);x.globalAlpha=1});
const rp=ptAt(rmP),RX=px(rp[0]),RY=py(rp[1]);x.beginPath();x.arc(RX,RY,11,0,7);x.fillStyle='#fff';x.fill();x.beginPath();x.arc(RX,RY,6.5,0,7);x.fillStyle='#ff7a2a';x.fill();
x.textAlign='left';x.textBaseline='alphabetic';x.fillStyle='#ffd24a';x.font='700 28px Fredoka,Arial,sans-serif';x.fillText(MAP.title,24,40);x.fillStyle='rgba(235,240,255,.88)';x.font='600 14px Arial,sans-serif';x.fillText(MAP.sub(rmP>=.999),24,60);
x.strokeStyle='#fff';x.lineWidth=3;x.beginPath();x.moveTo(24,H-26);x.lineTo(24+5*K,H-26);x.stroke();x.fillStyle='#fff';x.font='700 13px Arial,sans-serif';x.fillText(MAP.scale,24+5*K+8,H-21);
x.fillStyle='rgba(225,230,245,.72)';x.font='italic 600 12px Arial,sans-serif';x.textAlign='right';x.fillText(MAP.note,W-18,H-12);
x.textAlign='center';x.fillStyle='#fff';x.font='800 16px Arial,sans-serif';x.fillText('N',W-90,32);x.beginPath();x.moveTo(W-90,38);x.lineTo(W-98,60);x.lineTo(W-90,54);x.lineTo(W-82,60);x.closePath();x.fill()}"""

COMMON['lmd'] = r"""/* Apollo lunar module descent stage (the base that stays on the Moon after liftoff); simplified model, not a photo */
function mkLMD(){const g=new THREE.Group(),gold=M(0xd8a640,{metalness:.8,roughness:.32,emissive:0x221500}),alS=M(0xc9ced4,{metalness:.7,roughness:.35}),blk=M(0x252525,{roughness:.7});
const b=mesh(new THREE.CylinderGeometry(1.55,1.55,1.4,8),gold,[0,1.7,0],g);b.castShadow=true;b.rotation.y=Math.PI/8;
mesh(new THREE.BoxGeometry(2.3,.12,2.3),blk,[0,2.45,0],g).castShadow=true;
[0,1,2,3].forEach(i=>{const a=i*Math.PI/2+Math.PI/4,c=Math.cos(a),s=Math.sin(a);strut([c*1.35,1.9,s*1.35],[c*2.7,.18,s*2.7],.08,alS,g);strut([c*1.4,1.1,s*1.4],[c*2.1,.7,s*2.1],.05,alS,g);mesh(new THREE.CylinderGeometry(.42,.48,.12,14),alS,[c*2.7,.08,s*2.7],g).castShadow=true});
mesh(new THREE.CylinderGeometry(.25,.55,.7,14,1,true),blk,[0,.75,0],g);return g}
"""

COMMON['setsurf'] = r"""function setSurf(m){const dusk=m===1,sp=dusk?new THREE.Vector3(Math.cos(.42)*44,5,Math.sin(.42)*44):new THREE.Vector3(36,24,22);
sc.fog=new THREE.Fog(0x000000,dusk?55:70,dusk?160:190);sc.background=new THREE.Color(0x000000);
sun.color.set(dusk?0xffe6c8:0xffffff);sun.intensity=dusk?1.6:2.2;hemi.color.set(0x9aa6c8);hemi.groundColor.set(0x1a1a1a);hemi.intensity=dusk?.16:.26;OUT.visible=false;DD.visible=false;
/* no air on the Moon: black sky, sharp shadows, Earth hanging above the horizon */
placeMachines(dusk);ESKY.position.set(-150,dusk?38:62,-170);
sun.position.copy(sp);SUNM.position.copy(sp).normalize().multiplyScalar(360);HALO.position.copy(SUNM.position)}"""

COMMON['sky'] = r"""const ESKY=mesh(new THREE.SphereGeometry(10,48,32),new THREE.MeshBasicMaterial({map:pl.d,fog:false}),[0,0,0],S);ESKY.visible=false;ESKY.rotation.set(.3,2.2,0);
const sky=on=>{SKYM.visible=false;SUNM.visible=HALO.visible=hemi.visible=ESKY.visible=on;if(!on){sc.fog=null;sc.background=new THREE.Color(0x000005)}};"""

COMMON['piau'] = r"""const PIAU=(p,w)=>{if(/^PIA\d+$/.test(p)){const a=p.slice(3,5)+'/'+p.toLowerCase()+'/'+p;return['https://assets.science.nasa.gov/dynamicimage/assets/science/psd/photojournal/pia/pia'+a+'.jpg?w='+w+'&h='+w+'&fit=clip&crop=faces%2Cfocalpoint','https://assets.science.nasa.gov/content/dam/science/psd/photojournal/pia/pia'+a+'.jpg','https://d2pn8kiwq2w21t.cloudfront.net/original_images/jpeg'+p+'.jpg']}const u='https://images-assets.nasa.gov/image/'+p+'/'+p;return[u+'~medium.jpg',u+'~large.jpg',u+'~orig.jpg',u+'~small.jpg']};
const PIAPAGE=p=>/^PIA\d+$/.test(p)?'https://photojournal.jpl.nasa.gov/catalog/'+p:'https://images.nasa.gov/details/'+p;"""

COMMON['illus'] = r"""/* illustrations made in code for slides that have no NASA photo (always labelled "ILLUSTRATION") */
function drawIllus(kind){const c=document.createElement('canvas');c.width=c.height=800;const x=c.getContext('2d'),W=800,H=800,r=mkRng(1967);
if(kind==='atlas'){let g=x.createLinearGradient(0,0,0,H);g.addColorStop(0,'#2d6fc4');g.addColorStop(.7,'#9cc6ee');g.addColorStop(1,'#f2d7b0');x.fillStyle=g;x.fillRect(0,0,W,H);
for(let i=0;i<60;i++){const cx=W*.5+(r()-.5)*W*1.1,cy=H*.8+r()*H*.25,rr=50+r()*120;x.fillStyle='rgba(255,255,255,'+(.25+r()*.35)+')';x.beginPath();x.arc(cx,cy,rr,0,7);x.fill()}
const fg=x.createRadialGradient(W/2,H*.74,10,W/2,H*.74,130);fg.addColorStop(0,'#fffbe0');fg.addColorStop(.35,'#ffc94d');fg.addColorStop(.7,'rgba(255,120,30,.6)');fg.addColorStop(1,'rgba(255,90,20,0)');x.fillStyle=fg;x.beginPath();x.ellipse(W/2,H*.77,80,150,0,0,7);x.fill();
x.fillStyle='#e4e8ee';x.fillRect(W/2-30,H*.34,60,H*.33);x.fillStyle='#c9cfd8';x.fillRect(W/2-30,H*.34,14,H*.33);x.fillStyle='#f4f4f0';x.fillRect(W/2-26,H*.18,52,H*.16);
x.beginPath();x.moveTo(W/2-26,H*.18);x.lineTo(W/2+26,H*.18);x.lineTo(W/2,H*.07);x.closePath();x.fill();x.fillStyle='#b0b6c0';x.fillRect(W/2-30,H*.335,60,6);
x.fillStyle='#1b2a5a';x.font='700 22px Arial';x.save();x.translate(W/2+8,H*.62);x.rotate(-Math.PI/2);x.fillText('ATLAS',0,0);x.restore();x.save();x.translate(W/2+8,H*.32);x.rotate(-Math.PI/2);x.font='700 16px Arial';x.fillText('CENTAUR',0,0);x.restore()}
else{/* bounce: three touchdowns of Surveyor 3, not to scale */
x.fillStyle='#000';x.fillRect(0,0,W,H);for(let i=0;i<180;i++){x.fillStyle='rgba(255,255,255,'+(.3+r()*.7)+')';x.fillRect(r()*W,r()*H*.6,1.5,1.5)}
x.fillStyle='#4f8fff';x.beginPath();x.arc(W*.82,H*.16,34,0,7);x.fill();x.fillStyle='rgba(0,0,0,.55)';x.beginPath();x.arc(W*.82+14,H*.16,34,0,7);x.fill();
let g=x.createLinearGradient(0,H*.62,0,H);g.addColorStop(0,'#9a9792');g.addColorStop(1,'#55534f');x.fillStyle=g;x.beginPath();x.moveTo(0,H*.66);x.quadraticCurveTo(W*.5,H*.6,W,H*.66);x.lineTo(W,H);x.lineTo(0,H);x.fill();
x.fillStyle='rgba(40,40,40,.45)';x.beginPath();x.ellipse(W*.28,H*.82,190,46,0,0,7);x.fill();
const T=[[W*.86,H*.7],[W*.6,H*.73],[W*.4,H*.77],[W*.24,H*.8]],hh=[0,250,110,40];x.strokeStyle='#ffd24a';x.lineWidth=5;x.setLineDash([12,10]);
x.beginPath();x.moveTo(W*.95,H*.08);x.quadraticCurveTo(W*.9,H*.4,T[0][0],T[0][1]);x.stroke();
for(let i=1;i<4;i++){x.beginPath();x.moveTo(T[i-1][0],T[i-1][1]);x.quadraticCurveTo((T[i-1][0]+T[i][0])/2,Math.min(T[i-1][1],T[i][1])-hh[i],T[i][0],T[i][1]);x.stroke()}x.setLineDash([]);
const lander=(cx,cy,s)=>{x.save();x.translate(cx,cy);x.scale(s,s);x.strokeStyle='#e8ecf2';x.lineWidth=4;x.beginPath();x.moveTo(-30,0);x.lineTo(-12,-34);x.lineTo(12,-34);x.lineTo(30,0);x.stroke();x.fillStyle='#e8ecf2';x.fillRect(-14,-52,28,20);x.beginPath();x.moveTo(0,-52);x.lineTo(0,-80);x.stroke();x.fillStyle='#3a5bc9';x.fillRect(-16,-90,32,12);x.restore()};
lander(T[0][0],T[0][1],.8);lander(T[1][0],T[1][1],.8);lander(T[2][0],T[2][1],.8);lander(T[3][0],T[3][1],1.1);
x.fillStyle='#fff';x.font='800 28px Fredoka,Arial';x.textAlign='center';['1','2','3'].forEach((n,i)=>x.fillText(n,T[i+(i===2?1:0)][0],T[i+(i===2?1:0)][1]+44));
x.font='700 24px Fredoka,Arial';x.fillText('≈ 10 m',(T[0][0]+T[1][0])/2,T[0][1]-hh[1]+10);x.fillText('≈ 3 m',(T[1][0]+T[2][0])/2,T[1][1]-hh[2]+6)}
const vg=x.createRadialGradient(W/2,H/2,H*.35,W/2,H/2,H*.75);vg.addColorStop(0,'rgba(0,0,0,0)');vg.addColorStop(1,'rgba(0,0,0,.35)');x.fillStyle=vg;x.fillRect(0,0,W,H);return c.toDataURL('image/jpeg',.88)}"""

# ======================================================================================
#                                    SURVEYOR 3
# ======================================================================================
SURVEYOR = {
'file': 'surveyor3.html', 'who': 'Surveyor 3', 'title': 'Surveyor 3 — Abandoned but not Forgotten',
'ov': r"""<div id="ov"><img id="hero" alt="Surveyor 3 3D mascot"><h1 id="t1">Surveyor 3</h1><p id="t2">Abandoned but not Forgotten</p><p id="t3" style="font-size:14px;opacity:.8;margin:0 0 14px"></p><p style="font-size:12px;opacity:.7;margin:0 16px 12px;max-width:520px">NASA Space Apps 2026 · Data: NASA/JPL (Surveyor program) and NASA/JSC (Apollo 12) · Moon globe: stylized illustration, not real NASA imagery · Open source, Apache-2.0</p><button id="go">▶ Start</button></div>""",
'mascot': r"""/* the cartoon mascot comes from assets/js/mascots.js (shared with the Explorers page) */
const KIND='surveyor3';const mkLRO=()=>MASCOT.build(KIND);
const lro=mkLRO();lro.visible=false;sc.add(lro);
let wave=0,talk=0,flying=0,mood='';
const SITE_MOOD={M1:'',M2:'surprised'};
function animLRO(L,t){MASCOT.anim(L,t,{wave,talk,flying,mood})}
try{$('hero').src=MASCOT.snapshot(KIND,440,{mood:'happy',wave:1,t:.6})}catch(e){$('hero').style.display='none'}""",
'sites': r"""const S3_SRC='https://science.nasa.gov/mission/surveyor-3/',A12_SRC='https://www.nasa.gov/mission/apollo-12/';
const SITES=[{"c":"M1","n":"Surveyor 3 · Ocean of Storms","lat":-3.016,"lon":-23.4157,"l":"17 Apr 1967","r":"Landed 20 Apr 1967","end":"Last contact 4 May 1967 · visited by Apollo 12 on 20 Nov 1969","src":S3_SRC,"s2":"https://images.nasa.gov/details/as12-48-7136","col":16763213,"t":9,"en":"That's me, Surveyor 3! I landed in the Ocean of Storms, a huge dark plain on the Moon.","info":"That's me! I landed in Oceanus Procellarum, the Ocean of Storms: a giant plain of old, dark lava. I came to rest inside a small crater, about 200 meters wide."},
{"c":"M2","n":"Apollo 12 · Intrepid","lat":-3.0128,"lon":-23.4219,"l":"14 Nov 1969","r":"Landed 19 Nov 1969","end":"Astronauts Pete Conrad and Alan Bean made two moonwalks","src":A12_SRC,"s2":"https://images.nasa.gov/details/AS12-48-7133","col":6742015,"t":10,"en":"Two and a half years later, Apollo 12 landed just 180 meters away from me. I had visitors!","info":"On November 19, 1969, the Apollo 12 lunar module Intrepid landed right next to my crater. Pete Conrad and Alan Bean had practiced a pinpoint landing, and they came down so close that they could walk over to see me."}];""",
'pinhide': "/* Apollo 12 landed next to Surveyor 3: the two places share one marker on the globe */\npins[1].m.visible=false;pins[1].ring.visible=false;",
'stops': r"""const STOPS=[
{n:"First touchdown",yr:"20 Apr 1967",sub:"My engines kept firing: I bounced about 10 m up!",t:9,en:"Stop one: my first touchdown. Uh-oh, my engines didn't switch off!",info:"Shiny rocks fooled my landing radar, so my small engines kept firing after I touched the ground. Boing! I bounced about 10 meters back up."},
{n:"Second touchdown",yr:"20 Apr 1967",sub:"Another bounce, about 3 m high",t:8,en:"Stop two: I bounced again, about 3 meters high.",info:"I touched down a second time and bounced again, about 3 meters high. Then my team on Earth switched my engines off."},
{n:"My resting place",yr:"Apr – May 1967",sub:"Inside a crater · I dug, filmed and slept",t:10,en:"Stop three: my resting place, on the slope of a small crater.",info:"On my third touchdown I finally stayed put, on the inside slope of a crater. For two weeks I took more than 6,000 TV pictures and dug into the Moon with my scoop. Then the long, freezing lunar night came, and I fell silent on May 4, 1967."},
{n:"Intrepid lands",yr:"19 Nov 1969",sub:"Apollo 12 lands about 180 m away",t:9,en:"Stop four: two and a half years later, Apollo 12 landed close to me!",info:"On November 19, 1969, the Apollo 12 lunar module Intrepid landed about 180 meters from my crater. It was the first pinpoint landing on the Moon, and I was the target!"},
{n:"Head crater",yr:"20 Nov 1969",sub:"Pete and Al start their second moonwalk",t:8.5,en:"Stop five: the astronauts set off on their second moonwalk.",info:"The next day, Pete Conrad and Alan Bean set off on their second moonwalk. They walked from crater to crater, describing the ground and picking up rocks."},
{n:"Bench crater",yr:"20 Nov 1969",sub:"Collecting Moon rocks on the way",t:8,en:"Stop six: they collected rocks at Bench crater.",info:"At Bench crater they collected Moon rocks to bring home. Scientists still study Apollo 12 rocks today."},
{n:"Sharp crater",yr:"20 Nov 1969",sub:"Then they turned toward my crater",t:8,en:"Stop seven: Sharp crater. Then they turned toward me!",info:"After Sharp crater, the astronauts headed for my crater. Mission Control had a special job for them: bring home pieces of me!"},
{n:"A visit to me!",yr:"20 Nov 1969",sub:"They took my camera home",t:10,en:"My last stop: the astronauts walked down into my crater and visited me!",info:"Pete and Al walked down the slope of my crater and checked me over. They cut off my TV camera, my scoop and some tubes, and carried them back to Earth."}];
const WP=[[20.5,-13],[19,-13.6],[17.5,-14.8],[16,-15.6],[14.5,-16.5],[8,-6],[5.5,-6.8],[3,-8],[1,-11],[0,-14],[-1,-17],[-1,-20],[4,-21],[9,-20.5],[13.2,-18.8]],STOPI=[0,2,4,5,7,9,11,14];
const JUMP=new Set([5]);/* no line between my resting place and Intrepid: 2½ years passed, nothing travelled */
const LSIDE=[1,1,-1,1,-1,1,1,1],LBO=[[0,0],[0,14],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]];
const MAP={bg:['#4c4b56','#1b1a22'],title:"Surveyor 3's landing site",sub:d=>'Ocean of Storms, Moon · 1967 – 1969 · '+(d?'my bounces + the Apollo 12 moonwalk':'follow the numbers…'),scale:'≈ 75 m',note:'Schematic map · not to scale · positions approximate',
feat:(x,px,py,K)=>{const cx=px(16),cy=py(-16),R=7*K;x.beginPath();x.arc(cx,cy,R,0,7);const g=x.createRadialGradient(cx+R*.2,cy+R*.2,R*.1,cx,cy,R);g.addColorStop(0,'rgba(0,0,0,.35)');g.addColorStop(1,'rgba(0,0,0,.08)');x.fillStyle=g;x.fill();x.setLineDash([10,8]);x.strokeStyle='rgba(235,235,250,.55)';x.lineWidth=3;x.stroke();x.setLineDash([]);
x.fillStyle='rgba(235,240,255,.85)';x.textAlign='center';x.font='italic 700 18px Fredoka,Arial,sans-serif';x.fillText('Surveyor crater',cx,cy+R+22);x.font='600 13px Arial,sans-serif';x.fillText('(about 200 m wide)',cx,cy+R+40);
[[3,-8],[0,-14],[-1,-20]].forEach(([a,b])=>{x.beginPath();x.arc(px(a),py(b),1.7*K,0,7);x.strokeStyle='rgba(235,235,250,.25)';x.lineWidth=2;x.stroke()});
x.font='italic 600 13px Arial,sans-serif';x.fillStyle='rgba(255,220,140,.9)';x.fillText('…2½ years later…',px(11.6),py(-10.6))}};""",
'srcconst': "const OPP_SRC=S3_SRC,OPP_MAP='https://images.nasa.gov/details/AS12-48-7133';",
'maplabel': 'Apollo 12 photo',
'tracks': r"""{/* the astronauts' footprints from Intrepid to me */const tm=new THREE.MeshBasicMaterial({color:0x55524e,transparent:true,opacity:.55}),tgm=new THREE.CircleGeometry(.09,8);for(let i=0;i<90;i++){const p=i/90,xx=-20+20*p+Math.sin(p*9)*1.2,zz=-14+14*p+Math.cos(p*7)*.8,sd=(i%2?.17:-.17),f=mesh(tgm,tm,[xx+sd,hgt(xx+sd,zz)+.03,zz],SG);f.rotation.x=-Math.PI/2;f.scale.set(1.7,1,1)}}""",
'models': r"""/* Surveyor 3 today (simplified model, not a photo). Its TV camera and scoop are missing: Apollo 12 took them home. */
const RM=new THREE.Group();SG.add(RM);RM.visible=false;
{const alS=M(0xc9ced4,{metalness:.7,roughness:.35}),whS=M(0xe8e6e0,{roughness:.6});const C=[0,1,2].map(i=>{const a=i*2.0944+.3;return[Math.cos(a)*.75,1.0,Math.sin(a)*.75]});
C.forEach((c,i)=>{strut(c,C[(i+1)%3],.045,alS,RM);strut(c,[0,1.2,0],.035,alS,RM);const f=[c[0]*2.1,.12,c[2]*2.1];strut(c,f,.06,alS,RM);strut([c[0]*.5,1.1,c[2]*.5],[c[0]*1.6,.5,c[2]*1.6],.03,alS,RM);mesh(new THREE.CylinderGeometry(.24,.28,.1,16),whS,[f[0],.06,f[2]],RM).castShadow=true});
strut([0,1.2,0],[0,3.1,0],.055,alS,RM);const pn=mesh(new THREE.BoxGeometry(1.15,.03,.8),panS,[0,3.15,0],RM);pn.rotation.x=-.5;pn.castShadow=true;
const an=mesh(new THREE.BoxGeometry(.75,.03,.75),whS,[.15,2.65,.3],RM);an.rotation.x=1.05;an.castShadow=true;
[-1,1].forEach(s=>{mesh(new THREE.BoxGeometry(.5,.38,.42),whS,[s*.6,1.35,-.15],RM).castShadow=true;strut([s*.5,1.1,-.35],[s*.85,2.3,-.5],.015,alS,RM)});
mesh(new THREE.BoxGeometry(.6,.3,.5),M(0xb98a2e,{metalness:.6,roughness:.4}),[0,1.05,0],RM).castShadow=true}
RM.scale.setScalar(1.1);
const LMD=mkLMD();SG.add(LMD);
function placeMachines(dusk){RM.position.y=hgt(0,0);RM.rotation.set(0,dusk?.8:.4,0);RM.visible=true;LMD.position.set(-20,hgt(-20,-14),-14);LMD.rotation.y=.4}
const surfTick=null;""",
'fb': r"""const FB=[
{pia:'S69-55553',em:'🛰️',t:'Meet Surveyor 3',yr:'1967',cr:'NASA',nt:'An artist\'s view of me resting on the Moon',big:['302 kg','my weight after landing'],rows:[['Run by','NASA JPL, California'],['Built by','Hughes Aircraft Company'],['Height','about 3 m'],['My tools','a TV camera + a digging scoop']],l:[
["I'm Surveyor 3, a robot lander. NASA's JPL ran my mission, and Hughes Aircraft built me.",6],
["My job was to check if the Moon's ground was safe for astronauts to land on.",5.5]]},
{pia:'S69-57076',em:'🗺️',t:'Why go first?',yr:'1966 – 1967',cr:'NASA',nt:'A Lunar Orbiter photo of the region where I landed',big:['5','Surveyors landed safely (out of 7)'],rows:[['Big worry','would a lander sink into deep dust?'],['The plan','send robots before people'],['My big sister','Surveyor 1 landed first, in 1966'],['Map makers','Lunar Orbiters photographed landing spots']],l:[
["Before people could land on the Moon, scientists had a big worry: was the ground hard, or deep, soft dust?",6.5],
["So NASA sent robot landers like me first, to find out!",4]]},
{draw:'atlas',em:'🚀',t:'Liftoff!',yr:'17 Apr 1967',cr:'Illustration',nt:'Atlas-Centaur rocket, Cape Kennedy',big:['3 days','to fly to the Moon'],rows:[['Rocket','Atlas-Centaur'],['Launch site','Cape Kennedy, Florida'],['Trip','less than 3 days'],['Arrival','20 Apr 1967']],l:[
["On April 17, 1967, I launched from Florida on an Atlas-Centaur rocket.",5],
["Less than three days later, I reached the Moon.",3.5]]},
{draw:'bounce',em:'🦘',t:'A bouncy landing',yr:'20 Apr 1967',cr:'Illustration',nt:'My three touchdowns (not to scale)',big:['3','touchdowns in one landing'],rows:[['Braking','one big rocket, then 3 small engines'],['The problem','shiny rocks fooled my radar'],['Bounces','about 10 m, then about 3 m high'],['Came to rest','inside a crater about 200 m wide']],l:[
["Landing was tricky. Shiny rocks fooled my radar, and my engines didn't switch off!",5.5],
["I bounced twice before I came to rest. Boing, boing!",4]]}
];""",
'srcname': 'NASA · Surveyor 3',
'pics': r"""/* black-and-white views, the way my TV camera saw the Moon */
const grey=(n)=>{const g=x.createLinearGradient(0,0,0,H);g.addColorStop(0,'#8c8c8c');g.addColorStop(1,'#5a5a5a');x.fillStyle=g;x.fillRect(0,0,W,H);for(let i=0;i<n;i++){const v=50+r()*150;x.fillStyle='rgba('+v+','+v+','+v+',.45)';x.beginPath();x.ellipse(r()*W,r()*H,.8+r()*3,.6+r()*2,r()*3,0,7);x.fill()}};
const rock=(cx,cy,rr)=>{x.fillStyle='rgba(10,10,10,.55)';x.beginPath();x.ellipse(cx+rr*1.2,cy+rr*.3,rr*1.6,rr*.45,0,0,7);x.fill();const g=x.createRadialGradient(cx-rr*.4,cy-rr*.4,1,cx,cy,rr);g.addColorStop(0,'#d8d8d8');g.addColorStop(1,'#505050');x.fillStyle=g;x.beginPath();x.ellipse(cx,cy,rr,rr*.7,0,0,7);x.fill()};
const bw=()=>{const gg=x.getImageData(0,0,W,H),dd=gg.data;for(let i=0;i<dd.length;i+=4){const v=(dd[i]+dd[i+1]+dd[i+2])/3;dd[i]=dd[i+1]=dd[i+2]=v}x.putImageData(gg,0,0)};
if(k===1){grey(1600);x.fillStyle='rgba(30,30,30,.4)';x.beginPath();x.ellipse(W*.52,H*.66,150,46,0,0,7);x.fill();x.fillStyle='#d9d9d9';x.beginPath();x.ellipse(W*.5,H*.6,120,42,0,0,7);x.fill();x.fillStyle='#bdbdbd';x.fillRect(W*.5-120,H*.6-8,240,16);x.fillStyle='#e9e9e9';x.beginPath();x.ellipse(W*.5,H*.6-8,120,38,0,0,7);x.fill();
x.strokeStyle='#cfcfcf';x.lineWidth=16;x.beginPath();x.moveTo(W*.52,H*.58);x.lineTo(W*.86,-10);x.stroke();x.strokeStyle='rgba(120,120,120,.6)';x.lineWidth=3;x.beginPath();x.ellipse(W*.5,H*.66,170,60,0,0,7);x.stroke();for(let i=0;i<20;i++)rock(r()*W,H*.75+r()*H*.25,2+r()*5);bw()}
else if(k===2){grey(1700);x.save();x.translate(W*.5,H*.58);x.rotate(-.18);x.fillStyle='#2d2d2d';x.fillRect(-170,-26,340,52);x.fillStyle='rgba(220,220,220,.5)';x.fillRect(-170,-30,340,6);x.fillStyle='#1c1c1c';x.fillRect(-170,-10,340,22);x.restore();
for(let i=0;i<3;i++){x.fillStyle='rgba(30,30,30,.7)';x.beginPath();x.ellipse(W*(.2+i*.08),H*.82-i*10,22,10,0,0,7);x.fill()}for(let i=0;i<25;i++)rock(r()*W,H*.3+r()*H*.7,2+r()*6);bw()}
else if(k===3){x.fillStyle='#000';x.fillRect(0,0,W,H);for(let i=0;i<80;i++){x.fillStyle='rgba(255,255,255,'+(.3+r()*.7)+')';x.fillRect(r()*W,r()*H,1.5,1.5)}
const cx=W*.5,cy=H*.46;const g=x.createRadialGradient(cx,cy,60,cx,cy,120);g.addColorStop(0,'rgba(255,235,200,1)');g.addColorStop(.18,'rgba(255,170,90,.9)');g.addColorStop(.45,'rgba(200,90,50,.35)');g.addColorStop(1,'rgba(0,0,0,0)');x.fillStyle=g;x.beginPath();x.arc(cx,cy,120,0,7);x.fill();x.fillStyle='#000';x.beginPath();x.arc(cx,cy,62,0,7);x.fill();
x.fillStyle='#777';x.beginPath();x.moveTo(0,H*.86);x.quadraticCurveTo(W*.5,H*.8,W,H*.86);x.lineTo(W,H);x.lineTo(0,H);x.fill()}
else{grey(1500);x.fillStyle='#000';x.beginPath();x.moveTo(0,0);x.lineTo(W,0);x.lineTo(W,H*.22);x.quadraticCurveTo(W*.5,H*.36,0,H*.3);x.closePath();x.fill();x.fillStyle='rgba(40,40,40,.45)';x.beginPath();x.ellipse(W*.25,H*.45,260,40,-.12,0,7);x.fill();for(let i=0;i<34;i++){const t=r();rock(r()*W,H*.35+t*H*.62,2+t*13)}bw()}
""",
'stamp': "x.fillText('SURVEYOR 3 · TV CAMERA · FRAME '+String(1000+k*173),12,H-12)}",
'picnames': "const PICS=['My own footpad in the moon dust','A trench dug by my scoop','Earth hiding the Sun: an eclipse seen from the Moon','The crater slope all around me'];",
'pick': 'My pick: ⭐ A visit to me, when astronauts came by!',
'picki': 7,
'tags': "' · ★ WHERE I LANDED':i===STOPS.length-1?' · ✕ LAST STOP'",
'twinletter': 'A',
'twin': "b.querySelector('.tg').textContent='MY VISITORS · LANDED 19 NOV 1969';b.querySelector('b').textContent='Apollo 12 · Intrepid';b.querySelector('em').textContent='Landed 180 m away · astronauts walked to me';",
'tour': r"""async function tour(again){manual=0;free=0;document.body.classList.remove('fr');$('mb').style.display='block';
await say(again?"Let's tour again! Here is where it all began.":"Welcome to the Moon! This is where my adventure began.",4);
wave=0;
await goSite(0,3);
await say("The Ocean of Storms: a giant plain of old, dark lava on the Moon.",4.5);
if(!manual)await toSurface(0);
await say("Here I am today, still sitting in my crater. (An illustrative model, not a photo.)",4.5);
await Promise.all([(async()=>{await say("My TV camera sent home more than 6,000 pictures.",4);await say("I even saw Earth slide in front of the Sun: an eclipse, seen from the Moon!",5)})(),showPics()]);
await say("With my scoop, I dug little trenches. The ground was firm enough for astronauts!",5.5);
await say("Then the long lunar night came. It got so cold that I fell silent in May 1967.",5.5);
await say("But that was not the end of my story. Two and a half years later, I had visitors! Abandoned, but not forgotten.",6.5);
await fromSurface();
wave=1;mood='thinking';
await say("Let me show you my landing site, and the path my visitors walked.",4);mood='';wave=0;
$('card').style.display='none';rmShow(0,0);
await say("It all began with a very bouncy landing. Follow the numbers!",3.5);await achieve(0,0);
for(let k=1;k<STOPS.length&&!manual;k++){const p0=rmP,p1=progAt(k);rmH=-1;await tw(2.2,q=>{rmP=p0+(p1-p0)*ez(q);rmDraw()});rmP=p1;rmH=k;rmDraw();await say(STOPS[k].en,STOPS[k].t);await achieve(k,0)}
rmP=1;rmH=-1;rmDraw();await wait(.8);rmHide();await wait(.6);
wave=1;await say("I wasn't alone forever. Come meet my visitors!",3.5);wave=0;
await goSite(1,3);await say(SITES[1].en,SITES[1].t);mood='';
await goSite(0,2.6);
wave=1;mood="wink";await say("Intrepid's landing stage is still my neighbor on the Moon today.",5);mood="";
wave=0;manual=0;free=1;document.body.classList.add('fr');$('mb').style.display='none';mkChips();showCard(cur);await say("Now it's your turn! Pick any card to explore.",4.5)}""",
'ach': r"""const ACH=[
{s:2,pia:'as12-48-7121',em:'🏗️',t:'Proved the Moon could hold a lander',d:'April 1967',big:['Firm','ground, not deep dust'],
 rows:[['Where','inside a crater, Ocean of Storms'],['How I tested it','pressing and digging with my scoop'],['Pictures','more than 6,000 TV images'],['Good news for','the Apollo lunar modules']],
 why:'If the ground had been deep, soft dust, a heavy Apollo lander could have sunk. My tests showed the surface was firm enough for astronauts.',
 story:"My tests showed that the Moon's ground was firm enough for astronauts to land on. Great news for Apollo!",
 cr:'NASA/JSC',nt:'Me in my crater, photographed by Apollo 12 in 1969',
 src:[['NASA image AS12-48-7121','https://images.nasa.gov/details/as12-48-7121'],['NASA: Surveyor 3','https://science.nasa.gov/mission/surveyor-3/']]},
{s:2,pia:'as12-48-7110',em:'🥄',t:'First digging on the Moon',d:'April 1967',big:['1st','robot scoop to dig on the Moon'],
 rows:[['Tool','a scoop on a robot arm (surface sampler)'],['What it did','dug trenches, lifted and dropped soil'],['Driven by','my team on Earth'],['Discovery','the soil was clumpy, like damp sand']],
 why:'Digging showed what lies under the surface and how strong the soil is. That helped engineers design landing legs, boots and tools for the astronauts.',
 story:"My scoop dug the first trenches on the Moon. The soil was clumpy, a bit like damp sand at the beach.",
 cr:'NASA/JSC',nt:'My footpad and scoop, photographed by Apollo 12',
 src:[['NASA image AS12-48-7110','https://images.nasa.gov/details/as12-48-7110'],['NASA: Surveyor 3','https://science.nasa.gov/mission/surveyor-3/']]},
{s:3,pia:'AS12-48-7133',em:'🛬',t:'Apollo 12 landed right next to me',d:'19 Nov 1969',big:['180 m','away: a pinpoint landing'],
 rows:[['Lunar module','Intrepid'],['Astronauts','Pete Conrad and Alan Bean'],['In orbit','Richard Gordon, in Yankee Clipper'],['Why it mattered','astronauts could land on a target']],
 why:'Apollo 11 landed several kilometers past its target. Apollo 12 landed almost exactly where it aimed, next to me. Later missions could now aim for exciting places.',
 story:"Two and a half years later, Apollo 12 landed right next to my crater: the first pinpoint landing on the Moon!",
 cr:'NASA/JSC',nt:'Two U.S. spacecraft on the Moon: me, and Intrepid behind',
 src:[['NASA image AS12-48-7133','https://images.nasa.gov/details/AS12-48-7133'],['NASA: Apollo 12','https://www.nasa.gov/mission/apollo-12/']]},
{s:7,pia:'as12-48-7136',em:'👨‍🚀',t:'The first robot visited by people on another world',d:'20 Nov 1969',big:['31 months','alone before my visitors came'],
 rows:[['Visitors','Pete Conrad and Alan Bean'],['They took','my TV camera, my scoop and other parts'],['Why','to see how the Moon changes machines'],['Today','my camera is in a museum']],
 why:'By studying my parts, scientists learned how dust, sunlight and radiation change machines left on the Moon for years.',
 story:"Pete Conrad came to visit me! The astronauts took my camera and scoop home, so scientists could study them.",
 cr:'NASA/JSC',nt:'Pete Conrad checks me over; Intrepid in the background',
 src:[['NASA image AS12-48-7136','https://images.nasa.gov/details/as12-48-7136'],['NASA: Apollo 12','https://www.nasa.gov/mission/apollo-12/']]},
{s:7,pia:'PIA12903',em:'🛰️',t:'Spotted from orbit, 40 years later',d:'2009',big:['40 years','after the visit, seen from space'],
 rows:[['Camera','NASA\'s Lunar Reconnaissance Orbiter (LRO)'],['You can see','me, Intrepid and the astronauts\' paths'],['Year','2009']],
 why:'Orbiters let us check on old landing sites without going back. They show that the things we left behind are still there.',
 story:"Forty years later, NASA's Lunar Reconnaissance Orbiter photographed me and Intrepid from space.",
 cr:'NASA/GSFC/Arizona State University',nt:'LRO view of the Apollo 12 and Surveyor 3 site',fit:'contain',
 src:[['NASA photo PIA12903','https://photojournal.jpl.nasa.gov/catalog/PIA12903'],['NASA: Lunar Reconnaissance Orbiter','https://science.nasa.gov/mission/lro/']]}
];""",
'fincomment': '/* Surveyor 3 still sits in its crater; its TV camera is at the Smithsonian National Air and Space Museum. */',
'finale': r"""const yrs=new Date().getFullYear()-1967;
await say("So... what happened to me after the visit?",4);
await say("Back on Earth, scientists studied my camera and parts, to see how two and a half years on the Moon had changed them.",7);
await say("They found tiny Earth germs inside my camera. Later, scientists decided the germs most likely got in after it came home.",7);
await say("My camera is now in a museum, the Smithsonian's National Air and Space Museum.",5);
await say("And I'm still sitting in my crater, "+yrs+" years after I landed: abandoned, but not forgotten.",6);""",
'intro': "mood='happy';await say(\"I'm Surveyor 3, a robot lander from NASA! I helped get the Moon ready for astronauts.\",5.5);mood='';",
'q': "Want to know how I got to the Moon? Let's go back in time!",
'after': "That's how I got to the Moon! Now let me show you where I landed.",
'endbtns': '<button id="frp" class="yl">↺ Recap</button><button id="fnx" class="pu">Next ➜</button>',
'fnx': gonext('surveyor3', 'apollo17-lrv.html') + "$('fnx').onclick=()=>{const b=$('fnx');b.classList.remove('pop');void b.offsetWidth;b.classList.add('pop');setTimeout(()=>goNext('next'),350)};",
}

# ======================================================================================
#                                 APOLLO 17 LRV
# ======================================================================================
LRV = {
'file': 'apollo17-lrv.html', 'who': 'Apollo 17 LRV', 'title': 'Apollo 17 Lunar Roving Vehicle — Abandoned but not Forgotten',
'ov': r"""<div id="ov"><img id="hero" alt="Apollo 17 Lunar Roving Vehicle 3D mascot"><h1 id="t1">Apollo 17 LRV</h1><p id="t2">Abandoned but not Forgotten</p><p id="t3" style="font-size:14px;opacity:.8;margin:0 0 14px"></p><p style="font-size:12px;opacity:.7;margin:0 16px 12px;max-width:520px">NASA Space Apps 2026 · Data: NASA (Apollo 17, Lunar Roving Vehicle) · Moon globe: stylized illustration, not real NASA imagery · Open source, Apache-2.0</p><button id="go">▶ Start</button></div>""",
'mascot': r"""/* the cartoon mascot comes from assets/js/mascots.js (shared with the Explorers page) */
const KIND='lrv';const mkLRO=()=>MASCOT.build(KIND);
const lro=mkLRO();lro.visible=false;sc.add(lro);
let wave=0,talk=0,flying=0,mood='';
const SITE_MOOD={M1:'',M2:'happy'};
function animLRO(L,t){MASCOT.anim(L,t,{wave,talk,flying,mood})}
try{$('hero').src=MASCOT.snapshot(KIND,440,{mood:'happy',wave:1,t:.6})}catch(e){$('hero').style.display='none'}""",
'sites': r"""const LRV_SRC='https://www.nasa.gov/mission/apollo-17/',A15_SRC='https://www.nasa.gov/mission/apollo-15/';
const SITES=[{"c":"M1","n":"Apollo 17 LRV · Taurus-Littrow","lat":20.1908,"lon":30.7717,"l":"7 Dec 1972","r":"Landed 11 Dec 1972","end":"Last drive 13 Dec 1972 · about 35.7 km driven","src":LRV_SRC,"s2":"https://images.nasa.gov/details/as17-146-22367","col":16763213,"t":9,"en":"That's me, the Apollo 17 rover! I drove in the Taurus-Littrow valley on the Moon.","info":"That's me! I drove in the valley of Taurus-Littrow, surrounded by tall mountains, at the edge of the Sea of Serenity. Gene Cernan and Jack Schmitt drove me for three days."},
{"c":"M2","n":"Apollo 15 LRV · Hadley-Apennine","lat":26.1322,"lon":3.6339,"l":"26 Jul 1971","r":"Landed 30 Jul 1971","end":"The first car ever driven on the Moon","src":A15_SRC,"s2":"https://images.nasa.gov/search?q=apollo%2015%20lunar%20roving%20vehicle","col":6742015,"t":10,"en":"My big brother, the Apollo 15 rover, was the first car ever driven on the Moon, in July 1971.","info":"Three rovers like me were driven on the Moon: on Apollo 15, 16 and 17. The Apollo 15 rover went first, in July 1971, near a long, winding valley called Hadley Rille. All three are still parked on the Moon."}];""",
'pinhide': "/* the two rover sites are far apart, so both markers are shown */",
'stops': r"""const STOPS=[
{n:"Challenger lands",yr:"11 Dec 1972",sub:"I unfolded from the lander's side",t:9,en:"Stop one: the lander Challenger touched down, with me folded up on its side.",info:"Gene and Jack landed their lunar module, Challenger, in the valley. I traveled folded up like a book on its side. They pulled a few straps, and I unfolded onto the ground!"},
{n:"Duct-tape fix",yr:"12 Dec 1972",sub:"A broken fender fixed with maps and tape",t:9.5,en:"Stop two: my broken fender got a clever fix.",info:"On the first day, a hammer accidentally knocked off part of my right rear fender. Without it, I sprayed dark dust all over the astronauts. Overnight, the team on Earth invented a fix: maps, tape and clamps!"},
{n:"Nansen (South Massif)",yr:"12 Dec 1972",sub:"7.6 km from the lander: my farthest point",t:9.5,en:"Stop three: the foot of the South Massif, my farthest point from the lander.",info:"We drove to the foot of a giant mountain, the South Massif, about 7.6 kilometers from the lander. No Apollo crew ever drove farther away from their lunar module."},
{n:"Shorty crater",yr:"12 Dec 1972",sub:"Jack found orange soil!",t:9.5,en:"Stop four: Shorty crater, where Jack found orange soil!",info:"At Shorty crater, Jack Schmitt scuffed the ground and shouted: there's orange soil! It was made of tiny glass beads from ancient volcanic fire fountains."},
{n:"Camelot crater",yr:"12 Dec 1972",sub:"Big boulders on the way back",t:8.5,en:"Stop five: Camelot crater, full of big boulders.",info:"On the way back we stopped at Camelot crater, where the astronauts studied big boulders blasted out of the ground."},
{n:"Tracy's Rock",yr:"13 Dec 1972",sub:"A giant split boulder at the North Massif",t:9.5,en:"Stop six: a giant split boulder at the North Massif.",info:"On the last day we drove north. At the foot of the North Massif sat a huge boulder split into pieces. Gene named it Tracy's Rock, after his daughter."},
{n:"Speed record",yr:"13 Dec 1972",sub:"18 km/h downhill: a Moon record",t:9,en:"Stop seven: downhill, I reached 18 kilometers per hour, a lunar speed record!",info:"Driving back downhill with heavy Moon rocks on board, I reached about 18 kilometers per hour. That is still the fastest anyone has driven on the Moon!"},
{n:"Final parking spot",yr:"14 Dec 1972",sub:"My camera filmed Challenger's liftoff",t:10,en:"My last stop: Gene parked me so my camera could watch the liftoff.",info:"At the end, Gene parked me a short walk east of the lander, with my TV camera pointed at it. On December 14, 1972, Mission Control steered my camera from Earth and filmed Challenger blasting off."}];
const WP=[[14,-12],[16.5,-14.5],[12,-16],[7,-19.5],[3,-23],[5,-20.5],[7.5,-17.5],[8.8,-16.2],[10,-15],[12.5,-12],[13.5,-6],[12.5,-2.5],[16,-3.5],[19,-7],[18.5,-9.5],[17.5,-11]],STOPI=[0,1,4,6,8,11,13,15];
const JUMP=new Set();
const LSIDE=[-1,1,1,-1,-1,1,1,1],LBO=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]];
const MAP={bg:['#4a4a54','#1a1a22'],title:"The rover's road trip",sub:d=>'Taurus-Littrow valley, Moon · 11 – 14 Dec 1972 · '+(d?'about 35.7 km in 3 drives':'driving…'),scale:'≈ 2.5 km',note:'Schematic map · positions approximate',
feat:(x,px,py,K)=>{const blob=(a,b,rx,ry,lab,ly)=>{const cx=px(a),cy=py(b);const g=x.createRadialGradient(cx,cy-ry*.3,4,cx,cy,Math.max(rx,ry));g.addColorStop(0,'rgba(200,200,215,.35)');g.addColorStop(1,'rgba(200,200,215,.04)');x.fillStyle=g;x.beginPath();x.ellipse(cx,cy,rx,ry,0,0,7);x.fill();
x.fillStyle='rgba(235,240,255,.85)';x.textAlign='center';x.font='italic 700 16px Fredoka,Arial,sans-serif';x.fillText(lab,cx,cy+(ly||0))};
blob(2,-27.5,9*K,3*K,'South Massif',10);blob(10,1.2,8*K,2.4*K,'North Massif',4);blob(22,-1,4*K,4*K,'Sculptured Hills',-2*K);
x.fillStyle='rgba(235,240,255,.6)';x.font='italic 600 15px Fredoka,Arial,sans-serif';x.textAlign='center';x.fillText('Taurus-Littrow valley',px(5),py(-9))}};""",
'srcconst': "const OPP_SRC=LRV_SRC,OPP_MAP='https://images.nasa.gov/details/S72-03145';",
'maplabel': 'NASA traverse map',
'tracks': r"""{/* my wheel tracks */const tm=new THREE.MeshBasicMaterial({color:0x55524e,transparent:true,opacity:.5}),tgm=new THREE.CircleGeometry(.13,8);[-.86,.86].forEach(zz=>{for(let i=0;i<60;i++){const xx=-2.4-i*.36,z=zz+Math.sin(i*.12)*.9,f=mesh(tgm,tm,[xx,hgt(xx,z)+.04,z],SG);f.rotation.x=-Math.PI/2;f.scale.set(1.9,1,1)}})}""",
'models': r"""/* the Apollo 17 rover today (simplified model, not a photo) */
const RM=new THREE.Group();SG.add(RM);RM.visible=false;
{const alS=M(0xc9ced4,{metalness:.7,roughness:.35}),wm=M(0xb0b4ba,{metalness:.55,roughness:.5}),fen=M(0xc4c8ce,{roughness:.5,side:2}),seat=M(0x55698c,{roughness:.6}),gold=M(0xd2a23c,{metalness:.7,roughness:.35});
mesh(new THREE.BoxGeometry(3.0,.12,1.25),alS,[0,.78,0],RM).castShadow=true;
[[1,1],[1,-1],[-1,1],[-1,-1]].forEach(([a,b])=>{const w=mesh(new THREE.CylinderGeometry(.41,.41,.23,22),wm,[a*1.15,.41,b*.86],RM);w.rotation.x=Math.PI/2;w.castShadow=true;mesh(new THREE.CylinderGeometry(.16,.16,.25,12),dkS,[a*1.15,.41,b*.86],RM).rotation.x=Math.PI/2;
const fg=new THREE.Group();fg.position.set(a*1.15,.41,b*.86);fg.rotation.z=Math.PI/2;RM.add(fg);const fm=mesh(new THREE.CylinderGeometry(.48,.48,.27,16,1,true,0,Math.PI),fen,[0,0,0],fg);fm.rotation.x=Math.PI/2;fm.castShadow=true;strut([a*1.15,.41,b*.86],[a*.8,.75,b*.55],.04,alS,RM)});
[-1,1].forEach(s=>{mesh(new THREE.BoxGeometry(.5,.06,.45),seat,[-.25,1.05,s*.3],RM).castShadow=true;mesh(new THREE.BoxGeometry(.06,.5,.45),seat,[-.52,1.3,s*.3],RM).castShadow=true;strut([-.25,.84,s*.3],[-.25,1.02,s*.3],.03,alS,RM)});
strut([.55,.84,0],[.55,1.2,0],.04,alS,RM);mesh(new THREE.BoxGeometry(.25,.3,.45),dkS,[.6,1.3,0],RM).castShadow=true;
strut([1.25,.84,-.35],[1.25,2.1,-.35],.03,alS,RM);const um=mesh(new THREE.ConeGeometry(.55,.2,18,1,true),M(0xe6e2d6,{side:2,roughness:.5}),[1.25,2.2,-.35],RM);um.rotation.set(Math.PI+.5,0,.3);um.castShadow=true;
strut([1.05,.84,.5],[1.05,1.6,.5],.02,alS,RM);mesh(new THREE.CylinderGeometry(.06,.06,.4,10),gold,[1.05,1.75,.5],RM);
strut([1.4,.84,.3],[1.4,1.3,.3],.025,alS,RM);mesh(new THREE.BoxGeometry(.28,.2,.2),dkS,[1.45,1.38,.3],RM).castShadow=true;
mesh(new THREE.BoxGeometry(.5,.55,1.0),gold,[-1.45,1.1,0],RM).castShadow=true}
const LMD=mkLMD();SG.add(LMD);
/* the U.S. flag the crew planted (simplified) */
const FLAG=new THREE.Group();SG.add(FLAG);{const ft=cv(128,80,(x,w,h)=>{for(let i=0;i<13;i++){x.fillStyle=i%2?'#fff':'#c8102e';x.fillRect(0,i*h/13,w,h/13+1)}x.fillStyle='#0a3161';x.fillRect(0,0,w*.42,h*.54);x.fillStyle='#fff';for(let i=0;i<30;i++)x.fillRect(4+(i%6)*8,4+Math.floor(i/6)*8,2,2)});
strut([0,0,0],[0,2.4,0],.03,M(0xdddddd,{metalness:.6}),FLAG);strut([0,2.35,0],[1.1,2.35,0],.02,M(0xdddddd,{metalness:.6}),FLAG);mesh(new THREE.PlaneGeometry(1.1,.68),new THREE.MeshStandardMaterial({map:ft,side:2,roughness:.8}),[.55,2.0,0],FLAG).castShadow=true}
function placeMachines(dusk){RM.position.y=hgt(0,0);RM.rotation.set(0,dusk?.7:.25,0);RM.visible=true;LMD.position.set(-13,hgt(-13,-9),-9);LMD.rotation.y=.3;FLAG.position.set(-8.5,hgt(-8.5,-12),-12);FLAG.rotation.y=.6}
const surfTick=null;""",
'fb': r"""const FB=[
{pia:'7017604',em:'🏭',t:'Born at Boeing',yr:'1971',cr:'NASA/MSFC',nt:'Workers test how a rover unfolds, at Boeing in Kent, Washington',big:['210 kg','my weight on Earth (about 35 kg on the Moon)'],rows:[['Built by','Boeing, for NASA Marshall'],['Wheels','made by General Motors, from woven piano wire'],['Power','two 36-volt batteries'],['Length','about 3 m']],l:[
["I was built by Boeing for NASA, so astronauts could drive far across the Moon.",5.5],
["My wheels were made of woven piano wire, because rubber tires would not work on the Moon.",6]]},
{pia:'7020219',em:'📦',t:'Folded like a book',yr:'1971',cr:'NASA/MSFC',nt:'A rover being installed in a lunar module at Kennedy Space Center',big:['3','rovers were driven on the Moon'],rows:[['Where I rode','folded in a bay on the lander\'s side'],['Unfolding','astronauts pulled straps and pins'],['Rovers on the Moon','Apollo 15, 16 and 17'],['Seats','2 astronauts + their tools']],l:[
["To fit inside the lunar lander, I folded up like a book, tucked into its side.",5.5]]},
{pia:'S72-55070',em:'🚀',t:'Night liftoff!',yr:'7 Dec 1972',cr:'NASA',nt:'Apollo 17 lights up the night at Kennedy Space Center',big:['1st','night launch of a Saturn V'],rows:[['Rocket','Saturn V'],['Crew','Gene Cernan, Jack Schmitt, Ron Evans'],['Trip','about 4 days to the Moon'],['The last','Apollo Moon landing mission']],l:[
["On December 7, 1972, Apollo 17 blasted off at night on a giant Saturn V rocket.",5.5],
["It was the last Apollo mission to the Moon.",3.5]]},
{pia:'as17-134-20435',em:'🏔️',t:'The valley of Taurus-Littrow',yr:'Dec 1972',cr:'NASA/JSC',nt:'A wide view of my landing valley',big:['2 km','tall mountains all around'],rows:[['Lander','Challenger'],['Astronauts','Gene Cernan (commander) and Jack Schmitt (geologist)'],['In orbit','Ron Evans, in America'],['Why here','old mountains + younger volcanic soil']],l:[
["We landed in a deep valley between giant mountains, called Taurus-Littrow.",5],
["Jack Schmitt was a real geologist, the first scientist to walk on the Moon!",5]]},
{pia:'as17-147-22527',em:'🚗',t:'My first test drive',yr:'11 Dec 1972',cr:'NASA/JSC',nt:'Gene Cernan test-drives me on the first day',big:['13 km/h','my usual top speed'],rows:[['Steering','a T-shaped hand controller'],['Each wheel','had its own electric motor'],['Could carry','about 490 kg, astronauts included'],['Navigation','a computer that always pointed home']],l:[
["Gene took me for a quick test drive. Each of my four wheels had its own electric motor.",6],
["Let's roll! The valley was waiting.",3]]}
];""",
'srcname': 'NASA · Apollo 17',
'pics': r"""/* views from my trip (color, like the astronauts' film cameras) */
const reg=(n)=>{const g=x.createLinearGradient(0,0,0,H);g.addColorStop(0,'#9a9894');g.addColorStop(1,'#5c5a56');x.fillStyle=g;x.fillRect(0,0,W,H);for(let i=0;i<n;i++){const v=60+r()*140;x.fillStyle='rgba('+v+','+v+','+(v-4)+',.4)';x.beginPath();x.ellipse(r()*W,r()*H,.8+r()*3,.6+r()*2,r()*3,0,7);x.fill()}};
const blk=(hy)=>{x.fillStyle='#000';x.beginPath();x.moveTo(0,0);x.lineTo(W,0);x.lineTo(W,hy);for(let i=20;i>=0;i--)x.lineTo(i*W/20,hy-Math.abs(Math.sin(i*.8))*40-r()*8);x.closePath();x.fill()};
if(k===1){reg(1500);blk(H*.2);x.save();x.translate(W*.5,H*.62);x.rotate(-.08);const g=x.createRadialGradient(0,0,10,0,0,170);g.addColorStop(0,'#e8873a');g.addColorStop(.6,'#c26a2c');g.addColorStop(1,'rgba(150,110,80,0)');x.fillStyle=g;x.beginPath();x.ellipse(0,0,200,60,0,0,7);x.fill();x.fillStyle='rgba(120,60,20,.45)';x.fillRect(-120,-10,240,20);x.restore();
for(let i=0;i<12;i++){x.fillStyle='rgba(40,40,40,.45)';x.beginPath();x.ellipse(W*(.1+i*.07),H*(.85-i*.012),12,6,0,0,7);x.fill()}}
else if(k===2){x.fillStyle='#000';x.fillRect(0,0,W,H);const cx=W*.6,cy=H*.3,R=48;const g=x.createRadialGradient(cx-14,cy-14,4,cx,cy,R);g.addColorStop(0,'#bfe3ff');g.addColorStop(.5,'#3c7fd6');g.addColorStop(1,'#1b3f86');x.fillStyle=g;x.beginPath();x.arc(cx,cy,R,0,7);x.fill();x.fillStyle='rgba(255,255,255,.7)';x.beginPath();x.ellipse(cx-8,cy-10,20,8,.3,0,7);x.fill();x.fillStyle='rgba(0,0,0,.75)';x.beginPath();x.arc(cx+28,cy,R,-Math.PI/2,Math.PI/2);x.fill();
x.fillStyle='#6f6d69';x.beginPath();x.moveTo(0,H*.8);x.quadraticCurveTo(W*.5,H*.74,W,H*.8);x.lineTo(W,H);x.lineTo(0,H);x.fill();x.save();x.translate(W*.25,H*.62);x.rotate(-.5);x.fillStyle='#e6e1d2';x.beginPath();x.ellipse(0,0,120,40,0,0,7);x.fill();x.strokeStyle='#a39f94';x.lineWidth=2;for(let i=0;i<10;i++){x.beginPath();x.moveTo(0,0);x.lineTo(Math.cos(i*.63)*120,Math.sin(i*.63)*40);x.stroke()}x.restore();x.strokeStyle='#bbb';x.lineWidth=6;x.beginPath();x.moveTo(W*.25,H*.64);x.lineTo(W*.3,H);x.stroke()}
else if(k===3){x.fillStyle='#000';x.fillRect(0,0,W,H);for(let i=0;i<30;i++){x.fillStyle='rgba(255,255,255,.5)';x.fillRect(r()*W,r()*H*.3,1.5,1.5)}
x.fillStyle='#7c7a76';x.beginPath();x.moveTo(0,H*.5);x.lineTo(W*.45,H*.16);x.lineTo(W,H*.38);x.lineTo(W,H);x.lineTo(0,H);x.fill();
let g=x.createLinearGradient(0,H*.6,0,H);g.addColorStop(0,'#8e8c88');g.addColorStop(1,'#5c5a56');x.fillStyle=g;x.beginPath();x.moveTo(0,H*.68);x.quadraticCurveTo(W*.5,H*.62,W,H*.68);x.lineTo(W,H);x.lineTo(0,H);x.fill();
for(let i=0;i<900;i++){const v=60+r()*140;x.fillStyle='rgba('+v+','+v+','+v+',.35)';x.fillRect(r()*W,H*.3+r()*H*.7,1+r()*2,1+r()*2)}
x.fillStyle='rgba(0,0,0,.55)';x.beginPath();x.ellipse(W*.66,H*.88,250,34,0,0,7);x.fill();
const piece=(pts,c1,c2)=>{const gg=x.createLinearGradient(pts[0][0],pts[0][1]-120,pts[0][0]+120,pts[0][1]);gg.addColorStop(0,c1);gg.addColorStop(1,c2);x.fillStyle=gg;x.beginPath();pts.forEach((p,i)=>i?x.lineTo(p[0],p[1]):x.moveTo(p[0],p[1]));x.closePath();x.fill()};
piece([[W*.3,H*.88],[W*.31,H*.58],[W*.4,H*.45],[W*.52,H*.47],[W*.55,H*.88]],'#a9a6a0','#5e5c58');
piece([[W*.57,H*.88],[W*.58,H*.5],[W*.68,H*.42],[W*.8,H*.5],[W*.83,H*.88]],'#9d9a94','#55534f');
x.fillStyle='#e6e6e6';x.fillRect(W*.2,H*.76,10,28);x.beginPath();x.arc(W*.2+5,H*.74,8,0,7);x.fill()}
else{x.fillStyle='#000';x.fillRect(0,0,W,H);for(let i=0;i<40;i++){x.fillStyle='rgba(255,255,255,.6)';x.fillRect(r()*W,r()*H*.5,1.5,1.5)}x.fillStyle='#6b6965';x.beginPath();x.moveTo(0,H*.82);x.quadraticCurveTo(W*.5,H*.78,W,H*.82);x.lineTo(W,H);x.lineTo(0,H);x.fill();
x.fillStyle='#c9952f';x.fillRect(W*.38,H*.66,W*.24,H*.1);x.strokeStyle='#bbb';x.lineWidth=6;[[.38,.76,.3,.86],[.62,.76,.7,.86]].forEach(([a,b,c2,d2])=>{x.beginPath();x.moveTo(W*a,H*b);x.lineTo(W*c2,H*d2);x.stroke()});
const fg=x.createRadialGradient(W*.5,H*.6,4,W*.5,H*.6,140);fg.addColorStop(0,'rgba(255,250,230,.95)');fg.addColorStop(.3,'rgba(255,200,120,.55)');fg.addColorStop(1,'rgba(255,160,60,0)');x.fillStyle=fg;x.beginPath();x.arc(W*.5,H*.6,140,0,7);x.fill();
x.fillStyle='#d8d8d8';x.beginPath();x.moveTo(W*.42,H*.5);x.lineTo(W*.58,H*.5);x.lineTo(W*.56,H*.34);x.lineTo(W*.44,H*.34);x.closePath();x.fill();x.fillStyle='#222';x.fillRect(W*.47,H*.38,W*.06,H*.04);
for(let i=0;i<40;i++){const a=Math.PI*(.15+r()*.7),L=40+r()*160;x.strokeStyle='rgba(255,230,180,'+(.2+r()*.4)+')';x.lineWidth=1+r()*2;x.beginPath();x.moveTo(W*.5,H*.62);x.lineTo(W*.5+Math.cos(a)*L*1.4,H*.62+Math.sin(a)*L*.4);x.stroke()}}
""",
'stamp': "x.fillText('APOLLO 17 · ROVER TRIP · FRAME '+String(1000+k*173),12,H-12)}",
'picnames': "const PICS=['Orange soil at Shorty crater','Earth above my umbrella antenna','Tracy\\'s Rock, a giant split boulder','Challenger lifting off for home'];",
'pick': 'My pick: ⭐ Shorty crater, where Jack found orange soil!',
'picki': 3,
'tags': "' · ★ WHERE WE LANDED':i===STOPS.length-1?' · ✕ LAST STOP'",
'twinletter': 'B',
'twin': "b.querySelector('.tg').textContent='MY BIG BROTHER · JULY 1971';b.querySelector('b').textContent='Apollo 15 rover';b.querySelector('em').textContent='Hadley-Apennine · the first car on the Moon';",
'tour': r"""async function tour(again){manual=0;free=0;document.body.classList.remove('fr');$('mb').style.display='block';
await say(again?"Let's tour again! Here is where it all began.":"Welcome to the Moon! This is where my adventure began.",4);
wave=0;
await goSite(0,3);
await say("Taurus-Littrow: a deep valley between giant mountains, at the edge of the Sea of Serenity.",5);
if(!manual)await toSurface(0);
await say("Here I am, still parked on the Moon. (An illustrative model, not a photo.)",4.5);
await Promise.all([(async()=>{await say("On our trip, we saw amazing things.",3);await say("Orange soil, giant boulders, and Earth hanging in the black sky!",5)})(),showPics()]);
await say("In three days, Gene and Jack drove me about 36 kilometers. They brought home about 110 kilograms of Moon rocks.",7);
await say("Then they climbed back into Challenger and flew home. I had to stay behind.",5);
await say("I've been parked here ever since, with my wheel tracks all around me. Abandoned, but not forgotten.",6.5);
await fromSurface();
wave=1;mood='thinking';
await say("Let me show you my road trip!",3);mood='';wave=0;
$('card').style.display='none';rmShow(0,0);
await say("It all began at the lander, Challenger. Follow the numbers!",3.5);await achieve(0,0);
for(let k=1;k<STOPS.length&&!manual;k++){const p0=rmP,p1=progAt(k);rmH=-1;await tw(2.2,q=>{rmP=p0+(p1-p0)*ez(q);rmDraw()});rmP=p1;rmH=k;rmDraw();await say(STOPS[k].en,STOPS[k].t);await achieve(k,0)}
rmP=1;rmH=-1;rmDraw();await wait(.8);rmHide();await wait(.6);
wave=1;await say("I wasn't the only rover on the Moon. Come meet my big brother!",4);wave=0;
await goSite(1,3);await say(SITES[1].en,SITES[1].t);mood='';
await goSite(0,2.6);
wave=1;mood="wink";await say("All three Apollo rovers are still parked on the Moon today.",4.5);mood="";
wave=0;manual=0;free=1;document.body.classList.add('fr');$('mb').style.display='none';mkChips();showCard(cur);await say("Now it's your turn! Pick any card to explore.",4.5)}""",
'ach': r"""const ACH=[
{s:1,pia:'as17-137-20979',em:'🛠️',t:'The famous duct-tape fix',d:'12 Dec 1972',big:['Maps + tape','a homemade fender'],
 rows:[['Problem','a broken rear fender'],['Why it mattered','dust sprayed everywhere and heated things up'],['Idea from','the team on Earth'],['Made of','stiff maps, tape and clamps']],
 why:'Moon dust is dark, sticky and sharp. Without a fender it covered the astronauts and the rover, which can make equipment overheat. A simple fix saved the mission.',
 story:"My fender broke, so the team invented a fix with maps, tape and clamps. It worked for the rest of the mission!",
 cr:'NASA/JSC',nt:'My repaired fender, with Jack Schmitt aboard',
 src:[['NASA image AS17-137-20979','https://images.nasa.gov/details/as17-137-20979'],['NASA image S72-55170 (planning the fix)','https://images.nasa.gov/details/S72-55170']]},
{s:3,pia:'as17-137-20990',em:'🟠',t:'Orange soil discovered',d:'12 Dec 1972',big:['3.6 billion','year-old volcanic glass beads'],
 rows:[['Found by','Jack Schmitt, at Shorty crater'],['Made of','tiny beads of orange glass'],['Formed by','ancient volcanic fire fountains'],['Bonus','the beads hold traces of water']],
 why:'The orange beads were sprayed out by volcanoes long ago. They show that the Moon was once a fiery, volcanic world, and they even hold tiny traces of water.',
 story:"At Shorty crater, Jack found orange soil: tiny glass beads from volcanoes that erupted billions of years ago!",
 cr:'NASA/JSC',nt:'The orange soil at Shorty crater',
 src:[['NASA image AS17-137-20990','https://images.nasa.gov/details/as17-137-20990'],['NASA image S73-15171 (the beads up close)','https://images.nasa.gov/details/S73-15171']]},
{s:5,pia:'S73-22871',em:'🪨',t:"Tracy's Rock",d:'13 Dec 1972',big:['Split','a giant boulder that rolled down a mountain'],
 rows:[['Where','the foot of the North Massif'],['Named after','Gene Cernan\'s daughter, Tracy'],['Size','bigger than a house'],['Studied','the crew chipped off rock samples']],
 why:'Boulders that roll down from the mountains bring old rocks from high up to where astronauts can reach them, like free deliveries from the Moon\'s past.',
 story:"At the North Massif, we found a huge split boulder. Gene named it Tracy's Rock, after his daughter.",
 cr:'NASA/JSC',nt:'Jack Schmitt next to the huge split boulder',
 src:[['NASA image S73-22871','https://images.nasa.gov/details/S73-22871'],['NASA image AS17-140-21493','https://images.nasa.gov/details/AS17-140-21493']]},
{s:6,pia:'as17-134-20473',em:'🏎️',t:'Fastest on the Moon',d:'13 Dec 1972',big:['18 km/h','the lunar speed record'],
 rows:[['Driver','Gene Cernan'],['Where','downhill, on the way back'],['Helped by','a heavy load of Moon rocks'],['Usual speed','about 8 to 13 km/h']],
 why:'A record that still stands after more than 50 years: no one has driven faster on the Moon.',
 story:"With heavy rocks on board, I rolled downhill at 18 kilometers per hour, still the speed record on the Moon!",
 cr:'NASA/JSC',nt:'Earth above my high-gain antenna',
 src:[['Guinness World Records: lunar speed record','https://www.guinnessworldrecords.com/world-records/66103-lunar-speed-record'],['NASA image AS17-134-20473','https://images.nasa.gov/details/as17-134-20473']]},
{s:7,pia:'as17-146-22367',em:'🅿️',t:'Parked forever, filming the liftoff',d:'14 Dec 1972',big:['35.7 km','driven in 3 days'],
 rows:[['Driving time','about 4.5 hours in total'],['Farthest from lander','7.6 km'],['Last job','my TV camera filmed Challenger\'s liftoff'],['Camera steered by','Ed Fendell, at Mission Control']],
 why:'My camera, steered from about 384,000 km away, recorded the best view of a lunar module lifting off. Then I stayed behind, parked forever.',
 story:"Gene parked me where my camera could watch. Steered from Earth, it filmed Challenger blasting off for home!",
 cr:'NASA/JSC',nt:'My final parking spot, camera pointed at the lander',
 src:[['NASA image AS17-146-22367','https://images.nasa.gov/details/as17-146-22367'],['NASA: Apollo 17','https://www.nasa.gov/mission/apollo-17/']]}
];""",
'fincomment': '/* The Apollo 17 rover is still parked east of the Challenger descent stage; LRO has photographed its tracks. */',
'finale': r"""const yrs=new Date().getFullYear()-1972;
await say("So... what happened to me after the astronauts left?",4);
await say("On December 14, 1972, Mission Control steered my camera and filmed Challenger lifting off. Gene Cernan was the last person to walk on the Moon.",8);
await say("NASA's Lunar Reconnaissance Orbiter has photographed my wheel tracks from space. They are still there!",6);
await say("In 2013, the Mars rover Opportunity finally drove farther than me. Way to go, Oppy!",5);
await say("Now, "+yrs+" years later, I'm still parked in the valley: abandoned, but not forgotten.",6);""",
'intro': "mood='happy';await say(\"I'm the Apollo 17 Lunar Roving Vehicle, a real car that astronauts drove on the Moon!\",5.5);mood='';",
'q': "Want to know how I got to the Moon? Let's go back in time!",
'after': "That's how I got to the Moon! Now let me show you where I drove.",
'endbtns': '<button id="frp" class="yl">↺ Recap</button><button id="fnx" class="pu">Next: Mars ➜</button>',
'fnx': gonext('lrv', 'opportunity.html') + "$('fnx').onclick=()=>{const b=$('fnx');if(b.dataset.busy)return;b.dataset.busy=1;b.classList.remove('pop');void b.offsetWidth;b.classList.add('pop');b.textContent=\"🚀 Let's go learn about Mars!\";try{fetch(NEXT_PAGE,{cache:'force-cache'}).catch(()=>{})}catch(e){}speak(\"Let's go learn about Mars!\",'LRO',2.5).then(()=>{goNext('next');setTimeout(()=>{delete b.dataset.busy;b.textContent='Next: Mars ➜'},8000)})};",
}
