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

        dic_entries[alpha_key].append([fa, eng])