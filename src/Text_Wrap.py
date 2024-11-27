import textwrap

def wrap(string, max_width):
    wrapped_text = textwrap.wrap(string, width=max_width)
    txt = ""
    for wrp_txt in wrapped_text:
        # print(wrp_txt)
        txt = txt + '\n' + wrp_txt
    return txt.strip()


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
