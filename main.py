#import thư viện
from lxml import html, etree
import requests
import vne_xpath
from bs4 import BeautifulSoup
import scraper
from read import read
import os
from datetime import datetime
######################################### CONFIG ###############################
debug=True
welcome="Phần mềm đang khởi động..."
reader_notice = "Đang đọc bài: "
end_notice = "Kết thúc bài đọc."
version = "v1.0 beta"
#-------------------------------------------------------------------------------
logfile = "./Saved_articles/log/log_" + str(datetime.now()) + ".txt"
article_data={}
def article_scraper(arcount):
    counter = 1
    while True:# Đếm số bài tốt nhất (số bài có thay đổi theo thời gian)
        if counter == 8:counter +=1
        if counter == arcount and arcount != None:
            print("........")
            break
        article = dom.xpath(vne_xpath.get_best_article(counter)+"/@href")
        title = dom.xpath(vne_xpath.get_best_article(counter)+"/text()")
        #print(article)
        if article != []:
            article_data[article[0]]=title[0]
            counter+=1
        else:break
    #print(article_data)
    return url_list, article_data
print("Chào mừng đến phần mềm đọc tin trên Vnexpress.net")
print(f"Version {version}")
print("#"*60)
print("1 : Chỉ đọc Top Story ( 3 bài )")
print("2 : Đọc tất cả ( gồm Top Story và khoảng 20 Editor's Picks )")
print("3 : Chọn các bài để đọc từ danh sách ở lựa chọn 2")
print(" NOTE : LỰA CHỌN 3 CHƯA LÀM XONG")
option = input("Lựa chọn : ")
#########################  INIT  ##############################
while True:
    try:
        page = requests.get('https://vnexpress.net/')   #Gửi request đến VNE
        break
    except:
        print("Failed to connect to Vnexpress.net. Trying again...")
if debug:
    with open("content.html", "wb") as contentfile:
        contentfile.write(page.content)
#----------------------------------------------------------------
source = BeautifulSoup(page.content, "html.parser")
dom = etree.HTML(str(source))
#----------------------------------------------------------------
top_article = dom.xpath(vne_xpath.top_story+"/@href")
top_2 = dom.xpath(vne_xpath.top2+"/@href")
top_3 = dom.xpath(vne_xpath.top3+"/@href")
article_data[top_article[0]] = top_article = dom.xpath(vne_xpath.top_story+"/text()")[0]
article_data[top_2[0]] = top_2 = dom.xpath(vne_xpath.top2+"/text()")[0]
article_data[top_3[0]] = top_3 = dom.xpath(vne_xpath.top3+"/text()")[0]
#print(article_data)
#----------------------------------------------------------------
if option == "2":
    url_list, article_data = article_scraper("None")
url_list = list(article_data.keys())
print("Các bài sẽ đọc:")
for url in url_list:
    if article_data[url] == "": print("error..")
    print(article_data[url])
for url in url_list:
    try:
        rtitle=article_data[url]
        readed_text=scraper.scrape_article_text(url)
        filename = url.replace("https://vnexpress.net/","")
        filename = filename.replace(".html","")
    except:
        print("Failed scraping article. Trying next one....")
        read(None, "Phần mềm không lấy được văn bản từ bài báo, đang thử bài tiếp theo", False)
        continue
    if rtitle !="" : read("./speech.mp3",reader_notice+rtitle,False)
    with open("./Saved_articles/text/"+filename+".txt","w",encoding="utf-8") as article_file:
        article_file.write(readed_text)
    read("./Saved_articles/audio/"+filename+".mp3",readed_text,True)
    read("./speech.mp3",end_notice,False)



