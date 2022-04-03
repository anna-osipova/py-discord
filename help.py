def split(word):
    return [char for char in word]

# ????? include:abc exclude:de

def get_message(suggestions):
    if len(suggestions) > 0:
       return ', '.join(suggestions)
    else:
        return 'No matches'

def give_help(words, message, separation_symbol):
    results = []
    parts = [x.strip() for x in message.split()]

    pattern = next(x for x in parts if len(x) == 5)
    include = split(next(x for x in parts if x[0:7] == 'include')[8:])
    exclude = split(next(x for x in parts if x[0:7] == 'exclude')[8:])

    for word in words:
        matches = True
        split_word = split(word)

        for i, _ in enumerate(pattern):
            if pattern[i] != separation_symbol and pattern[i] != word[i]:
                matches = False
                continue

        for letter in include:
            if not letter in split_word:
                matches = False

        for letter in exclude:
            if letter in split_word:
                matches = False

        results.append(word) if matches else None

    return get_message(results)
