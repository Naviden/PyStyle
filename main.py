
def color_guide():
    print('\n')
    print('\u001b[1mStandard Colors\u001b[0m\n')
    for j in range(0, 8):
        code = str(j)
        print(f"\u001b[48;5;{code}m {code.center(8)}", end='')
    print("\u001b[0m")

    print('\n')
    print('\u001b[1mHigh-Intensity Colors\u001b[0m\n')
    for j in range(8, 16):
        code = str(j)
        print(f"\u001b[48;5;{code}m {code.center(8)}", end='')
    print("\u001b[0m")

    print('\n')
    print('\u001b[1mColors\u001b[0m\n')
    for m in range(0, 6):
        for n in range(0, 36):
            code = str(m * 36 + (n + 16))
            print(f"\u001b[48;5;{code}m {code.ljust(3)}", end='')
        print("\u001b[0m")

    print('\n')
    print('\u001b[1mGrayscale colors\u001b[0m\n')
    for j in range(232, 256):
        code = str(j)
        print(f"\u001b[48;5;{code}m {code.ljust(5)}", end='')
    print("\u001b[0m")

color_guide()

def text_formatter(text, bc=82, tc=0, bold=False, underline=False, reversed=False):
    if bold:
        b = '\u001b[1m'
    else:
        b = ''
    if underline:
        u = '\u001b[4m'
    else:
        u = ''
    if reversed:
        r = '\u001b[7m'
    else:
        r = ''

    return(f'{b}{u}{r}\u001b[48;5;{bc}m\u001b[38;5;{tc}m{text}\u001b[0m')
