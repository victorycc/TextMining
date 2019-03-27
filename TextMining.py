
#方法1
# with open("./DataCleaning/beefnoodle_res_diary.txt", "r", encoding="utf-8") as f:
#     article = f.read()
#
# import jieba
# # 準備詞庫
# jieba.load_userdict("dict.txt.big")
#
# # 若斷詞過後，與我們想要的詞有些微出入，可自行創建詞庫。
# jieba.load_userdict("food_dict.txt")
# print(" ".join( jieba.cut(article) ) )
#
# # 抓關鍵詞方法(3)
# from jieba.analyse import extract_tags
# jieba.analyse.set_stop_words("stop_words.txt")
# print(extract_tags(article, 10))


#方法2
import jieba
from jieba.analyse import extract_tags
import glob

import pandas as pd
df = pd.DataFrame(columns=["Context"])

for cut_word in glob.glob("DataCleaning/*.txt"):
    print("Now, we process the file is : ", cut_word)

    # 讀取DataCleaning資料夾的所有檔案，並且斷詞。
    with open(cut_word, "r", encoding ="utf-8") as f:
        article = f.read()
        # 準備詞庫
        jieba.load_userdict("dict.txt.big")

        # 若斷詞過後，與我們想要的詞有些微出入，可自行創建詞庫。
        jieba.load_userdict("food_dict.txt")


# 計算關鍵詞時，若有出現我們、和、的...等無關簡要的關鍵詞，則這些詞需建立在stop_words.txt，讓程式自動忽略，
# 以利後續的資料分析。

        jieba.analyse.set_stop_words("stop_words.txt")

        word_cut = " ".join(jieba.cut(article))
        print(word_cut)
        print(extract_tags(article, 10))
        print("\n")

    # 做好的斷詞寫進去檔案
    with open("result.txt", "w", encoding="utf-8") as f2:
        newfile = f2.write(word_cut)
        print("This section is written to the file.")

print("All Done~~")
