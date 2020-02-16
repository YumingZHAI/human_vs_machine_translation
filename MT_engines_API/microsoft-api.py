# https://www.microsoft.com/en-us/translator/business/trial/
# https://portal.azure.com/#home    (inscription, credit card)
# https://github.com/MicrosoftTranslator/Text-Translation-API-V3-Python/blob/master/Translate.py

# key: to_be_replaced_with_your_key
# endpoint: https://api.cognitive.microsofttranslator.com
# code the key & endpoint in the file "app-env". Then "source app-env" to set the environment variable

# -*- coding: utf-8 -*-

# This simple app uses the '/translate' resource to translate text from one language to another.
# This sample runs on Python 2.7.x and Python 3.x.
# You may need to install requests and uuid.
# Run: pip install requests uuid

import os, requests, uuid, json, sys
# from pprint import pprint

key_var_name = 'MICROSOFT_KEY'
if not key_var_name in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
subscription_key = os.environ[key_var_name]

endpoint_var_name = 'MICROSOFT_END_POINT'
if not endpoint_var_name in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(endpoint_var_name))
endpoint = os.environ[endpoint_var_name]

# If you encounter any issues with the base_url or path, make sure
# that you are using the latest endpoint:
# https://docs.microsoft.com/azure/cognitive-services/translator/reference/v3-0-translate
path = '/translate?api-version=3.0'
params = '&from=en&to=zh-Hans'
constructed_url = endpoint + path + params

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

g = sys.argv[1]

genreName = g.lower().replace('-all', '')
results = open("bleu_files/"+ genreName + "-microsoftT.txt", "w")
with open("bleu_files/" + genreName + "-engSent.txt", "r") as lines:
    i = 1
    print("Microsoft Translate API working.")
    for line in lines:
        # print("Translating sentence ", i)
        text = line.strip()
        body = [{'text': text}]
        request = requests.post(constructed_url, headers=headers, json=body) 
        response = request.json()
        # print(response)
        mt = list(response[0]["translations"][0]["text"])
        mt[:] = (value for value in mt if value != ' ')
        for c in mt:
            print(c, file=results, end=" ")
        print(file=results)
        i+=1
results.close()

