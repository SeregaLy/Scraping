# Веб-скрейпинг для создания набора данных с использованием Python
# можем использовать библиотеку BeautifulSoup в Python для задачи очистки
# веб-страниц для создания набора данных:

import csv  # импортируем библиотеку для работы с csv
from urllib.request import urlopen  # импортируем библиотеку для скачивания страницы
from bs4 import BeautifulSoup   # импортируем библиотеку для работы с веб-страницами

html = urlopen(
    "https://en.wikipedia.org/wiki/Comparison_of_programming_languages") # Ссылка на веб-страницу
soup = BeautifulSoup(html, "html.parser")   # Создаем объект для работы с веб-страницей
table = soup.findAll("table", {"class": "wikitable"})[0]    # Получаем объект для работы с веб-страницей
rows = table.findAll("tr")    # Получаем объект для работы с веб-страницей

with open("language.csv", "wt+", newline="") as f:    # Открываем файл для записи данных
    writer = csv.writer(f)    # Создаем объект для работы с csv
    for i in rows:    # Проходимся по объекту для работы с веб-страницей
        row = []    # Создаем объект для работы с csv
        for cell in i.findAll(["td", "th"]):    # Получаем объект для работы с веб-страницей
            row.append(cell.get_text()) # Добавляем в объект для работы с csv данные
        writer.writerow(row)    # Работаем с объектом для работы с csv

import pandas as pd # Импортируем библиотеку для работы с данными

a = pd.read_csv("language.csv") # Считываем данные из файла
a.head()    # Показываем первые 5 значений
