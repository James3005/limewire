import requests, os, time, json
from datetime import datetime
now = datetime.now()
cookie="_ga=GA1.1.351419465.1657127026;bitmedia_fid=eyJmaWQiOiIzYjY4ZGY0OWZiYTVlM2FhMDM3MjcxMzNmNjcwODkwMSIsImZpZG5vdWEiOiJmOTVmZDg5ZmEyNjJmZjBkYjBlYWUyOWViN2IxYTU4ZCJ9;AccExist=292239;_ga_7Z81E54NN3=GS1.1.1657124681.14.1.1657127334.0;SesHashKey=jg2nyloyfr3c17u5;SesToken=ses_id%3D292239%26ses_key%3Djg2nyloyfr3c17u5;uuid=Pd4f02300-6eb0-448f-a74d-e7e48fd90af2;PHPSESSID=j5buhd4egchhu2reb0ju3c2d6p"
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")
headers={
  'sec-gpc':'1',
    'sec-fetch-site':'same-origin',
    'sec-fetch-mode':'navigate',
    'sec-fetch-user':'?1',
    'sec-fetch-dest':'document',
    'referer':'https://earnbitmoon.club/',
    'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Mobile Safari/537.36',
    'cookie':cookie,
    }
headerss={
  'Host':'api-secure.solvemedia.com',
  'user-agent':'Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.70 Mobile Safari/537.36',
  'accept': '*/*',
  'sec-gpc': '1',
  'sec-fetch-site': 'cross-site',
  'sec-fetch-mode': 'no-cors',
  'sec-fetch-dest': 'script',
  'referer': 'https://earnbitmoon.club/',
  'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
  
  
}
headerssss={
  'sec-gpc':'1',
  'Host': 'earnbitmoon.club',
  'content-length': '466',
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'x-requested-with': 'XMLHttpRequest',
    'sec-fetch-site':'same-origin',
    'sec-fetch-mode':'cors',
    #'sec-fetch-user':'?1',
    'sec-fetch-dest':'empty',
    'referer':'https://earnbitmoon.club/',
    'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Mobile Safari/537.36',
    'cookie':cookie,
    }
url='https://earnbitmoon.club/'
headers1={
  "Host":"earnbitmoon.club",
  'sec-gpc':'1',
  'content-length': '19',
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'x-requested-with': 'XMLHttpRequest',
  "origin":"https://earnbitmoon.club",
  'sec-fetch-site':'same-origin',
  'referer':url,
  'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
  'upgrade-insecure-requests':'1',
  'user-agent':'Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Mobile Safari/537.36',
  'cookie':cookie,
}
headers2={
  "Host":"earnbitmoon.club",
  'sec-gpc':'1',
  'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
  'sec-fetch-site':'same-origin',
  'sec-fetch-mode':'no-cors',
  'sec-fetch-dest':'image',
  'referer':url,
  'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
  'user-agent':'Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Mobile Safari/537.36',
  'cookie':cookie,}
headers3={
  "Host":"earnbitmoon.club",
  'sec-gpc':'1',
  'content-length': '62',
  'accept': '*/*',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'x-requested-with': 'XMLHttpRequest',
  "origin":"https://earnbitmoon.club",
  'sec-fetch-site':'same-origin',
  'sec-fetch-mode':'cors',
  'sec-fetch-dest':'empty',
  'referer':url,
  'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
  'user-agent':'Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Mobile Safari/537.36',
  'cookie':cookie,
}
headers4={
  "Host":"earnbitmoon.club",
  'sec-gpc':'1',
  'content-length': '169',
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'x-requested-with': 'XMLHttpRequest',
  "origin":"https://earnbitmoon.club",
  'sec-fetch-site':'same-origin',
  "sec-fetch-dest":"empty",
  "sec-fetch-mode":"cors",
  'referer': url,
  'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
  'user-agent':'Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Mobile Safari/537.36',
  'cookie':cookie,
}
def ocr_space_file(filename, overlay=True, api_key='K88088832088957', language='eng'):
  payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               "FileType":".Auto",
               "IsCreateSearchablePDF":"false",
               "isSearchablePdfHideTextLayer":"true",
               "detectOrientation":"false",
               "isTable":"false",
               "scale":"true",
               "OCREngine":"2",
               "detectCheckbox":"false",
               "checkboxTemplate":"0",
               }
  with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          timeout=30
                          )
                          
  return r.text
