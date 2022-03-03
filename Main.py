from distutils.file_util import write_file
import encodings
import mailparser
from bs4 import BeautifulSoup

mail = mailparser.parse_from_file('f copy.eml')
body = mail.body
body = body.split('</html>')[0]+'</html>'
with open('body.html', 'r+', encoding='utf-8') as f:
    f.write('<!DOCTYPE html>\n')
    f.write(body)
    soup = BeautifulSoup(f,features='html.parser')
    # print(soup)
    # # kill all script and style elements
    # for script in soup(["script", "style"]):
    #     print(script)
    #     script.extract()    # rip it out
    # #  get text
    text = soup.get_text()
    print(text)
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    print(text)

