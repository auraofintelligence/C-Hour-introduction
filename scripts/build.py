"""Build the public C-Hour introduction from reviewed content and source records."""
from pathlib import Path
import json, html, re, argparse
from urllib.parse import quote

ROOT=Path(__file__).resolve().parents[1]
BASE='https://auraofintelligence.github.io/C-Hour-introduction/'
def load(name,default):
    p=ROOT/'data'/name
    return json.loads(p.read_text(encoding='utf-8-sig')) if p.exists() else default
def esc(value): return html.escape(str(value),quote=True)
def rich(value):
    value=esc(value)
    value=re.sub(r'\[([EPS][0-9]+)\]',lambda m:f'<a href="references.html#{m[1]}" aria-label="Source {m[1]}">[{m[1]}]</a>',value)
    return value
def para(text):return f'<p>{rich(text)}</p>'
def slug(text):return re.sub(r'[^a-z0-9]+','-',text.lower()).strip('-')
def img_path(name):
    name=name.removeprefix('assets/images/')
    if not name.endswith(('.webp','.png')):name+='.webp'
    return 'assets/images/'+name if (ROOT/'assets/images'/name).exists() else 'assets/images/home.webp'
def image(name,alt,classes='',lazy=True):return f'<img class="{classes}" src="{img_path(name)}" alt="{esc(alt)}" width="1536" height="1024" '+('loading="lazy" decoding="async"' if lazy else 'fetchpriority="high"')+'>'
def button(label,url,secondary=False):return f'<a class="button{" secondary" if secondary else ""}" href="{esc(url)}">{label}</a>'

parser=argparse.ArgumentParser();parser.add_argument('--batch',type=int,default=2);args=parser.parse_args()
all_chapters=load('chapters.json',[])
chapters=all_chapters if args.batch>1 else []
refs=load('references.json',{'documents':[],'links':[],'missing':[]})
projects=load('projects.json',[])
if isinstance(projects,dict):projects=projects.get('projects',[])
pages=[('index','Welcome')]+[(p['slug'],p.get('shortTitle',p['title'])) for p in chapters]
if args.batch>1:pages.append(('projects','Connected projects'))
pages += [('references','Reference library')]
if args.batch>1:pages.append(('corrections','Reading the archive'))
pages += [('licence','Licence')]
if args.batch>1:pages += [('site-map','Site map')]

def nav(current):
    links=[('index.html#explore','Explore'),('index.html#the-idea','The idea'),('projects.html' if args.batch>1 else 'index.html#connections','Connected projects'),('references.html','References')]
    return '<header class="site-header"><div class="wrap header-inner"><a class="brand" href="index.html" aria-label="C-Hour home"><img src="assets/images/logo.png" alt="" width="43" height="43">C-Hour</a><button class="menu-toggle" aria-expanded="false" aria-controls="main-nav">Menu</button><nav id="main-nav" class="main-nav" aria-label="Main navigation">'+''.join(f'<a href="{u}"'+(' aria-current="page"' if u==current+'.html' else '')+f'>{l}</a>' for u,l in links)+f'<a class="nav-cta" href="{"choose-an-adventure.html" if chapters else "index.html#explore"}">Find your adventure <span aria-hidden="true">↗</span></a></nav></div></header>'