ttt=1
tttt=0
a=0
while True:
  os.system('clear')
  time_now = now.strftime("%d/%m/%Y, %H:%M:%S")
  print(time_now)
  print("số lần chạy:",ttt)
  print("số lần nhận được:",tttt)
  #no fault_code
  try:
    r=requests.get(f'https://earnbitmoon.club/',headers=headers,timeout=30)
    coin=r.text.split('id="sidebarCoins">')[1].split('<')[0]
    user=r.text.split('font class="text-success">')[1].split('<')[0]
    num=r.text.split('class="text-danger"><b>')[1].split(' ')[0]
    print('username   :',user)
    print('coin       :',coin)
    print('total claim:',num,'claims')
    token=r.text.split("var token = '")[1].split("'")[0]
    if ttt==1:
      tttt=int(num)
      a=int(num)
      tttt=tttt-a
    f=open("home.txt","w")
    f.write(r.text)
    f.close()
  except:
    pass
  #no fault-code
  try:
    s=requests.get('https://api-secure.solvemedia.com/papi/_challenge.js?k=5TuPjHOPoHvCPuSfsUohIl19kOkG2877;f=_ACPuzzleUtil.callbacks%5B0%5D;l=en;t=img;s=standard;c=js,h5c,h5ct,svg,h5v,v/h264,v/webm,h5a,a/mp3,a/ogg,ua/chrome,ua/chrome103,os/android,os/android12.537,fwv/Br.2yA.wkws93,jslib/jquery,adblk,htmlplus;am=aUpWSkPIdTxv9aG1Q8h1PA;ca=ajax;ts=1657442989;ct=1657443226;th=white;r=0.03152066419806343',headers=headerss,timeout=30)
    challenge=s.text.split('"challenge":"')[1].split('"')[0]
    link='https://api-secure.solvemedia.com/papi/media?c='+challenge+';w=300;h=150;fg=000000;bg=000000'
  except:
    pass
  #no fault-code
  try:
    t=requests.get(link,headers=headerss,timeout=30)
    file = open("img.png", "wb")
    file.write(t.content)
    file.close()
    print("tải ảnh xong")
  except:
    pass
  try:
    test_file = ocr_space_file(filename='img.png', language='eng')
    code=test_file.split('"ParsedText":"')[1].split('"')[0]
    code=code.strip()
    code=code.replace("\n","")
    code=code.replace(" ","")
    print("lấy code xong:", code)
  except:
    pass
  try:
    data="a=getFaucet&token="+token+"&captcha=0&challenge="+challenge+"&response="+code
    print("data",data)
    res=requests.post('https://earnbitmoon.club/system/ajax.php',data=data,headers=headerssss,timeout=30)
    if res.status_code==200:
      aa=res.text.split('fa-fw\"><\/i> ')[1].split('<')[0]
      print(aa)
      if str(aa)!="Please confirm you're not a robot!":
        s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
        print(s2)
        tttt=int(num)-a
        print("chờ 300")
        time.sleep(280)
      elif str(aa)=="Please confirm you're not a robot!":
        print("đang giải robot")
        data="cID=0&rT=1&tM=light"
        resss=requests.post("https://earnbitmoon.club/system/libs/captcha/request.php",data=data,headers=headers1,timeout=30)
        keys=json.loads(resss.text)
        l=[]
        k=[]
        for x in keys:
          urll='https://earnbitmoon.club/system/libs/captcha/request.php?cid=0&hash='+x
          ressss=requests.get(urll,headers=headers2,timeout=30)
          l.append(len(ressss.content))
          k.append(x)
        if l[0]==l[1] and l[0]==l[2] and l[0]==l[3] and l[0]!=l[4]:
            an=4
        elif l[0]==l[1] and l[0]==l[2] and l[0]!=l[3] and l[0]==l[4]:
            an=3
        elif l[0]==l[1] and l[0]!=l[2] and l[0]==l[3] and l[0]==l[4]:
            an=2
        elif l[0]!=l[1] and l[0]==l[2] and l[0]==l[3] and l[0]==l[4]:
            an=1
        else:
            an=0
        time.sleep(20)
        data="cID=0&pC="+str(k[an])+"&rT=2"
        resssss=requests.post('https://earnbitmoon.club/system/libs/captcha/request.php',data=data,headers=headers3,timeout=30)
        data="a=proccessAntibot&token="+str(token)+"&captcha-idhf=0&captcha-hf="+str(k[an])
        ressssss=requests.post('https://earnbitmoon.club/system/ajax.php',data=data,headers=headers4,timeout=30)
        print(ressssss.text)
        time.sleep(3)
      else:
        pass
  except:
    pass
  ttt += 1