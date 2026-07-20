from pathlib import Path
import csv
from navigation import build_nav
books=list(csv.DictReader(open('knowledge_graph/Books.csv',encoding='utf-8')))
site=Path('website');site.mkdir(exist_ok=True)
links=[]
for b in books:
 slug=b['slug'];title=b['title']
 out=Path('books')/slug/'website'/'index.html'
 out.parent.mkdir(parents=True,exist_ok=True)
 nav=build_nav(title)
 out.write_text(f'<html><body>{nav}<h1>{title}</h1></body></html>',encoding='utf-8')
 links.append((title,f'books/{slug}/website/index.html'))
idx='<h1>Books</h1><ul>'+''.join(f'<li><a href="{u}">{t}</a></li>' for t,u in links)+'</ul>'
(site/'index.html').write_text(idx,encoding='utf-8')
print('Generated',len(links),'books')
