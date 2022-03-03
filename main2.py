from distutils.file_util import write_file
import encodings
import mailparser
from bs4 import BeautifulSoup 

mail = mailparser.parse_from_file('f copy.eml')
body = mail.body
with open('body.html', 'w', encoding='utf-8') as f:
    f.write('<!DOCTYPE html>\n')
    f.write(body)
with open('body.html', 'r', encoding='utf-8') as f:
    soup=BeautifulSoup(f,features='html.parser')
    text=soup.get_text(separator='\n\n')
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk + '\n' for chunk in chunks if chunk)
    print(text)
with open('text.md','w',encoding='utf-8') as t:
    t.write(text)
