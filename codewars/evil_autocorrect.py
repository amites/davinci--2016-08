import re


def autocorrect(input):
    return re.sub('(?<!\w)(you|u)+(?!\w)', 'your sister', input, flags=re.IGNORECASE)