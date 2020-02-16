from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.bleu_score import SmoothingFunction
import sys

sf = SmoothingFunction()
genre = sys.argv[1]
genre = genre.lower().replace('-all', '')

bleu4mt = open("bleu_files/" + genre + "-bleu-4engines.txt", "w")  # all the four MT engines

print("Calculating BLEU scores for each sentence.")

with open("bleu_files/" + genre + "-human.txt", "r") as human, open("bleu_files/" + genre + "-googleT.txt", "r") as google, \
     open("bleu_files/" + genre + "-microsoftT.txt", "r") as microsoft, open("bleu_files/" + genre + "-baiduT.txt", "r") as baidu, \
     open("bleu_files/" + genre + "-tencentT.txt", "r") as tencent:
     i = 1
     for h, g, m, b, t in zip(human, google, microsoft, baidu, tencent):
         # print("Calculating BLEU scores for sentence ", i)
         i += 1
         candidate = h.strip().split(" ")
         # print(candidate)

         reference4 = []
         gt = g.strip().split(" ")
         reference4.append(gt)
         microT = m.strip().split(" ")
         reference4.append(microT)
         bt = b.strip().split(" ")
         reference4.append(bt)
         tt = t.strip().split(" ")
         reference4.append(tt)

         mt4 = sentence_bleu(reference4, candidate, smoothing_function=sf.method4)
         print(mt4, file=bleu4mt)

bleu4mt.close()

