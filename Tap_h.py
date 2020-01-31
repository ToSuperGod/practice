import requests
from bs4 import BeautifulSoup
import os
import pymysql as mysql # 加载所有

def above():
    respurl = "https://www.taptap.com/topic/7810614"
    gameName = "王者荣耀"
    disscuss(gameName,respurl)  # 评论

def disscuss(gameName,respurl):  # 给我传一个游戏名称
    head = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
    time = 30

    host = "localhost"  # 127.0.0.1 = 本机IP
    user = "root"
    password = "mysql2020>"
    db = "mysql"  # 数据库
    port = 3306  # number类型

    dbHelp = mysql.connect(host=host, user=user, password=password, db=db, port=port )
    print("连接成功")
    cur = dbHelp.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS `%s`(ID INT PRIMARY KEY AUTO_INCREMENT,gName VARCHAR(200),pName VARCHAR (200),theme VARCHAR (200),postContent VARCHAR (1000),userName VARCHAR (200),userText VARCHAR (300))" % (
            gameName))

    inTo = "insert into `%s`" % (gameName) + "(gName) values('%s')" % (gameName)
    cur.execute(inTo)
    dbHelp.commit()  # 提交游戏名字

    # 加for循环 url
    for i in range(1,2):
        response = requests.get(url=respurl, headers=head, timeout=time)
        if response.status_code == 200:
            response.encoding = "utf-8"
            soup = BeautifulSoup(response.text, "html.parser")
            try:
                divs_1_list = soup.find_all(name="div", attrs={"class": "user-name-identity"})
                if divs_1_list != None:
                    userName = divs_1_list[0].a.text
                    print("版主:", userName)
                    # cur.execute("update `%s`(gName) set userName='%s' where id=%d" % (userName, num))
                else:
                    print("版主很懒没有留下名字！")
            except Exception:
                print("获取版主名字错误！！！")

            try:
                divs_2_list = soup.find_all(name="div", attrs={"class": "top-title-author"})
                if divs_2_list != None:
                    theme = divs_2_list[0].h1.p.text
                    print("主题:", theme)
                else:
                    print("版主很懒，没写主题！")
            except Exception:
                print("获取帖子主题错误！！！")

            divs_3_list = soup.find_all(name="div", attrs={"class": "bbcode-body bbcode-body-v2 js-open-bbcode-image"})
            count = 1
            try:
                if divs_3_list != None:
                    for divs_3 in divs_3_list:
                        postContent = divs_3.text
                        print("内容：", postContent)
                        # 图片部分
                        filename = "社区/" + userName
                        if not os.path.exists(filename):
                            os.makedirs(filename)
                        url_T = divs_3.img['src']
                        codeImg = requests.get(url_T)
                        # 将图片写入文件
                        try:
                            with open('./社区/%s/%d' % (userName, count) + '.png', 'wb') as fp:
                                fp.write(codeImg.content)
                                count += 1
                        except Exception:
                            print("保存图片错误！！！")
                else:
                    print("版主很懒，未为贴子写内容！")
            except Exception:
                print("获取帖子内容错误！！！")
            # 插入数据库
            inTo = "insert into `%s`" % (gameName) + "(pName ,theme,postContent) values('%s','%s','%s')" % (
            userName, theme, postContent)
            cur.execute(inTo)
            dbHelp.commit()  # 提交

            divs_4_list = soup.find_all(name="div", attrs={"class": "posts-item-text topic-posts-item-text"})
            try:
                if divs_4_list != None:
                    for divs_4 in divs_4_list:
                        name = divs_4.span.a.text
                        # no = divs_4.ul.li.text
                        data = divs_4.div.text
                        print("楼主名字：", name)
                        # print("楼号：", no)
                        print("评论内容：", data)
                        try:
                            inTo = "insert into `%s`" % (gameName) + "(userName,userText) values('%s','%s')" % (
                            name, data)
                            cur.execute(inTo)
                            dbHelp.commit()
                        except Exception:
                            pass
            except Exception:
                pass
        else:
            print("这网页中毒了，快给它解药！")

if __name__ == '__main__':
     above()

        # divs_4_list = soup.find_all(name="div", attrs={"class": "posts-item-text topic-posts-item-text"})
        # try:
        #     if divs_4_list != None:
        #         taptapUser_list = []
        #         for divs_4 in divs_4_list:
        #             taptapUser = divs_4.span.a.text  # 名字
        #             print("楼主名字：", taptapUser)
        #             taptapUser_list.append(taptapUser)
        #     else:
        #         print("楼主很懒，没有留下名字！")
        # except Exception:
        #     print("获取帖子评论楼主名字错误！！！")
        # inTo = "insert into `%s`" % (gameName) + "(userName) values('%s')" % (taptapUser)
        # cur.execute(inTo)
        # dbHelp.commit()


        # divs4_1_list = soup.find_all(name="li", attrs={"class": "topic-floor"})
        # try:
        #     if divs4_1_list != None:
        #         topicFloor=[1,2]
        #         for divs4_1 in divs4_1_list:
        #             topicFloor = divs4_1.string  # 楼号
        #
        #             # print("楼号：", topicFloor)
        #     else:
        #         print("暂无楼号！")
        # except Exception:
        #     print("获取帖子评论楼号错误！！！")
        #
        # divs4_2_list = soup.find_all(name="div", attrs={
        #     "class": "item-text-body bbcode-body bbcode-body-v2 js-open-bbcode-image"})
        # if divs4_2_list != None:
        #     try:
        #
        #         for divs4_2 in divs4_2_list:
        #             userText = divs4_2.text  # 主内容
        #             # print("评论内容：", userText)
        #     except Exception:
        #         print("获取帖子评论内容错误！！！")
        # else:
        #     print("暂无评论内容！")






        # divs4_1_list = soup.find_all(name="li", attrs={"class": "topic-floor"})
        # divs_4_list = soup.find_all(name="div", attrs={"class": "posts-item-text topic-posts-item-text"})
        # divs4_2_list = soup.find_all(name="div", attrs={
        #     "class": "item-text-body bbcode-body bbcode-body-v2 js-open-bbcode-image"})
        # try:
        #     if divs_4_list != None:
        #
        #         for divs_4 in divs_4_list:
        #             taptapUser = divs_4.span.a.text  # 名字
        #             print("楼主名字：", taptapUser)
        #
        #             if divs4_1_list != None:
        #                 for divs4_1 in divs4_1_list:
        #                     topicFloor = divs4_1.string  # 楼号
        #
        #                     if divs4_2_list != None:
        #                         for divs4_2 in divs4_2_list:
        #                             userText = divs4_2.text  # 主内容
        #                             # print("评论内容：", userText)
        #                             sql_insert = "insert into `%s`" % (
        #                                 gameName) + "(userName,topic_NO,userText) values(%s, %s, %s)"
        #                             indata = (str(taptapUser), str(topicFloor), str(userText))
        #                             cur.execute(sql_insert, indata)
        #                             dbHelp.commit()
        #                             continue
        #                 continue
        #             else:
        #                 print("暂无楼号！")
        #     else:
        #         print("楼主很懒，没有留下名字！")
        # except Exception:
        #     print("获取帖子评论楼主名字错误！！！")





