#############################################################
#############################################################
#                                                           #
# This script determines how ambiguous letters are          #
# phonetically transcribed to their corresponding phones    #
# depending on the context.                                 #
#                                                           #
# Antonios Kyparissiadis                                    #
#                                                           #
# School of Psychology, University of Nottingham            #
#                                                           #
# Version 1.0                                               # 
# January, 2016                                             #
#                                                           #
#############################################################
#############################################################



pallatisingVowels = ['ε', 'έ', 'ι', 'ί', 'η', 'ή', 'υ', 'ύ']
pallatisingDiphthongs = ['αι', 'αί', 'οι', 'οί']
vowels = ['α', 'ά', 'ι', 'ί', 'ε', 'έ', 'ε', 'ω', 'ώ', 'ο', 'ό', 'η', 'ή']
consonants = 'βγδζθκλμνξπρσςτφχψ'


def trueIndex(index, syllabified):
    counter = 0
    for letter in syllabified[:index+1]:
        if letter == '-':
            counter += 1
    trueIndex = index - counter
    return trueIndex

def gamma(index, word, syllabified):
    if index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] in ['χ', 'γ' ,'κ']:
        if index != 0:
            return 'h'
        else:
            return ''
    elif (index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] in pallatisingVowels) or (index < len(syllabified)-2 and str(word[trueIndex(index, syllabified)+1]+word[trueIndex(index, syllabified)+2]) in pallatisingDiphthongs):
        if index != 0 and word[trueIndex(index, syllabified)-1] == 'γ':
            return 'G'
        else:
            return 'j'
    elif index != 0 and word[trueIndex(index, syllabified)-1] == 'γ':
        return 'g'
    else:
        return 'J' 

def kappa(index, word, syllabified):
    if index != 0 and word[trueIndex(index, syllabified)-1] == 'γ':
        if index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] in pallatisingVowels or (index < len(syllabified)-2 and str(word[trueIndex(index, syllabified)+1]+word[trueIndex(index, syllabified)+2])) in pallatisingDiphthongs:
            return 'G'
        else:
            return 'g'
    elif (index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] in pallatisingVowels) or (index < len(syllabified)-2 and str(word[trueIndex(index, syllabified)+1]+word[trueIndex(index, syllabified)+2])) in pallatisingDiphthongs:
        return 'c'
    elif index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] == 'κ':
        return ''
    else:
        return 'k'

def lamda(index, word, syllabified):
                                                            #not end of word
    if index < len(syllabified)-2 and word[trueIndex(index, syllabified)+1] == 'ι' and  syllabified[index+2] in 'άαεέοόωώ':
        return 'L'
    elif index < len(syllabified)-3 and word[trueIndex(index, syllabified)+1] in 'οε' and word[trueIndex(index, syllabified)+2] == 'ι' and syllabified[index+3] in 'άαεέοόωώ':
        return 'L'
    elif index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] == 'λ':
        return ''
    else:
        return 'l'

def mi(index, word, syllabified):
    if index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] ==  'π' :
        return 'b'
##    elif index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] == 'β':
##        return 'M'
    else:
        return 'm'
    

def ni(index, word, syllabified):
    if index < len(syllabified)-1 and (word[trueIndex(index, syllabified)+1] == 'τ' or word[trueIndex(index, syllabified)+1] == 'ν'):
        return ''
    elif index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] == 'κ':
        return 'h'
    elif index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] == 'ι' and index < len(syllabified)-2 and syllabified[index+2] in 'άαεέοόωώ':
        return 'N'
    elif index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] in 'οε' and index < len(syllabified)-2 and syllabified[index+2] == 'ι' and index < len(syllabified)-3 and syllabified[index+3]in 'άαεέοόωώ':
        return 'N'
    else:
        return 'n'

def pi(index, word, syllabified):
    if index != 0 and word[trueIndex(index, syllabified)-1] == 'μ':
        return ''
    else:
        return 'p'

def sigma(index, word, syllabified):
    if index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] in ['μ', 'δ', 'β']:
        return 'z'   
    else:
        return 's'

def tau(index, word, syllabified):
    if (index != 0 and word[trueIndex(index, syllabified)-1] == 'ν') or (index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] == 'ζ'): 
        return 'd'                                 
    else:                                          
        return 't'

def chi(index, word, syllabified):
    if (index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] in pallatisingVowels) or (index < len(syllabified)-2 and word[trueIndex(index, syllabified)+1] + word[trueIndex(index, syllabified)+2] in pallatisingDiphthongs):
        return 'X'
    else:
        return 'x'


def alpha(index, word, syllabified):
    if index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] == 'ι':
        return 'e'
    elif index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] == 'ί':
        return 'έ'
    elif index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] == 'ύ':
        return 'ά'
    else:
        return 'a'
    
def jota(index, word, syllabified):
                              #previous letter                                      not  end of word                     next character              
    if index != 0 and word[trueIndex(index, syllabified)-1] in 'λνκγχ' and index < len(syllabified)-1 and syllabified[index+1] in 'άαεέοόωώ':
        return ""       #previous letter                                   not  end of word                     next character
    elif index >= 2 and word[trueIndex(index, syllabified)-2] in 'γλ' and word[trueIndex(index, syllabified)-1] in 'οε' and index < len(syllabified)-1 and syllabified[index+1] in 'άαεέοόωώ':
        return ''
