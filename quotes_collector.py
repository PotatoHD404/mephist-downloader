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
        quote_link = prepod_info['Перлы']
        if 'form_fraza' not in quote_link:
            count = len(fetch(quote_link).xpath('/html/body/table[3]/tr[1]/td[3]/table/tr/td/div[2]/div/a'))
            count = 1 if count == 0 else count
            # [el.text for el in ]
            k = 0
            for i in range(1, count + 1):
                review_page = fetch(quote_link + f'&stc={i}')
                quote_infos = {}
                quote_infos["Оценка"] = [el.text for el in review_page.xpath(
                    "/html/body/table[3]/tr[1]/td[3]/table/tr/td/div/table/tr/td[2]/table/tr/td[2]/div[1]/ul/li[1]")]
                quote_infos["Текст"] = [el.text_content() for el in
                                        review_page.xpath("/html/body/table[3]/tr[1]/td[3]/table/tr/td/div/a")]
                quote_infos["Ник и дата"] = [el.text_content() for el in review_page.xpath(
                    "/html/body/table[3]/tr[1]/td[3]/table/tr/td/div/div[contains(@class, 'sign')]")]

                for j in range(len(quote_infos['Текст'])):
                    quote_info = {}
                    quote_info["Оценка"] = quote_infos["Оценка"][j]
                    quote_info["Текст"] = quote_infos["Текст"][j]
                    quote_info["Ник и дата"] = quote_infos["Ник и дата"][j]
                    write_file(quote_info, BASE_PATH + f'/{prepod}/quotes/{k}.json')
                    k += 1
                    print(quote_info)


if __name__ == "__main__":
    main()
