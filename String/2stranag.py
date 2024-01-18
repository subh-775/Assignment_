# CHECK IF ANAGRAM

def findAnagrams(s: str, p: str) -> list[int]:
    s_len, p_len = len(s), len(p)

    if s_len < p_len:
        return []

    freq_p = [0] * 26
    window = [0] * 26

    for i in range(p_len):
        freq_p[ord(p[i]) - ord('a')] += 1
        window[ord(s[i]) - ord('a')] += 1

    ans = [0] if freq_p == window else []

    for i in range(p_len, s_len):
        window[ord(s[i - p_len]) - ord('a')] -= 1
        window[ord(s[i]) - ord('a')] += 1

        if freq_p == window:
            ans.append(i - p_len + 1)

    return ans
