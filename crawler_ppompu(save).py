from bs4 import BeautifulSoup
import http.cookiejar, urllib
import re
import time
from datetime import datetime
from operator import eq
import os
from django.db.models import Avg, Max, Min
from pyfcm import FCMNotification
import re


push_service = FCMNotification(api_key="AAAAQ7wC7ec:APA91bEUz5oX8bwnhcSKwYi2ESrKs2KBkdwhuA9NHyzYzsmaFROed3oPSuOHmsoeFMjtYq35NFZQ1VLbwnW-V54fKwWVC5hF0mt2QWwyf0AFBMOFaG5m0rWx7hUVVu65MQ_F9INDGOB0")



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websaver.settings")

import django

django.setup()


from parsed_data.models import PpompuData
from parsed_data.models import KeywordData

def souping(url, decode='utf-8'):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) '\
		'Gecko/20071127 Firefox/2.0.0.11'
    req = urllib.request.Request(url, headers={'User-Agent': user_agent})
    resp = urllib.request.urlopen(req)
    html = resp.read()
    soup = BeautifulSoup(html.decode('cp949','ignore'), 'html.parser')

    return soup

    
article_list=[]

def ppompu_init(i):
    data = []
    page = i
    url_ppompu = "http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page=" + str(i)

    soup_ppompu = souping(url_ppompu)
    for row in soup_ppompu.find_all('tr', {'class':{'list0', 'list1'}}):

        site_name = '뽐뿌게시판'

        link = 'http://www.ppomppu.co.kr/zboard/'+row.find('td', {'valign':'middle'}).a.get('href')
        try:
            comment = int(row.find('span', {'class':'list_comment2'}).span.getText())
        except:
            comment = 0

        testd = row.find('nobr',{"class": "eng list_vspace"}).parent.get("title")
        date = (testd[:2]+testd[3:5]+testd[6:8]+testd[9:11]+testd[12:14]+testd[15:17])

        title = row.find('td', {'valign':'middle'}).a.font.getText()
        
        post_num = int(link[len(link)-6:len(link)])
             
        data.append([site_name, post_num ,link, comment, title, date])

    return data

#data = ppompu_init()
#print (data)

#data = PpompuData.objects.aggregate(Max('post_num'))

#print(data.get('post_num__max'))


#for x in range(0, 20):
#    print (x)
#if __name__ == '__main__':

#  article_list = ppompu_init()
#  for x in article_list:
#      PpompuData(site_name = x[0], link = x[2], comment = x[3], post_num=x[1], title = x[4]).save()
            

def insert():
    previous_data = PpompuData.objects.aggregate(Max('post_num'))
    previous_last = previous_data.get('post_num__max')
    page = isPreviousPost()
    ppompu_keyword_data = KeywordData.objects.filter(bulletinName = '뽐뿌게시판')

    if previous_last == None:
        current_dataset = ppompu_init(page)
        listzz = []
        for y in current_dataset:
            PpompuData(site_name = y[0], link = y[2], comment = y[3], post_num=y[1], title = y[4], date = y[5]).save()
            

    else :
        
        while (page>0):
            current_dataset = ppompu_init(page)
            listzz = []
                   
            
            for x in current_dataset:
                if x[1] > previous_last:
                    for j in ppompu_keyword_data:
                        regex = re.compile(j.keyword)
                        mo = regex.search(x[4])
                        if mo != None:
                            print("notification 전송합니다")
                            isContainKeyword(j.keyword, j.token, j.bulletinName)
                    PpompuData(site_name = x[0], link = x[2], comment = x[3], post_num=x[1], title = x[4], date = x[5]).save()

            page=page-1
  
#글삭제시 글번호 당겨지는거 처리해야함!!            
def isPreviousPost():
    previous_data = PpompuData.objects.aggregate(Max('post_num'))
    previous_last = previous_data.get('post_num__max')
    page = 1
    k=0
    if previous_last == None:
        return 1
    else :
        
        while k == 0:
            
            current_dataset = ppompu_init(page)

            for x in current_dataset:
                if x[1] <= previous_last:
                    return page
            page=page+1


def isContainKeyword(keyword, token, bulletinName):
    
    registration_id = token
    message_title = bulletinName +"게시판"
    message_body = keyword +" 키워드 게시물을 확인해 주세요"
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

        

while(True):
    insert()
    print("끝")
    time.sleep(300)
 
