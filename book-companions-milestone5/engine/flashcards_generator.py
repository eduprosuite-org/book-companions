from pathlib import Path
Path('books/sample-book/flashcards/generated.csv').write_text('question,answer\nExample,Answer',encoding='utf-8')
