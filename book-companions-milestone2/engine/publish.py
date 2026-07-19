from pathlib import Path
import yaml
cfg=yaml.safe_load(open("config/books.yaml"))
out=Path("website/books.html")
items="".join(f"<li>{b['title']}</li>" for b in cfg["books"])
out.write_text(f"<h1>Books</h1><ul>{items}</ul>",encoding="utf-8")
print("Website generated:",out)
