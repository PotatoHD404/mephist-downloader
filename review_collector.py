import json
import requests
import lxml.html
from collector import BASE_PATH, fetch, write_file


# noinspection PyDictCreation
def main():
    # for i, link in enumerate(prepod_links):
    for prepod in range(1100):
        with open(BASE_PATH + f'/{prepod}.json') as o:
            # link = 'http://www.mephist.ru/prepod/resp/3E5C58416DA5F05FC325701E007A8052'
            prepod_info = json.load(o)
        for i, link in enumerate(prepod_info['Отзывы']):
            review_page = fetch(link)
            review_info = {}
            review_info["Название"] = review_page.xpath("/html/body/table[3]/tr[1]/td[3]/p/u")[0].text
            review_info["Текст"] = ''.join(review_page.xpath("/html/body/table[3]/tr[1]/td[3]/p/text()"))
            review_info["Оценка"] = review_page.xpath('//*[@id="rez"]')[0].text_content()
            review_info["Ник"] = review_page.xpath("/html/body/table[3]/tr[1]/td[3]/div/font[1]")[0].text
            review_info["Дата"] = review_page.xpath("/html/body/table[3]/tr[1]/td[3]/div/font[3]")[0].text
            write_file(prepod_info, BASE_PATH + f'/{prepod}/{i}.json')
            print(review_info)


if __name__ == "__main__":
    main()