def footer(current):
    idx=next((i for i,p in enumerate(pages) if p[0]==current),0);prev=pages[(idx-1)%len(pages)];nxt=pages[(idx+1)%len(pages)]
    map_link='<a href="site-map.html">Site map</a>' if args.batch>1 else ''
    return f'''<div class="wrap"><nav class="page-turn" aria-label="Previous and next pages"><a href="{prev[0]}.html"><small>← Previous page</small><strong>{esc(prev[1])}</strong></a><a href="{nxt[0]}.html"><small>Next page →</small><strong>{esc(nxt[1])}</strong></a></nav></div><footer class="site-footer"><div class="wrap"><div class="footer-grid"><div><a class="brand" href="index.html"><img src="assets/images/logo.png" width="43" height="43" alt="">C-Hour</a><p>Joyful Responsible Abundance begins with people. A community invitation from Minjerribah to Australia and Oceania.</p></div><div class="footer-links"><a href="index.html#explore">Explore the idea</a><a href="references.html">Reference library</a><a href="references/originals/C-Hour-Joyful-Responsible-Abundance-Plan.docx">Download the full plan</a>{map_link}</div><div class="footer-links"><a href="https://github.com/auraofintelligence/C-Hour-introduction">Project on GitHub ↗</a><a href="https://auraofintelligence.github.io/strange-but-true/contact.html">Talk with Luke ↗</a><a href="licence.html">Strange But True licence</a></div></div><div class="footer-bottom"><span>© 2026 Luke Nathan Hayes / Aura of Intelligence</span><span>GenAI concept artwork. A proposed future, shaped together.</span></div></div></footer><a class="to-top" href="#top" aria-label="Back to top">↑</a>'''
def hero(title,description,art='home',home=False,context=''):
    return f'<section class="hero {"" if home else "chapter-hero"}">{image(art,"Imagined community future: "+re.sub("<[^>]+>","",title),"hero-image",False)}<div class="wrap hero-content">'+(f'<div class="hero-context">{esc(context)}</div>' if context else '')+f'<h1>{title}</h1><p>{rich(description)}</p>'+((button('Choose your adventure','#explore')+button('Meet the C-hour','#the-idea',True)).join(['<div class="buttons">','</div>']) if home else '')+'</div><div class="hero-caption">GenAI concept artwork · An imagined future</div></section>'
def page(name,title,description,content):
    out=f'''<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#071e24"><title>{esc(title)} | C-Hour</title><meta name="description" content="{esc(description)}"><link rel="canonical" href="{BASE}{'' if name=='index' else name+'.html'}"><meta property="og:title" content="{esc(title)} | C-Hour"><meta property="og:description" content="{esc(description)}"><meta property="og:type" content="website"><meta property="og:url" content="{BASE}{'' if name=='index' else name+'.html'}"><link rel="icon" type="image/png" href="favicon.png"><link rel="apple-touch-icon" href="apple-touch-icon.png"><link rel="stylesheet" href="assets/site.css"><script src="assets/site.js" defer></script></head><body id="top"><a class="skip" href="#main">Skip to content</a>{nav(name)}<main id="main">{content}</main>{footer(name)}</body></html>'''
    (ROOT/(name+'.html')).write_text(out,encoding='utf-8')
def card(title,text,art,url):
    return f'<a class="glow-card image-card" href="{url}">{image(art,title)}<div class="card-body"><h3>{esc(title)}<span class="card-arrow" aria-hidden="true">↗</span></h3><p>{esc(text)}</p></div></a>'
def chapter_url(name):return name+'.html' if chapters else 'references.html#plan'

