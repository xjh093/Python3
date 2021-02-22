#!/usr/bin/env python3
# coding=utf-8
# Haocold
# 2021-02-20 13:31:25

"""
网页资源获取
获取所有链接与名字
"""

import os
import sys
import time
import requests # 网页抓取
from bs4 import BeautifulSoup as bs # 网页解析

all_items = []

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}

def main():
    doMyWork()
    
def doMyWork():
    global stocks
    
    # 绝对路径
    dir, _ = os.path.split(os.path.abspath(sys.argv[0]))
    # 创建文件
    path = time.strftime('%Y-%m-%d')+'.md'
    file = open(dir+'/'+path, 'w')
    
    # 网址
    for i in range(1,300):
        url = 'https://www.yikm.net/nes?page='+ str(i) + '&tag=&e='
        r = requests.get(url, headers = headers)
        #print(r.text) # 获取网页内容
        soup = bs(r.text, 'lxml')
        
        # 获取所有 a 标签
        all_a = soup.find_all('a')
        for a in all_a:
            url = a['href']
            name = a.string
            
            if url and name and '/play' in url:
                print(name, file = file)
                print(url, file = file)
                
                #item = dict()
                #item["name"] = name
                #item["url"] = url
                #all_items.append(item)

    #print(all_items)
    #print(all_items, file = file)
    print("done!")

if __name__ == '__main__':
    main()
