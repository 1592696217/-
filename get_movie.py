import requests
import re

def get_info(url):
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text
    except:
        print('error')


def parse_info(result):
    d={}
    names=re.findall('<a class="pic-pack-outer" target="_blank" href=".+" title="(.+)"><img',result)
    movies=re.findall('<a class="pic-pack-outer" target="_blank" href="(.+)"\s+title',result)
    for name,movie in zip(names,movies):
        d[name]=movie

    return d


urls=["http://www.1905.com/vod/list/n_1/o3p{}.html".format(i) for i in range(1,2)]

for url in urls:
    result=get_info(url)
    print(parse_info(result))

