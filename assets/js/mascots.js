/* Odyssey & Orbit — shared 3D cartoon mascots (needs three.js r128 loaded first).
   MASCOT.build(kind)          -> THREE.Group (cartoon machine with face, gloves and name sign)
   MASCOT.anim(obj,t,state)    -> animate it; state = {wave,talk,flying,mood}
   MASCOT.snapshot(kind,size,state) -> PNG data URL, auto-framed, transparent background
   kinds: 'surveyor3' | 'lrv' | 'opportunity' | 'ingenuity'                                   */
(function(){
const M=(c,o={})=>new THREE.MeshStandardMaterial(Object.assign({color:c,roughness:.6},o));
const B=c=>new THREE.MeshBasicMaterial({color:c});
const mesh=(g,m,p=[0,0,0],par)=>{const o=new THREE.Mesh(g,m);o.position.set(...p);par&&par.add(o);return o};
const cv=(w,h,f)=>{const c=document.createElement('canvas');c.width=w;c.height=h;f(c.getContext('2d'),w,h);return new THREE.CanvasTexture(c)};
const ez=p=>p<.5?2*p*p:1-Math.pow(-2*p+2,2)/2;
function rbox(w,h,d,r,n){const g=new THREE.BoxGeometry(w,h,d,n,n,n),p=g.attributes.position,v=new THREE.Vector3(),c=new THREE.Vector3(),hx=w/2-r,hy=h/2-r,hz=d/2-r;
for(let i=0;i<p.count;i++){v.fromBufferAttribute(p,i);c.set(Math.max(-hx,Math.min(hx,v.x)),Math.max(-hy,Math.min(hy,v.y)),Math.max(-hz,Math.min(hz,v.z)));v.sub(c);if(v.lengthSq()>1e-9)v.normalize().multiplyScalar(r);p.setXYZ(i,c.x+v.x,c.y+v.y,c.z+v.z)}
g.computeVertexNormals();return g}
function drawNasa(x,cx,cy,r){x.save();x.beginPath();x.arc(cx,cy,r,0,7);x.clip();x.fillStyle='#0b3d91';x.fillRect(cx-r,cy-r,2*r,2*r);x.fillStyle='#fff';
for(let i=0;i<14;i++){x.beginPath();x.arc(cx+Math.sin(i*97)*r*.8,cy+Math.cos(i*57)*r*.8,r*.03,0,7);x.fill()}
x.strokeStyle='#fc3d21';x.lineWidth=r*.14;x.lineCap='round';x.beginPath();x.moveTo(cx-r*1.05,cy+r*.55);x.quadraticCurveTo(cx-r*.1,cy-r*1.05,cx+r*1.05,cy-r*.15);x.stroke();
x.fillStyle='#fff';x.font='800 '+Math.round(r*.52)+'px Arial,sans-serif';x.textAlign='center';x.textBaseline='middle';x.fillText('NASA',cx,cy+r*.08);x.restore();
x.strokeStyle='#fff';x.lineWidth=r*.06;x.beginPath();x.arc(cx,cy,r,0,7);x.stroke()}
function drawFace(x,md,bl,mo){const W=512,H=300;x.clearRect(0,0,W,H);
const op=!bl&&md!=='happy',lk=md==='thinking'?[.4,-.5]:md==='sad'?[0,.2]:[0,0],ink='#2a1a10';
const brow=(cx,y,rot,len)=>{x.save();x.translate(cx,y);x.rotate(rot);x.strokeStyle='#3a2414';x.lineWidth=9;x.lineCap='round';x.beginPath();x.moveTo(-len/2,0);x.quadraticCurveTo(0,-14,len/2,0);x.stroke();x.restore()};
const eye=(cx,cy,rx,ry,wink)=>{
if(!op||wink){x.strokeStyle=ink;x.lineWidth=9;x.lineCap='round';x.beginPath();
if(md==='happy'){x.arc(cx,cy+22,rx*.7,Math.PI*1.12,Math.PI*1.88)}else{x.moveTo(cx-rx*.75,cy+6);x.quadraticCurveTo(cx,cy+(wink?-30:24),cx+rx*.75,cy+6)}
x.stroke();return}
x.fillStyle='#fff';x.strokeStyle=ink;x.lineWidth=6;x.beginPath();x.ellipse(cx,cy,rx,ry,0,0,7);x.fill();x.stroke();
const ir=rx*.74,ix=cx+lk[0]*rx*.3,iy=cy+lk[1]*ry*.3+(md==='sad'?8:0),g=x.createRadialGradient(ix,iy+8,4,ix,iy,ir);
g.addColorStop(0,'#d19552');g.addColorStop(.55,'#7a4a22');g.addColorStop(1,'#3b200c');
x.fillStyle=g;x.beginPath();x.arc(ix,iy,ir,0,7);x.fill();
x.fillStyle='#0a0604';x.beginPath();x.arc(ix,iy,ir*(md==='surprised'?.34:.5),0,7);x.fill();
x.fillStyle='#fff';x.beginPath();x.arc(ix-ir*.32,iy-ir*.34,ir*.26,0,7);x.fill();x.beginPath();x.arc(ix+ir*.3,iy+ir*.36,ir*.12,0,7);x.fill();
if(md==='sad'){x.fillStyle='rgba(255,255,255,.8)';x.beginPath();x.arc(ix+ir*.4,iy-ir*.05,ir*.13,0,7);x.fill()}};
const big=md==='surprised',rx=big?64:56,ry=big?78:66,ey=big?122:126;
eye(156,ey,rx,ry,false);eye(356,ey,rx,ry,md==='wink');
if(md==='surprised'){brow(156,16,-.05,64);brow(356,16,.05,64)}
else if(md==='thinking'){brow(156,22,-.3,64);brow(356,40,.12,64)}
else if(md==='sad'){brow(160,34,-.32,64);brow(352,34,.32,64)}
else if(md==='happy'){brow(156,32,-.1,60);brow(356,32,.1,60)}
else{brow(156,40,-.08,60);brow(356,40,.08,60)}
x.fillStyle='rgba(255,105,140,'+(md==='happy'?.5:md==='sad'?.18:.3)+')';x.beginPath();x.ellipse(70,212,34,20,0,0,7);x.fill();x.beginPath();x.ellipse(442,212,34,20,0,0,7);x.fill();
const mx=256,my=206;x.lineCap='round';
if(md==='surprised'){x.fillStyle='#8c1230';x.beginPath();x.ellipse(mx,my+24,24,34,0,0,7);x.fill();x.fillStyle='#ff7a8f';x.beginPath();x.ellipse(mx,my+42,15,11,0,0,7);x.fill()}
else if(md==='thinking'){x.strokeStyle='#8c1230';x.lineWidth=8;x.beginPath();x.moveTo(mx-34,my+30);x.quadraticCurveTo(mx-4,my+8,mx+10,my+26);x.quadraticCurveTo(mx+22,my+38,mx+38,my+22);x.stroke()}
else if(md==='sad'){x.strokeStyle='#8c1230';x.lineWidth=8;x.beginPath();x.moveTo(mx-40,my+38);x.quadraticCurveTo(mx,my+2,mx+40,my+38);x.stroke()}
else{const h=md==='happy'?50:26+mo*34,w=md==='happy'?68:54;
x.fillStyle='#8c1230';x.beginPath();x.moveTo(mx-w,my);x.quadraticCurveTo(mx,my+8,mx+w,my);x.quadraticCurveTo(mx+w*.7,my+h*1.3,mx,my+h*1.3);x.quadraticCurveTo(mx-w*.7,my+h*1.3,mx-w,my);x.fill();
x.fillStyle='#ff6f86';x.beginPath();x.ellipse(mx,my+h*.98,w*.48,h*.26,0,0,7);x.fill()}}
function drawSym(x,s){x.clearRect(0,0,128,128);x.lineJoin='round';x.lineCap='round';x.textAlign='center';x.textBaseline='middle';
if(s==='!'||s==='?'){x.font='900 112px Arial,sans-serif';x.lineWidth=14;x.strokeStyle='#1a2350';x.strokeText(s,64,68);x.fillStyle=s==='!'?'#ffd23f':'#ffffff';x.fillText(s,64,68)}
else if(s==='*'){x.fillStyle='#ffd23f';x.strokeStyle='#a8741a';x.lineWidth=4;[[40,70,26],[88,40,20],[92,96,15]].forEach(([a,b,r])=>{x.beginPath();for(let i=0;i<8;i++){const rr=i%2?r*.32:r,an=i*Math.PI/4-Math.PI/2;x.lineTo(a+Math.cos(an)*rr,b+Math.sin(an)*rr)}x.closePath();x.fill();x.stroke()})}
else if(s==='~'){x.strokeStyle='#9bb4ff';x.lineWidth=8;x.beginPath();for(let i=0;i<60;i++){const a=i*.3,r=4+i*.85;x.lineTo(64+Math.cos(a)*r*.9,64+Math.sin(a)*r*.9)}x.stroke()}}
const SIGN={surveyor3:['Surveyor 3','Moon Lander','(1967)'],lrv:['Apollo 17','Lunar Rover','(1972)'],opportunity:['Opportunity','Rover','(2004 – 2018)'],ingenuity:['Ingenuity','Mars Helicopter','(2021 – 2024)']};
const fitFont=(x,txt,max,maxW,style)=>{let s=max;x.font=style+' '+s+'px "Trebuchet MS",Arial,sans-serif';while(x.measureText(txt).width>maxW&&s>20){s-=2;x.font=style+' '+s+'px "Trebuchet MS",Arial,sans-serif'}};

function build(kind){
let q=4711;const rq=()=>(q=(q*16807)%2147483647)/2147483647;
const O=new THREE.Group(),G=new THREE.Group();O.add(G);
const dirt=(x,w,h,n,big)=>{for(let i=0;i<n;i++){x.fillStyle=rq()<.6?'rgba(110,70,35,'+(.05+rq()*.12)+')':'rgba(255,245,220,'+(.05+rq()*.1)+')';x.beginPath();x.ellipse(rq()*w,rq()*h,1+rq()*(big?7:4),1+rq()*(big?5:3),rq()*3,0,7);x.fill()}};
const creamT=cv(256,256,(x,w,h)=>{x.fillStyle='#f4e8cf';x.fillRect(0,0,w,h);const g=x.createLinearGradient(0,0,0,h);g.addColorStop(0,'rgba(255,255,255,.2)');g.addColorStop(1,'rgba(150,100,55,.3)');x.fillStyle=g;x.fillRect(0,0,w,h);dirt(x,w,h,420,1)});
const tanT=cv(256,256,(x,w,h)=>{x.fillStyle='#d6b98c';x.fillRect(0,0,w,h);const g=x.createLinearGradient(0,0,0,h);g.addColorStop(0,'rgba(255,240,205,.25)');g.addColorStop(1,'rgba(120,70,30,.35)');x.fillStyle=g;x.fillRect(0,0,w,h);x.strokeStyle='rgba(90,60,30,.4)';x.lineWidth=2;[.18,.5,.82].forEach(b=>{x.beginPath();x.moveTo(0,b*h);x.lineTo(w,b*h);x.stroke()});dirt(x,w,h,500,1)});
const treadT=cv(256,64,(x,w,h)=>{x.fillStyle='#3a2f27';x.fillRect(0,0,w,h);x.fillStyle='#6b5640';for(let i=0;i<24;i++)x.fillRect(i*w/24,0,w/48,h);dirt(x,w,h,160,0)});
const meshT=cv(256,64,(x,w,h)=>{x.fillStyle='#8f9296';x.fillRect(0,0,w,h);x.strokeStyle='#d9dde2';x.lineWidth=1.5;for(let i=-h;i<w;i+=8){x.beginPath();x.moveTo(i,0);x.lineTo(i+h,h);x.stroke();x.beginPath();x.moveTo(i+h,0);x.lineTo(i,h);x.stroke()}x.fillStyle='#e6c26a';for(let i=0;i<16;i++){x.save();x.translate(i*w/16+8,h/2);x.beginPath();x.moveTo(-6,-18);x.lineTo(4,0);x.lineTo(-6,18);x.lineTo(-1,18);x.lineTo(9,0);x.lineTo(-1,-18);x.closePath();x.fill();x.restore()}});
const cellT=cv(256,128,(x,w,h)=>{x.fillStyle='#15266a';x.fillRect(0,0,w,h);x.strokeStyle='#4663c4';x.lineWidth=2;for(let i=0;i<=8;i++){x.beginPath();x.moveTo(i*w/8,0);x.lineTo(i*w/8,h);x.stroke()}for(let j=0;j<=4;j++){x.beginPath();x.moveTo(0,j*h/4);x.lineTo(w,j*h/4);x.stroke()}x.strokeStyle='#d9b45a';x.lineWidth=6;x.strokeRect(2,2,w-4,h-4);dirt(x,w,h,120,0)});
const tan=M(0xffffff,{map:tanT,metalness:.3,roughness:.5,emissive:0x2a1c0c}),cream=M(0xffffff,{map:creamT,roughness:.5,emissive:0x1c150c}),brass=M(0xb98a2e,{metalness:.6,roughness:.35,emissive:0x2a1c00}),silv=M(0xd5dae0,{metalness:.5,roughness:.35,emissive:0x1a1c20}),
wh=M(0xfbfbff,{roughness:.45,emissive:0x15151a}),blk=M(0x15161c,{roughness:.5}),dark=M(0x2a2d36,{roughness:.4,metalness:.3}),dishM=M(0xe9e6df,{metalness:.4,roughness:.35,emissive:0x1d1b17}),
panM=M(0xffffff,{map:cellT,metalness:.4,roughness:.4,emissive:0x080c28}),tire=M(0xffffff,{map:treadT,roughness:.95,emissive:0x0a0805}),capM=M(0x2b2a2f,{roughness:.6,metalness:.4}),
carb=M(0x24262e,{roughness:.45,metalness:.35,emissive:0x0c0d12}),al=M(0xcfd4da,{metalness:.6,roughness:.35,emissive:0x15171a}),foilW=M(0xf4f2ec,{roughness:.5,emissive:0x1a1a18});
const limb=(a,b,r,m,par)=>{const A=new THREE.Vector3(...a),Bv=new THREE.Vector3(...b),d=Bv.clone().sub(A),o=mesh(new THREE.CylinderGeometry(r,r,d.length(),10),m,[0,0,0],par);o.position.copy(A).add(Bv).multiplyScalar(.5);o.quaternion.setFromUnitVectors(new THREE.Vector3(0,1,0),d.clone().normalize());return o};
const lgT=cv(256,256,(x,w,h)=>drawNasa(x,128,128,112));
const U={kind,wheels:[],wheelAxis:'z'};
/* ---- the face box (every machine has one) ---- */
mesh(rbox(1.0,.86,.84,.1,8),cream,[0,.95,0],G);
const fc=document.createElement('canvas');fc.width=512;fc.height=300;const fx=fc.getContext('2d'),ft=new THREE.CanvasTexture(fc);drawFace(fx,'',0,0);
mesh(new THREE.PlaneGeometry(1.0,.585),new THREE.MeshBasicMaterial({map:ft,transparent:true}),[0,.95,.426],G);
[-1,1].forEach(s=>mesh(rbox(.05,.36,.4,.02,2),brass,[s*.51,.95,-.06],G));

if(kind==='opportunity'){
mesh(rbox(1.9,.4,1.1,.09,6),tan,[0,0,0],G);mesh(rbox(1.96,.05,1.16,.02,2),brass,[0,.2,0],G);mesh(rbox(1.78,.05,1.0,.02,2),panM,[0,.26,0],G);
[-1,1].forEach(s=>{const w=mesh(rbox(1.7,.05,.56,.02,2),panM,[0,.2,s*.86],G);w.rotation.x=-.1*s;[-.6,.6].forEach(x=>limb([x,.1,s*.5],[x,.17,s*.76],.022,brass,G))});
mesh(new THREE.PlaneGeometry(.36,.36),new THREE.MeshBasicMaterial({map:lgT,transparent:true}),[-.15,-.01,.556],G);
mesh(new THREE.CylinderGeometry(.17,.21,.28,16),dark,[0,.42,0],G);
mesh(new THREE.CylinderGeometry(.045,.055,.5,12),silv,[0,1.62,-.02],G);mesh(new THREE.CylinderGeometry(.1,.1,.07,14),brass,[0,1.4,-.02],G);
const cam=new THREE.Group();cam.position.set(0,1.97,-.02);G.add(cam);
mesh(rbox(.86,.3,.3,.05,4),silv,[0,0,0],cam);mesh(new THREE.BoxGeometry(.88,.045,.32),brass,[0,.17,0],cam);
[-.22,.22].forEach(x=>{mesh(new THREE.CylinderGeometry(.095,.105,.14,18),dark,[x,0,.2],cam).rotation.x=Math.PI/2;mesh(new THREE.SphereGeometry(.07,14,10),B(0x2f6bff),[x,0,.275],cam)});
limb([-.72,.28,-.32],[-.82,1.25,-.38],.014,brass,G);
const dish=new THREE.Group();dish.position.set(.55,.3,-.34);G.add(dish);limb([0,0,0],[0,.14,0],.03,brass,dish);
const tilt=new THREE.Group();tilt.position.y=.16;tilt.rotation.x=.6;dish.add(tilt);mesh(new THREE.CylinderGeometry(.26,.26,.03,28),dishM,[0,0,0],tilt);
[1,-1].forEach(s=>[-.72,0,.72].forEach(x=>{const w=new THREE.Group();w.position.set(x,-.36,s*.72);G.add(w);
mesh(new THREE.CylinderGeometry(.3,.3,.26,24,1),[tire,capM,capM],[0,0,0],w).rotation.x=Math.PI/2;mesh(new THREE.CylinderGeometry(.14,.14,.28,16),brass,[0,0,0],w).rotation.x=Math.PI/2;
limb([x,-.36,s*.72],[x*.45,-.05,s*.6],.04,silv,G);U.wheels.push(w)}));
U.tick=(t,s)=>{dish.rotation.y=Math.sin(t*.9)*.4;tilt.rotation.x=.6+(s.mood==='sad'?.5:0);cam.rotation.y=Math.sin(t*.7)*.5};
}
else if(kind==='ingenuity'){
mesh(rbox(1.04,.06,.88,.02,2),brass,[0,.5,0],G);
mesh(new THREE.PlaneGeometry(.34,.34),new THREE.MeshBasicMaterial({map:lgT,transparent:true}),[-.506,1.0,0],G).rotation.y=-Math.PI/2;
[[1,1],[1,-1],[-1,1],[-1,-1]].forEach(([sx,sz])=>{limb([sx*.36,.55,sz*.3],[sx*.86,-.52,sz*.74],.035,carb,G);limb([sx*.62,0,sz*.53],[sx*.3,.5,sz*.25],.018,carb,G);mesh(new THREE.CylinderGeometry(.11,.13,.05,14),carb,[sx*.88,-.56,sz*.76],G)});
mesh(new THREE.CylinderGeometry(.08,.08,.08,14),dark,[.18,.47,.2],G);mesh(new THREE.SphereGeometry(.05,10,8),B(0x2f6bff),[.18,.42,.2],G);
mesh(new THREE.CylinderGeometry(.05,.07,1.15,12),silv,[0,1.95,0],G);mesh(new THREE.CylinderGeometry(.14,.16,.12,16),brass,[0,1.43,0],G);
const rotor=(y,flip)=>{const g=new THREE.Group();g.position.y=y;G.add(g);mesh(new THREE.CylinderGeometry(.1,.1,.09,14),silv,[0,0,0],g);
[0,Math.PI].forEach(a=>{const bg=new THREE.BoxGeometry(1.08,.025,.16);bg.translate(.6,0,0);const b=mesh(bg,carb,[0,0,0],g);b.rotation.y=a;b.rotation.x=flip*.12});
const disc=mesh(new THREE.CircleGeometry(1.15,40),new THREE.MeshBasicMaterial({color:0xd8e2f2,transparent:true,opacity:0,depthWrite:false,side:2}),[0,0,0],g);disc.rotation.x=-Math.PI/2;g.userData.disc=disc;return g};
const r1=rotor(1.9,1),r2=rotor(2.2,-1);
mesh(new THREE.CylinderGeometry(.035,.035,.18,8),silv,[0,2.42,0],G);mesh(rbox(.9,.05,.56,.02,2),panM,[0,2.52,0],G);
limb([.42,1.3,-.3],[.5,1.62,-.34],.012,brass,G);
U.tick=(t,s)=>{const rs=s.flying?.95:(s.mood==='sad'?.06:.32);U.sp+=rs;r1.rotation.y=U.sp;r2.rotation.y=-U.sp*1.03;r1.userData.disc.material.opacity=r2.userData.disc.material.opacity=rs>.5?.16:rs>.2?.07:0};
}
else if(kind==='surveyor3'){
/* tripod spaceframe under the face box, 3 legs with crushable footpads */
const C=[0,1,2].map(i=>{const a=i*2.0944-Math.PI/2;return[Math.cos(a)*.62,.44,Math.sin(a)*.62]});
C.forEach((c,i)=>{limb(c,C[(i+1)%3],.035,al,G);limb(c,[0,.56,0],.025,al,G);
const f=[c[0]*1.75,-.5,c[2]*1.75];limb(c,f,.05,al,G);limb([c[0]*.55,.52,c[2]*.55],[c[0]*1.3,-.15,c[2]*1.3],.022,al,G);
mesh(new THREE.CylinderGeometry(.19,.22,.08,18),foilW,[f[0],-.55,f[2]],G);mesh(new THREE.BoxGeometry(.13,.12,.13),brass,[c[0]*1.03,.36,c[2]*1.03],G)});
/* two white thermal compartments */
[-1,1].forEach(s=>mesh(rbox(.34,.28,.3,.04,3),foilW,[s*.62,.46,-.2],G));
/* scoop arm (surface sampler) folded at the front-left */
limb([-.32,.5,.3],[-.62,.2,.58],.03,al,G);limb([-.62,.2,.58],[-.75,.0,.7],.025,al,G);mesh(new THREE.BoxGeometry(.16,.1,.12),silv,[-.78,-.04,.72],G);
/* mast with solar panel + planar antenna */
mesh(new THREE.CylinderGeometry(.045,.055,1.25,12),silv,[0,1.98,-.18],G);
const sp=new THREE.Group();sp.position.set(0,2.6,-.18);G.add(sp);const pn=mesh(rbox(.95,.04,.62,.015,2),panM,[0,0,0],sp);pn.rotation.x=-.45;
const ant=mesh(rbox(.6,.035,.6,.015,2),dishM,[.0,2.18,.12],G);ant.rotation.x=1.05;
/* TV camera with its tilted mirror, on top-right of the box */
mesh(new THREE.CylinderGeometry(.1,.11,.34,16),silv,[.33,1.55,-.12],G);const mir=new THREE.Group();mir.position.set(.33,1.78,-.12);G.add(mir);
const mm=mesh(new THREE.BoxGeometry(.2,.03,.16),M(0x2f6bff,{metalness:.9,roughness:.15,emissive:0x0a1a55}),[0,0,0],mir);mm.rotation.z=.7;
/* omni antenna whips */
[-1,1].forEach(s=>limb([s*.45,.44,-.3],[s*.75,1.35,-.42],.012,brass,G));
U.tick=(t,s)=>{mir.rotation.y=Math.sin(t*.8)*.7;sp.rotation.z=Math.sin(t*.6)*.04};
}
else if(kind==='lrv'){
/* Apollo Lunar Roving Vehicle: open chassis, 4 wire-mesh wheels with fenders, 2 seats, umbrella antenna */
mesh(rbox(2.4,.09,1.2,.03,2),al,[0,.08,0],G);mesh(rbox(2.1,.04,1.0,.02,2),M(0x9aa3ad,{metalness:.5,roughness:.4}),[0,.14,0],G);
mesh(new THREE.CylinderGeometry(.09,.12,.4,12),al,[0,.33,0],G);
const meshM=M(0xffffff,{map:meshT,metalness:.5,roughness:.45,emissive:0x111111}),fendM=M(0xd2d6dc,{metalness:.3,roughness:.5,emissive:0x101214});
[[1,1],[1,-1],[-1,1],[-1,-1]].forEach(([sx,sz])=>{const w=new THREE.Group();w.position.set(sx*.9,-.2,sz*.66);G.add(w);
mesh(new THREE.CylinderGeometry(.36,.36,.24,26,1,true),meshM,[0,0,0],w).rotation.x=Math.PI/2;
const hub=mesh(new THREE.CylinderGeometry(.13,.13,.26,14),dark,[0,0,0],w);hub.rotation.x=Math.PI/2;
for(let i=0;i<3;i++){const s2=mesh(new THREE.BoxGeometry(.66,.03,.02),silv,[0,0,sz*.12],w);s2.rotation.z=i*Math.PI/3}
const fg=new THREE.Group();fg.position.set(sx*.9,-.2,sz*.66);fg.rotation.z=Math.PI/2;G.add(fg);const fm=mesh(new THREE.CylinderGeometry(.43,.43,.28,18,1,true,0,Math.PI),fendM,[0,0,0],fg);fm.rotation.x=Math.PI/2;fm.material.side=2;
limb([sx*.9,-.2,sz*.66],[sx*.62,.08,sz*.45],.035,al,G);U.wheels.push(w)});
/* two seats at the back */
[-1,1].forEach(s=>{mesh(new THREE.BoxGeometry(.4,.05,.36),M(0x3a5a9a,{roughness:.6}),[-.78,.32,s*.3],G);mesh(new THREE.BoxGeometry(.05,.38,.36),M(0x3a5a9a,{roughness:.6}),[-1.0,.5,s*.3],G);limb([-.78,.14,s*.3],[-.78,.3,s*.3],.02,al,G)});
/* T-handle hand controller */
limb([.55,.2,0],[.62,.5,0],.025,dark,G);limb([.62,.5,-.1],[.62,.5,.1],.025,dark,G);
/* umbrella high-gain antenna + low-gain helix + TV camera */
limb([1.0,.14,-.35],[1.0,1.55,-.35],.025,al,G);const umb=new THREE.Group();umb.position.set(1.0,1.62,-.35);umb.rotation.set(.5,0,-.35);G.add(umb);
mesh(new THREE.ConeGeometry(.42,.16,18,1,true),M(0xe8e3d4,{roughness:.5,side:2,emissive:0x1a1810,wireframe:false}),[0,0,0],umb).rotation.x=Math.PI;
limb([.85,.14,.4],[.85,1.15,.4],.018,al,G);mesh(new THREE.CylinderGeometry(.05,.05,.32,10),brass,[.85,1.28,.4],G);
mesh(new THREE.BoxGeometry(.22,.16,.16),dark,[1.12,.95,.15],G);mesh(new THREE.SphereGeometry(.05,10,8),B(0x2f6bff),[1.23,.95,.15],G);limb([1.12,.14,.15],[1.12,.87,.15],.02,al,G);
/* battery boxes + NASA logo + flag on the front */
mesh(rbox(.36,.18,.5,.03,2),brass,[1.0,.25,0],G);
mesh(new THREE.PlaneGeometry(.28,.28),new THREE.MeshBasicMaterial({map:lgT,transparent:true}),[.7,.27,.505],G);
U.tick=(t,s)=>{umb.rotation.y=Math.sin(t*.5)*.25};
}
/* ---- arms + gloves + name sign (all machines) ---- */
const arm=s=>{const a=new THREE.Group();a.position.set(.58*s,.84,.1);G.add(a);
const pts=[[0,0,0],[.2*s,-.05,.05],[.38*s,-.17,.1],[.42*s,-.38,.12]].map(p=>new THREE.Vector3(...p)),cu=new THREE.CatmullRomCurve3(pts);
mesh(new THREE.TubeGeometry(cu,20,.058,10,false),blk,[0,0,0],a);
for(let i=1;i<8;i++){const u=i/9,r=mesh(new THREE.TorusGeometry(.066,.016,6,14),blk,[0,0,0],a);r.position.copy(cu.getPointAt(u));r.quaternion.setFromUnitVectors(new THREE.Vector3(0,0,1),cu.getTangentAt(u))}
mesh(new THREE.SphereGeometry(.09,12,8),dark,[0,0,0],a);
const gl=new THREE.Group();gl.position.copy(pts[3]);gl.rotation.order='ZYX';a.add(gl);
const pm=mesh(new THREE.SphereGeometry(.16,18,14),wh,[0,0,0],gl);pm.scale.set(1,1.05,.9);
[-.07,0,.07].forEach(x=>mesh(new THREE.SphereGeometry(.06,10,8),wh,[x,-.12,.09],gl));
mesh(new THREE.SphereGeometry(.07,10,8),wh,[s<0?0:-.11,s<0?.2:.1,s<0?.03:.1],gl);
if(s<0)mesh(new THREE.CylinderGeometry(.05,.055,.12,10),wh,[0,.15,.03],gl);
a.userData.gl=gl;return a};
const A0=arm(-1),A1=arm(1);
const tx=SIGN[kind]||['NASA','Explorer',''];
const sgT=cv(512,380,(x,w,h)=>{const g=x.createLinearGradient(0,0,0,h);g.addColorStop(0,'#14337d');g.addColorStop(1,'#0a1c52');x.fillStyle=g;x.fillRect(0,0,w,h);
x.strokeStyle='#f0c24a';x.lineWidth=10;x.strokeRect(14,14,w-28,h-28);drawNasa(x,w/2,80,46);
x.textAlign='center';x.textBaseline='middle';x.fillStyle='#fff';fitFont(x,tx[0],72,440,'italic 900');x.fillText(tx[0],w/2,178);
x.fillStyle='#ffd23f';fitFont(x,tx[1],60,440,'italic 900');x.fillText(tx[1],w/2,248);
x.fillStyle='#fff';x.font='700 36px Arial,sans-serif';x.fillText(tx[2],w/2,318)});
const sg=new THREE.Group();sg.rotation.y=-.25;sg.rotation.z=-.06;A1.userData.gl.add(sg);
limb([0,-.3,0],[0,.45,0],.03,brass,sg);mesh(new THREE.SphereGeometry(.045,10,8),brass,[0,-.3,0],sg);
mesh(rbox(1.04,.8,.06,.03,4),brass,[.14,.8,0],sg);mesh(new THREE.PlaneGeometry(.94,.7),new THREE.MeshBasicMaterial({map:sgT}),[.14,.8,.036],sg);
mesh(new THREE.PlaneGeometry(.94,.7),M(0x0a1c52),[.14,.8,-.036],sg).rotation.y=Math.PI;
/* puff when flying/driving, light, mood symbol */
const fl=mesh(new THREE.SphereGeometry(kind==='ingenuity'?.3:.22,10,8),kind==='ingenuity'?new THREE.MeshBasicMaterial({color:0xd9a77a,transparent:true,opacity:.55}):B(0xff9a3c),[0,kind==='ingenuity'?-.75:-.7,kind==='ingenuity'?0:-.15],G);fl.scale.setScalar(.01);
const li=new THREE.PointLight(0x66e0ff,0,7);O.add(li);
const sc2=document.createElement('canvas');sc2.width=sc2.height=128;const sx=sc2.getContext('2d'),st=new THREE.CanvasTexture(sc2),sym=new THREE.Sprite(new THREE.SpriteMaterial({map:st,transparent:true,depthTest:false}));
const tall=kind==='ingenuity'||kind==='surveyor3';sym.position.set(tall?-1.05:1.15,tall?1.55:2.1,.3);sym.scale.setScalar(.01);sym.renderOrder=5;O.add(sym);
Object.assign(U,{G,arms:[A0,A1],fl,li,fx,ft,fk:'',sx,st,sk:'',sym,sT0:0,sp:0,symY:sym.position.y});
O.userData=U;return O}

function anim(L,t,s){s=s||{};const u=L.userData,md=s.mood||'',tk=s.talk?1:0,wave=s.wave;
u.G.position.y=Math.sin(t*3)*.06+(md==='surprised'?Math.abs(Math.sin(t*6))*.14:0);
u.G.rotation.z=Math.sin(t*2)*.04+(md==='thinking'?.1:0);u.G.rotation.x=md==='sad'?.1:0;
let l=[0,-.55+Math.sin(t*3)*.05],r=[-.3,.5+Math.sin(t*3+1)*.05];
if(wave)l=[0,-2.4+Math.sin(t*9)*.35];
if(md==='thinking')l=[-1.25,-.35];
if(md==='sad'){l=[0,-.3];r=[0,.25]}
if(md==='surprised'){l=[0,-2.0+Math.sin(t*12)*.1];r=[-.2,.9]}
if(md==='happy'||md==='wink')l[1]+=Math.sin(t*5)*.12;
if(tk)r[1]+=Math.abs(Math.sin(t*5))*.15;
const A0=u.arms[0],A1=u.arms[1];A0.rotation.set(l[0],0,l[1]);A1.rotation.set(r[0],0,r[1]);
A0.userData.gl.rotation.set(0,0,wave?Math.sin(t*9+1)*.28:0);A1.userData.gl.rotation.set(-A1.rotation.x,0,-A1.rotation.z);
if(u.kind!=='ingenuity'){u.sp+=s.flying?.3:0;u.wheels.forEach((g,i)=>g.rotation.z=-u.sp+Math.sin(t*3+i)*.05)}
u.tick&&u.tick(t,s);
const bl=(t%3.2)<.12?1:0,mo=tk?Math.abs(Math.sin(t*12)):0,key=md+'|'+bl+'|'+Math.round(mo*5);
if(u.fk!==key){u.fk=key;drawFace(u.fx,md,bl,mo);u.ft.needsUpdate=true}
const sy={surprised:'!',thinking:'?',happy:'*',wink:'*',sad:'~'}[md]||'';
if(u.sk!==sy){u.sk=sy;u.sT0=t;drawSym(u.sx,sy||' ');u.st.needsUpdate=true}
const pp=Math.min(1,Math.max(0,(t-u.sT0)*3));u.sym.visible=!!sy;
u.sym.scale.setScalar(sy?.6*(pp<1?ez(pp)*1.15:1+Math.sin(t*5)*.05):.01);u.sym.position.y=u.symY+Math.sin(t*4)*.05;
if(s.flying){const f=1+Math.sin(t*(u.kind==='ingenuity'?30:40))*.25;if(u.kind==='ingenuity')u.fl.scale.set(f*1.6,.25,f*1.6);else u.fl.scale.setScalar(f)}else u.fl.scale.setScalar(.01)}

let SR=null;
function snapshot(kind,size,state){size=size||440;state=state||{};
if(!SR){SR=new THREE.WebGLRenderer({antialias:true,alpha:true,preserveDrawingBuffer:true});SR.setPixelRatio(1)}
SR.setSize(size,size);const s2=new THREE.Scene(),c2=new THREE.PerspectiveCamera(30,1,.1,80);
s2.add(new THREE.AmbientLight(0xffffff,.95));const d=new THREE.DirectionalLight(0xffffff,1.5);d.position.set(3,5,7);s2.add(d);
const m=build(kind);s2.add(m);anim(m,state.t||.5,state);m.updateMatrixWorld(true);
const bx=new THREE.Box3();m.traverse(o=>{if(o.isMesh&&o.visible&&o.scale.x>.05)bx.expandByObject(o)});
const c=bx.getCenter(new THREE.Vector3()),z=bx.getSize(new THREE.Vector3()),dist=Math.max(z.y,z.x)*.5/Math.tan(15*Math.PI/180)*(state.pad||1.08)+z.z*.5;
c2.position.set(c.x+dist*.12,c.y+dist*.08,c.z+dist);c2.lookAt(c);SR.render(s2,c2);const url=SR.domElement.toDataURL('image/png');
s2.traverse(o=>{if(o.geometry)o.geometry.dispose();if(o.material){[].concat(o.material).forEach(mm=>{mm.map&&mm.map.dispose();mm.dispose()})}});return url}
window.MASCOT={build,anim,snapshot,drawNasa};
})();
