# -*- coding: utf-8 -*-

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tmt.v20180321 import tmt_client, models
import json, re, sys

g = sys.argv[1]

genreName = g.lower().replace('-all', '')
results = open("bleu_files/"+ genreName + "-tencentT.txt", "w")
with open("bleu_files/" + genreName + "-engSent.txt", "r") as lines:
    i = 1
    print("Tencent Translate API working.")
    for line in lines:
        # print("Translating sentence ", i)
        text = line.strip()
        try:
            cred = credential.Credential("to_be_replaced_with_your_secretId", "to_be_replaced_with_your_secretKey")
            httpProfile = HttpProfile()
            httpProfile.endpoint = "tmt.tencentcloudapi.com"

            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile
            client = tmt_client.TmtClient(cred, "ap-shanghai", clientProfile)

            req = models.TextTranslateRequest()
            text = re.sub('"', '\\"', text)
            params = '{"SourceText":"' + text + '", "Source":"en", "Target":"zh", "ProjectId":to_be_replaced_with_your_projectId}'

            req.from_json_string(params)

            resp = client.TextTranslate(req)
            a = resp.to_json_string()     

            mt = list(json.loads(a)["TargetText"])
            mt[:] = (value for value in mt if value != ' ')
            for c in mt:
                print(c, file=results, end=" ")
            print(file=results)
            i += 1
        except TencentCloudSDKException as err:
            print(err)
results.close()






