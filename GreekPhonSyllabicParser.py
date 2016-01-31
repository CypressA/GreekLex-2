#############################################################
#############################################################
#                                                           #
# A phonetic syllabifier that parses Greek single           #
# strings into their constituent syllables. Offers          #
# the option of syllabifying entire databases.              #
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
import phonConsRules
import sys

phoneticSymbols = 'DGJLNTXcbdgfhkjmlnpsrtvxzaeiouάέίόύ'
consonants ='DGJLNTXcbdgfhkjmlnpsrtvxz'
vowels = 'aeiouάέίόύ'

def checkSymbols(phonString):
    for symbol in phonString:
        if symbol not in phoneticSymbols:
            sys.exit(symbol + ' is not an acceptable symbol')

def checkAllConsonants(phones):
    if all(x in consonants for x in phones):
        return True
    else:
        return False

def fixClusters(parsed):
    ''' (string) -> string
    The input is a rough approximation of syllabification as all consonants/consonant clusters are assigned to the beginning of each syllable.
    This function fixes any clusters that need to be split by determining the part of the cluster that needs to go the previous syllable's coda.
'''
    index = -1
    for char in parsed:
        index += 1 #start of syllable     #next is consonant        #second next is consonant   
        if char == '-' and parsed[index+1] in consonants and parsed[index+2] in consonants:
            cluster = ''
            for i in range(index + 1,len(parsed)):  #find the whole cluster
                if parsed[i] in consonants:    
                    cluster += parsed[i]    
                else:
                    break
            outcomes = []
            for i in range(len(cluster)-1):
                outcomes.append(phonConsRules.decideCluster(cluster[len(cluster)-i-2] + cluster[len(cluster)-i-1], False, False))          
            if False in outcomes:
                parsed = list(parsed)
                parsed.pop(index)
                parsed.insert(index-1+len(cluster)-outcomes.index(False), '-')
            parsed = ''.join(parsed)
    return(parsed)
                    

def parser(phones):
    '''(string) -> string
    Parses Greek phonetic input into its constituent syllables. 
'''
    index = -1
    checkSymbols(phones)
    if checkAllConsonants(phones):
        return(phones)
    syllables = []
    thisSyllable = '' 
    for phone in phones:
        thisSyllable += phone
        if phone in vowels:
            syllables.append(thisSyllable)
            thisSyllable = ''
    if thisSyllable != '' and len(phones) != 1 :
        syllables[len(syllables)-1] = syllables[len(syllables)-1] + thisSyllable        
    parsed = '-'.join(syllables)
    return(fixClusters(parsed))
    

    
def syllabifyLexicon(filename):
    '''(filename) - > file (phonSyllables.txt)
        

    Syllabifies a database and adds two new columns, the syllables of each word and their number.
    The input file needs to have the words at the first column. The program will ignore anything else.
    Assumes headers on the first line
    
    '''
    lexicon = []
    with open(filename, 'r') as file: 
        for line in file.readlines()[1:]:
            lexicon.append(re.split(r'\t',line.rstrip())[0])
            
    overall_list = [] 

    for word in lexicon:
        list_of_syllables = parser(word).split('-')
        overall_list.append(list_of_syllables)

   
    with open('phonSyllables.txt', 'w') as f:
        f.write( 'Word	syll	syll num' + '\r\n')

        for item in range(0, len(lexicon)):
            
            length = len(overall_list[item])
            syllables = '-'.join(overall_list[item])
            f.write(lexicon[item] + '\t' + syllables + '\t' + str(length) + '\n')
