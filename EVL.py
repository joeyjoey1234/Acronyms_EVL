import random
import time





## seperate everything im lazy
#def process(x):
#   e_word = open('C:\\Users\\LEET\\Downloads\\Temp\\e.txt', 'a')
#   v_word = open('C:\\Users\\LEET\\Downloads\\Temp\\v.txt', 'a')
#   l_word = open('C:\\Users\\LEET\\Downloads\\Temp\\l.txt', 'a')
#    if 'e' in x[0]:
#        e_word.write(x)
#    elif 'v' in x[0]:
#        v_word.write(x)
#    elif 'l' in x[0]:
#        l_word.write(x)
#    else:
#        pass

### all the words
#f = open('C:\\Users\\LEET\\Downloads\\Temp\\words.txt','a')

#while True:
#    line = ''
#    while len(line) == 0 or line[-1] != '\n':
#        tail = f.readline()
#        if tail == '':
#            time.sleep(0.2)
#            continue
#        line += tail
#    process(line)



evl_file = open('C:\\Users\\LEET\\Downloads\\Temp\\evl.txt','a')

def process():
    while True:
        evl = ['','','']
        ## the below loads the whole file into mem, not a good idea for low mem systems
        e_word = random.choice(open('C:\\Users\\LEET\\Downloads\\Temp\\e.txt').readlines())
        v_word = random.choice(open('C:\\Users\\LEET\\Downloads\\Temp\\v.txt').readlines())
        l_word = random.choice(open('C:\\Users\\LEET\\Downloads\\Temp\\l.txt').readlines())
        evl[0] = e_word.strip('\n')
        evl[1] = v_word.strip('\n')
        evl[2] = l_word.strip('\n')
        good = ", ".join(evl)
        print(good + '\n')
        evl_file.write(good + '\n')

process()








