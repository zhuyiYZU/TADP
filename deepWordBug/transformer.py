# -*- coding: utf-8 -*-
import sys

import numpy as np

def swap(wordid,word_index,index2word,top_words=20000):
    word = index2word[wordid]
    if len(word)!=1:
        s = np.random.randint(0,len(word)-1)
        cword = word[:s] + word[s+1] + word[s] + word[s+2:]
        if cword in word_index:
            wid = word_index[cword] + 3
            if wid>=top_words:
                wid = 2
        else:
            wid = 2
    else:
        cword = word
        if cword in word_index:
            wid = word_index[cword] + 3
            if wid>=top_words:
                wid = 2
        else:
            wid = 2
    return (cword,wid)
    
def flip(wordid,word_index,index2word,top_words=20000):
    word = index2word[wordid]
    s = np.random.randint(0,len(word))
    # cword = word[:s] + chr(97+np.random.randint(0,26)) + word[s+1:]
    letter = ord(word[s])
    rletter = np.random.randint(0,25)+97
    if rletter >= letter:
        rletter += 1
    cword = word[:s] + chr(rletter) + word[s+1:]
    if cword in word_index:
        wid = word_index[cword] + 3
        if wid >= top_words:
            wid = 2
    else:
        wid = 2
    return (cword,wid)

def f2(wordid,word_index,index2word,top_words=20000):
    word = index2word[wordid]
    s = np.random.randint(0,len(word))
    letter = ord(word[s])
    rletter = np.random.randint(0,25)+97
    if rletter >= letter:
        rletter += 1
    cword = word[:s] + chr(rletter) + word[s+1:]
    if len(word)>1:
        s2 = np.random.randint(0,len(word)-1)
        if s2>=s:
            s2+=1
        letter = ord(word[s2])
        rletter = np.random.randint(0,25)+97
        if rletter >= letter:
            rletter += 1
        cword = cword[:s2] + chr(rletter) + cword[s2+1:]
    if cword in word_index:
        wid = word_index[cword] + 3
        if wid>=top_words:
            wid = 2
    else:
        wid = 2
    return (cword,wid)
    
def remove(wordid,word_index,index2word,top_words=20000):
    word = index2word[wordid]
    s = np.random.randint(0,len(word))
    if len(word)>1:
        cword = word[:s] + word[s+1:]
    else:
        cword = word
    if cword in word_index:
        wid = word_index[cword] + 3
        if wid>=top_words:
            wid = 2
    else:
        wid = 2
    return (cword,wid)

def remove2(wordid,word_index,index2word,top_words=20000):
    word = index2word[wordid]
    s = np.random.randint(0,len(word))
    if len(word)>1:
        cword = word[:s] + word[s+1:]
    else:
        cword = word
    if len(cword)>1:
        s = np.random.randint(0,len(cword))
        cword = cword[:s] + cword[s+1:]
    if cword in word_index:
        wid = word_index[cword] + 3
        if wid>=top_words:
            wid = 2
    else:
        wid = 2
    return (cword,wid)
    
def insert(wordid,word_index,index2word,top_words=20000):
    word = index2word[wordid]
    s = np.random.randint(0,len(word)+1)
    cword = word[:s] + chr(97+np.random.randint(0,26)) + word[s:]
    if cword in word_index:
        wid = word_index[cword] + 3
        if wid>=top_words:
            wid = 2
    else:
        wid = 2
    return (cword,wid)

homos = {'-':'˗','9':'৭','8':'Ȣ','7':'𝟕','6':'б','5':'Ƽ','4':'Ꮞ','3':'Ʒ','2':'ᒿ','1':'l','0':'O',"'":'`','a': 'ɑ', 'b': 'Ь', 'c': 'ϲ', 'd': 'ԁ', 'e': 'е', 'f': '𝚏', 'g': 'ɡ', 'h': 'հ', 'i': 'і', 'j': 'ϳ', 'k': '𝒌', 'l': 'ⅼ', 'm': 'ｍ', 'n': 'ո', 'o':'о', 'p': 'р', 'q': 'ԛ', 'r': 'ⲅ', 's': 'ѕ', 't': '𝚝', 'u': 'ս', 'v': 'ѵ', 'w': 'ԝ', 'x': '×', 'y': 'у', 'z': 'ᴢ'}

