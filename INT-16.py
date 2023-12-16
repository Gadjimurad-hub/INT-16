def title(text):
    string = ''
    for i in range(len(text)):
        if i == 0 and text[i] != ' ':
            string += text[i].upper()
        elif text[i] not in '0123456789' and text[i - 1] == ' ':
            string += text[i].upper()
        else:
            string += text[i]
    print(string)


inpstr = "тесТОвое задание   для pt"
title(inpstr)
