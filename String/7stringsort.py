from collections import Counter
def frequencySort(s: str) -> str:
    freq_dict = Counter(s)
    sorted_counts = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))
    out = ""
    for letr, count in sorted_counts:
        temp_str = f"{letr}"*count
        out+=temp_str
    return out

s = "loveleetcode"
print(frequencySort(s))