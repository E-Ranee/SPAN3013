phonological_transcription_list = open("phonological.txt", encoding="utf8").readlines()

g_allophones = ["g", "ɣ"]

bilabial_phonemes = ["m", "p", "b"]
labiodental_phonemes = ["f"]
dental_phonemes = ["t", "d"]
interdental_phonemes = ["θ", "ð"]
alveolar_phonemes = ["s", "z", "n", "l", "r", "ɾ"]
palatal_phonemes = ["t͡ʃ"]
velar_phonemes = ["x", "k", "g"]

nasal_sounds = ["n", "m", "ɲ", "ɱ", "ŋ", "n̪", "n̟"]
lateral_sounds = ["l", "l̪", "l̟"]
x_allophones = ["x", "ç", "χ"]

consonants = ["b", "β", "d", "ð", "g", "ɣ", "m", "ɱ", "n", "ŋ", "n̪", "n̟", "ɲ", "l", "l̪", "l̟", "x", "ç", "χ", "r", "ɾ", "t͡ʃ", "ʝ"]
vowels = ["a", "ɑ", "o", "ɔ", "e", "ɛ", "i", "u", "w", "j"]
voiced_sounds = ["b", "β", "d", "ð", "g", "ɣ", "z", "m", "ɱ", "n", "ŋ", "n̪", "n̟", "ɲ", "l", "l̪", "l̟", "ð", "r", "ɾ", "ʝ"]
voiceless_sounds = ["s", "p", "t", "x", "ç", "χ", "f", "θ", "t͡ʃ", "k"]

def b_allophone(word, nasal_sounds):
    """Checks if B is the first sound or after a nasal or if it should be an allophone"""
    temp_word = list(word)
    length = len(temp_word)
    for index in range(len(temp_word)):
        if temp_word[index] == "B":
        #position inicial
            if index == 0:
                temp_word[index] = "b"
            elif index < length and temp_word[index+1].lower() in voiceless_sounds:
                temp_word[index] = "p"
            elif temp_word[index-1].lower() in nasal_sounds:
                temp_word[index] = "b"
            else:
                temp_word[index] = "β"
    temp_word = "".join(temp_word)
    return temp_word

def d_allophone(word, nasal_sounds, lateral_sounds):
    """Checks if D is the first sound or after a nasal or lateral or if it should be an allophone"""
    temp_word = list(word)
    nasal_sounds = ["n", "m", "ɲ", "ɱ", "ŋ", "n̪", "n̟"]
    lateral_sounds = ["l", "l̪", "l̟"]
    for index in range(len(temp_word)):
        if temp_word[index] == "D":
        #position inicial
            if index == 0:
                temp_word[index] = "d"
            elif temp_word[index-1].lower() in nasal_sounds:
                temp_word[index] = "d"
            elif temp_word[index-1].lower() in lateral_sounds:
                temp_word[index] = "d"
            else:
                temp_word[index] = "ð"
    temp_word = "".join(temp_word)
    return temp_word

def g_allophone(word, nasal_sounds):
    """Checks if G is the first sound or after a nasal or if it should be an allophone"""
    temp_word = list(word)
    for index in range(len(temp_word)):
        if temp_word[index] == "G":
        #position inicial
            if index == 0:
                temp_word[index] = "g"
            elif temp_word[index-1].lower() in nasal_sounds:
                temp_word[index] = "g"
            else:
                temp_word[index] = "ɣ"
    temp_word = "".join(temp_word)
    return temp_word

def voiced_s(word, voiced_sounds):
    """Checks if the next phoneme is voiced"""
    temp_word = list(word)
    length = len(word)
    for index in range(length-1):
        if temp_word[index] == "S":
            if temp_word[index+1].lower() in voiced_sounds:
                temp_word[index] = "z"
            else:
                temp_word[index] = "s"
    temp_word = "".join(temp_word)
    return temp_word

