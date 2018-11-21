from bs4 import BeautifulSoup
import requests

def get_info(url):
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text
    except:
        return

def parse_info(result):
    l=[]
    L=[]
    soup=BeautifulSoup(result,'lxml')
    movies=soup.select('div[class="grid-2x grid-3x-md grid-6x-sm"] a[href]')
    dates=soup.select('div[class="day7"] ul[class="week"] li b')
    imgs=soup.select('div[class="day7"] ul[class="week"] li img[src]')
    weathers=soup.select('div[class="day7"] ul[class="txt txt2"] li')
    MaxTs=soup.select('div[class="day7"] div[class="zxt_shuju"] ul li span')
    MinTs=soup.select('div[class="day7"] div[class="zxt_shuju"] ul li b')
    fengs=soup.select('div[class="day7"] ul[class="txt"] li')
    for date,weather,MaxT,MinT,feng in zip(dates,weathers,MaxTs,MinTs,fengs):
        d={'日期':date.get_text().strip(),'天气':weather.get_text().strip(),'最高温度':MaxT.get_text().strip(),'最低温度':MinT.get_text().strip(),'风向':feng.get_text().strip()}
        l.append(d)
    for img in imgs:
        image=img.attrs
        L.append(image)
    return l

def print_image(L):
    i=0
    for image in L:
        for url in image.values():
            r=requests.get('https:'+url)
            i+=1
            with open("{}.jpg".format(i),'wb') as f:
                f.write(r.content)


def main():
    city=input("请输入你所在的城市:")
    
url='https://www.tianqi.com/guangzhou/'
result=get_info(url)
print(parse_info(result))
# print_image(L)


