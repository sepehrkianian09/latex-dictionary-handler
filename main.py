from typing import Dict
import pandas as pd

dic_alpha: Dict[str, str] = {"ب": "ب", "پ": "پ", "ت": "ت", "م": "م"}


alpha: list[str] = list(dic_alpha.values())
dic_entries: Dict[str, list] = dict()
for i in alpha:
    dic_entries[i] = []


jj = pd.read_csv("template.csv")

for j in jj.itertuples():
    eng = j.word
    fa = j.translation
    key = fa[0]
    if key in dic_alpha.keys():
        alpha_key = dic_alpha[key]

        dic_entries[alpha_key].append((fa, eng))


import json

with open("convert.json", "a+") as convert_file:
    # new_dic_entries = json.loads(convert_file.read())
    # assert new_dic_entries == dic_entries
    convert_file.write(json.dumps(dic_entries))
