def read_words():
    words_file = open('./words_5.txt', 'r')
    words = []

    for word in words_file.readlines():
        words.append(word[0:5])

    return words
