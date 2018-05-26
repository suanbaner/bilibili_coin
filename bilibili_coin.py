# -*- coding=utf-8 -*-
import requests,json,re
def coinadd(av):
    prompt_data = {'aid': str(av), 'multiply': '1', 'cross_domain': 'true', 'csrf': cookies['bili_jct']}
    headers = {
        "Host": "api.bilibili.com",
        "Cache-Control": "no-cache",
        "Proxy-Connection": "keep-alive",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Origin": "https://www.bilibili.com",
        "Referer": "https://www.bilibili.com/video/av" + str(av),
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    test_page = requests.post("https://api.bilibili.com/x/web-interface/coin/add",data = prompt_data,headers=headers,cookies = cookies)
    print test_page.text


key_data = {'user': '', 'passwd': ''}   #在此处填写b站账号密码
access_page = requests.post("https://api.kaaass.net/biliapi/user/login", data=key_data).text
page_json = json.loads(access_page)
access_key = page_json["access_key"]

login_page = requests.get("https://api.kaaass.net/biliapi/user/sso?access_key="+str(access_key)).text
login_json = json.loads(login_page)
cookies_tmp = login_json["cookie"]
cookies={}
for line in cookies_tmp.split(';'):
    line = line.strip()
    if not line.split():
        break
    name,value=line.strip().split('=',1)
    cookies[name]=value  #为字典cookies添加内容
    login_page2 = requests.get("https://api.kaaass.net/biliapi/user/info?access_key="+str(access_key)+'&furtherInfo=false')
guichu_page = requests.get('https://www.bilibili.com/ranking/all/119/1/1').text
avlisttmp = re.findall('/av(.*?)/',guichu_page)
avlist = {}.fromkeys(avlisttmp).keys()
for av in avlist[:5]:
    coinadd(av)