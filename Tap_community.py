import requests
from bs4 import BeautifulSoup
import os
import pymysql as mysql # 加载所有
import time


# 腾超
def top():
    top = ["download", "new", "reserve", "sell", "played"]
    resp = requests.get(url=url_one+"top/"+top[0], headers=head, timeout=time)
    # print(resp.status_code)
    if resp.status_code == 200:
        # print(resp.text)
        soup = BeautifulSoup(resp.text, "html.parser")
        # print(soup)
        div_list = soup.find_all(name="div", attrs={"class": "top-card-left"})  # 游戏名字、图片、地址标签
        p_list = soup.find_all(name="p", attrs={"class": "middle-footer-rating"})  # 游戏评分标签
        game_rank = 0
        for div,p in zip(div_list,p_list):
            game_rank += 1  # 游戏排名
            game_name = div.a.img.attrs.get("title")  # 游戏名字
            game_eva = p.span.string  # 游戏评分
            game_img = div.a.img.attrs.get("src")  # 游戏图片
            game_url = div.a.attrs.get("href")  # 游戏地址
            game(game_url)
            print("Top"+str(game_rank)+"\n"+game_name+"\n", "评分:"+game_eva+"\n", game_img+"\n", game_url+"\n")
        pass
    else:
        print("重新获取数据")
        top()
    pass


def developers():
    resp = requests.get(url=url_one + "top/developers", headers=head, timeout=time)
    # print(resp.status_code)
    if resp.status_code == 200:
        # print(resp.text)
        soup = BeautifulSoup(resp.text, "html.parser")
        # print(soup)
        a_list = soup.find_all(name="a", attrs={"class": "developer-item"})  # 厂商排名标签
        img_list = soup.find_all(name="img", attrs={"class": "img-circle"})  # 厂商图片标签
        div_list = soup.find_all(name="div", attrs={"class": "developer-name-wrap"})  # 厂商名字标签
        span_list1 = soup.find_all(name="span", attrs={"class": "fans"})  # 厂商粉丝数量标签
        span_list2 = soup.find_all(name="span", attrs={"class": "rating"})  # 厂商评分标签
        span_list3 = soup.find_all(name="span", attrs={"class": "info-item"})  # 厂商游戏数、评价数、帖子数标签
        for a, img, div, span1, span2 in zip(a_list, img_list, div_list, span_list1, span_list2):
            dev_rank = a.span.string  # 厂商排名
            dev_name = div.span.string  # 厂商名字
            dev_img = img.attrs.get("src")  # 厂商图片
            dev_url = a.attrs.get("href")  # 厂商页面地址
            dev_fans = span1.string  # 厂商粉丝数
            dev_rating = span2.string.replace("\n","").replace(" ", "")  # 厂商评分
            i = 0
            while i < 90:
                dev_game = span_list3[i].string  # dev_games 厂商游戏数
                i += 1
                dev_eva = span_list3[i].string  # dev_eva 厂商评价数
                i += 1
                dev_post = span_list3[i].string  # dev_post厂商帖子数
                i += 1
            print("Top" + str(dev_rank) + "\n" + dev_name + "  ",
                  dev_fans, dev_rating+"\n", dev_game + "  ", dev_eva + "  ", dev_post + "\n", dev_img + "\n", dev_url)
            dev_details(dev_url)
            dev_evas(dev_url)
        pass
    else:
        print("重新获取数据")
        developers()
    pass


