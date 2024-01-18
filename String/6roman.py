def romanToInt(s: str) -> int:
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    i = 0

    while i < len(s):
        if i + 1 < len(s) and s[i:i+2] in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
            result += roman_dict[s[i+1]] - roman_dict[s[i]]
            i += 2
        else:
            result += roman_dict[s[i]]
            i += 1

    return result
