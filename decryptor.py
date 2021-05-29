def get_charmap():
    charmap = {
        1: '⎋', 2: '1', 3: '2', 4: '3', 5: '4', 6: '5', 7: '6', 8: '7', 9: '8',
        10: '9', 11: '0', 12: '-', 13: '=', 14: '⌫', 15: '⇥', 16: 'q', 17: 'w',
        18: 'e', 19: 'r', 20: 't', 21: 'y', 22: 'u', 23: 'i', 24: 'o', 25: 'p',
        26: '[', 27: ']', 28: '⏎', 29: '⌃', 30: 'a', 31: 's', 32: 'd', 33: 'f',
        34: 'g', 35: 'h', 36: 'j', 37: 'k', 38: 'l', 39: ';', 40: '\'', 41: '`',
        42: '⇧', 43: '#', 44: 'z', 45: 'x', 46: 'c', 47: 'v', 48: 'b', 49: 'n',
        50: 'm', 51: ',', 52: '.', 53: '/', 54: '⇧', 55: '<?>', 56: '⌥', 57: '␣',
        58: '⇪', 59: '<?>', 60: '<?>', 86: '\\', 100: '⌥', 101: '<?>', 102: '<?>',
        103: '↑', 104: '<?>', 105: '←', 106: '→', 107: '<?>', 108: '↓', 109: '<?>',
        110: '<?>', 111: '⌦', 112: '<?>', 112: '<?>', 113: '<?>', 114: '<?>', 115: '<?>',
        116: '<?>', 117: '<?>', 118: '<?>', 119: '<?>', 120: '<?>', 121: '<?>', 122: '<?>',
        123: '<?>', 124: '<?>', 125: '⌘'
    }
    return charmap


def decrypt(charArr: list):
    encoded_chars = charArr
    decoded_chars = []
    c_map = get_charmap()
    for i in encoded_chars:
        decoded_chars.append(c_map.get(i, '<?>'))
    text = "".join(decoded_chars)
    return text


def decryp2r(charArr: list):
    alphanumerics = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w',
                     'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's','d', 'f',
					 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    encoded_chars = charArr
    decoded_chars = []
    c_map = get_charmap()
    for i in encoded_chars:
        char_in_question = c_map.get(i, '<?>')
        if char_in_question in alphanumerics:
            decoded_chars.append(char_in_question)
        else:
            if len(decoded_chars) != 0:
                if decoded_chars[-1] != ' ':
                    decoded_chars.append(' ')
    text = "".join(decoded_chars)
    return text
