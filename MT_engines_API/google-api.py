# https://cloud.google.com/translate/docs/quickstart-client-libraries
# Google Cloud Translation, project billing (credit card), service account, GCPlatform
# download the private key (name_project.json)

# in each new session of shell: define the environment variable like this:  
# export GOOGLE_APPLICATION_CREDENTIALS="/path/name_project.json"

# install the package: 
# pip install --upgrade google-cloud-translate

# Imports the Google Cloud client library
# from google.cloud import translate  => AttributeError: module 'google.cloud.translate' has no attribute 'Client'
# solution: Update your samples to explicitly use the v2 version of the library if you are using the 2.0.0 library version: GoogleCloudPlatform/python-docs-samples#2498
from google.cloud import translate_v2 as translate
import sys

# Instantiates a client
translate_client = translate.Client()
# print(translate_client.get_languages())

g = sys.argv[1]

genreName = g.lower().replace('-all', '')
results = open("bleu_files/"+ genreName + "-googleT.txt", "w")
with open("bleu_files/" + genreName + "-engSent.txt", "r") as lines:
    i = 1
    print("Google Translate API working.")
    for line in lines:
        # print("Translating sentence ", i)
        text = line.strip()
        translation = translate_client.translate(text, target_language='zh')
        mt = list(translation['translatedText'])
        mt[:] = (value for value in mt if value != ' ')
        for c in mt:
            print(c, file=results, end=" ")
        print(file=results)
        i+=1
results.close()


