def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word in i:
            same_words.append(i)
        elif root_word.upper() in i.upper():
            same_words.append(i)
        elif root_word.lower() in i.lower():
            same_words.append(i)
    return same_words
result_1 = single_root_words('дом', 'ДомиК', 'дымный', 'домовой')
result_2 = single_root_words('город', 'гора', 'ГоРОДской', 'ПРИГОРОДНЫЙ')
print(result_1)
print(result_2)
