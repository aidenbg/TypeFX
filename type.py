from time import sleep

#Write a '^' to go to the next line
#Write a '%' to skip one line and go to the next line
#syntax = type("Whatever text you want")
def t(txt, time=None):
    txt = str(txt)
    for i in txt:
        if i == '^':
            txt.replace(i,'')
            print('', flush = True)
        elif i == '%':
            txt.replace(i,'')
            print('\n')
        else:
            if time != None:
                sleep(time)
            else:
                sleep(0.08)
            print(i, end = '')
    print('', flush = True)
