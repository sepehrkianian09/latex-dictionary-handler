from typing import Dict
import pandas as pd

dic_alpha: Dict[str, str] = {"ب": "ب", "پ": "پ", "ت": "ت", "م": "م"}


alpha: list[str] = list(dic_alpha.values())


class WordEntry:
    def __init__(self, word: str, translation: str):
        self.__word = word
        self.__translation = translation

    def get_key(self):
        return self.__translation[0]

    def get_context(self):
        return [self.__translation, self.__word]


def df_to_context(df: "pd.DataFrame") -> "Dict[str, list]":
    context: Dict[str, list] = dict()
    for i in alpha:
        context[i] = []

    for j in df.itertuples():
        word_entry = WordEntry(word=j.word, translation=j.translation)

        if word_entry.get_key() in dic_alpha.keys():
            alpha_key = dic_alpha[word_entry.get_key()]

            context[alpha_key].append(word_entry.get_context())

    return context


dic_entries = df_to_context(df=pd.read_csv("template.csv"))
