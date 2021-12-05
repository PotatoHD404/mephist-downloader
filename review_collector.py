import json
import requests
import lxml.html
from collector import BASE_PATH, fetch, write_file


# noinspection PyDictCreation
def main():
    prepods_page = fetch('http://www.mephist.ru/mephist/prepods.nsf/teachers')
    prepod_links = map(lambda el: 'http://www.mephist.ru' + el.attrib['href'].replace("\\", "/"),
                       prepods_page.xpath('/html/body/form/table[3]/tr[1]/td[5]/table/tr/td/a'))
    # for i, link in enumerate(prepod_links):
    link = 'http://www.mephist.ru/prepod/resp/3E5C58416DA5F05FC325701E007A8052'
    review_info = fetch(link)
    # print(dir(review_info.xpath("/html/body/table[3]/tr[1]/td[3]/table[1]/tr[6]/td[2]")[0]))
    # print(review_info.xpath("/html/body/table[3]/tr[1]/td[3]/table[1]/tr[6]/td[2]/a")[0].attrib['href'])
    prepod_info = {}
    # print(review_info.xpath("/html/body/table[3]/tr[1]/td[3]/table[1]/tr[6]/td[2]/@href"))
    prepod_info["Название"] = review_info.xpath("/html/body/table[3]/tr[1]/td[3]/p/u")[0].text
    prepod_info["Текст"] = ''.join(review_info.xpath("/html/body/table[3]/tr[1]/td[3]/p/text()"))
    prepod_info["Оценка"] = review_info.xpath('//*[@id="rez"]')[0].text_content()
    prepod_info["Ник"] = review_info.xpath("/html/body/table[3]/tr[1]/td[3]/div/font[1]")[0].text
    prepod_info["Дата"] = review_info.xpath("/html/body/table[3]/tr[1]/td[3]/div/font[3]")[0].text
    # write_file(prepod_info, BASE_PATH + f'/{i}.json')
    print(prepod_info)


if __name__ == "__main__":
    main()
