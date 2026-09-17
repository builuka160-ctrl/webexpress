import re,subprocess,sys,tempfile,os,urllib.request
page=sys.argv[1]; sec=sys.argv[2]; vid=sys.argv[3]
html=urllib.request.urlopen('http://127.0.0.1:8099/'+page).read().decode()
probe="""<script>
(function(){
 var out=function(t){document.body.setAttribute('data-test',t)};
 var v=document.getElementById('%s'),s=document.getElementById('%s');
 var tries=0;
 var go=function(){
   tries++;
   if(!v||!s){out('no-elements');return}
   if(!v.duration||isNaN(v.duration)){if(tries<200){setTimeout(go,50)}else{out('video-never-ready src='+v.src)}return}
   var total=s.offsetHeight-window.innerHeight;
   document.documentElement.style.scrollBehavior='auto';window.scrollTo({top:s.offsetTop+Math.round(total*0.75),behavior:'instant'});
   window.dispatchEvent(new Event('scroll'));
   setTimeout(function(){
     var r=s.getBoundingClientRect();var p=Math.max(0,Math.min(1,-r.top/total));out('dur='+v.duration.toFixed(2)+' t='+v.currentTime.toFixed(2)+' expected='+(p*v.duration).toFixed(2)+' p='+p.toFixed(2));
   },4000);
 };
 window.addEventListener('load',function(){setTimeout(go,300)});
})();
</script></body>"""%(vid,sec)
import os.path as _p
tmp=_p.join('/home/kali/webexpress-site',_p.dirname(page),'.scrubtest.html')
open(tmp,'w').write(html.replace('</body>',probe))
r=subprocess.run(['timeout','60','google-chrome-stable','--headless=new','--disable-gpu','--no-sandbox',
  '--autoplay-policy=no-user-gesture-required','--virtual-time-budget=12000','--window-size=1440,900','--dump-dom',
  'http://127.0.0.1:8099/'+_p.join(_p.dirname(page),'.scrubtest.html')],capture_output=True,text=True)
os.remove(tmp)
m=re.search(r'data-test="([^"]*)"',r.stdout)
print(page,'->',m.group(1) if m else 'NO RESULT')
