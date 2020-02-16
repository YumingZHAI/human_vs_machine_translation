import urllib.request
import urllib.parse
import hashlib
import random
import traceback
import json
import sys

appid = 'to_be_replaced_with_your_appid'
secretKey = 'to_be_replaced_with_your_secretKey'

g = sys.argv[1]

genreName = g.lower().replace('-all', '')
results = open("bleu_files/" + genreName + "-baiduT.txt", "w")

with open("bleu_files/" + genreName + "-engSent.txt", "r") as lines:
    i = 1
    print("Baidu Translate API working.")
    for line in lines:
        # print("Translating sentence ", i)
        text = line.strip()

        httpClient = None
        myurl = '/api/trans/vip/translate'
        query = text
        fromLang = 'en'
        toLang = 'zh'
        salt = random.randint(32768, 65536)

        sign = appid + query + str(salt) + secretKey    
        m1 = hashlib.md5()   
        m1.update(sign.encode(encoding="utf-8"))
        sign = m1.hexdigest()

        myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
            query) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign

        try:
            response = urllib.request.urlopen('http://api.fanyi.baidu.com' + myurl)
            html = response.read().decode("utf-8")
            # print (html)
            jsonData = json.loads(html)
            result = jsonData["trans_result"][0]["dst"]
            mt = list(result)
            mt[:] = (value for value in mt if value != ' ')
            for c in mt:
                print(c, file=results, end=" ")
            print(file=results)
            i += 1
        except:
            traceback.print_exc()
        finally:
            if httpClient:
                httpClient.close()
results.close()

