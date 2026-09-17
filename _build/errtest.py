import re,subprocess,os,sys,urllib.request
page=sys.argv[1]
html=urllib.request.urlopen('http://127.0.0.1:8099/'+page).read().decode()
pre="<script>window.__errs=[];window.addEventListener('error',function(e){window.__errs.push(e.message+' @'+e.lineno)});</script></head>"
probe="""<script>
window.addEventListener('load',function(){setTimeout(function(){
 var v=document.querySelector('video');
 document.body.setAttribute('data-test','errs='+JSON.stringify(window.__errs)+' videos='+document.querySelectorAll('video').length+
  ' src='+(v?v.getAttribute('src'):'none')+' w='+window.innerWidth+' scrub='+(document.querySelector('.scrub')?document.querySelector('.scrub').className:'-'));
},600)});
</script></body>"""
tmp='/home/kali/webexpress-site/.errtest.html'
open(tmp,'w').write(html.replace('</head>',pre).replace('</body>',probe))
r=subprocess.run(['timeout','60','google-chrome-stable','--headless=new','--disable-gpu','--no-sandbox',
  '--virtual-time-budget=8000','--window-size=1440,900','--dump-dom','http://127.0.0.1:8099/.errtest.html'],capture_output=True,text=True)
os.remove(tmp)
m=re.search(r'data-test="([^"]*)"',r.stdout)
print(m.group(1) if m else 'NO RESULT')
