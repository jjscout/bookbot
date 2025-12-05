from collections import Counter
from typing import Dict, Union


def count_words(text):
    num_words = len(text.split())
    return num_words


def count_characters(text: str):
    return Counter(text.lower())


def sort_characters(counts: dict):
    counts = [{"char": character, "num": num} for character, num in counts.items()]

    def _sort_on(count: Dict[str, Union[str, int]]):
        return count["num"]

    counts.sort(reverse=True, key=_sort_on)
    return counts
