file = open('words_fr.txt', 'r')

words = []
for line in file :
    words.append(line.rstrip('\n'))

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