home=hero('A little of your time.<br><em>A world of possibility.</em>','Explore a future where everyday care, curiosity and community contribution help more people live well. Beginning on Minjerribah, with an invitation to Australia and Oceania.','home',True)
home+='''<div class="wrap welcome-strip"><div><strong>One hour. A human contribution.</strong><p>A C-hour recognises one verified hour of time freely given.</p></div><div><strong>Thanks shaped together.</strong><p>Communities choose their own recognition, rewards and reciprocity.</p></div><div><strong>More life to enjoy.</strong><p>Care, learning, creativity and shared capability. The hour has no monetary equivalent.</p></div></div>'''
home+='<section class="section" id="explore"><div class="wrap"><div class="section-heading"><h2>What would you<br>love to be part of?</h2><p>Start with an interest, something you already contribute, or a little help that would make your day easier.</p></div><div class="card-grid">'
for title,text,art,dest in [('Food, gardens and good company','Grow something. Share a meal. Pass on a skill. Explore how a simple gathering can grow into shared capability.','food-and-wellbeing','food-and-wellbeing'),('Making, learning and discovery','Try a new craft, fix something useful or explore AI with a friendly guide. Your next adventure can begin with curiosity.','choose-an-adventure','choose-an-adventure'),('Care, connection and everyday life','The support we give family, friends and neighbours already matters. Discover recognition that fits around real life.','community-hours','community-hours')]:home+=card(title,text,art,chapter_url(dest))
home+='</div></div></section>'
home+='<section class="section" id="the-idea"><div class="wrap story-split"><div><h2>The things that<br>make a community.</h2><p>Looking after someone. Teaching a skill. Bringing people together. Much of what makes life work never appears in a financial account.</p><p>The Community-Hour makes voluntary human contribution visible. One verified hour is one C-hour, with the story of what happened alongside it.</p><p>Money, human contribution and real outcomes each have their own records. This helps people appreciate the work and understand what it made possible.</p>'+button('How Community Hours work',chapter_url('community-hours'))+'</div><figure>'+image('community-hours','Concept illustration of care, learning and shared human contribution')+'<figcaption class="figure-note">Human time, care and judgement remain at the centre.</figcaption></figure></div></section>'
home+='''<section class="section mint-panel"><div class="wrap"><div class="section-heading"><h2>Joyful. Responsible.<br>Abundance.</h2><p>A life worth enjoying, care for our effects on others, and useful capacity that more people can share.</p></div><div class="mini-grid"><article><div class="number">01 / Follow your curiosity</div><h3>More possible lives</h3><p>Try different work, learn when you need to, and make room for care, rest, travel and new chapters.</p></article><article><div class="number">02 / Build useful capability</div><h3>Grow it together</h3><p>Connect practical projects, shared knowledge and tools that people can understand, shape and maintain.</p></article><article><div class="number">03 / Keep the person first</div><h3>Your life, your choices</h3><p>Explore personal agents that help with everyday life while leaving you in charge of observation, memory and sharing.</p></article></div></div></section>'''
home+='<section class="section"><div class="wrap story-split"><figure>'+image('sensorium','Imagined personal agent and community intelligence connections')+'<figcaption class="figure-note">Personal intelligence and shared learning, imagined together.</figcaption></figure><div><h2>A conversation.<br>Then a possibility.</h2><p>Imagine asking a personal agent about something you would enjoy, a contribution you already make, or a skill you want to try.</p><p>The proposed Sensorium connects these conversations with phones, optional wearables, local computing and living models of places. You choose what stays private and what you share.</p>'+button('Explore the Sensorium',chapter_url('sensorium'))+'<div class="concept-note">This is a thought experiment growing towards practical pilots. People who try it can challenge the idea and change its direction. Trust has to grow through useful experiences.</div></div></div></section>'
home+='<section class="section" id="connections"><div class="wrap"><div class="section-heading"><h2>A small island.<br>A very open horizon.</h2><p>Beginning with relationships on Minjerribah, the proposal connects food, stories, personal intelligence and shared enterprise across Australia and Oceania.</p></div><div class="card-grid">'
for title,text,art,dest in [('Mutual Futures','Explore shared ownership, Universal Intelligence and more room for learning, care and rest.','mutual-futures','mutual-futures'),('The first connected pilot','A flexible starting sketch for hosts, households, visitors and builders to shape together.','pilot','pilot'),('The projects around it','Follow purposeful connections into Straddie food, media, learning, twins and community tools.','projects','projects')]:home+=card(title,text,art,chapter_url(dest))
home+='</div></div></section>'
if chapters:
    home+='<section class="section"><div class="wrap"><div class="section-heading"><h2>Take the longer journey.</h2><p>Thirteen chapters connect the everyday idea with the people, software and resources that could bring it to life.</p></div><div class="chapter-list">'+''.join(f'<a class="chapter-item" href="{p["slug"]}.html"><span>{i+1:02}</span><span>{esc(p["shortTitle"])}</span><span>↗</span></a>' for i,p in enumerate(chapters))+'</div></div></section>'
home+='<section class="section mint-panel"><div class="wrap story-split"><div><h2>Bring an interest.<br>Bring a better idea.</h2><p>This invitation begins with Luke Nathan Hayes, Aura of Intelligence and the GAJRA Earth concept. It has room to change through the people who join the conversation.</p></div><div>'+button('Read the plan and references','references.html')+'<p style="margin-top:24px">The plan, source archive and related public projects are here to explore at your own pace.</p></div></div></section>'
page('index','Joyful Responsible Abundance','Explore Community Hours and a joyful, responsible future shaped by people, beginning on Minjerribah.',home)

