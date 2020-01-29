
# 笔趣看网站
# 1.模拟搜索
# 2.图书查询-章节列表
# 3.获取章节内容
# 4.本地存储 txt、mysql

def searchBook():
    print("************笔趣看小说下载****************")
    print("************作者：老猫****************")
    bookName = input("请输入图书的名称：")
    # 1.转移字符:中文在URL中乱码
    bookName = bookName.encode("gbk")
    # 2.请求
    resp = requests.get(url = url_one,params={"searchkey":bookName},headers=head,timeout=time)
    # 3.判断是否请求成功
    if resp.status_code == 200:
        resp.encoding = "gbk"
        # print(resp.text)
        # 4.解析内容： 1.解析的数据源 2.
        soup = BeautifulSoup(resp.text,"html.parser")
        # 4.1 Tag 根据标签的名称获取,只获取第一个出现的
        title = soup.title.string
        # img = soup.img
        # a = soup.a
        # print(title,img,a)
        # 4.2 string->None     text->Null 获取内容
        print(title.string)
        # 4.3 获取属性 attrs 属性字典集合  get()函数 访问
        # print(img.attrs.get("src"))
        # 4.4 查询 find_all() 查询所有标签，list列表【tag，tag，tag~~~】
        # find() = soup.Tag 第一个出现的标签
        # name 标签名 string 单个 list 多个
        div_list = soup.find_all(name="div",attrs={"class":"caption"})
        for div in div_list:
            # 判断不能None
            bookname = div.h4.a.string
            bookurl = div.h4.a.attrs.get("href")
            bookauthor = div.small.string
            bookdir = div.p.string
            if bookname != None and bookurl != None and bookauthor != None and bookdir != None:
                bookname.replace(" ", "")
                bookurl.replace(" ", "")
                bookauthor.replace(" ", "")
                bookdir.replace(" ", "")
                print(bookname + "\n", bookurl + "\n", bookauthor + "\n", bookdir + "\n")
                # 5.保存到字典
                book_dict[bookname] = bookurl
    else:
        print("网络有问题，重新来过")
        searchBook()
    pass

def getBookChapter():
    bookname = input("请你输入已找到图书的名称")
    # 判断是否存在字典中
    # keys() 字典key的列表集合
    if bookname in book_dict.keys():
        resp = requests.get(url=book_dict[bookname], headers=head, timeout=time)
        # 判断是否请求成功
        if resp.status_code == 200:
            resp.encoding = "gbk"
            soup = BeautifulSoup(resp.text, "html.parser")
            title = soup.title.string
            print(title.string)
            dd_list = soup.find_all(name="dd",attrs={"class":"col-md-3"})
            for dd in dd_list:
                # try:带区域内会出现异常 except：Exception父类 捕捉异常
                try:
                    chapter = dd.a.attrs.get("title")
                    chapterUrl = dd.a.attrs.get("href")
                    print(chapter)
                    chapterUrl_2 = book_dict[bookname] + chapterUrl
                    book_find[chapter] = chapterUrl_2
                    print(chapterUrl_2)


                    bookurl = book_dict[bookname]
                    getBookChapterContent(chapter,chapterUrl,bookurl,bookname)

                except Exception:
                    print("有小问题——1")
                    continue # 继续循环
    else:
        print("名称错了，不要皮了，从头再来")
        getBookChapter()

    pass


def getBookChapterContent(chapter,chapterUrl,bookurl,bookname):

    if "http" not in chapterUrl:
        chapterUrl = bookurl + chapterUrl

    resp = requests.get(url=chapterUrl)
    if resp.status_code == 200:
        resp.encoding = "gbk"
        soup4 = BeautifulSoup(resp.text,"html.parser")
        div = soup4.find(name="div",attrs={"id":"htmlContent"})
        text = div.text
        if text != None and text != " ":
            text = div.text.replace("<br/>","\n")
            saveTxt(text,bookname,chapter)  # 保存
            chapter_dict[chapter] = text # 保存到字典中
    else:
        print("加载失败")



    # bookSection = input("请输入章节名称：")
    # if bookSection in book_find.keys():
    #     resp = requests.get(url=book_find[bookSection], headers=head, timeout=time)
    #     if resp.status_code == 200:
    #         resp.encoding = "gbk"
    #         soup = BeautifulSoup(resp.text, "html.parser")
    #         title = soup.title.string
    #         print(title)
    #         div_list = soup.find_all(name="div",attrs={"class":"panel-body"})
    #         for div in div_list:
    #             try:
    #                 chapter = div.text
    #                 print(chapter)
    #             except Exception:
    #                 print("有小问题_2")
    #             continue
    #
    #     else:
    #         print("失败了")

def saveTxt(text,bookname,chapter):
    path = "小说/"+bookname
    # 验证路径是否存在
    if not os.path.exists(path):
        # 创建
        # os.mkdir(path) # 船舰一个目录
        os.makedirs(path) # 多级

    # file文件管理，创建、打开、写入、读取、清理缓存、关闭
    file = open(path + "/" + chapter + ".txt", "w", encoding="utf-8")
    file.write(text)
    file.flush()
    file.close()
    pass
def saveCsv(): # 5
    # 标题行
    headers = ['章节名称','内容']
    rows = [] # 写入的二位列表
    file = open('test.csv','w',encoding="utf-8") # 创建csv文件
    f_csv = csv.writer(file)  # 转换读和写方式：表结构
    # 循环保存到字典中的内容
    for key in chapter_dict.keys():
        text =chapter_dict[key]
        row = [key,text]   # 保存名称和内容
        rows.append(row)  # 添加到rows
    f_csv.writerow(headers)  # 写单行数据
    f_csv.writerows(rows)  # 写多行数据
    pass

# python入口
if __name__ == '__main__':
    url_one = "https://www.biqukan.cc/modules/article/search.php?searchkey=%D4%AA%D7%F0"
    head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
    time =30
    import requests  # 请求
    from bs4 import  BeautifulSoup #解析类   查询 设置 soup.Tag soup.find_oil()
    import os  # 管理目录 目录的创建、修改
    import csv # csv管理
    book_dict = {}  # 存储图书  名称：路径······
    book_find ={}  #某本书章节名，地址
    chapter_dict = {} # 存储图书   章节:内容

    searchBook()
    getBookChapter()
    saveCsv()
    # getBookChapterContent()
    pass