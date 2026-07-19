from pathlib import Path
Path('books/sample-book/mcqs/generated.csv').write_text('question,option1,option2,answer\nQ,A,B,A',encoding='utf-8')