for p in chapters:
    body=hero(esc(p['title']),p['description'],p['hero'])
    sections=p['sections'];toc=''.join(f'<a href="#{slug(s["title"])}">{esc(s["title"])}</a>' for s in sections)
    body+='<section class="section"><div class="wrap reading-layout"><aside class="contents"><details open><summary>In this chapter</summary>'+toc+'</details><a href="index.html#explore">← Explore C-Hour</a></aside><article class="article-body"><p class="reading-note">Adapted from the 23 September 2026 plan. The proposed system is open to development with participants.</p>'
    for i,s in enumerate(sections):
        body+=f'<section id="{slug(s["title"])}"><h2>{esc(s["title"])}</h2>'+''.join(para(t) for t in s.get('paragraphs',[]))
        if s.get('cards'):body+='<div class="section-cards">'+''.join(f'<article class="glow-card text-card"><h3>{esc(c["title"])}</h3>{para(c["text"])}</article>' for c in s['cards'])+'</div>'
        for step in s.get('steps',[]):body+=f'<div class="step"><h3>{esc(step["title"])}</h3>{para(step["text"])}</div>'
        if s.get('links'):body+='<div class="link-list">'+''.join(f'<a href="{esc(link["url"])}">{esc(link["label"])} ↗</a>' for link in s['links'])+'</div>'
        if i==0 and p['slug']=='people-and-purpose':
            body+='<div class="luke-portraits"><figure><img src="assets/images/luke-formal.jpeg" alt="Luke Nathan Hayes wearing glasses and a blue collared shirt" width="1080" height="1350" loading="lazy" decoding="async"><figcaption>Luke Nathan Hayes</figcaption></figure><figure><img src="assets/images/luke-in-office.jpeg" alt="Luke with long hair at his desk in his office" width="1152" height="2048" loading="lazy" decoding="async"><figcaption>Luke in his office</figcaption></figure></div><p class="portrait-credit">Photographs supplied by Luke.</p>'
        elif i==0 and len(sections)>1:
            art={'sensorium':'software','community-hours':'reciprocity','food-and-wellbeing':'choose-an-adventure','mutual-futures':'growing-together','software':'sensorium','pilot':'people-and-purpose'}.get(p['slug'],'home')
            body+='<figure class="wide-figure">'+image(art,'GenAI concept illustration of the connections explored in this chapter')+'<figcaption class="figure-note">GenAI concept illustration. The arrangements shown are imagined possibilities.</figcaption></figure>'
        body+='</section>'
    body+='</article></div></section>'
    page(p['slug'],p['title'],p['description'],body)

library=hero('Follow the ideas.<br>Find the sources.','The current plan, original documents and public references behind C-Hour. Explore the evidence, the proposals and the changes in thinking.','references')
library+='<section class="section"><div class="wrap"><div class="story-split"><div><h2>Begin with the current plan.</h2><p>Planning edition 5, dated 23 September 2026, brings the idea together. The original Word document is preserved unchanged.</p>'+button('Download the full plan','references/originals/C-Hour-Joyful-Responsible-Abundance-Plan.docx')+'</div><div class="concept-note"><p>Older sources contain superseded financial assumptions. The current plan defines C-hours as non-monetary recognition of voluntary human time, with community-chosen reciprocity.</p><p>'+('<a href="corrections.html">Read the archive correction guide →</a>' if args.batch>1 else 'Appendix B in the plan explains the corrections and exact editions involved.')+'</p></div></div></div></section>'
library+='<section class="section"><div class="wrap"><h2>Explore the reference library.</h2><label for="reference-search">Search by title, topic or source</label><input class="search-box" id="reference-search" data-search type="search" placeholder="Try food, Sensorium, care or AI"><div class="filter-row">'+''.join(f'<button class="filter-button" data-filter="{x}" aria-pressed="{str(i==0).lower()}">{x}</button>' for i,x in enumerate(['All','Current plan','Historical source','Context','Web reference']))+'</div><p class="results-count" aria-live="polite">'+str(len(refs['documents'])+len(refs['links']))+' references shown</p><div class="reference-list">'
for d in refs['documents']:
    anchors=''.join(f'<span id="{esc(a)}"></span>' for a in d.get('anchors',[]))
    library+=f'<article id="{esc(d["id"])}" class="reference" data-entry data-theme="{esc(d["sourceStatus"].capitalize())}">{anchors}<p class="file-meta">{esc(d["sourceStatus"].capitalize())} · {esc(d["format"])} · {d["size"]/1024:.0f} KB</p><h3>{esc(d["title"])}</h3><p>{esc(d["note"])}</p><a href="{quote(d["file"],safe="/")}">Open original document ↗</a></article>'