##    elif index >= 2 and word[trueIndex(index, syllabified)-2] == 'ν' and word[trueIndex(index, syllabified)-1] in 'οε' and index < len(syllabified)-1 and syllabified[index+1] in 'άαεέοόωώ':
##        return ''
    elif index != 0 and word[trueIndex(index, syllabified)-1] in 'βδρ' and index < len(syllabified)-1 and syllabified[index+1] in 'άαεέοόωώ':
        return 'j'
    elif index >= 2 and word[trueIndex(index, syllabified)-1] == 'τ' and word[trueIndex(index, syllabified)-2] == 'ν' and  index < len(syllabified)-1 and syllabified[index+1] in 'άαεέοόωώ':
        return 'j'
    elif index >= 2 and word[trueIndex(index, syllabified)-2] in 'βδρ' and word[trueIndex(index, syllabified)-1] in 'οε' and index < len(syllabified)-1 and syllabified[index+1] in 'άαεέοόωώ':
        return 'j'
    elif index >= 2 and word[trueIndex(index, syllabified)-2] == 'μ' and word[trueIndex(index, syllabified)-1] == 'π' and index < len(syllabified)-1 and syllabified[index+1] != '-':
        return 'j'
    elif index != 0 and word[trueIndex(index, syllabified)-1] in 'πστθφξψ' and index < len(syllabified)-1 and syllabified[index+1] in 'άαεέοόωώ':
        return 'X'
    elif index >= 2 and word[trueIndex(index, syllabified)-2] in 'πστθφξψχ' and word[trueIndex(index, syllabified)-1] in 'οε' and index < len(syllabified)-1 and syllabified[index+1] in 'άαεέοόωώ':
        return 'X'
    elif index != 0 and word[trueIndex(index, syllabified)-1] == 'μ' and index < len(syllabified)-1 and syllabified[index+1] in 'άαεέοόωώ':
        return 'N'
    elif index >= 2 and word[trueIndex(index, syllabified)-2] == 'μ' and word[trueIndex(index, syllabified)-1] in 'οε' and index < len(syllabified)-1 and syllabified[index+1] in 'άαεέοόωώ':
        return 'N'
    elif index != 0 and (word[trueIndex(index, syllabified)-1] in ['ο', 'α', 'ε'] or (word[trueIndex(index, syllabified)-1] == 'υ' and word[trueIndex(index, syllabified)-2] != 'ο')):
        return ""
    else:
        return 'i'  
        
    
    
def jotaS(index, word, syllabified):
    if index!= 0 and word[trueIndex(index, syllabified)-1] in ['ο', 'α', 'ε']:
        return ""
    else:
        return 'ί'
    

def epsilon(index, word, syllabified):
    if index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] == 'ι':
        if (index != 0 and word[trueIndex(index, syllabified)-1] in 'πστθφξψδλγνμχ') and (index < len(syllabified)-2 and not syllabified[index+2]=='-'):
            return ''
        else:
            return 'i'
    elif index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] == 'ί':
        return 'ί'
    elif index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] == 'ύ':
        return 'έ'
    else:
        return 'e'
        

def ypsilon(index, word, syllabified):
    if index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] in 'β' and (index != 0 and not word[trueIndex(index, syllabified)-1] in consonants):
        return ''
    elif index != 0 and word[trueIndex(index, syllabified)-1] == 'ο':
        return ""
    elif index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] in 'ζ' and (index != 0 and not word[trueIndex(index, syllabified)-1] in consonants):
        return 'v'
    elif index != 0 and word[trueIndex(index, syllabified)-1] in ['ε', 'α']:
        if index < len(syllabified)-1 and (word[trueIndex(index, syllabified)+1] in vowels or word[trueIndex(index, syllabified)+1] in ['μ', 'ν', 'γ', 'λ', 'ρ', 'δ']):
            return 'v'
        else:
            return 'f'
    elif index != 0 and word[trueIndex(index, syllabified)-1] in 'πστθφξψ' and index < len(syllabified)-1 and syllabified[index+1] in 'άαεέοόωώ':
        return 'X'
    elif index != 0 and word[trueIndex(index, syllabified)-1] == 'μ' and index < len(syllabified)-1 and syllabified[index+1] in 'άαεέοόωώ':
        return 'N'
    elif index != 0 and word[trueIndex(index, syllabified)-1] == 'γ' and index < len(syllabified)-1 and syllabified[index+1] in 'άαεέοόωώ':
        return ''    
    else:
        return 'i'
    
def ypsilonS(index, word, syllabified):
    if index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] == 'β' and (index != 0 and not word[trueIndex(index, syllabified)-1] in consonants):
        return ''
    elif index != 0 and word[trueIndex(index, syllabified)-1] == 'ο':
        return ""
    elif index != 0 and word[trueIndex(index, syllabified)-1] in ['ε', 'α']:
        if index < len(syllabified)-1 and (word[trueIndex(index, syllabified)+1] in vowels or word[trueIndex(index, syllabified)+1] in ['μ', 'ν', 'γ', 'λ', 'ρ', 'δ']):
            return 'v'
        else:
            return 'f'
    else:
        return 'ί'
    
  

def omikron(index, word, syllabified):
    if index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] == 'ι':
        if (index != 0 and word[trueIndex(index, syllabified)-1] in 'πστθφξψδλγνμχ') and (index < len(syllabified)-2 and not syllabified[index+2]=='-'):
            return ''
        else:
            return 'i'
    elif index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] == 'ί':
        return 'ί'
    elif index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] == 'υ':
        return 'u'
    elif index < len(syllabified)-1 and word[trueIndex(index, syllabified)+1] == 'ύ':
        return 'ύ'
    else:
        return 'o'
    
    

