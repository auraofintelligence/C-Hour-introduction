"""Check generated local links, fragments, image assets and reference integrity."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[1]
class Scan(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.ids=set();self.h1=0;self.hero=0;self.image_missing_alt=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.add(a['id'])
        if tag=='h1':self.h1+=1
        if 'hero-image' in a.get('class',''):self.hero+=1
        if tag=='img' and 'alt' not in a:self.image_missing_alt+=1
        for prop in ['href','src']:
            if prop in a:self.links.append(a[prop])
scans={};errors=[]
for p in ROOT.glob('*.html'):
    s=Scan();s.feed(p.read_text(encoding='utf-8'));scans[p.name]=s
    if s.h1!=1:errors.append(f'{p.name}: needs one h1, got {s.h1}')
    if s.hero!=1:errors.append(f'{p.name}: needs one hero image')
    if s.image_missing_alt:errors.append(f'{p.name}: missing image alt')
for name,s in scans.items():
    for link in s.links:
        u=urlparse(link)
        if u.scheme or u.netloc:continue
        target=unquote(u.path) or name
        if not (ROOT/target).exists():errors.append(f'{name}: missing {target}')
        if u.fragment and target in scans and unquote(u.fragment) not in scans[target].ids:errors.append(f'{name}: missing anchor {target}#{u.fragment}')
refs=json.loads((ROOT/'data/references.json').read_text(encoding='utf-8-sig'))
for ref in refs['documents']:
    p=ROOT/ref['file']
    if not p.exists():errors.append(f'Missing source: {p.name}')
    elif hashlib.sha256(p.read_bytes()).hexdigest()!=ref['sha256']:errors.append(f'Source changed: {p.name}')
if errors:print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(scans)} HTML pages, local links and fragments, image assets, and {len(refs["documents"])} unchanged original documents.')
