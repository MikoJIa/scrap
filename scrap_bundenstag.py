import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}


# person_url_list = []
# for i in range(0, 720, 12):
#     url = f'https://www.bundestag.de/ajax/filterlist/de/abgeordnete/biografien/862712-862712?limit=12&noFilterSet=true&offset={i}'
#     # print(url)
#     # теперь сгенерируем get() - запрос на нужной страничке и собрать все ссылки
#     response = requests.get(url, headers=headers)
#     # забираем контент
#     result = response.content
#     # создаём объект BeautifulSoup в который в качестве параметров передаём результат и тип
#     # парсера lxml
#     soup = BeautifulSoup(result, 'lxml')
#     # Теперь мы можем извлекать данные из получаемых страниц
#     persons = soup.find_all(class_='bt-slide-content')
#
#     for item in persons:
#         persons_href = 'https://www.bundestag.de' + item.find('a').get('href')
#         person_url_list.append(persons_href)
#
# with open('person_url_file.txt', 'a', encoding='utf-8') as file:
#     for line in person_url_list:
#         file.write(f'{line}\n')

# брать ссылки мы теперь можем из нашего сохранённого файла

with open('person_url_file.txt', 'r', encoding='utf-8') as file:
    # сохраним наш новый список на всякий случай срезав ненужные пробулы через strip()
    # с помощбю list comprehension
    lines = [line.strip() for line in file.readline()]
    # И создаём новый цикл for на итерации которого мы будем пробегатся по списку ссылок
    # и извлекать по одной
    for line in lines:
        #  отправляем запрос по ссылке с помощью библиотеки requests
        g = requests.get(line)
        # сохраняем контент
        result = g.content
        # помещаем его в пораметры объекта BeautifulSoup
        soup = BeautifulSoup(result, 'lxml')
        person = soup.find(class_='bt-biografie-name').find('h3').text
        person_name_company = person.strip().split(',')
        person_name = person_name_company[0]
        person_company = person_name_company[1]


