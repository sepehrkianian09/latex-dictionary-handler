from ast import List
from typing import Dict
import pandas as pd

from custom_io import JSONCustomSerializable


import icu
collator = icu.Collator.createInstance(icu.Locale('fa_IR'))


class WordEntry(JSONCustomSerializable):
    def __init__(self, word: str, translation: str):
        self.word = word
        self.translation = translation

    def get_key(self):
        return self.translation[0]

    def to_dict(self):
        return {
            'word': self.word,
            'translation': self.translation
        }

    def __eq__(self, value: object) -> bool:
        if isinstance(value, dict):
            return value == self.to_dict()
        return False
    
    def sorting_key(self):
        return collator.getSortKey(self.translation.replace("آ", "ا"))
    
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
        for entry in sorted(entries, key=WordEntry.sorting_key):
            str_item += f"\\dic{{{entry.word}}}{{{entry.translation}}}\n"
        return str_item

    def to_latex(self, context: "Dict[str, list[WordEntry]]") -> str:
        def get_context_item_key(context_item):
            return collator.getSortKey(context_item[0])
        return "\n".join(
            [self.alphakey_to_latex(key, entries) for key, entries in sorted(context.items(), key=get_context_item_key)]
        )


def context_total_len(context: "Dict[str, list[WordEntry]]") -> int:
    return sum([len(entries) for entries in context.values()])

dic_entries = Alphabet().df_to_context(df=pd.read_csv("template.csv"))
latex_out = LatexFormattingVisitor().to_latex(dic_entries)

with open("latex.out", "w", encoding="utf-8") as f:
    f.write(latex_out)