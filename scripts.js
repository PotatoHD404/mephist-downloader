// Инфа о преподе
$x("/html/body/form/table[3]/tbody/tr[1]/td[5]/table/tbody/tr/td/a").map(el => el.href); // Преподы
$x("/html/body/table[3]/tbody/tr[1]/td[3]/table[1]/tbody/tr[2]/td[2]/table/tbody/tr/td/div[1]").map(el => el.innerText); // Преподает предмет
$x("/html/body/table[3]/tbody/tr[1]/td[3]/table[1]/tbody/tr[3]/td[2]")[0].innerText; // Преподает на факультете
$x("/html/body/table[3]/tbody/tr[1]/td[3]/table[1]/tbody/tr[4]/td[2]")[0].innerText; // Преподает на кафедре
$x("/html/body/table[3]/tbody/tr[1]/td[3]/table[1]/tbody/tr[6]/td[2]/a")[0].href; // Изрек перлов
$x("/html/body/table[3]/tbody/tr[1]/td[3]/table[2]/tbody/tr/td[1]/a").map(el => el.href); // Материалы данного препода
$x("/html/body/table[3]/tbody/tr[1]/td[3]/text()").map(el => el.data).slice(7).join("").split("\n\n"); // Отзывы по почте?
$x('//*[@id="rez"]')[0].innerText.replace(/[\(\)]/gm, "").split(" "); // Оценка отзыва // Оценка отзывов по почте
$x("/html/body/table[3]/tbody/tr[1]/td[3]/img").map(el => el.currentSrc); // Фото
$x("/html/body/table[3]/tbody/tr[1]/td[3]/p[2]").map(el => el.innerText)[0].split("\n").slice(1, 4).map(el => el.match(/(?:[А-Я,а-я,ё, ,\/]+)(?:\: ?)(-?\d\,\d{2}) \(голосовало: (\d+)\)/d)); // Статы
$x("/html/body/table[3]/tbody/tr[1]/td[3]/table[4]/tbody/tr/td/a").map(el => el.href); // Ссылки на отзывы

// Отзыв
$x("/html/body/table[3]/tbody/tr[1]/td[3]/p/u")[0].innerText //Название отзыва
$x("/html/body/table[3]/tbody/tr[1]/td[3]/p")[0].innerText //Текст отзыва
$x('//*[@id="rez"]')[0].innerText.replace(/[\(\)]/gm, "").split(" "); // Оценка отзыва
$x("/html/body/table[3]/tbody/tr[1]/td[3]/div/font[1]")[0].innerText // Nickname
$x("/html/body/table[3]/tbody/tr[1]/td[3]/div/font[3]")[0].innerText // date

// Перлы
$x("/html/body/table[3]/tbody/tr[1]/td[3]/table/tbody/tr/td/div[2]/div/a").length // number of pages
$x("/html/body/table[3]/tbody/tr[1]/td[3]/table/tbody/tr/td/div/table/tbody/tr/td[2]/table/tbody/tr/td[2]/div[1]/ul/li[1]").map(el => el.innerText); // Оценки
$x("/html/body/table[3]/tbody/tr[1]/td[3]/table/tbody/tr/td/div/a").map(el => el.innerText); // Текст отзыва
$x("/html/body/table[3]/tbody/tr[1]/td[3]/table/tbody/tr/td/div/div[contains(@class, 'sign')]").map(el => el.innerText).map(el => el.match(/Posted (?:by (.+))?(\d{2}.\d{2}.\d{4})/gm)); // Кто и когда оставил перл

Материалы
// http://www.mephist.ru/mephist/material.nsf/getLink?OpenAgent&pid=F27F730411E3897E432580A9005F816E&user_code=718749&filename=0755049 ссылки без ввода капчи
$x("/html/body/table[3]/tbody/tr[1]/td[3]/table/tbody/tr[2]/td[2]")[0].innerText // тип материала
$x("/html/body/table[3]/tbody/tr[1]/td[3]/table/tbody/tr[3]/td[2]")[0].innerText // Предмет
$x("/html/body/table[3]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td[2]")[0].innerText // Преподается на факультете
$x("/html/body/table[3]/tbody/tr[1]/td[3]/table/tbody/tr[5]/td[2]")[0].innerText // Преподается на семестре
$x("/html/body/table[3]/tbody/tr[1]/td[3]/table/tbody/tr[6]/td[2]/a")[0].href // Преподаватель
$x("/html/body/table[3]/tbody/tr[1]/td[3]/table/tbody/tr[7]/td[2]")[0].innerText // Описание
$x("/html/body/table[3]/tbody/tr[1]/td[3]/table/tbody/tr[8]/td[2]")[0].innerText // Прислал
$x("/html/body/table[3]/tbody/tr[1]/td[3]/table/tbody/tr[9]/td[2]")[0].innerText.split(" ")[0] // Дата добавления

$x('//div/ul/li[1]').map(el => el.innerText) // Оценки
$x("/html/body/table[3]/tbody/tr[1]/td/div/text()").map(el => el.data); // Текст комментариев
$x("/html/body/table[3]/tbody/tr[1]/td/div/p/font").map(el => el.innerText).map(el => el.match(/Posted (?:by (.+))?(\d{2}.\d{2}.\d{4})/gm)); // Кто написал коммент и когда
