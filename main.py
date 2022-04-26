file = open('words_en.txt', 'r')
words = []
for line in file :
    words.append(line.rstrip('\n'))

"""FIND WORDS OF A SPECIFIC LENGTH"""

def length(number):
    totallist = []
    for word in words:
            w = list(word.lower())
            if len(w) == number :
                        totallist.append(word)
    return totallist

"""FIND WORDS STARTING BY"""

def starts_w(string):
    startlist = []
    s = list(string.lower())    # the .lower() helps avoiding lettercase problems
    
    for word in words:
        w = list(word.lower())
        verif = []
        if len(s) <= len(w):
            for i in range(len(s)):
                if s[i] == w[i] : verif.append(True)
                else : verif.append(False)
            if not False in verif:
                startlist.append(word)
    
    return startlist

def starts_w_nb(string,number):
    startlist = []
    s = list(string.lower())
    
    for word in words:
        w = list(word.lower())
        verif = []
        if len(w) == number :
            if len(s) <= len(w):
                for i in range(len(s)):
                    if s[i] == w[i] : verif.append(True)
                    else : verif.append(False)
                if not False in verif:
                    startlist.append(word)
    
    return startlist

"""FIND WORDS ENDING BY"""

def ends_w(string):
    endlist = []
    s = list(string.lower())

    for word in words:
        w = list(word.lower())
        verif = []
        if len(s) <= len(w):
            for i in range(1,len(s)+1):
                if s[-i] == w[-i] : verif.append(True)
                else : verif.append(False)
            if not False in verif:
                endlist.append(word)

    return endlist

def ends_w_nb(string,number):
    endlist = []
    s = list(string.lower())

    for word in words:
        w = list(word.lower())
        verif = []
        if len(w) == number :
            if len(s) <= len(w):
                for i in range(1,len(s)+1):
                    if s[-i] == w[-i] : verif.append(True)
                    else : verif.append(False)
                if not False in verif:
                    endlist.append(word)

    return endlist

"""FIND WORDS STARTING AND ENDING BY"""

def starts_n_ends(string1,string2):
    s_list = []
    se_list = []
    s1 = list(string1.lower())
    s2 = list(string2.lower())

    for word in words:
        w = list(word.lower())
        verif = []
        if len(s1)+len(s2) <= len(w):
            for i in range(len(s1)):
                if s1[i] == w[i] : verif.append(True)
                else : verif.append(False)
            if not False in verif:
                s_list.append(word)

    for word in s_list:
        w = list(word.lower())
        verif = []
        for i in range(1,len(s2)+1):
            if s2[-i] == w[-i] : verif.append(True)
            else : verif.append(False)
        if not False in verif:
            se_list.append(word)
    
    return se_list

def starts_n_ends_nb(string1,string2,number):
    s_list = []
    se_list = []
    s1 = list(string1.lower())
    s2 = list(string2.lower())
    if number >= len(s1) + len(s2):
        for word in words:
            w = list(word.lower())
            verif = []
            if len(w) == number :
                if len(s1)+len(s2) <= len(w):
                    for i in range(len(s1)):
                        if s1[i] == w[i] : verif.append(True)
                        else : verif.append(False)
                    if not False in verif:
                        s_list.append(word)

        for word in s_list:
            w = list(word.lower())
            verif = []
            for i in range(1,len(s2)+1):
                if s2[-i] == w[-i] : verif.append(True)
                else : verif.append(False)
            if not False in verif:
                se_list.append(word)
        
        return se_list
    
    else : raise ValueError('Specified word length too small.')

"""LOOK FOR LETTERS IN A WORD"""

def is_there(letter) :
    totallist = []
    for word in words:
            w = list(word.lower())
            if letter in w :
                        totallist.append(word)
    return totallist

def is_there_nb(letter,number):
    totallist = []
    for word in words:
            w = list(word.lower())
            if len(w) == number :
                if letter in w :
                            totallist.append(word)
    return totallist

def is_there_starts_nb(string,tup,nb) :
    totallist = []
    s_list = starts_w_nb(string,nb)
    for word in s_list :
        w = list(word.lower())
        verif = []
        for letter in tup :
            if letter in w : verif.append(True)
            else : verif.append(False)
        if False in verif : pass
        else : totallist.append(word)
    return totallist

def is_there_spec(letter,nb) :
    totallist = []
    for word in words:
            w = list(word.lower())
            if w[nb-1] == letter :
                        totallist.append(word)
    return totallist

def is_there_spec_nb(letter,nb1,nb2) :
    totallist = []
    for word in words:
            w = list(word.lower())
            if len(w) == nb2 :
                if w[nb1-1] == letter :
                            totallist.append(word)
    return totallist
