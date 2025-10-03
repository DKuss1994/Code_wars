# Reverse words (7 kyu)


# Sprache: Python
# Datum: 2025-10-03

# Complete the function that accepts a string parameter,
# and reverses each word in the string. All spaces in the string should be retained.

def reverse_words(txt):
    list_txt = txt.split(" ")
    reserve_list = []
    new_txt = ""
    list_txt = txt.split(" ")
    for reserve in list_txt:
        reserve_word = reserve[::-1]
        reserve_list.append(reserve_word)
    for reserve_txt in reserve_list:
        new_txt += reserve_txt + " "
    return new_txt[:-1]


