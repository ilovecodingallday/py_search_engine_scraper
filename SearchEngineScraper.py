import requests, lxml
from bs4 import BeautifulSoup
import re


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0",
}






while (True):
    def googleSearch():
        query = input('Search : ')
        search = query.replace(' ', '+')
        results = 11
        url = (f"https://www.google.com/search?q={search}&num={results}")

        requests_results = requests.get(url)
        soup_link = BeautifulSoup(requests_results.content, "html.parser")
        links = soup_link.find_all("a")

        for link in links:
            link_href = link.get('href')
            if "url?q=" in link_href and not "webcache" in link_href:
              title = link.find_all('h3')
              if len(title) > 0:
                  print(link.get('href').split("?q=")[1].split("&sa=U")[0])
                  print(title[0].getText())
                  print("--------------------------------------------------------------------------------------------")
                  print("")

    def bingSearch():
        query = input('Search : ')
        search = query.replace(' ', '+')
        results = 11

        html = requests.get(f'https://www.bing.com/news/search?q={search}&num={results}', headers=headers)
        soup = BeautifulSoup(html.text, 'lxml')

        for result in soup.select('.card-with-cluster'):
            title = result.select_one('.title').text
            link = result.select_one('.title')['href']

            print(f'{title}\n{link}')
            print("--------------------------------------------------------------------------------------------")
            print("")

    def duckSearch():
        query = input('Search : ')
        search = query.replace(' ', '+')
        results = 11

        page = requests.get(f'https://duckduckgo.com/html/?q={search}&num={results}', headers=headers).text
        soup = BeautifulSoup(page, 'html.parser')
        links = soup.find_all("a", class_="result__url", href=True)

        for link in links:
            print(link['href'])
            print("--------------------------------------------------------------------------------------------")
            print("")

    def quitProgram():
        print("THANK YOU FOR SEARCHING!")
        quit()


    def default():

        print("Hello")

    switcher = {
        1: googleSearch,
        2: bingSearch,
        3: duckSearch,
        4: quitProgram,
        5: default
    }
    def switch(operation):
      return switcher.get(operation, default)()
      
    print('''SELECT A SEARCH ENGINE
    1. Google 
    2. Bing
    3. DuckDuck Go
    4. QUIT
    ''')
    # Take input from user
    choice = int(input("Select operation from 1,2,3,4 : "))

    switch(choice)



