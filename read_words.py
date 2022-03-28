def read_words(file_name):
    words_file = open(file_name, 'r')
    words = []

    for word in words_file.readlines():
        words.append(word[0:5])

    return words