def dev_details(dev_url):
    resp = requests.get(url=dev_url, headers=head, timeout=time)
    # print(resp.status_code)
    if resp.status_code == 200:
        # print(resp.text)
        soup = BeautifulSoup(resp.text, "html.parser")
        # print(soup)
        div1 = soup.find(name="div", attrs={"class": "main-content main-intro main-header-tips"})  # 厂商简介标签
        div2_list = soup.find_all(name="div", attrs={"class": "col-sm-4 rec-apps"})  # 推荐游戏标签
        div3 = soup.find(name="div", attrs={"class": "main-content main-developer-apps main-header-tips"})  # 厂商游戏标签
        if div1:
            dev_brief = div1.p.string  # 厂商简介
        else:
            dev_brief = "无"
        if div2_list:
            i = 0
            game_name = []  # 游戏名称
            game_img = []  # 游戏图片
            game_url = []  # 游戏地址
            while i < 3:
                game_name.append(div2_list[i].div.a.string)  # 游戏名称
                game_img.append(div2_list[i].a.img.attrs.get("src"))  # 游戏图片
                game_url.append(div2_list[i].div.a.attrs.get("href"))  # 游戏地址
                i += 1
        else:
            game_name = ["无", "无", "无"]  # 游戏名称
            game_img = ["无", "无", "无"]  # 游戏图片
            game_url = ["无", "无", "无"]  # 游戏地址
        if div3:
            dev_games_url = div3.a.attrs.get("href")  # 厂商所有游戏地址
        else:
            dev_games_url = "无"
        print("厂商简介", dev_brief+"\n", "推荐游戏")
        for i in range(3):
            print(game_name[i], game_img[i], game_url[i] + "\n")
        if dev_games_url:
            print("厂商所有游戏地址", dev_games_url)
            print("厂商游戏")
            dev_games(dev_games_url)
        else:
            print("厂商所有游戏地址", dev_games_url)
            print("厂商游戏", "无")
    else:
        print("网络问题，重新连接")
        dev_details(dev_url)

    pass


def dev_games(games_url):
    resp = requests.get(url=games_url, headers=head, timeout=time)
    # print(resp.status_code)
    if resp.status_code == 200:
        # print(resp.text)
        soup = BeautifulSoup(resp.text, "html.parser")
        # print(soup)
        div_list = soup.find_all(name="div", attrs={"class": "taptap-app-item swiper-slide"})  # 厂商所有游戏的标签
        span_list = soup.find_all(name="div", attrs={"class": "item-caption-label"})  # 厂商所有游戏的评分标签
        for div, span in zip(div_list, span_list):
            game_name = div.div.a.h4.string  # 厂商游戏姓名
            game_url = div.div.a.attrs.get("href")  # 厂商游戏地址
            game_img = div.a.img.attrs.get("data-src")  # 厂商游戏图片
            game_eva = span.span.span.string  # 厂商游戏评分
            print(game_name, game_eva, game_img, game_url)
    pass


def dev_evas(dev_url):
    eva_url = dev_url+"/review"
    resp = requests.get(url=eva_url, headers=head, timeout=time)
    # print(resp.status_code)
    if resp.status_code == 200:
        # print(resp.text)
        soup = BeautifulSoup(resp.text, "html.parser")
        # print(soup)
        div_list = soup.find_all(name="div", attrs={"class": "rating-item"})
        i = 5
        for div in div_list:
            rating = div.div.attrs.get("style").replace("width: ", "")
            print(str(i)+"星", rating)
            i -= 1
    else:
        print("网络错误，重新连接")
        dev_evas(dev_url)
    pass


def forum(dev_url):
    forum_url = dev_url+"/topic"

    pass


def search():
    game_name = input("请输入游戏名称")
    resp = requests.get(url=url_one+"search/"+game_name, headers=head, timeout=time)
    # print(resp.status_code)
    if resp.status_code == 200:
        # print(resp.text)
        soup = BeautifulSoup(resp.text, "html.parser")
        # print(soup)
        div_list = soup.find_all(name="div", attrs={"class": "taptap-app-card"})
        i = 0
        for div in div_list:
            game_name = div.a.img.attrs.get("title")
            game_img = div.a.img.attrs.get("src")
            game_url = div.a.attrs.get("href")
            i += 1
            game_dict[game_name] = game_url
            print("第"+str(i)+"个\n"+game_name+"\n", game_img+"\n", game_url+"\n")
        getGame()
        pass
    else:
        print("重新获取数据")
        search()
    pass