def nasal_allophones(word, bilabial_phonemes, labiodental_phonemes, dental_phonemes, interdental_phonemes, alveolar_phonemes, palatal_phonemes, velar_phonemes):
    """Checks what the next phoneme is"""
    temp_word = list(word)
    length = len(word)
    for index in range(length-1):
        if temp_word[index] == "N":
            if temp_word[index+1].lower() in bilabial_phonemes:
                temp_word[index] = "m"
            elif temp_word[index+1].lower() in labiodental_phonemes:
                temp_word[index] = "ɱ"
            elif temp_word[index+1].lower() in dental_phonemes:
                temp_word[index] = "n̪"
            elif temp_word[index+1].lower() in interdental_phonemes:
                temp_word[index] = "n̟"
            elif temp_word[index+1].lower() in velar_phonemes:
                temp_word[index] = "ŋ"
            else:
                temp_word[index] = "n"
    
    temp_word = "".join(temp_word)
    return temp_word

def m_allophones(word, bilabial_phonemes, labiodental_phonemes):
    """Checks what the next phoneme is"""
    temp_word = list(word)
    length = len(word)
    for index in range(length-1):
        if temp_word[index] == "M":
            if temp_word[index+1].lower() in bilabial_phonemes:
                temp_word[index] = "m"
            elif temp_word[index+1].lower() in labiodental_phonemes:
                temp_word[index] = "ɱ"
            else:
                temp_word[index] = "m"
    
    temp_word = "".join(temp_word)
    return temp_word

def l_allophones(word, dental_phonemes, interdental_phonemes):
    """Checks what the next phoneme is"""
    temp_word = list(word)
    length = len(word)
    for index in range(length-1):
        if temp_word[index] == "L":
            if temp_word[index+1].lower() in dental_phonemes:
                temp_word[index] = "l̪"
            elif temp_word[index+1].lower() in interdental_phonemes:
                temp_word[index] = "l̟"
            else:
                temp_word[index] = "l"
    
    temp_word = "".join(temp_word)
    return temp_word

def jota_allophones(word):
    """[x] before a, /ç/ before i or e, /χ/ before o or u"""
    temp_word = list(word)
    length = len(word)
    for index in range(length-1):
        if temp_word[index] == "X":
            if temp_word[index+1].lower() in ["a", "ɑ"]:
                temp_word[index] = "x"
            elif temp_word[index+1].lower() in ["e", "ɛ", "i"]:
                temp_word[index] = "ç"
            else:
                temp_word[index] = "χ"
    
    temp_word = "".join(temp_word)
    return temp_word

def e_allophone(word):
    temp_word = list(word)
    length = len(temp_word)
    for index in range(len(temp_word)):
        if temp_word[index] == "E":
            # /e/ in open syllable. Check if next phoneme is a vowel or if two phonemes away is a vowel
            if index + 1 < length and temp_word[index+1] in vowels:
                temp_word[index] = "e"
            elif index + 2 < length and temp_word[index+2] in vowels: #doesn't account for complex onsets
                temp_word[index] = "e"
            # /e/ in closed syllable, closed by nasal d or z
            #       check if next phoneme is a nasal/d/z and if the phoneme afterwards is a consonant
            elif index + 2 < length and (temp_word[index+1] in nasal_sounds or temp_word[index+1] in ["d", "z"]) and temp_word[index+2] in consonants:
                temp_word[index] = "e"
            # /ɛ/ if phoneme before or phoneme afterwards is an [r]
            elif index > 0 and index < length and (temp_word[index-1] == "r" or temp_word[index+1] == "r"):
                temp_word[index] = "ɛ"
            # /ɛ/ if phoneme afterwards is an [x]
            elif index < length and temp_word[index+1] == "x":
                temp_word[index] = "ɛ"
            # /ɛ/ if phoneme afterwards is an [i]
            elif index < length and temp_word[index+1] == "i":
                temp_word[index] = "ɛ"
            # /ɛ/ if phoneme afterwards is a consonant that isn't nasal/s/d/z and phoneme after is a consonant
            elif index + 2 < length and (temp_word[index+1] not in nasal_sounds and temp_word[index+1] not in ["d", "z","s"]) and temp_word[index+2] in consonants:
                temp_word[index] = "ɛ"
            # /ɛ/ if phoneme afterwards is a /g/ and phoneme after is an /s/
            elif index + 2 < length and temp_word[index+1] in g_allophones and temp_word[index+2] == "s":
                temp_word[index] = "ɛ"

            else:
                temp_word[index] = "e"
    temp_word = "".join(temp_word)
    return temp_word

