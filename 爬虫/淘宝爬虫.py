#encoding:utf-8
import requests
from str_dic import str_dic
from json import loads
from bs4 import BeautifulSoup
import re
import urllib2


#获取人物列表
def get_user_list(page):
    data = """
q: 
viewFlag: A
sortType: default
searchStyle: 
searchRegion: city:
searchFansNum: 
currentPage:1
pageSize: 100
"""
    data_dic=str_dic(data)
    data_dic['currentPage'] = page
    response = requests.post('https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8',data_dic)
    html = response.text
    result = loads(html)
    return result['data']['searchDOList']

#获取图片地址
def parse(html):
    soup = BeautifulSoup(html,'html.parser')
    img_list = set()
    imgs = soup.find_all('img',src=re.compile(r'img.alicdn.com'))
    for img in imgs:
        tupian = img['src']
        img_list.add(tupian)
    return img_list

#下载图片
def down_pic(img_list,path,x):
    if img_list is None:
        return None

    y = 1

#用读写操作下载
    for img in img_list:
        f = open(path+str(x)+'-'+str(y)+'.jpg','wb')
        data = urllib2.urlopen('http:'+img).read()
        f.write(data)
        
        print ('%d-%d下载完成'%(x,y))
        y += 1



if __name__ == '__main__':
    x = 0
    path = "E://java/taobao/"
    for page in range(1,5):
        for user in get_user_list(page):
            try:
                user_id = user['userId']
                url = 'https://mm.taobao.com/self/aiShow.htm?spm=719.7763510.1998643336.2.mZYkiD&userId={}'.format(user_id)
        
                res = requests.get(url)
                html = res.text
                img_list = parse(html)
        
                down_pic(img_list,path,x)
                print x
                x+=1
            except:
                print "页面获取失败"

        
        
        
        
        
        