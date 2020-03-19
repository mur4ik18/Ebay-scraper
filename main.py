import requests
from bs4 import BeautifulSoup
class SearchEngine():
    def __init__(self):
        # shell
        try:
            self.shell = ".s-item"
        except:
            print("")
        # title
        try:
            self.title = ".s-item__title"
        except:
            print('')    
        # price value
        try:    
            self.price = ".s-item__price"
        except:
            print('')
        # sold rate
        try:     
            self.solds = ".s-item__hotness.s-item__itemHotness > .NEGATIVE"
        except:
            print("")
        # rate
        try:     
            self.stars = ".b-starrating__star > .clipped"
        except:
            print('') 
        




    def searchInput(self):
        inputSearch = str(input('What you want find? '))
        inputValue = '+'.join(inputSearch.split())
        pagesNumValue = int(input("How much pages you need?"))
        yield self.URLopener(inputValue,pagesNumValue)
'''
    def URLopener(self, a,b):
        URL = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + str(a) + "&_pgn="
        r = requests.get(URL+str(i))
        html = BeautifulSoup(r.content, 'html.parser')  
'''    