def count_vowels(s):
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count