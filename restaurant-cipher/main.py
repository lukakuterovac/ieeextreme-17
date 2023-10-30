def get_max_value_key(dict):
    max_value = 0
    max_key = ""
    for key, value in dict.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key


n = int(input())
for i in range(n):
    letters = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0}
    sentence = input()
    for letter in sentence:
        if letter.upper() in letters.keys():
            letters[letter.upper()] += 1
    print(get_max_value_key(letters))
