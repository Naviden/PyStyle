
import sys


def change_color(fun):
    def color(text):
        return fun(f"\033[1;32;10m{text}\033[0;37;10m ")
    return color


@change_color
def print_color(text):
    # print(text)
    return text


a = print_color('asghar memadi')
# print(f'nkjnk knkjnk kjnkjnkj {a} kjnkjnk kjbjkjk kjnk ')

# text color
# for i in range(0, 16):
#     for j in range(0, 16):
#         code = str(i * 16 + j)
#         # print(code)
#         print(f"\u001b[38;5;{code}m {code.ljust(4)}", end='')
#     print ("\u001b[0m")

# background color
# for i in range(0, 16):
#     for j in range(0, 16):
#         code = str(i * 16 + j)
#         # print(code)
#         print(f"\u001b[48;5;{code}m {code.ljust(5)}", end='')
#     print("\u001b[0m")
print('\n')
print('\u001b[1mStandard Colors\u001b[0m\n')
for j in range(0, 8):
    code = str(j)
    # print(code)
    print(f"\u001b[48;5;{code}m {code.center(8)}", end='')
print("\u001b[0m")

print('\n')
print('\u001b[1mHigh-Intensity Colors\u001b[0m\n')
for j in range(8, 16):
    code = str(j)
    # print(code)
    print(f"\u001b[48;5;{code}m {code.center(8)}", end='')
print("\u001b[0m")

print('\n')
print('\u001b[1mColors\u001b[0m\n')
for j in range(16, 52):
    code = str(j)
    print(f"\u001b[48;5;{code}m {code.ljust(3)}", end='')
print("\u001b[0m")
for j in range(52, 88):
    code = str(j)
    print(f"\u001b[48;5;{code}m {code.ljust(3)}", end='')
print("\u001b[0m")
for j in range(88, 124):
    code = str(j)
    print(f"\u001b[48;5;{code}m {code.ljust(3)}", end='')
print("\u001b[0m")
for j in range(124, 160):
    code = str(j)
    print(f"\u001b[48;5;{code}m {code.ljust(3)}", end='')
print("\u001b[0m")
for j in range(160, 196):
    code = str(j)
    print(f"\u001b[48;5;{code}m {code.ljust(3)}", end='')
print("\u001b[0m")
for j in range(196, 232):
    code = str(j)
    print(f"\u001b[48;5;{code}m {code.ljust(3)}", end='')
print("\u001b[0m")

print('\n')
print('\u001b[1mGrayscale colors\u001b[0m\n')
for j in range(232, 256):
    code = str(j)
    print(f"\u001b[48;5;{code}m {code.ljust(5)}", end='')
print("\u001b[0m")


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


# ass = text_formatter('shunbul')
# print(f'asghar memadi {ass} e maas!')
