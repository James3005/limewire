import requests, os, time
cookie="_ga=GA1.1.1532479092.1656690580;bitmedia_fid=eyJmaWQiOiI3YjQ3YWMxOWRiYzkzYWY2NDgwZTdhNzdjMTZmNTgwYiIsImZpZG5vdWEiOiJmOTVmZDg5ZmEyNjJmZjBkYjBlYWUyOWViN2IxYTU4ZCJ9;AccExist=292239;SesHashKey=exa3app9bulb7jng;SesToken=ses_id%3D292239%26ses_key%3Dexa3app9bulb7jng;PHPSESSID=cfgnghkf70h61c9hvs0738jms4;_ga_7Z81E54NN3=GS1.1.1657004470.6.0.1657004470.0"
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
while True:
  os.system('clear')
  try:
    r=requests.get(f'https://earnbitmoon.club/',headers=headers,timeout=30)
    coin=r.text.split('id="sidebarCoins">')[1].split('<')[0]
    user=r.text.split('font class="text-success">')[1].split('<')[0]
    num=r.text.split('class="text-danger"><b>')[1].split('<')[0]
    print('username   :',user)
    print('coin       :',coin)
    print('total claim:',num)
    token=r.text.split("var token = '")[1].split("'")[0]
  except:
    break
  try:
    s=requests.get('https://api-secure.solvemedia.com/papi/_challenge.js?k=5TuPjHOPoHvCPuSfsUohIl19kOkG2877;f=_ACPuzzleUtil.callbacks%5B0%5D;l=en;t=img;s=standard;c=js,h5c,h5ct,svg,h5v,v/h264,v/webm,h5a,a/mp3,a/ogg,ua/chrome,ua/chrome103,os/android,os/android12.537,fwv/BraF.w.pdia45,jslib/jquery,htmlplus;am=9QNTJ4tgKNzztdb0i2Ao3A;ca=ajax;ts=1657004442;ct=1657004470;th=white;r=0.955937747185081',headers=headerss,timeout=30)
    challenge=s.text.split('"challenge":"')[1].split('"')[0]
    link='https://api-secure.solvemedia.com/papi/media?c='+challenge+';w=300;h=150;fg=000000;bg=000000'
  except:
    break
  try:
    t=requests.get(link,headers=headerss,timeout=30)
    file = open("img.png", "wb")
    file.write(t.content)
    file.close()
    print("tải ảnh xong")
  except:
    break
  try:
    test_file = ocr_space_file(filename='img.png', language='eng')
    code=test_file.split('"ParsedText":"')[1].split('"')[0]
    code=code.strip()
    code=code.replace(" ","")
    print("lấy code xong")
  except:
    break
  try:
    data="a=getFaucet&token="+token+"&captcha=0&challenge="+challenge+"&response="+code
    res=requests.post('https://earnbitmoon.club/system/ajax.php',data=data,headers=headerssss,timeout=30)
    if res.status_code==200:
      print(res.text.split('fa-fw\\"><\\/i>')[1].split('<')[0])
      for i in range(300):
        ii=300-i
        print('username   :',user)
        print('coin       :',coin)
        print('total claim:',num)
        print("wait :",ii,"s")
        os.system('clear')
        time.sleep(1)
  except:
    print(res.text.split('fa-fw\\"><\\/i>')[1].split('<')[0])
    break