def getGame():
    game_name = input("请输入已经找到的游戏名称")
    if game_name in game_dict.keys():
        game(game_dict[game_name])
        pass
    else:
        print("游戏名称错误，请重新输入")
        getGame()
    pass


def game(game_url):
    print(game_url)
    padata(game_url)
    above_1(game_url)
    Game(game_url)
    pass


# if __name__ == '__main__':
#     url_one= "https://www.taptap.com/"
#     head = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
#     time = 15
#     game_dict = {}  # 存储搜索到的游戏名称与地址
#     # top()
#     # search()
#     developers()
#     pass



# 杨雨澄

def padata(url):
    resp = requests.get(url=url,headers=head)
    url_get = resp.url
    coding = resp.encoding = "utf=8"
    print(url_get)
    print(resp.status_code)

    print(resp.status_code)
    url_get = resp.url
    print(url_get)
    soup = BeautifulSoup(resp.text, "html.parser")
    #print(resp.text)
    div_list0 = soup.find(name= "div",attrs= "base-info-wrap")
    headertitle = div_list0.h1.text
    print(headertitle)
    span_list15 = soup.find_all(name="span",attrs="count-stats")
    for span in span_list15:
        anzhuang = span.text
        print(anzhuang)
    button_list0 = soup.find(name="button",attrs ="btn btn-primary btn-lg android js-header-android-download")
    download1 = button_list0.span.text.replace("     ","")
    downloadurl1 = button_list0.attrs.get("data-taptap-app-icon")
    print("安卓")
    print(download1,downloadurl1)
    button_list1 = soup.find(name="button",attrs="btn btn-primary ios")
    if button_list1 !=None:
        download2 = button_list1.span.text.replace("     ","")
        print("IOS")
        print(download2)
    else:
        pass
    button_list2 = soup.find(name="p",attrs = "intro")
    downloadurl2 = button_list2.a.attrs.get("href")
    print(downloadurl2)
    div_list1 = soup.find(name="div",attrs={"class": "main-body-common main-body-developer main-body-description"})
    if div_list1 != None:
        authortitle = div_list1.h3.text # 开发者的话
        authorspeak = div_list1.p.text.replace(" ","\n").replace("，","\n")
        print(authortitle,authorspeak)
    else:
        pass
    div_list2 = soup.find(name="div", attrs={"class":"main-body-common main-body-reason"})
    if div_list2 !=None:
        eidtortitle = div_list2.h3.text
        eidtorspeak = div_list2.p.text
        print(eidtortitle,eidtorspeak)
    else:
        pass
    div_list3 = soup.find(name="div", attrs={"class":"main-body-common main-body-number"})
    if div_list3 != None:
        qun = div_list3.p.text
        print(qun)
    else:
        pass
    div_list4 = soup.find(name="div", attrs={"class":"main-body-common main-body-images"})
    if div_list4 != None:
        VideoandPhoto = div_list4.h3.text.replace("                                              ","")
        summ = div_list4.a.text.replace("  ","")
        print(VideoandPhoto,summ)
    else:
        pass
    div_list20 = soup.find_all(name="div",attrs={"class":"video-info"})
    if div_list20 != None:
        videosum = 0
        for div in div_list20:
            if videosum <10:
                videoname = div.h4.a.text # 只显示头10个视频
                videourl = div.h4.a.attrs.get("href")
                videosum = videosum+1
                print(videoname,videourl)
            else:
                break
    else:
        pass
    # div_list5 = soup.find(name="div", attrs={"class":"video-options"})
    # videos = div_list5.div.attrs.get("style")
    # print(videos)
    ul_list5 = soup.find_all(name="ul", attrs={"class": "main-body-common list-unstyled main-body-additional"})
    if ul_list5 != None:
        for ul in ul_list5:
            ziti = ul.span.text
            print(ziti)
        else:
            pass
    ul_list6 = soup.find(name="div", attrs={"class":"main-body-common main-body-description"})
    if ul_list6 != None:
        jianjie = ul_list6.h3.text # 简介
        print(jianjie)
    else:
        pass
    ul_list7 = soup.find(name="div", attrs={"id":"description"})
    if ul_list7 != None:
        neirong = ul_list7.text.replace("                                      ","").replace("。","\n").replace("，","\n")
        print(neirong)
    else:
        pass
    div_list21 = soup.find(name="div",attrs={"class":"wrapper"})
    if div_list21 != None:
        jiangxiang = div_list21.h5.text
        jiangxiang2 = div_list21.p.text
        print(jiangxiang,jiangxiang2)
    else:
        pass
    ul_list8 = soup.find(name="div", attrs={"class": "main-body-common main-body-log main-body-description"})
    if ul_list8 != None:
        gengxin = ul_list8.span.text
        print(gengxin)
    else:
        pass
    ul_list9 = soup.find(name="div", attrs={"id":"app-log"})
    if ul_list9 != None:
        GXneirong = ul_list9.text.replace("                    ","").replace("。","\n").replace("，","\n")
        print(GXneirong)# 更新内容
    else:
        pass
    ul_list10 = soup.find(name="div", attrs={"class": "main-body-common main-body-info"})
    if ul_list10 != None:
        message = ul_list10.h3.text
        print(message)
    else:
        pass
    #ul_list11 = soup.find_all(name="ul", attrs={"class": "list-unstyled body-info-list"})
    #for ul in ul_list11:
    #    xiangxi = ul.span.text
    #    print(xiangxi)
    spanlist1 = soup.find_all(name="span", attrs={"class":"info-item-title"})
    spanlist2 = soup.find_all(name="span", attrs={"class": "info-item-content"})
    for span1, span2 in zip(spanlist1, spanlist2):
        x1 = span1.string
        y1 = span2.string
        print(x1,y1)
    spanlist4 = soup.find(name="a", attrs={"class": "info-item-content link"})
    if spanlist4 != None:
        x2 = spanlist4.text
        y2 = spanlist4.attrs.get("href")
        print("厂商")
        print(x2,y2)
    else:
        pass
    spanlist3 = soup.find(name="a", attrs={"data-id": "58885"})
    if spanlist3 != None:
        x3 = spanlist3.text
        y3 = spanlist3.attrs.get("href")
        print("官网")
        print(x3, y3)
    else:
        pass
    pass