def a_allophone(word, lateral_sounds, x_allophones):
    """# /a/ except /ɑ/ in au, before o, in a syllable closed by l, and before [x]"""
    temp_word = list(word)
    length = len(temp_word)
    for index in range(length-1):
        if temp_word[index] == "A":
            if temp_word[index+1].lower() in x_allophones:
                temp_word[index] = "ɑ"
            elif temp_word[index+1].lower() in ["u", "o"]:
                temp_word[index] = "ɑ"
            elif index+2 <= len(temp_word) and temp_word[index+1] in lateral_sounds and temp_word[index+2] in consonants:
                temp_word[index] = "ɑ"
            else:
                temp_word[index] = "a"
    if temp_word[length-1] == "A":
        temp_word[length-1] = "a"

    temp_word = "".join(temp_word)
    return temp_word

def o_allophone(word):
    """/ɔ/ in contact with [r], before [x], between ɑ and r or l"""
    temp_word = list(word)
    for index in range(len(temp_word)):
        if temp_word[index] == "O":
            temp_word[index] = "o"
    for index in range(len(temp_word)-1):
        if temp_word[index] == "o":
            if temp_word[index+1].lower() in x_allophones:
                temp_word[index] = "ɔ"
            elif index > 0 and (temp_word[index-1].lower() == "r" or temp_word[index+1] == "r"):
                temp_word[index] = "ɔ"
            elif index > 0 and temp_word[index-1].lower() == "ɑ" and (temp_word[index+1] == "r" or temp_word[index+1] in lateral_sounds):
                temp_word[index] = "ɔ"
            else:
                temp_word[index] = "o"
    temp_word = "".join(temp_word)
    return temp_word

def repeated_letters(word):
    temp_word = list(word)
    for index in range(len(temp_word)-1):
        if temp_word[index].lower() == temp_word[index+1].lower():
            temp_word[index+1] = ":"
    temp_word = "".join(temp_word)
    return temp_word

def phonetic_transcription(word):
    temp_word = list(word)
    temp_word = repeated_letters(temp_word)
    temp_word = b_allophone(temp_word, nasal_sounds)
    temp_word = d_allophone(temp_word, nasal_sounds, lateral_sounds)
    temp_word = g_allophone(temp_word, nasal_sounds)
    temp_word = b_allophone(temp_word, nasal_sounds)

    temp_word = voiced_s(temp_word, voiced_sounds)
    temp_word = nasal_allophones(temp_word, bilabial_phonemes, labiodental_phonemes, dental_phonemes, interdental_phonemes, alveolar_phonemes, palatal_phonemes, velar_phonemes)
    temp_word = m_allophones(temp_word, bilabial_phonemes, labiodental_phonemes)
    temp_word = l_allophones(temp_word, dental_phonemes, interdental_phonemes)
    temp_word = jota_allophones(temp_word)

    temp_word = a_allophone(temp_word, lateral_sounds, x_allophones)
    temp_word = e_allophone(temp_word)
    temp_word = o_allophone(temp_word)
    
    return temp_word


clean_list = [x.replace('\n', '') for x in phonological_transcription_list]
# for word in clean_list:
#     print(phonetic_transcription(word))
print()
result = phonetic_transcription(clean_list)
print(result)
print()
print(phonetic_transcription("SiBoiAENfOkAɾmEENkONSEGiɾ"))

f = open("result.txt", encoding='utf8', mode='w')
f.write(result)
f.flush()