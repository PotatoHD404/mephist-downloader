import json
import requests
import lxml.html

BASE_PATH = '/Users/potatohd/Documents/mephist/downloaded'


def fetch(link, return_text=False):
    done = False
    data = None
    while not done:
        try:
            data = requests.get(link).text
            done = True
        except Exception as e:
            print(e, type(e))
    if return_text:
        return data

    html = lxml.html.fromstring(data)
    return html


def write_file(data, path):
    print(f'Writing to {path}')
    done = False
    while not done:
        try:
            with open(path, "w") as out:
                out.write(json.dumps(data))
                done = True
        except Exception as e:
            print(e, type(e))


# noinspection PyDictCreation
def main():
    prepods_page = fetch('http://www.mephist.ru/mephist/prepods.nsf/teachers')
    prepod_links = map(lambda el: 'http://www.mephist.ru' + el.attrib['href'].replace("\\", "/"),
                       prepods_page.xpath('/html/body/form/table[3]/tr[1]/td[5]/table/tr/td/a'))
    for i, link in enumerate(prepod_links):
        prepod_page = fetch(link)
        # print(dir(prepod_page.xpath("/html/body/table[3]/tr[1]/td[3]/table[1]/tr[6]/td[2]")[0]))
        # print(prepod_page.xpath("/html/body/table[3]/tr[1]/td[3]/table[1]/tr[6]/td[2]/a")[0].attrib['href'])
        prepod_info = {}
        # print(prepod_page.xpath("/html/body/table[3]/tr[1]/td[3]/table[1]/tr[6]/td[2]/@href"))
        prepod_info["Имя"] = prepod_page.xpath("/html/body/table[3]/tr[1]/td[3]/table[1]/tr[1]/td[2]/b/font")[0].text
        prepod_info["Предметы"] = [el.text for el in
                                   prepod_page.xpath(
                                       "/html/body/table[3]/tr[1]/td[3]/table[1]/tr[2]/td[2]/table/tr/td/div[1]")]
        prepod_info["Факультет"] = prepod_page.xpath("/html/body/table[3]/tr[1]/td[3]/table[1]/tr[3]/td[2]")[0].text
        prepod_info["Кафедра"] = prepod_page.xpath("/html/body/table[3]/tr[1]/td[3]/table[1]/tr[4]/td[2]")[0].text
        prepod_info["Перлы"] = prepod_page.xpath("/html/body/table[3]/tr[1]/td[3]/table[1]/tr[6]/td[2]/a")[0].attrib[
            'href']
        prepod_info["Материалы"] = ['http://www.mephist.ru' + el.attrib['href'].replace('\\', '/') for el in
                                    prepod_page.xpath("/html/body/table[3]/tr[1]/td[3]/table[2]/tr/td[1]/a")]
        prepod_info["Информация"] = prepod_page.xpath("/html/body/table[3]/tr[1]/td[3]/text()")
        prepod_info["Оценка отзыва по почте"] = prepod_page.xpath('//*[@id="rez"]')[0].text_content()
        prepod_info["Имена отзывов по почте"] = [el.text for el in
                                                 prepod_page.xpath('/html/body/table[3]/tr[1]/td[3]/a')]
        prepod_info["Фото"] = ['http://www.mephist.ru' + el.attrib['src'] for el in
                               prepod_page.xpath('/html/body/table[3]/tr[1]/td[3]/img')]

        prepod_info["Статы"] = prepod_page.xpath('/html/body/table[3]/tr[1]/td[3]/p[2]')[0].text_content()
        review_links = ['http://www.mephist.ru' + el.attrib['href'].replace('\\', '/') for el in
                        prepod_page.xpath('/html/body/table[3]/tr[1]/td[3]/table[4]/tr/td/a')]
        prepod_info["Отзывы"] = review_links
        write_file(prepod_info, BASE_PATH + f'/{i}.json')


if __name__ == "__main__":
    main()
