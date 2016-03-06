from bs4 import BeautifulSoup
import sys

html = ''
with open('D_MEGA.HTM','r') as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

#ignoring header
trs =  soup.find_all('tr')[1:]
orig_stdout = sys.stdout

#redirecting stdout
f = open("output.txt",'w')
sys.stdout = f

for tr in trs:
    tds = tr.find_all('td')
    #data cleaning
    if len(tds) >= 8:
        print (tds[0].text + "\t" +  tds[1].text + "\t" + tds[2].text + "\t" + tds[3].text + "\t" + tds[4].text + "\t" + tds[5].text + "\t" + tds[6].text + "\t" + tds[7].text)

sys.stdout = orig_stdout
f.close()
        
        
