import requests             #импортируем библиотеку реквест

from bs4 import BeautifulSoup           #импортируем библотеку beautifulsoup(для извлечения данных из html)     


def get_html(url):                        #ф-я принимает url
    try:                                    
        result = requests.get(url)          #с помощью request берем данные с этого url
        result.raise_for_status()           #если проблема, мы обработаем исключение
        return result.text                  #ессли все ок возвращаем текст
    except(requests.RequestException, ValueError):          #исключения, проблемы с сервером
        return False



'''
 id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    sport = db.Column(db.String, nullable=False)
    time = db.Column(db.DateTime, nullable=True, default=datetime.now())
    result = db.Column(db.String, nullable=False)
    coefficient 
'''



def id(html):
    soup = BeautifulSoup(html, 'html.parser')
    raw_data = soup.find('div', id = 'games_content').find_all('c-events__item_game')
    print(raw_data)





#def resultW1(html):
#    soup = BeautifulSoup(html, 'html.parser')
#   resultW1 = soup.find('div', class_ = "c-bets").findAll('span')
#    print (resultW1)

if __name__ == "__main__":                              #
    html = get_html("https://1xstavka.ru/live")          
    if html:
        id(html)
    
#if __name__ == "__main__":
 #   html = get_html('https://www.olimp.bet/')
  #  if html:
   #     get_first_result(html)
        #with open('olimp.ru.html', "w", encoding="utf8") as f:
        #   f.write(html)


       # with open('1xstavka.ru.html', "w", encoding= "utf8") as f:       #записываем результат функции в файл
        #    f.write(html)'''

#if __name__ == "__main__":
    #html = get_html('https://www.ligastavok.ru/')
    #if html:
     #    with open('ligastavok.ru.html', "w") as f:
    #        f.write(html)
 
#if __name__ == "__main__":
 #   html = get_html('https://www.pari.ru/')
  #  if html:
   #     with open('pari.ru.html', "w", encoding="utf8") as f:
    #        f.write(html)
