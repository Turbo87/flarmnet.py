def decrypt(input):
    characters = []
    for i in xrange(0, len(input), 2):
        ascii = int(input[i:i + 2], 16)
        characters.append(chr(ascii))

    output = ''.join(characters).strip()
    if len(output) == 0:
        return None

    return output.decode('iso-8859-1')