def homoglyph(wordid,word_index,index2word,top_words=20000):
    word = index2word[wordid]
    s = np.random.randint(0,len(word))
    if word[s] in homos: 
        rletter = homos[word[s]]
    else:
        rletter = word[s]
    cword = word[:s] + rletter + word[s+1:]
    if cword in word_index:
        wid = word_index[cword] + 3
        if wid >= top_words:
            wid = 2
    else:
        wid = 2
    return (cword,wid)



def reandsw(wordid, word_index, index2word, top_words=20000):
    def remove(word):
        s = np.random.randint(0,len(word))
        if len(word) > 1:
            cword = word[:s] + word[s+1:]
        else:
            cword = word
        return cword

    def swap(word):
        if len(word) != 1:
            s = np.random.randint(0, len(word) - 1)
            cword = word[:s] + word[s+1] +word[s] +word[s+2:]
        else:
            cword = word
        return cword

    word = index2word[wordid]
    cword_remove = remove(word)
    wid_remove = 0
    if cword_remove in word_index:
        wid_remove = word_index[cword_remove]+3
        if wid_remove >= top_words:
            wid_remove = 2
    else:
        wid_remove = 2

    cword_swap = swap(cword_remove)
    if cword_swap in word_index:
        wid_swap = word_index[cword_swap] + 3
        if wid_swap >= top_words:
            wid_swap = 2
    else:
        wid_swap = 2
    return (cword_swap,wid_swap)



def alltrans(wordid, word_index, index2word, top_words=20000):
    def remove(word):
        s = np.random.randint(0,len(word))
        if len(word) > 1:
            cword = word[:s] + word[s+1:]
        else:
            cword = word
        return cword

    def swap(word):
        if len(word) != 1:
            s = np.random.randint(0, len(word) - 1)
            cword = word[:s] + word[s+1] +word[s] +word[s+2:]
        else:
            cword = word
        return cword

    def insert(word):
        s = np.random.randint(0, len(word) + 1)
        cword = word[:s] + chr(97 + np.random.randint(0, 26)) + word[s:]
        return cword

    def homoglyph(word):
        s = np.random.randint(0, len(word))
        if word[s] in homos:
            rletter = homos[word[s]]
        else:
            rletter = word[s]
        cword = word[:s] + rletter + word[s + 1:]
        return cword

    word = index2word[wordid]
    cword_remove = remove(word)
    wid_remove = 0
    if cword_remove in word_index:
        wid_remove = word_index[cword_remove]+3
        if wid_remove >= top_words:
            wid_remove = 2
    else:
        wid_remove = 2

    cword_swap = swap(cword_remove)
    if cword_swap in word_index:
        wid_swap = word_index[cword_swap] + 3
        if wid_swap >= top_words:
            wid_swap = 2
    else:
        wid_swap = 2

    cword_insert = insert(cword_swap)
    if cword_insert in word_index:
        wid_insert = word_index[cword_insert] + 3
        if wid_insert >= top_words:
            wid_insert = 2
    else:
        wid_insert = 2

    cword_homoglyph = homoglyph(cword_insert)
    if cword_homoglyph in word_index:
        wid_homoglyph = word_index[cword_homoglyph] + 3
        if wid_homoglyph >= top_words:
            wid_homoglyph = 2
    else:
        wid_homoglyph = 2
    return (cword_homoglyph,wid_homoglyph)





def transform(name):
    if "swap" in name:
        return swap
    elif "flip" in name:
        return flip
    elif "f2" in name:
        return f2
    elif "insert" in name:
        return insert
    elif "remove" in name:
        return remove
    elif "r2" in name:
        return remove2
    elif "homoglyph" in name:
        return homoglyph
    elif "reandsw" in name:
        return reandsw
    elif "alltrans" in name:
        return alltrans
    else:
        print('No transformer function found')
        sys.exit(1)