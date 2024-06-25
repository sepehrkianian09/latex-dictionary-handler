from typing import Dict
import pandas as pd

dic_alpha: Dict[str, str] = {"ب": "ب", "پ": "پ", "ت": "ت", "م": "م"}


alpha: list[str] = list(dic_alpha.values())

def df_to_context(df: "pd.DataFrame") -> "Dict[str, list]":
    context: Dict[str, list] = dict()
    for i in alpha:
        context[i] = []

    for j in df.itertuples():
        eng: str = j.word
        fa: str = j.translation
        
        def get_key():
            return fa[0]
        
        def get_jj():
            return [fa, eng]

        if get_key() in dic_alpha.keys():
            alpha_key = dic_alpha[get_key()]

            context[alpha_key].append(get_jj())

    return context


dic_entries = df_to_context(df=pd.read_csv("template.csv"))
