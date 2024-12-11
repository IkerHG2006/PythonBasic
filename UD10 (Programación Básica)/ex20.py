def binari_a_enter(binari):
    enter = 0
    for idx, bit in enumerate(reversed(binari)):
        if bit == '1':
            enter += 2 ** idx
    return enter