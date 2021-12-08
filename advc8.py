import numpy as np
import time
from funcy import print_calls

disp = {}
disp[0] = "abcefg"
disp[6] = "abdefg"
disp[9] = "abcdfg"

disp[2] = "acdeg"
disp[3] = "acdfg"
disp[5] = "abdfg"

disp[1] = "cf"
disp[4] = "bcdf"
disp[7] = "acf"
disp[8] = "abcdefg"

map = {}
#returs the digit that maps to the segment string above "disp"
def check_digit(s):
    global disp
    if disp[0] == ''.join(sorted(s)):
        return 0
    elif disp[1] == ''.join(sorted(s)):
        return 1
    elif disp[2] == ''.join(sorted(s)):
        return 2
    elif disp[3] == ''.join(sorted(s)):
        return 3
    elif disp[4] == ''.join(sorted(s)):
        return 4
    elif disp[5] == ''.join(sorted(s)):
        return 5
    elif disp[6] == ''.join(sorted(s)):
        return 6
    elif disp[7] == ''.join(sorted(s)):
        return 7
    elif disp[8] == ''.join(sorted(s)):
        return 8
    elif disp[9] == ''.join(sorted(s)):
        return 9
    else:
        return None

def translate(inputs):
    global disp
    #print(inputs)
    six_words = []
    five_words = []
    tmp = inputs[0].split(' ')
    for j in tmp:
        if len(j) == 2:
            one = j
        if len(j) == 3:
            seven = j
        if len(j) == 4:
            four = j
        if len(j) == 6:
            six_words.append(j)
        if len(j) == 5:
            five_words.append(j)

    #7 - 1 gives a
    for item in seven:
        if item not in one:
            a = item
            break
    #print("a mapped to: " + a)
    map[a] = 'a'

    #all four letters of 4 are present in 9
    #Go through all items in 6word list and pull out 9
    count = 0
    nine = ''
    if (nine == ''):
        for l in four:
            if l in six_words[0]:
                count = count + 1
            if (count == 4):
                nine = six_words[0] 
                six_words.remove(nine)

    if (nine == ''):
        count = 0
        for l in four:
            if l in six_words[1]:
                count = count + 1
            if (count == 4):
                nine = six_words[1] 
                six_words.remove(nine)

    if (nine == ''):
        count = 0
        for l in four:
            if l in six_words[2]:
                count = count + 1
            if (count == 4):
                nine = six_words[2] 
                six_words.remove(nine)
    #print(nine)

    #9 - 4 will give a and g
    g = nine
    #Remove 4 from 9
    for item in four:
        g = g.replace(item,'')
    #Remove a, that should give you g
    g = g.replace(a,'')
    #print("g mapped to: "+g)
    map[g] = 'g'

    #Among 5 segment dights, three is the only digit that has a 1 in it
    for item in five_words:
        if (set(one) < set(item)):
            three = item
            five_words.remove(three)
            break

    #From 3, you can get d by removing 1, a and g
    d = three
    d = d.replace(a,'')
    d = d.replace(g,'')
    for item in one:
        d = d.replace(item,'')
    #print("d mapped to: "+d)
    map[d] = 'd'

    #4 -d -1 will give b
    b = four
    b = b.replace(d,'')
    for item in one:
        b = b.replace(item,'')
    #print("b mapped to: "+b)
    map[b] = 'b'

    #Now, 0 is the only digit that has a 1 as subset
    #and the other one has to be 6
    for item in six_words:
        if (set(one) < set(item)):
            zero = item
        else:
            six = item

    e = zero
    e = e.replace(g,'')
    e = e.replace(a,'')
    e = e.replace(b,'')
    for item in one:
        e = e.replace(item,'')
    #print("e mapped to: "+e)
    map[e] = 'e'

    for item in three:
        if item not in six:
            c = item
    #print("c mapped to: "+c)
    map[c] = 'c'

    one = one.replace(c,'')
    f = one[0]
    #print("f mapped to: "+f)
    map[f] = 'f'

    #Now we have created a complete map of letters
    #print(map)
    result = ''

    tmp = inputs[1].split(' ')
    for j in tmp:
        t = ''
        #Create the original display by mapping it back
        for l in range(len(j)):
            t = t + map[j[l]]
        #print('Checking ' + j + ' :' + t)
        result = result + str(check_digit(t))
    return result

#for i in lst:
#    translate(i)    
start_time = time.time()
with open("advc8.txt") as fin:
    data = [i.strip() for i in fin]

total = 0
for i in data:
    total = total + int(translate(i.split(' | ')))
print(total)
print("--- %s seconds ---" % (time.time() - start_time))

    