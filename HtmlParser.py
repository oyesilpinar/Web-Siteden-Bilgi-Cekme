"""
1.Olarak siteye bağlan
2. olarak sitedeki fakültelerin oldugu classa gir
3. olarak clasların hrefine gir
4. olarak hreflerin içindeki bilgiyi çek
5. olarak bu bilgileri tek tek içindekileri for un indisine yaz
"""
import requests
from bs4 import BeautifulSoup
fakulteler=[]
r=requests.get('http://www.firat.edu.tr/tr')


soup= BeautifulSoup(r.content,"html.parser")

gelen_veri=soup.find_all("li",{"class":"col-sm-3"},limit=1)

fakultetablosu=(gelen_veri[0].contents)[len(gelen_veri[0].contents)-2]
for a in fakultetablosu.find_all('a', href=True):
    print("URL:",a.get('href'))
    fakulteler.append(a['href'])

fakultetablosu=fakultetablosu.find_all("li")

for i in fakultetablosu:
    icerik=i.text
    print(icerik)