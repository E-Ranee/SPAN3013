phonological_transcription_list = open("phonological.txt").readlines()
from functions import *

# [b] in absolute initial position or after nasal
# /β/ allophone
b_allophones = ["b", "β"]

# [d] in absolute initial position, after a nasal or a lateral
# /ð/ allophone
d_allophones = ["d", "ð"]

# [g] in absolute initial position or after nasal
# /ɣ/ allophone
g_allophones = ["g", "ɣ"]

# [s] before voiceless consonant
# /z/ before voiced consonant
s_allophones = ["s", "z"]

# [m] in syllable initial position (after consonant)
#     or before a bilabial consonant (b / β)
# [ɲ]
# /ŋ/ before velar consonant
# /ɱ/ before [f]
# /n̪/ before dental (d / t)
# /n̟/ before interdental (θ / ð)
m_allophones = ["m", "ɱ", "n"]
n_allophones = ["n", "m", "ɱ", "ŋ", "n̪", "n̟"]

# /l̪/ before dental
# /l̟/ before interdental
l_allophones = ["l", "l̪", "l̟"]

# [r] word initial, intervocalic, written -rr-, or after a nasal
# [ɾ] intervocalic, end of syllable, after consonant that isn't n/s/l

# [x] before a
# /ç/ before i or e
# /χ/ before o or u
x_allophones = ["x", "ç", "χ"]

# /e/ in open syllable or closed by nasal, d, or z
# /ɛ/ in contact with [r], before [x], in ei diphthong, 
#     in a closed syllable that isn't closed by a nasal, 
#     s, d, z, or x (gs)
e_allophones = ["e", "ɛ"]

# /a/
# /ɑ/ in au, before o, in a syllable closed by l, and before [x]
a_allophones = ["a", "ɑ"]

# /o/
# /ɔ/ in contact with [r], before [x], betweem soft a and r or l
o_allophones = ["o", "ɔ"]

bilabial_phonemes = ["m", "p", "b"]
labiodental_phonemes = ["f"]
dental_phonemes = ["t", "d"]
interdental_phonemes = ["θ", "ð"]
alveolar_phonemes = ["s", "z", "n", "l", "r", "ɾ"]
palatal_phonemes = ["t͡ʃ"]
velar_phonemes = ["x", "k", "g"]

nasal_sounds = ["n", "m", "ɲ", "ɱ", "ŋ", "n̪", "n̟"]

consonants = ["b", "β", "d", "ð", "g", "ɣ", "m", "ɱ", "n", "ŋ", "n̪", "n̟", "ɲ", "l", "l̪", "l̟", "x", "ç", "χ", "r", "ɾ", "t͡ʃ", "ʝ"]
vowels = ["a", "ɑ", "o", "ɔ", "e", "ɛ", "i", "u", "w", "j"]

voiced_sounds = ["b", "β", "d", "ð", "g", "ɣ", "z", "m", "ɱ", "n", "ŋ", "n̪", "n̟", "ɲ", "l", "l̪", "l̟", "ð", "r", "ɾ", "ʝ"]
voiceless_sounds = ["s", "p", "t", "x", "ç", "χ", "f", "θ", "t͡ʃ", "k"]


