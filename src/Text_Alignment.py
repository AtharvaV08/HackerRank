# width = 9
# print('H'.ljust(width, '-'))
# print('HackerRank'.rjust(width, '-'))

# + "               " + "HHHHH"

def getnCharacters(length):
    character = ''
    for i_width in range(0, length):
        character = character + 'H'
    return character


if __name__ == '__main__':
    height = int(input())
    width = height * 2 - 1
    char_width = 1
    print('H'.center(width, ' '))
    for line_no in range(1, height):
        char_width = char_width + 2
        chars = getnCharacters(char_width)
        print(chars.center(width, ' '))
    pillar_width = height
    char_width = 5
    for line in range(0, pillar_width + 1):
        l_pillar = "  " + getnCharacters(char_width)
        r_pillar = "               " + getnCharacters(char_width)
        pillars = l_pillar.ljust(pillar_width, ' ') + r_pillar.rjust(pillar_width, ' ')
        print(pillars)
    letter = 'H'
    mid_pillar_height = 3
    mid_line_length = 25
    for mid_line in range(0, mid_pillar_height):
        lines = getnCharacters(mid_line_length)
        print("  "+lines)
    pillar_width = height
    char_width = 5
    for line in range(0, pillar_width + 1):
        l_pillar = "  " + getnCharacters(char_width)
        r_pillar = "               " + getnCharacters(char_width)
        pillars = l_pillar.ljust(pillar_width, ' ') + r_pillar.rjust(pillar_width, ' ')
        print(pillars)
    # height = int(input())
    # width = height * 2 - 1
    # char_width = 1
    # print('H'.center(width, ' '))
    width = height * 2 - 1
    char_width = 11
    for line_no in range(height, 0, -1):
        char_width = char_width - 2
        chars = getnCharacters(char_width)
        print("                   "+chars.center(width, ' '))












  # HHHHH               HHHHH
