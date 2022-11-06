import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 '
                  'YaBrowser/22.1.3.942 Yowser/2.5 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9 '
}

df={}
tables = pd.read_html('https://priroda.permkrai.ru/deyatelnost/okhrana-okruzhayushchey-sredy/okhrana-okruzhayushchey-sredy/okhrana-okruzhayushchey-sredy')
lentables = len(tables)


def get_pd_table():
    for i in range(0, lentables):
        url = f'https://priroda.permkrai.ru/deyatelnost/okhrana-okruzhayushchey-sredy/okhrana-okruzhayushchey-sredy/okhrana-okruzhayushchey-sredy'
        req = requests.get(url=url,headers=headers)
        soup = BeautifulSoup(req.text, 'lxml')
        titlenames = soup.findAll('p', align="right")
        title_table = titlenames[i].text.strip()
        print(f'Получаю данные из таблицы: "{title_table}"...')
        tables = pd.read_html(url, index_col=0, header=0, thousands=" ")
        pd.set_option('display.max_colwidth',1000)
        df[title_table] = tables[i]

def pd_save():
    writer = pd.ExcelWriter('./res.xlsx', engine='xlsxwriter')
    
    for df_name in df.keys():
        print(f'Записываем данные в лист: {df_name}')
        df[df_name].to_excel(writer, sheet_name=df_name)
    writer.save()


def main():
    get_pd_table()
    print(' ')
    pd_save()
    print('\n[+] Данные записаны!')


if __name__ == '__main__':
    main()