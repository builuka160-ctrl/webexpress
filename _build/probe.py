import re,subprocess,os,sys,urllib.request
page,expr=sys.argv[1],sys.argv[2]
html=urllib.request.urlopen('http://127.0.0.1:8099/'+page).read().decode()
probe="""<script>window.addEventListener('load',function(){setTimeout(function(){
 document.body.setAttribute('data-test',String(%s));},700)});</script></body>"""%expr
tmp=os.path.join('/home/kali/webexpress-site',os.path.dirname(page),'.p.html')
open(tmp,'w').write(html.replace('</body>',probe))
r=subprocess.run(['timeout','60','google-chrome-stable','--headless=new','--disable-gpu','--no-sandbox',
 '--virtual-time-budget=9000','--window-size=1440,900','--dump-dom',
 'http://127.0.0.1:8099/'+os.path.join(os.path.dirname(page),'.p.html')],capture_output=True,text=True)
os.remove(tmp)
m=re.search(r'data-test="([^"]*)"',r.stdout)
print(m.group(1).replace('&quot;','"') if m else 'NO RESULT')
