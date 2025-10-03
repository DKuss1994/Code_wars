def reverse_words(txt):
    list_txt = txt.split(" ")
    reserve_list = []
    new_txt = ""
    for reserve in list_txt:
        reserve_word = reserve[::-1]
        reserve_list.append(reserve_word)
    for reserve_txt in reserve_list:


            new_txt += reserve_txt + " "
    if txt[-1] != " ":
        return new_txt[:-1]
    else:
        return new_txt