# 方强
# 爬取评价
def above_1(url):
    # url = "https://www.taptap.com/app/81447"
    Url = url + "/review"
    Evaluation(Url)


def Evaluation(Url):
    time = 10
    head = {
        "Cookie": "_lxsdk_cuid=16f4f24c9bcc8-07adbcd20d5e93-3a65420e-144000-16f4f24c9bcc8; _lxsdk=16f4f24c9bcc8-07adbcd20d5e93-3a65420e-144000-16f4f24c9bcc8; isid=E08C528A41C458E2F1CC86E26618C48F; token=P4jc4qGAEOUCtPvjYWySGNX3Uc8AAAAAsAkAAPaDhuG-ly94GZ3Qus-Eu2zLuCQGEA4w9oBKYI3ftsS23FmX8Lunvd93J32eO04CaQ; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1577890701; td_cookie=787082884; theme=moviepro; __mta=55351828.1577580808930.1578287447031.1578287452121.19; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=16f7933636d-153-b4a-c0f%7C%7C17"
        ,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
    # connect() 连接函数
    # host = "localhost"  # 127.0.0.1 = 本机ip
    # user = "root"
    # password = "Fang357000"
    # db = "mysql"  # 数据库
    # port = 3306  # number类型
    # dbHelp = mysql.connect(host=host, user=user, password=password, db=db, port=port)

    resp = requests.get(url=Url, headers=head, timeout=time)
    # print(resp.text)
    resp.encoding = "utf-8"
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "html.parser")
        a_list = soup.find_all(name="a", attrs={"data-taptap-tab": "review"})
        # print(li_list)
        for a in a_list:
            title = a.text
            print(title)  # 评价   条数
        div_list = soup.find_all(name="div", attrs={"class": "clearfix total-rating"})
        for div in div_list:
            title = div.span.string
            number = div.p.span.string
            print(title, number)  # 总评分 ：  分数
        div1_list = soup.find_all(name="div", attrs={"class": "clearfix recent-7-days"})
        for div in div1_list:
            all = div.text
            print(all)  # 最新版本等等等

        div3_list = soup.find_all(name="div", attrs={"class": "item-text-header"})
        a = "成功"

        for div in div3_list:
            name = div.span.a.string
            # i ="insert into Evaluation(name,Evaluation) values('%s','%s')"%(name,a)
            # cur.execute(i)
            # dbHelp.commit()  # 提交
            print("玩家名字:" + name)

        div2_list = soup.find_all(name="div", attrs={"class": "item-text-body"})
        for div in div2_list:
            evaluation = div.text
            print("评论：" + evaluation)