for d in refs['links']:
    library+=f'<article id="{esc(d["id"])}" class="reference" data-entry data-theme="Web reference"><p class="file-meta">Web reference · {esc(d["id"])}</p><h3>{esc(d["title"])}</h3><p>{esc(d.get("context",d.get("note","Referenced in the current plan.")))}</p><a href="{esc(d["url"])}">Visit source ↗</a></article>'
library+='</div><p class="empty-message" hidden>No matching references. Try a broader word or choose All.</p></div></section>'
if refs.get('missing'):
    library+='<section class="section"><div class="wrap"><h2>References still to locate.</h2><p>These works are cited in the plan but their files have not been located. Related documents are identified separately so the archive does not imply an exact match.</p>'+''.join(f'<div class="reference"><h3>{esc(m["title"])}</h3><p>{esc(m.get("note","Original file not located."))}</p></div>' for m in refs['missing'])+'</div></section>'
page('references','Reference library','Read the current C-Hour plan, download original references and follow verified public context sources.',library)

if args.batch>1:
    body=hero('Good ideas<br>grow connections.','Explore the public projects surrounding C-Hour. Each has its own purpose, stage of development and invitation.','projects')
    body+='<section class="section"><div class="wrap"><div class="section-heading"><h2>Find a useful next connection.</h2><p>These are related public workbenches, prototypes and proposals. A published project page does not mean a local service or partnership is operating.</p></div><div class="card-grid">'
    for p in projects:
        topic=(p.get('theme','')+' '+p['title']).lower()
        art=next((v for k,v in [('food','food-and-wellbeing'),('care','community-hours'),('health','food-and-wellbeing'),('media','stories'),('film','stories'),('story','stories'),('mutual','mutual-futures'),('enterprise','mutual-futures'),('twin','sensorium'),('aura','sensorium'),('civic','civic-ai'),('ai','software'),('learn','why-now'),('fund','growing-together')] if k in topic),'projects')
        body+=f'<article class="glow-card project-card">{image(art,"Concept artwork for "+p["title"])}<div class="project-copy"><p class="status">{esc(p.get("theme","Connected project"))} · {esc(p.get("status","Proposal"))}</p><h3>{esc(p["title"])}</h3><p>{esc(p["description"])}</p><a href="{esc(p["url"])}">Explore project ↗</a></div></article>'
    body+='</div></div></section>';page('projects','Connected projects','Explore the food, care, creative, AI and shared-enterprise projects connected with C-Hour.',body)
    # Preserve the full correction appendix as an archive reading aid.
    source=load('plan-source.json',{})
    corrections=source.get('corrections',{}).get('blocks',[]) if isinstance(source,dict) else []
    body=hero('Read the archive.<br>Keep the meaning clear.','Earlier documents trace the development of the idea. This guide preserves the current plan’s corrections so older assumptions do not become new promises.','corrections')
    body+='<section class="section"><div class="wrap reading-layout"><aside class="contents"><a href="references.html">← Reference library</a><a href="references.html#plan">Current planning edition</a></aside><article class="article-body"><section><h2>The current interpretation</h2><p>A C-hour recognises verified voluntary human time and has no monetary equivalent. Communities choose their own thanks and reciprocity. Money, contribution and outcomes remain separately recorded.</p><p>Proposed pilot arrangements, facilities, partnerships and intelligent agent capabilities are ideas to develop with people. The source archive does not establish that they are already operating.</p></section>'
    if corrections:
        for block in corrections:
            text=block.get('text','') if isinstance(block,dict) else str(block)
            kind=block.get('type','paragraph') if isinstance(block,dict) else 'paragraph'
            if not text:continue
            body+=f'<h2>{esc(text)}</h2>' if kind=='heading' else para(text)
    else:
        body+='<section><h2>Use Appendix B alongside earlier sources</h2><p>The original plan includes a detailed correction register by filename, page and section. It covers financial substitution, reciprocity, unpaid work, the Sensorium, personal sovereignty and the status of wider ambitions.</p>'+button('Open the complete correction register','references/originals/C-Hour-Joyful-Responsible-Abundance-Plan.docx')+'</section>'
    body+='<section><h2>How this website is licensed</h2><p>The source plan proposes future open-source development. This introduction website uses Luke’s requested Strange But True Public Source Licence, which reserves commercial rights. A separate future software release would need an explicit licence of its own.</p></section></article></div></section>'
    page('corrections','Reading the archive','Understand the current C-Hour definition and the corrections applying to earlier planning documents.',body)

