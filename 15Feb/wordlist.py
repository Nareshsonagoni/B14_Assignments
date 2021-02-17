
'''create a list of lines separated by . '''
import extras


def separate_by_fullstop(paragraph):

    separated_list = list(paragraph.split('.'))

    return separated_list


file = extras.paragraph
file2 = separate_by_fullstop(file)
# print(len(file2))