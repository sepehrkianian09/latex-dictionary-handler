from typing import Dict
import pandas as pd


class Alphabet:
    def __init__(self) -> None:
        self.dic_alpha: Dict[str, str] = {"ب": "ب", "پ": "پ", "ت": "ت", "م": "م"}

    def get_alphabet_keys(self) -> list[str]:
        return list(self.dic_alpha.values())
    
    def get_alpha_key(self, entry: "WordEntry") -> str:
        return self.dic_alpha[entry.get_key()]


alphabet = Alphabet()

class WordEntry:
    def __init__(self, word: str, translation: str):
        self.__word = word
        self.__translation = translation

    def get_key(self):
        return self.__translation[0]

    def __get_context(self):
        return [self.__translation, self.__word]
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, list):
            return value == self.__get_context()
        return False


def df_to_context(df: "pd.DataFrame") -> "Dict[str, list]":
    context: Dict[str, list] = dict()

    def put_entry_in_context(entry: "WordEntry"):
        if entry.get_key() in alphabet.dic_alpha.keys():
            alpha_key = alphabet.get_alpha_key(entry)

            if not context.__contains__(alpha_key):
                context[alpha_key] = []
            context[alpha_key].append(entry)

    for j in df.itertuples():
        put_entry_in_context(entry=WordEntry(word=j.word, translation=j.translation))

    return context


dic_entries = df_to_context(df=pd.read_csv("template.csv"))
