from urllib.request import *
a="http://"+input()
b=urlopen(a)
from bs4 import *
b=BeautifulSoup(b,"html.parser")
for c in b(["script","style"]):
    c.extract()
c=b.get_text()
d=b.title()
#b.description()
d=c.split("\n")
b=' '.join(d)
dic={}
f=open("word.txt","r").read().split(" ")
b=b.split(" ")
for z in b:
    if z not in f:
        c=b.count(z)
        dic[z]=c
sort=sorted(dic.items(),key=lambda t:t[1],reverse=True)
print(sort[0:5])
wor=[]
cou=[]
for b in range(5):
    wor.append(sort[b][0])
    cou.append(sort[b][1])
print(wor,cou)
from xlsxwriter import *
a=Workbook("data.xlsx")
b=a.add_worksheet("KARTHIK")
b.write(0,0,"word")
b.write(0,1,"count")
row=1
col=0
for z in range(5):
    b.write(row,col,wor[z])
    b.write(row,col+1,cou[z])
    row+=1
chart=a.add_chart({"type":"pie"})
chart.add_series({"categories":"=KARTHIK!A2:A6","values":"=KARTHIK!B2:B6"})
b.insert_chart("C7",chart)
a.close()
from os import *
system("start data.xlsx")
