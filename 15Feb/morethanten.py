
''' Extract the list of words that contains more than 10 words'''

import wordlist


array = wordlist.file2


def words_count(arr):
    nxt = []
    for item in arr:
        nw = item.split()
        nxt.append(nw)

    out_put = []
    len_words = []
    for lines in nxt:
        out_put.append(lines)
        len_words.append(len(lines))

    more_ten = []
    for i, v in enumerate(out_put):
        more_ten.append([])
        for word in v:
            if len(word) >= 10:
                more_ten[i].append(word)

    return more_ten


print(words_count(array))