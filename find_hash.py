"""find the hash of `MESSAGE` with different mode of
character(upper & lower) to get the hash ended with `1111`
"""
from hashlib import sha256
from random import choice
MESSAGE = 'Hi, my name is Mohammad Dori and 1167586958 is my student number.'


def get_hash(message: str) -> str:
    """get hash of message with sha256 algorithm

    Args:
        message (str): the message

    Returns:
        str: hash of message
    """
    the_hash = sha256()
    the_hash.update(message.encode('utf-8'))
    return the_hash.hexdigest()


count = 0
SEARCH = True
while SEARCH:
    count += 1
    print(count, end=" tried\r")
    new_message = ""
    for letter in MESSAGE:
        mode = choice(["upper", "lower"])
        if mode == "lower":
            new_message += letter.lower()
        else:
            new_message += letter.upper()

    message_hash = get_hash(new_message)
    if message_hash[-4:] == '1111':
        print(f'Found it! the string is \n"{new_message}"'
              f'\nand the hash is \n<{message_hash}>')
        print(f'{count} different modes were tried to find the answer!')
        SEARCH = False
