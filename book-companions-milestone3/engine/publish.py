from pathlib import Path
import csv

books=list(csv.DictReader(open('knowledge_graph/Books.csv',encoding='utf-8')))
index=['<h1>Books</h1><ul>']
for b in books:
    slug=b['slug']
    title=b['title']
    page=Path('books')/slug/'website'/'index.html'
    page.parent.mkdir(parents=True,exist_ok=True)
    page.write_text(f'<h1>{title}</h1><p>Generated page.</p>',encoding='utf-8')
    index.append(f'<li><a href="../books/{slug}/website/index.html">{title}</a></li>')
index.append('</ul>')
Path('website/index.html').parent.mkdir(parents=True,exist_ok=True)
Path('website/index.html').write_text(''.join(index),encoding='utf-8')
print('Generated',len(books),'book pages')
