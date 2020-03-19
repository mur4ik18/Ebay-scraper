import requests
from bs4 import BeautifulSoup

#   https://www.ebay.com/sch/i.html?_from=R40  (&_nkw=GTX+1060 - what we find)   (&_pgn=1 - pages)

find = input("What we find? ")
findList = find.split() 
WellList = '+'.join(findList)
URL = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + str(WellList) + "&_pgn="
#URL = "https://www.ebay.com/b/Video-Game-Consoles/139971/bn_320033?rt=nc&_pgn="
pagesNum = input("How much pages you need?")

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

f = open('output.txt', 'w')

s=0
for i in range(1, int(pagesNum)):
    try:
        r = requests.get(URL+str(i))
        html = BeautifulSoup(r.content, 'html.parser') 
    except:
        print("end work")
        print(s)
        break
    for el in html.select(shell):
        # title
        try:
            t = el.select(title)
            print(t[0].text)
            f.write(t[0].text)
            f.write('\n')
        except:
            print("")
        # link
        try:
            link = el.select('.s-item__link')
            print(link[0].get('href'))
            f.write(link[0].get('href'))
            f.write('\n')
        except:
            print("")
        
        # price
        try:
            p = el.select(price)
            print(p[0].text)
            f.write(p[0].text)
            f.write('\n')
        except:
            print("")
        # sold
        try:
            sold = el.select(solds)
            print(sold[0].text)
            f.write(sold[0].text)
            f.write('\n')
        except:
            print("")       
        # rate
        try:
            star = el.secect(stars)
            print(star[0].text)
            f.write(star[0].text)
        except:
            print("")
        s+=1
        print(s)
        f.write('--------------')
        f.write('\n')
    
f.close()