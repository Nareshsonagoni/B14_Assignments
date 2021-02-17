
''' create an array with count of words from each in paragraph'''

import wordlist


array = wordlist.file2


def words_count(arr):
    nxt = []
    for item in arr:
        nw = item.split()
        nxt.append(nw)

    out_put = []
    for line in nxt:
        out_put.append(len(line))

    return out_put

print(words_count(array))