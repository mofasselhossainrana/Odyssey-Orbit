/* Stylized Moon maps made in code (equirectangular, longitude -180 at the left edge).
   Maria (dark "seas") sit roughly at their real places so landing pins land in the right region.
   MOONMAP() -> {c: colour map data URL, h: height map data URL}. Not real NASA imagery. */
(function(){
const MARIA=[[33,-16,17,14],[28,17,9,8],[8.5,31,11,9],[17,59,7,6],[-8,51,9,8],[-15,35,5,5],[-21,-17,9,8],[-24,-39,5,5],[18,-57,20,26],[56,1,6,30],[7,-31,7,7],[-10,-23,5,5],[13,4,4,4],[-2,-5,6,9],[1,86,5,5],[37,-2,5,10],[-36,24,4,7]];
function rng(s){return()=>(s=(s*16807)%2147483647)/2147483647}
window.MOONMAP=function(){const W=1024,H=512,r=rng(1967);
const mk=()=>{const c=document.createElement('canvas');c.width=W;c.height=H;return[c,c.getContext('2d')]};
const [cc,x]=mk(),[hc,h]=mk();
const px=lo=>(lo+180)/360*W,py=la=>(90-la)/180*H;
x.fillStyle='#a6a4a0';x.fillRect(0,0,W,H);h.fillStyle='#b4b4b4';h.fillRect(0,0,W,H);
for(let i=0;i<9000;i++){const v=140+r()*60;x.fillStyle='rgba('+v+','+v+','+(v-4)+','+(.05+r()*.08)+')';x.fillRect(r()*W,r()*H,1+r()*3,1+r()*2)}
/* maria: dark and low */
MARIA.forEach(([la,lo,rl,ro])=>{const cx=px(lo),cy=py(la),sx=ro/360*W/Math.max(.35,Math.cos(la*Math.PI/180)),sy=rl/180*H;
for(let k=0;k<3;k++){const g=x.createRadialGradient(0,0,0,0,0,1);g.addColorStop(0,'rgba(66,66,72,.5)');g.addColorStop(.7,'rgba(74,74,80,.42)');g.addColorStop(1,'rgba(90,90,96,0)');
x.save();x.translate(cx+(r()-.5)*sx*.3,cy+(r()-.5)*sy*.3);x.scale(sx*(.8+r()*.4),sy*(.8+r()*.4));x.fillStyle=g;x.beginPath();x.arc(0,0,1,0,7);x.fill();x.restore();
const g2=h.createRadialGradient(0,0,0,0,0,1);g2.addColorStop(0,'rgba(60,60,60,.45)');g2.addColorStop(1,'rgba(60,60,60,0)');h.save();h.translate(cx,cy);h.scale(sx,sy);h.fillStyle=g2;h.beginPath();h.arc(0,0,1,0,7);h.fill();h.restore()}});
/* craters */
const crater=(cx,cy,rr,lat)=>{const sx=1/Math.max(.3,Math.cos(lat*Math.PI/180));
[[x,'rgba(40,40,44,.35)','rgba(235,235,230,.35)'],[h,'rgba(40,40,40,.6)','rgba(250,250,250,.5)']].forEach(([c,dk,lt])=>{c.save();c.translate(cx,cy);c.scale(sx,1);
c.fillStyle=lt;c.beginPath();c.arc(-rr*.12,-rr*.12,rr*1.12,0,7);c.fill();c.fillStyle=dk;c.beginPath();c.arc(rr*.08,rr*.08,rr,0,7);c.fill();c.restore()})};
for(let i=0;i<1400;i++){const la=(r()*2-1)*80,cx=r()*W,cy=py(la),rr=.8+Math.pow(r(),5)*16;crater(cx,cy,rr,la)}
/* Tycho and Copernicus with bright rays */
[[-43,-11,9],[9.6,-20,7]].forEach(([la,lo,rr])=>{const cx=px(lo),cy=py(la);x.strokeStyle='rgba(245,245,240,.07)';x.lineCap='round';
for(let k=0;k<26;k++){const a=r()*6.28,L=30+r()*110;x.lineWidth=1+r()*3;x.beginPath();x.moveTo(cx,cy);x.lineTo(cx+Math.cos(a)*L*1.4,cy+Math.sin(a)*L);x.stroke()}crater(cx,cy,rr,la)});
return{c:cc.toDataURL('image/jpeg',.9),h:hc.toDataURL('image/jpeg',.9)}};
})();
