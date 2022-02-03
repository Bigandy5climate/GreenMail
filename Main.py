import mailparser

mail = mailparser.parse_from_file('f copy.eml')
body = mail.body
bodyEnd = body.find('</html>=')+7
cleanBody = body[:bodyEnd]
print(bodyEnd)
