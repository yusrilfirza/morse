import json
with open("plain.txt","r") as content_file:
    content = content_file.read()
with open("code.txt", "r") as content_file:
    code = content_file.read()
print(content)
plain = []
a = []
b=''
d=[]
bla ='{"di-dah": "A","dah-di-di-dit": "B","dah-di-dah-dit": "C","dah-di-dit": "D","dit": "E","di-di-dah-dit": "F","dah-dah-dit": "G","di-di-di-dit": "H","di-dit": "I","di-dah-dah-dah": "J","dah-di-dah": "K","di-dah-di-dit": "L","dah-dah": "M","dah-dit": "N","dah-dah-dah": "O","di-dah-dah-dit": "P","dah-dah-di-dah": "Q","di-dah-dit": "R","di-di-dit": "S","dah": "T","di-di-dah": "U","di-di-di-dah": "V","di-dah-dah": "W","dah-di-di-dah": "X","dah-di-dah-dah": "Y","dah-dah-di-dit": "Z","dah-dah-dah-dah-dah": "0","di-dah-dah-dah-dah": "1","di-di-dah-dah-dah": "2","di-di-di-dah-dah": "3","di-di-di-di-dah": "4","di-di-di-di-dit": "5","dah-di-di-di-dit": "6","dah-dah-di-di-dit": "7","dah-dah-dah-di-dit": "8","dah-dah-dah-dah-dit": "9"}'
code2 = json.loads(bla)
for i in range(len(content)):
    if (content[i]!=' '):
        a.append(content[i])
    elif (content[i]==' '):
        c = b.join(a)
        plain.append(c)
        a = []
        print(code2[c],end='')
print(plain)

