const topo=require('topojson-client');
const world=require('world-atlas/countries-50m.json');
const lakes=require('@geo-maps/earth-lakes-1km/map.geo.json');
const L0=28.6,L1=42.4,T=5.6,B=-12.2,K=33;
const W=Math.round((L1-L0)*K),H=Math.round((T-B)*K);
const P=([lon,lat])=>[+((lon-L0)*K).toFixed(1),+((T-lat)*K).toFixed(1)];
const inView=c=>c[0]>L0-3&&c[0]<L1+3&&c[1]<T+3&&c[1]>B-3;
function ringPath(r){const pts=[];for(const c of r){const p=P(c);const l=pts[pts.length-1];if(!l||Math.abs(l[0]-p[0])+Math.abs(l[1]-p[1])>=1.1)pts.push(p)}if(pts.length<3)return'';return'M'+pts.map(p=>p.join(' ')).join('L')+'Z'}
function geomPath(g,filter){const polys=g.type==='Polygon'?[g.coordinates]:g.type==='MultiPolygon'?g.coordinates:[];return polys.filter(poly=>poly[0].some(inView)).map(poly=>poly.map(ringPath).join('')).join('')}
const fc=topo.feature(world,world.objects.countries);
const main={'404':'ke','800':'ug','834':'tz'};
const out={W,H,K,L0,T,countries:{},others:[],lakes:[]};
for(const f of fc.features){const id=String(f.id).padStart(3,'0');const d=geomPath(f.geometry);if(!d)continue;
  if(main[id])out.countries[main[id]]=d;else out.others.push(d);}
for(const g of lakes.geometries){const polys=g.type==='Polygon'?[g.coordinates]:g.coordinates;
  for(const poly of polys){const n=poly[0].filter(inView).length;if(n<1)continue;const xs=poly[0].map(c=>P(c)[0]),ys=poly[0].map(c=>P(c)[1]);if(Math.max(...xs)-Math.min(...xs)<7&&Math.max(...ys)-Math.min(...ys)<7)continue;const d=poly.map(ringPath).join('');if(d)out.lakes.push(d);}}
require('fs').writeFileSync('map.json',JSON.stringify(out));
console.log(W,H,Object.keys(out.countries),out.others.length,out.lakes.length,JSON.stringify(out).length);
