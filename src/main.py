#import thư viện
from lxml import html, etree
import requests
import vne_xpath
from bs4 import BeautifulSoup
import scraper
from read import read
import os
from datetime import datetime
from configparser import ConfigParser
from time import sleep
configur = ConfigParser()
try:
    configur.read('config.ini')
    save_html_content = configur.getboolean("config", "log_errors")
    log_errors = configur.getboolean("config", "log_errors")
    save_article_text = configur.getboolean("config", "log_errors")
    save_article_audio = configur.getboolean("config", "log_errors")
except:
    print("Sai kí tự ở file config.ini, hãy kiểm tra lại")
    for remaining in range(9,-1,-1):
        print(f"Thoát trong {remaining} sec",end="\r")
        sleep(1)
    exit()
version = "v1.0 beta"
reader_notice = "Đang đọc bài: "
end_notice = "Kết thúc bài đọc."
#-------------------------------------------------------------------------------

def selecion_splittor(selection_data):
    selection = selection_data.split(",")
    try:
        selection = list(map(int, selection))
    except ValueError:
        selection = False
    finally:return selection
def article_scraper(arcount):
    counter = 1
    while True:# Đếm số bài tốt nhất (số bài có thay đổi theo thời gian)
        if counter == 8:counter +=1
        if counter == arcount and arcount != None:
            print("........")
            break
        article = dom.xpath(vne_xpath.get_best_article(counter)+"/@href")
        title = dom.xpath(vne_xpath.get_best_article(counter)+"/@title")
        #print(article)
        if article != []:
            article_data[article[0]]=title[0]
            counter+=1
        else:break
    #print(article_data)
    return article_data
while True:
    try:
        article_data={}
        print("Chào mừng đến phần mềm đọc tin trên Vnexpress.net")
        print(f"Version {version}")
        print("#"*60)
        print("1 : Chỉ đọc Top Story ( 3 bài )")
        print("2 : Đọc tất cả ( gồm Top Story và khoảng 20 Editor's Picks )")
        print("3 : Chọn các bài để đọc từ danh sách ở lựa chọn 2")
        option = input("Lựa chọn : ")
        #########################  INIT  ##############################
        while True:
            try:
                page = requests.get('https://vnexpress.net/')   #Gửi request đến VNE
                break
            except:
                print("Failed to connect to Vnexpress.net. Trying again...")
        if save_html_content:
            with open("content.html", "wb") as contentfile:
                contentfile.write(page.content)
        #----------------------------------------------------------------
        source = BeautifulSoup(page.content, "html.parser")
        dom = etree.HTML(str(source))
        #----------------------------------------------------------------
        top_article = dom.xpath(vne_xpath.top_story+"/@href")
        top_2 = dom.xpath(vne_xpath.top2+"/@href")
        top_3 = dom.xpath(vne_xpath.top3+"/@href")
        article_data[top_article[0]] = top_article = dom.xpath(vne_xpath.top_story+"/@title")[0]
        article_data[top_2[0]] = top_2 = dom.xpath(vne_xpath.top2+"/@title")[0]
        article_data[top_3[0]] = top_3 = dom.xpath(vne_xpath.top3+"/@title")[0]
        #print(article_data)
        #----------------------------------------------------------------
        if option == "1":url_list = list(article_data.keys())
        elif option == "2":
            article_data = article_scraper("None")
            url_list = list(article_data.keys())
        elif option == "3":
            print("1 : Chọn các bài để đọc từ danh sách")
            print("2 : Bỏ các bài không muốn đọc trong danh sách & đọc các bài còn lại")
            print("3 : Bỏ từ bài thứ n trở đi (nhập số n)")
            option = input("Lựa chọn : ")
            article_data = article_scraper("None")
            url_list = list(article_data.keys())
            print("Danh sách bài đọc :" )
            url_index = {}
            for index, url in enumerate(url_list):
                print(str(index+1)+" : "+article_data[url].replace("\n", ""))
                url_index[index] = url
            if option == "1":
                while True:
                    selection_data = input("Chọn các bài muốn đọc (e.g: 1,2,3,4,5) :")
                    selection = selecion_splittor(selection_data)
                    if selection == False:
                        print("Bạn nhập lựa chọn không đúng,vui lòng nhập lại...")
                        continue
                    else :
                        new_list = []
                        selection.sort()
                        for i in selection:
                            new_list.append(url_index[i-1])
                        url_list = new_list.copy()
                        break
            elif option == "2":
                while True:
                    selection_data = input("Chọn các bài muốn bỏ (e.g: 1,2,3,4,5) :")
                    selection = selecion_splittor(selection_data)
                    if selection == False:
                        print("Bạn nhập lựa chọn không đúng,vui lòng nhập lại...")
                        continue
                    else :
                        selection.sort()
                        for i in selection:
                            url_list.remove(url_index[i-1])
                        break
            if option == "3":
                selection = int(input("Nhập số n : "))
                new_list = []
                for i in range(selection-1):
                    new_list.append(url_index[i])
                url_list = new_list.copy()






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
            if save_article_text :
                with open("./Saved_articles/text/"+filename+".txt","w",encoding="utf-8") as article_file:
                    article_file.write(readed_text)
            read("./Saved_articles/audio/"+filename+".mp3",readed_text,save_article_audio)
            read("./speech.mp3",end_notice,False)
        break


        
    except KeyboardInterrupt:
        print("Đang thoát...")
        exit(0)
    except Exception as Exception:
        if log_errors:
            date = str(datetime.now()).replace(":",".")
            with open(f"./Saved_articles/log/{date}.txt","w") as logfile:
                logfile.write(f"Error : {Exception}")
        print(f"Có lỗi : {Exception}")
        for remaining in range(9,-1,-1):
            print(f"Khởi động lại trong {remaining} giây",end="\r")
            sleep(1)
exit(0)