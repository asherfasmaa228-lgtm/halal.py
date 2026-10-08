import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="HalalScan Pro Max", layout="centered")

html = """
<!DOCTYPE html><html dir="rtl" lang="ar"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>HalalScan Pro Max</title><style>body{margin:0;font-family:sans-serif;background:#FFF8E1;text-align:center}header{background:linear-gradient(135deg,#1B5E20,#4CAF50);color:#fff;padding:14px;border-radius:0 0 22px 22px}#cam{width:92%;max-width:410px;height:280px;background:#000;border-radius:20px;margin:12px auto;overflow:hidden;position:relative}video,img{width:100%;height:100%;object-fit:cover}button{padding:12px 18px;border:none;border-radius:25px;margin:5px;font-weight:bold;cursor:pointer}.b1{background:#2E7D32;color:#fff}.b2{background:#1565C0;color:#fff}.b3{background:#E65100;color:#fff}#res{display:none;width:92%;max-width:410px;margin:10px auto;padding:16px;border-radius:18px}.halal{background:#E8F5E9;border:3px solid #4CAF50}.haram{background:#FFEBEE;border:3px solid #F44336}.ing{text-align:right;background:#fff;padding:12px;border-radius:12px;margin-top:8px;font-size:13px;line-height:1.7}.mode{width:92%;max-width:410px;margin:8px auto;display:flex;gap:6px}.mode button{flex:1;font-size:12px}</style></head><body>
<header><h3 style="margin:0">HalalScan Pro Max</h3><p style="margin:4px;font-size:11px">وضعين: طبق و كيس</p></header>
<div class="mode"><button onclick="setMode('dish')" id="m1" style="background:#2E7D32;color:white">وضع الطبق</button><button onclick="setMode('bag')" id="m2" style="background:#ddd">وضع الكيس</button></div>
<div id="cam"><video id="v" autoplay playsinline muted></video></div>
<button class="b1" onclick="openCam()">فتح الكاميرا</button>
<button class="b3" onclick="demo()">تجربة</button>
<div id="res"><h2 id="t"></h2><p id="c"></p><div class="ing" id="d"></div><button onclick="location.reload()" style="background:#333;color:white">جديد</button></div>
<script>
let mode='dish';
const HARAM=["pork","beer","wine","soju","alcohol","gelatin","lard","bacon","ham","خنزير","كحول"];
const DISHES={
bibimbap:{name:"بيبيمباب",halal:true,ing:"رز، خضار - حلال",safe:"حلال 100%"},
samgyeopsal:{name:"سامجيوبسال - خنزير",halal:false,ing:"بطن خنزير",safe:"حرام"},
soju:{name:"سوجو - كحول",halal:false,ing:"كحول 17%",safe:"حرام"},
ramen:{name:"رامن خنزير",halal:false,ing:"مرق خنزير",safe:"حرام"},
tteokbokki:{name:"توكبوكي",halal:true,ing:"كعك رز حلال",safe:"حلال"},
chips:{name:"شيبسي",halal:false,ing:"نكهة خنزير",safe:"حرام"},
choco:{name:"شوكولاتة",halal:true,ing:"كاكاو حلال",safe:"حلال"}
};
function setMode(m){mode=m;document.getElementById('m1').style.background=m=='dish'?'#2E7D32':'#ddd';document.getElementById('m2').style.background=m=='bag'?'#1565C0':'#ddd';}
async function openCam(){try{let s=await navigator.mediaDevices.getUserMedia({video:{facingMode:"environment"}});document.getElementById('v').srcObject=s;setTimeout(demo,1500);}catch(e){demo();}}
function showResult(k){let x=DISHES[k];let b=document.getElementById('res');b.style.display='block';b.className=x.halal?'halal':'haram';document.getElementById('t').innerHTML=(x.halal?'✅ ':'❌ ')+x.name;document.getElementById('c').innerText=x.safe;document.getElementById('d').innerHTML=x.ing;}
function demo(){if(mode=='dish'){let k=['bibimbap','tteokbokki','samgyeopsal','ramen','soju'];showResult(k[Math.floor(Math.random()*k.length)]);}else{let k=['chips','choco'];showResult(k[Math.floor(Math.random()*k.length)]);}}
</script></body></html>
"""
components.html(html, height=950, scrolling=True)
