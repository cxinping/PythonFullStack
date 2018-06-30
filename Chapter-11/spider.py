# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import os
import  pymysql


def get_html(web_url):
    header = {
        "User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"}
    html = requests.get(url=web_url, headers=header).text#response
    Soup = BeautifulSoup(html, "lxml")
    data = Soup.find("ol").find_all("li")  # filter
    return data


def get_info(all_move):
    f = open("c://dev/douban2.txt", "a")

    for info in all_move:
        #    rank
        nums = info.find('em')
        num = nums.get_text()

        #    name
        names = info.find("span")  # span name
        name = names.get_text()

        #    author
        charactors = info.find("p")
        charactor = charactors.get_text().replace(" ", "").replace("\n", "")  # Arrange the law of information
        charactor = charactor.replace("\xa0", "").replace("\xee", "").replace("\xf6", "").replace("\u0161", "").replace(
            "\xf4", "").replace("\xfb", "").replace("\u2027", "").replace("\xe5", "")

        remarks = info.find_all("span", {"class": "inq"})
        if remarks:  # remark
            remark = remarks[0].get_text().replace("\u22ef", "")
        else:
            remark = "此影片没有评价"
        print(remarks)

        # 评分
        scores = info.find_all("span", {"class": "rating_num"})
        score = scores[0].get_text()

        conn = pymysql.connect(host='localhost', port=3306, user='root',
                               passwd='root', db='pythondb', charset='utf8')
        c1 = conn.cursor()
        sql = 'insert into movie values ("%s","%s","%s")' % (num, name,score)
        c1.execute(sql)
        conn.commit()
        f.write(num + '、')
        f.write(name + "\n")
        f.write(charactor + "\n")
        f.write(remark + "\n")
        f.write(score)
        f.write("\n\n")

    f.close()


if __name__ == "__main__":
    '''
    if os.path.exists("c://dev/douban2.csv") == False:
        os.mkdir("c://dev/douban2.csv")
    if os.path.exists("c://dev/douban2.csv") == True:
        os.remove("c://dev/douban2.csv")
    '''
    page = 0  # Initializing the number of pages
    while page <= 225:
        web_url = "https://movie.douban.com/top250?start=%s&filter=" % page
        all_move = get_html(web_url)  # Return to the page of each page
        get_info(all_move)  # Matching the corresponding information to the local
        page += 25