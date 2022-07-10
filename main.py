import requests
from  bs4 import BeautifulSoup
def get_html(url):
    headers = {'user-agent':'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    html = response.text
    return html

def get_weather_now(text):
    url = f'https://www.google.com/search?q=погода+{text.lower()}'
    html = get_html(url)
    soup = BeautifulSoup(html,'html.parser')

    try:
        #temp = soup.find('div',class_='vk_bk TylWce SGNhVe').get_text(strip=True)
        for div in soup.find_all('div', {'class': 'vk_bk TylWce SGNhVe'}):
            name = div.find('span', {'class': 'wob_t q8U8x'}).get_text(strip=True)
            print(name.text)
        #print(f'температура воздуха сейчас {temp}')
    except:
        print(f'Город" {text}" не найден. Скорее всего, вы сделали опечатку')

def continue_execution():
    print('Хотите продолжить?')
    cont = input('')
    while cont == 'да':
        text = input('Введите город, в котором хотите узнать погоду: ')
        get_weather_now(text)
        print('Хотите продолжить?')
        cont = input('')

text = input('Введите город, в котором хотите узнать погоду: ')
get_weather_now(text)
continue_execution()