# if __name__ == '__main__':
#     import requests
#     from bs4 import BeautifulSoup
#     import csv  # csv管理
#     import pymysql as mysql
#
#     time = 10
#     head = {
#         "Cookie": "_lxsdk_cuid=16f4f24c9bcc8-07adbcd20d5e93-3a65420e-144000-16f4f24c9bcc8; _lxsdk=16f4f24c9bcc8-07adbcd20d5e93-3a65420e-144000-16f4f24c9bcc8; isid=E08C528A41C458E2F1CC86E26618C48F; token=P4jc4qGAEOUCtPvjYWySGNX3Uc8AAAAAsAkAAPaDhuG-ly94GZ3Qus-Eu2zLuCQGEA4w9oBKYI3ftsS23FmX8Lunvd93J32eO04CaQ; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1577890701; td_cookie=787082884; theme=moviepro; __mta=55351828.1577580808930.1578287447031.1578287452121.19; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=16f7933636d-153-b4a-c0f%7C%7C17"
#         ,
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
#     # connect() 连接函数
#     host = "localhost"  # 127.0.0.1 = 本机ip
#     user = "root"
#     password = "Fang357000"
#     db = "mysql"  # 数据库
#     port = 3306  # number类型
#     dbHelp = mysql.connect(host=host, user=user, password=password, db=db, port=port)
#     # print("连接成功")
#
#     # 获取游标：执行，编译str类型sql语句
#     cur = dbHelp.cursor()
#     # cur.execute("CREATE TABLE IF NOT EXISTS Evaluation(ID INT PRIMARY KEY AUTO_INCREMENT,"
#     #            "name VARCHAR(25),Evaluation VARCHAR(25))")
#     # i = cur.execute("INSERT INTO user_info(name) VALUES('l')")
#     # dbHelp.commit()  # 提交
#     # print(i)
#
#     above_1()






# 吴萌
# def above():
# #     url_one = "https://www.taptap.com/app/58885"
# #     Game(url_one)
# #     pass


def Game(gameName ,url_one):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
    time = 30
    url_one = url_one + "/topic"
    resp = requests.get(url=url_one, headers=head, timeout=time)
    if resp.status_code == 200:
        resp.encoding = "utf-8"
        soup = BeautifulSoup(resp.text, "html.parser")
        title = soup.title.string
        print(title.string)
        div1_list = soup.find_all(name="div", attrs={"class": "group-detail"})
        for div in div1_list:
            Gamename = div.h2.a.text
            attention = div.ul.text
            print(Gamename , attention )

        for i in range(1,3):
            url_one = "https://www.taptap.com/app/58885/topic?type=all&sort=commented&group_label_id=0&page=%d"
            url_two = url_one%(i)
            resp = requests.get(url=url_two,headers=head,timeout=time)

            div2_list = soup.find_all(name="ul", attrs={"class": "item-text-footer"})
            for div in div2_list:
                respurl = div.a.attrs.get("href")
                url_dic[gameName] = respurl
    else:
        print("竟然不联网，你有毒！")
    pass














