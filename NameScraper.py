import lxml.html 
import requests
import html

from bs4 import BeautifulSoup 

mylist = []

with open("fishingderbydrawcontest.html", "r", encoding='utf8') as f:
    content = f.read()

    soup = BeautifulSoup(content, 'lxml')
    
    names = soup.find_all(class_='_6qw4')
    
    for name in names:
        mylist.append(name.text)
    #    print(" ".join(name.text.split()))

    #print("\n\nWithout Duplicates: \n")
    #for elem in mylist:
    #    print(elem)

    orderedlist = list(set(mylist))

    for elem in orderedlist:
        print(elem)