def sort_word(word):
    char_count = [0] * 256
    for char in word:
        char_count[ord(char)] += 1

    for i in range(1, 256):
        char_count[i] += char_count[i-1]

    result = [None] * len(word)
    for char in word:
        result[char_count[ord(char)] - 1] = char
        char_count[ord(char)] -= 1

    return ''.join(result)


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return (first_string, second_string, False)

    first_string = first_string.lower().replace(" ", "")
    second_string = second_string.lower().replace(" ", "")

    first_string_sorted = sort_word(first_string)
    second_string_sorted = sort_word(second_string)

    if first_string_sorted == second_string_sorted:
        return (first_string_sorted, second_string_sorted, True)
    else:
        return (first_string_sorted, second_string_sorted, False)