# 自己
# def above():
#     respurl = "https://www.taptap.com/topic/7810614"
#     disscuss(respurl)  # 评论


def disscuss(respurl):  # 给我传一个游戏名称
    head = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
    time = 30
    response = requests.get(url = respurl,headers = head,timeout = time)
    if response.status_code == 200:
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text,"html.parser")

        try:
            divs_1_list = soup.find_all(name="div", attrs={"class": "user-name-identity"})
            if divs_1_list != None:
                userName = divs_1_list[0].a.text
                print("版主:", userName)
            else:
                print("版主很懒没有留下名字！")
        except Exception:
            print("获取楼主名字错误！！！")

        try:
            divs_2_list = soup.find_all(name="div", attrs={"class": "top-title-author"})
            if divs_2_list != None:
                topTitle = divs_2_list[0].h1.p.text
                print("主题:", topTitle)
            else:
                print("版主很懒，没写主题！")
        except Exception:
            print("获取帖子主题错误！！！")

        divs_3_list = soup.find_all(name="div", attrs={"class": "bbcode-body bbcode-body-v2 js-open-bbcode-image"})
        count = 1
        try:
            if divs_3_list != None:
                for divs_3 in divs_3_list:
                    codeBaby = divs_3.text
                    print("内容：", codeBaby)
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

        divs_4_list = soup.find_all(name="div", attrs={"class": "posts-item-text topic-posts-item-text"})
        try:
            if divs_4_list != None:
                for divs_4 in divs_4_list:
                    taptapUser = divs_4.span.a.text  # 名字
                    print("楼主名字：", taptapUser)
            else:
                print("楼主很懒，没有留下名字！")
        except Exception:
            print("获取帖子评论楼主名字错误！！！")

        divs4_1_list = soup.find_all(name="li", attrs={"class": "topic-floor"})
        try:
            if divs4_1_list != None:
                for divs4_1 in divs4_1_list:
                    topicFloor = divs4_1.string  # 楼号
                    print("楼号：", topicFloor)
            else:
                print("暂无楼号！")
        except Exception:
            print("获取帖子评论楼号错误！！！")

        divs4_2_list = soup.find_all(name="div", attrs={
             "class": "item-text-body bbcode-body bbcode-body-v2 js-open-bbcode-image"})
        try:
            if divs4_2_list != None:
                for divs4_2 in divs4_2_list:
                    item_text = divs4_2.text  # 主内容
                    print("评论内容：", item_text)


            else:
                print("暂无评论内容！")
        except Exception:
            print("获取帖子评论内容错误！！！")

        # 未完成的数据库
        # host = "localhost"  # 127.0.0.1 = 本机IP
        # user = "root"
        # password = "root"
        # db = "mysql"  # 数据库
        # port = 3306  # number类型
        # dbHelp = mysql.connect(host=host, user=user, password=password, db=db, port=port)
        # print("连接成功")
        # # 获取游标：执行、编译str类型sql语句
        # cur = dbHelp.cursor()

        # divs4_4_list = soup.find_all(name="div",attrs={"class":"list-unstyled item-text-footer"})
        # for divs4_4 in divs4_4_list:
        #     postTime = divs4_4.span.text
        #     print("评论时间：", postTime)
        #
        # divs4_3_list = soup.find_all(name="div",attrs={"class":"collapse in"})
        # for divs4_3 in divs4_3_list:
        #     item_text_body = divs4_3.div.a.text
        #     print("子回复内容：",item_text_body)

    else:
        print("这网页中毒了，快给它解药！")

if __name__ == '__main__':

    # 吴萌
    url_dic = {}

    # 腾超
    url_one = "https://www.taptap.com/"
    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
    time = 15
    game_dict = {}  # 存储搜索到的游戏名称与地址
    top()
    search()
    # developers()




    # above()
