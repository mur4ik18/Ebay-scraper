import requests
from bs4 import BeautifulSoup

URL = "https://www.ebay.com/b/Video-Game-Consoles/139971/bn_320033"

r = requests.get(URL)
html = BeautifulSoup(r.content, 'html.parser') 

try:
    shell = ".s-item"
except:
    print("")
try:
    title = ".s-item__title"
except:
    print('')    
try:    
    price = ".s-item__price"
except:
    print('')
try:     
    solds = ".s-item__hotness.s-item__itemHotness > .NEGATIVE"
except:
    print("")
try:     
    stars = ".b-starrating__star > .clipped"
except:
    print('')

s=0
for el in html.select(shell):
    try:
        t = el.select(title)
        print(t[0].text)
    except:
        print("")
    try:
        p = el.select(price)
        print(p[0].text)
    except:
        print("")
    try:
        sold = el.select(solds)
        print(sold[0].text)
    except:
        print("")       
    try:
        star = el.secect(stars)
        print(star[0].text)
    except:
        print("")
        
        
        
    
    s+=1
    print(s)