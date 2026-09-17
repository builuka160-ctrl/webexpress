#!/usr/bin/env python3
"""Injects the RU/LV switcher, dictionary and runtime into a demo page."""
import json, sys, os

RUNTIME = """
<script>
/* i18n: словарь ru -> lv, подмена текстовых узлов и атрибутов без перезагрузки */
(function(){
  var LV=__DICT__;
  var KEY='wx-lang';
  var qs=new URLSearchParams(location.search).get('lang');
  var lang=(qs||localStorage.getItem(KEY)||'ru').toLowerCase();
  if(lang!=='lv')lang='ru';
  var norm=function(s){return s.replace(/\\s+/g,' ').trim()};
  window.tr=function(s){if(lang!=='lv')return s;return LV[norm(s)]||s};
  window.wxLang=function(){return lang};

  var nodes=[],attrs=[],metas=[],title=document.title;
  var ATTRS=['alt','placeholder','aria-label','title','data-label'];
  function collect(){
    var w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT,{acceptNode:function(n){
      var p=n.parentNode&&n.parentNode.nodeName;
      if(p==='SCRIPT'||p==='STYLE')return NodeFilter.FILTER_REJECT;
      return norm(n.nodeValue)?NodeFilter.FILTER_ACCEPT:NodeFilter.FILTER_REJECT;
    }});
    var n;while(n=w.nextNode())nodes.push([n,n.nodeValue]);
    ATTRS.forEach(function(a){
      Array.prototype.forEach.call(document.querySelectorAll('['+a+']'),function(el){
        attrs.push([el,a,el.getAttribute(a)]);
      });
    });
    Array.prototype.forEach.call(document.querySelectorAll('meta[name="description"],meta[property^="og:"]'),function(m){
      metas.push([m,m.getAttribute('content')]);
    });
  }
  function apply(){
    var on=lang==='lv';
    nodes.forEach(function(p){
      var o=p[1],t=LV[norm(o)];
      p[0].nodeValue=(on&&t)?o.match(/^\\s*/)[0]+t+o.match(/\\s*$/)[0]:o;
    });
    attrs.forEach(function(p){
      var t=LV[norm(p[2])];
      p[0].setAttribute(p[1],(on&&t)?t:p[2]);
    });
    metas.forEach(function(p){
      var t=LV[norm(p[1])];
      p[0].setAttribute('content',(on&&t)?t:p[1]);
    });
    document.title=(on&&LV[norm(title)])?LV[norm(title)]:title;
    document.documentElement.lang=on?'lv':'ru';
    Array.prototype.forEach.call(document.querySelectorAll('.lang button'),function(b){
      b.setAttribute('aria-pressed',String(b.dataset.lang===lang));
    });
  }
  function set(l){
    lang=l;try{localStorage.setItem(KEY,l)}catch(e){}
    apply();
    document.dispatchEvent(new CustomEvent('wx:lang',{detail:l}));
  }
  document.addEventListener('DOMContentLoaded',function(){
    collect();apply();
    Array.prototype.forEach.call(document.querySelectorAll('.lang button'),function(b){
      b.addEventListener('click',function(){set(b.dataset.lang)});
    });
  });
})();
</script>
"""

SWITCH = ('<div class="lang" role="group" aria-label="Valoda / Язык">'
          '<button type="button" data-lang="ru" aria-pressed="true">RU</button>'
          '<button type="button" data-lang="lv" aria-pressed="false">LV</button>'
          '</div>')

def inject(page, css, anchor, css_anchor):
    s = open(page).read()
    lv = json.load(open(os.path.join(os.path.dirname(page), '.lv.json')))
    if 'window.wxLang' in s:
        raise SystemExit('already injected: ' + page)
    # switcher markup
    assert anchor in s, 'nav anchor not found'
    s = s.replace(anchor, SWITCH + '\n    ' + anchor, 1)
    # switcher styles
    assert css_anchor in s, 'css anchor not found'
    s = s.replace(css_anchor, css + css_anchor, 1)
    # runtime before the page's own script
    i = s.rindex('<script>')
    runtime = RUNTIME.replace('__DICT__', json.dumps(lv, ensure_ascii=False))
    s = s[:i] + runtime.strip() + '\n' + s[i:]
    open(page, 'w').write(s)
    print('injected', page, len(lv), 'strings')

if __name__ == '__main__':
    site = sys.argv[1]
    cfg = json.load(open(os.path.join(os.path.dirname(__file__), 'i18n_sites.json')))[site]
    inject(cfg['page'], cfg['css'], cfg['anchor'], cfg['css_anchor'])