body=hero('Share the ideas.<br>Credit their source.','The Strange But True Public Source Licence applies to original work in this website. Third-party material retains its own rights.','licence')
body+='<section class="section"><div class="wrap reading-layout"><aside class="contents"><a href="LICENSE.md">Download the licence</a><a href="https://github.com/auraofintelligence/C-Hour-introduction">View the repository ↗</a></aside><article class="article-body">'
for line in (ROOT/'LICENSE.md').read_text(encoding='utf-8-sig').splitlines():
    if line.startswith('# '):body+=f'<h2>{esc(line[2:])}</h2>'
    elif line.startswith('## '):body+=f'<h3>{esc(line[3:])}</h3>'
    elif line.strip():body+=para(line.removeprefix('- '))
body+='</article></div></section>';page('licence','Strange But True licence','Read the Strange But True Public Source Licence for C-Hour Introduction.',body)
page('404','Find your way back','Return to the C-Hour introduction.',hero('A different path<br>starts here.','That page could not be found. Explore the introduction or browse the reference library.','home')+'<div class="wrap section">'+button('Return to C-Hour','index.html')+'</div>')
if args.batch>1:
    body=hero('Every path<br>in one place.','Start with everyday contribution, follow the wider system or go straight to the source. This is your map of C-Hour.','sitemap')
    body+='<section class="section"><div class="wrap"><div class="map-root"><a class="button" href="index.html">C-Hour introduction</a></div><div class="map-grid">'
    groups=[('Begin with people',chapters[:5]),('Connect the possibilities',chapters[5:10]),('Build and grow',chapters[10:])]
    for title,items in groups:
        body+='<section class="map-branch"><h2>'+esc(title)+'</h2>'
        for p in items:body+=f'<a class="glow-card map-node" href="{p["slug"]}.html"><h3>{esc(p["shortTitle"])}</h3><p>{esc(p["description"])}</p><span aria-hidden="true">↗</span></a>'
        body+='</section>'
    body+='</div><section class="section"><h2>Sources and connections</h2><div class="chapter-list">'+''.join(f'<a class="chapter-item" href="{n}.html"><span>↗</span><span>{t}</span></a>' for n,t in [('projects','Connected projects'),('references','Reference library'),('corrections','Reading the archive'),('licence','Strange But True licence')])+'</div></section></div></section>'
    page('site-map','Site map','A visual map linking every chapter, related project collection and reference page in C-Hour.',body)
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{BASE}{"" if n=="index" else n+".html"}</loc></url>' for n,t in pages)+'</urlset>',encoding='utf-8')
(ROOT/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n',encoding='utf-8')
print(f'Built {len(pages)} public pages plus 404 for batch {args.batch}.')
