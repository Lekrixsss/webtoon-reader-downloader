import requests
from bs4 import BeautifulSoup

def test():
    print("webtoondl loaded correctly!")

def webtoonDL():
    pageId = 1
    epLinks = []
    epLinks_list = ["1"]
    while not(epLinks == epLinks_list):
        urlpage = url + "&page=" + str(pageId)
        print(pageId)
        page = requests.get(urlpage)
        soup = BeautifulSoup(page.content, "html.parser")
        epid = soup.find(id="_listUl")

        epLinks_list = epLinks #Записує epLinks в epLinks_list
        epLinks_list = [epLinks.strip() for epLinks in epLinks_list]
        for link in epid.find_all('a'):
            if link.get("href") in epLinks:
                break
            else:
                epLinks.append(link.get("href"))  # Якщо цього посилання ще не було воно записується в список

        print(epLinks)
        print(epLinks_list)
        pageId = pageId + 1
    return epLinks