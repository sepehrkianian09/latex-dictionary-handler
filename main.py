from ast import List
from typing import Dict
import pandas as pd


class WordEntry:
    def __init__(self, word: str, translation: str):
        self.word = word
        self.translation = translation

    def get_key(self):
        return self.translation[0]

    def __get_context(self):
        return [self.translation, self.word]

    def __eq__(self, value: object) -> bool:
        if isinstance(value, list):
            return value == self.__get_context()
        return False
    
    def __repr__(self) -> str:
        return f"{self.word}||{self.translation}"


class Alphabet:
    def __init__(self) -> None:
        pass

    def get_alpha_key(self, entry: "WordEntry") -> str:
        if entry.get_key() in ["ا", "آ"]:
            return "الف"
        return entry.get_key()

    def put_entry_in_context(self, context: Dict[str, list], entry: "WordEntry"):
        alpha_key = self.get_alpha_key(entry)

        if not context.__contains__(alpha_key):
            context[alpha_key] = []
        context[alpha_key].append(entry)

    def df_to_context(self, df: "pd.DataFrame") -> "Dict[str, list]":
        context: Dict[str, list] = dict()

        for j in df.itertuples():
            entry = WordEntry(word=j.word, translation=j.translation)

            self.put_entry_in_context(
                context=context,
                entry=entry,
            )

        return context


class LatexFormattingVisitor:
    def __init__(self) -> None:
        pass

    def alphakey_to_latex(self, alpha_key: str, entries: "list[WordEntry]") -> str:
        str_item = ""
        str_item += f"\\dicalphabet{{{alpha_key}}}\n"
        for entry in entries:
            str_item += f"\\dic{{{entry.word}}}{{{entry.translation}}}\n"
        return str_item

    def to_latex(self, context: "Dict[str, list[WordEntry]]") -> str:
        return "\n".join(
            [self.alphakey_to_latex(key, entries) for key, entries in context.items()]
        )


def context_total_len(context: "Dict[str, list[WordEntry]]") -> int:
    return sum([len(entries) for entries in context.values()])

dic_entries = Alphabet().df_to_context(df=pd.read_csv("template.csv"))
latex_out = LatexFormattingVisitor().to_latex(dic_entries)
