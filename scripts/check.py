"""Check public page metadata, duplicate IDs, local links/assets, anchors and ZIP integrity."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from zipfile import ZipFile
import json
ROOT=Path(__file__).resolve().parent.parent
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.refs=[];self.h1=0;self.meta={};self.lang=None
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='html':self.lang=a.get('lang')
  if tag=='img':assert 'alt' in a and a.get('width') and a.get('height'),'Image needs alt and dimensions'
  if tag=='meta':self.meta[a.get('name',a.get('property'))]=a.get('content')
  for key in ['href','src']:
   if a.get(key):self.refs.append(a[key])
pages=[*ROOT.glob('*.html'),*(ROOT/'en').glob('*.html')]
parsed={}
for path in pages:
 p=Page();p.feed(path.read_text());parsed[path]=p
 assert p.h1==1, (path,'h1')
 assert len(p.ids)==len(set(p.ids)),(path,'duplicate IDs')
 assert p.lang in ['de','en'],(path,'language')
 assert p.meta.get('description') and p.meta.get('og:image'),(path,'metadata')
for path,p in parsed.items():
 for ref in p.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  target=(path.parent/unquote(u.path)).resolve() if u.path else path
  if target.is_dir():target/='index.html'
  assert target.is_relative_to(ROOT),(path,ref,'outside site root')
  assert target.exists(),(path,ref,'missing')
  if u.fragment and target in parsed:assert u.fragment in parsed[target].ids,(path,ref,'missing anchor')
for archive in (ROOT/'assets/marketing').glob('*.zip'):
 with ZipFile(archive) as z:
  assert z.testzip() is None
  assert len(z.namelist())==len(set(z.namelist()))
  assert len([name for name in z.namelist() if name.startswith('screenshots/') and name.endswith('.png')])==24
print(f'Passed: {len(pages)} pages; local links, assets, anchors, metadata and marketing ZIP.')
