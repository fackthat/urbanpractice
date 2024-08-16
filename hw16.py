def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if i.lower() in root_word or root_word.lower() in i.lower():
            same_words.append(i)
    return same_words

result = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result)
print(result2)