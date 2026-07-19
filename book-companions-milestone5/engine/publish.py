from pathlib import Path
import markdown
src=Path('books/sample-book/content/index.md')
html=markdown.markdown(src.read_text(encoding='utf-8'))
out=Path('books/sample-book/website/index.html')
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(f'<html><body>{html}</body></html>',encoding='utf-8')
print('Generated',out)
