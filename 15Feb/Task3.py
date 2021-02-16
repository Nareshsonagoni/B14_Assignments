
'''create a list of lines separated by . '''
import extras


def separate_by_fullstop(paragraph):

    separated_list = list(paragraph.split('.'))

    return separated_list


file = extras.paragraph
print(separate_by_fullstop(file))