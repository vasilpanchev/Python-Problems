from typing import List


def contains_all_letters(a: str, b: str) -> bool:
    for letter in a:
        if letter not in b:
            return False
    for letter in b:
        if letter not in a:
            return False
    return True


def swapped_count(a: str, b: str) -> int:
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count


def find_anagrams(s: str, p: str) -> List[int]:
    anagrams_indices = []
    if len(p) <= len(s):
        word_length = len(p)
        for i in range(len(s) - word_length + 1):
            current_substring = s[i:i + word_length]
            if contains_all_letters(current_substring, p):
                swap_count = swapped_count(current_substring, p)
                if swap_count == 0 or swap_count == 2:
                    anagrams_indices.append(i)
    return anagrams_indices


print(find_anagrams("cbaebabacd", "abc"))
# Anagrams: "cba", "bac"

print(find_anagrams("abab", "ab"))
# Anagrams: "ab", "ba", "ab"
