#############################################################
#############################################################
#                                                           #
# A photetic converter that transcribes Greek orthographic, #
# syllabified forms to their phonetic equivalents. Offers   #
# the option of transcribing entire databases.              #
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



import re
import GPCrules



consistentGPCs = {'β': 'v', 'δ': 'D', 'ζ': 'z', 'θ': 'T', 
                   'ξ': 'ks', 'ρ': 'r','φ': 'f', 'ψ': 'ps', 'ς': 's', 'ω': 'o',
                  'ώ': 'ό', 'η': 'i', 'ή': 'ί', 'ά': 'ά', 'έ': 'έ', 'ό': 'ό', 'ϊ': 'i', 'ΐ': 'ί', 'ΰ': 'ί', 'ϋ': 'i'}

consistentLetters = ['β','δ','ζ','θ','ξ','ρ','φ', 'ψ', 'ς', 'η', 'ή', 'ω', 'ώ', 'ά', 'έ','ό', 'ϊ', 'ΐ', 'ϋ', 'ΰ']

phonVowels = ['ά', 'ί', 'ό', 'έ', 'ύ', 'a', 'e', 'i', 'u', 'o']

dubiousLetters = {'γ': GPCrules.gamma, 'κ': GPCrules.kappa, 'λ': GPCrules.lamda, 'μ': GPCrules.mi, 'ν': GPCrules.ni, 'π': GPCrules.pi,
                  'σ': GPCrules.sigma, 'τ': GPCrules.tau, 'χ': GPCrules.chi, 'α': GPCrules.alpha, 
                  'ι': GPCrules.jota, 'ί': GPCrules.jotaS, 'ε' : GPCrules.epsilon, 'υ': GPCrules.ypsilon,
                  'ύ': GPCrules.ypsilonS, 'ο': GPCrules.omikron}

def stripDoubles(phones = ""):
    output = ""
    counter = 0
    while counter < len(phones)-1:
        if not phones[counter] == phones[counter+1]:
            output = output + phones[counter]
        elif phones[counter] in phonVowels:
            output = output + phones[counter]
        counter += 1
    if counter == len(phones)-1:
        output = output + phones[counter]
    return output


def convert(orthForm = '', syllables = "", syllabified = False):
    ''' 'πάλι', 'πά-λι' -> pάli (boolean True -> pά-li)
'''
    phones = ""
    index = 0
    for letter in syllables:
        if letter == '-':
            phones = phones + '-'
        elif letter in consistentLetters:
            phones = phones + consistentGPCs[letter]
        else:
            phones = phones + dubiousLetters[letter](index, orthForm, syllables)
        index += 1
    phones = stripDoubles(phones)

    if syllabified:
        return phones
    else:
        return phones.replace('-', '')
    

def convertLexicon(filename):
    '''(filename) -> file (GPCconverted.txt)

    Converts the orhtographic forms of a database to their phonological equivalents
    and adds two new columns, the phonologically converted form and the syllabified phonological
    form (emerging from orthographic syllabification rules).
    
    The input file needs to have the words at the first column and their syllabified forms
    parsed with hyphens('-') in-between syllables on the second column. The program will ignore anything else.
    Assumes headers on the first line.

    Note that the syllabified output will entail the orthographic syllables, not the phonological ones
'''

    lexicon = []
    with open(filename, 'r') as f:
            for line in f.readlines()[1:]:
                lexicon.append(re.split(r'\t',line.rstrip())[:2])
    
    
    for entry in lexicon:
        entry.append(convert(entry[0], entry[1]))
        entry.append(convert(entry[0], entry[1], syllabified = True))
       

    with open('GPCconverted.txt', 'w') as f:
        f.write( 'Word	syll	phones	phonSyl' + '\r\n')
        for entry in lexicon:
            for item in entry:
                f.write(item + '\t')
            f.write('\n')
        
