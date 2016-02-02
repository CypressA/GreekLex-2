#############################################################
#############################################################
#                                                           #
# A syllabifier that parses Greek single words into their   #
# constituent syllables. Offers the option of syllabifying  #
# entire databases.                                         #
#                                                           #
# Antonios Kyparissiadis                                    #
#                                                           #
# antonios.kyparissiadis@nottingham.ac.uk                   #
# kyparissiadis@gmail.com                                   #
#                                                           #
# School of Psychology, University of Nottingham            #
#                                                           #
# Version 1.0                                               # 
# January, 2016                                             #
#                                                           #
#############################################################
#############################################################

import re
import codecs
import pickle
import os.path

consonants = ['β', 'γ', 'δ', 'ζ', 'θ', 'κ', 'λ', 'μ', 'ν', 'ξ', 'π', 'ρ', 'σ', 'τ', 'φ', 'χ', 'ψ', 'ς']
vowels = ['α', 'ά', 'ε', 'έ', 'η', 'ή', 'ι', 'ί', 'ϊ', 'ΐ', 'ο', 'ό', 'υ', 'ύ', 'ϋ', 'ΰ', 'ω', 'ώ']
always_together = ['ου', 'ού', 'οι', 'οί', 'αί', 'αι', 'ει', 'εί', 'αυ', 'αύ', 'ευ', 'εύ'] #diphthongs and combinations 
ambiguous = ['όι', 'οϊ', 'αϊ', 'αη', 'άι', 'ια', 'ιά','ιο', 'ιό', 'ιέ', 'ιε', 'υα', 'υά', 'άη', 'εϊ', 'ιω', 'ιώ', 'όε', 'υό'] 
# 'ηώ' and 'όη' are excluded from the ambiguity list in the absence of any data where the
# letters go in one syllable, and 'υέ', 'υώ' and 'υο' because they are always treated as 
# separate by Babiniotis (2008) Orthographiko Lexico

def legal_cons_clust():
    ''' -> pickle file

    Creates a list with all the legal initial consonant clusters found in the training set -GreekLex_v101 
    is provided in the folder for this purpose but any database can be used- and saves it as a pickle file.    
    '''
    initial_consonant_clusters = []
    with open('GreekLex2words.txt', 'r') as file:
        lexicon=[] 
        for line in file.readlines()[1:]:
            lexicon.append(re.split(r'\t',line.rstrip()))  
    for el in lexicon:
        word = el[1]
        cons_clust = ''
        counter = 0
        if len(word)>1 and word[0] in consonants and word[1] in consonants:
            if word[:2] not in initial_consonant_clusters:
                cluster = word[:2]
                initial_consonant_clusters.append(word[:2])
    initial_consonant_clusters.sort()
    with codecs.open('init_cons_clusters.pickle', 'wb') as f:
        pickle.dump(initial_consonant_clusters, f)

def vowels_together(word, counter):
    ''' (string, string, string) -> boolean.

    Retrieves predefined rules to decide if the two vowels need to go together.
    '''          #previous letter    letter 
    cluster = word[counter] + word[counter+1]
    if cluster in always_together:  
        return True
    elif cluster in ambiguous:
        return ruleBasedVowels(word, counter) 
    else:           #eg. ναός
        return False

def ruleBasedVowels(word, counter):
    '''(string, string) -> boolean                                  
    '''
    letter = word[counter+1]
    previous_letter = word[counter]
    next_letter = checkNext(word, counter)                                  #  This rule-based function is an over-simplification taking into account
    PREprevious_letter = checkPrev(word, counter)                           #  the frequency for each vowel cluster being separated or not and applying
    omikron = previous_letter == 'ο' and letter in ['ϊ']                    #  the majority rule to all cases. Ηence, it should  not be relied upon.
    omikronS = previous_letter == 'ό' and letter in ['ι']                     
    alpha = previous_letter == 'α' and letter in ['η']                      
    iota = previous_letter == 'ι' and counter != 0 and (letter in ['ά', 'ό', 'έ'] or          #iatros, iereas
                                       (letter == 'α' and next_letter not in ['ι', 'ί']) and  #miainw, diairw
                                        not PREprevious_letter == 'δ' )                       #'dia' is typically separated                     
    ypsilon = previous_letter == 'υ' and (letter in (['ι', 'ά'] or (letter == 'α'
                                                                   and next_letter not in ['ι', 'ί'])))                                                                 
    decide = omikron or omikronS or alpha or iota or ypsilon
    return(decide)

def checkNext(word, counter):
    if counter + 2 >= len(word):
        return None
    else:
        return word[counter + 2]

def checkPrev(word, counter):
    if counter == 0:
        return None
    else:
        return word[counter-1]

ambiguousList = []
ambiguousJustWords = []

def parser(word):
    ''' (string) -> list

    Syllabifies the input string of Greek letters (single word, no spaces, assumes a phonotactically
    correct initial cluster combination when present).    
    '''
    ambiGuous = False
    for letter in word:
        if letter not in consonants and letter not in vowels:
            print ('Input "' + word + '" does not seem to be a string of Greek lowercase letters')
            return 
    cluster_processed = False
    prev_vowels_make_cluster = False
    counter = -1
    list_of_syllables = []
    current_syllable = ''
    if len(word) < 3:
        return word
    else:
        for letter in word:
            counter += 1           

            if counter == 0 and not ((letter in consonants and word[counter + 1] in consonants) or #IT'S THE FIRST LETTER
            (letter in vowels and word[counter + 1] in vowels)):        #(unless there is a consonant or 
                current_syllable = letter                               # vowel cluster at the beginning)
                                                                                                                                                                                                                                    
            elif (counter + 1) == len(word):       #IT'S THE LAST LETTER       
                if letter in consonants and word[counter - 1] not in consonants: #if not part of a consonant cluster 
                    current_syllable += letter                                   #(because the cluster should already be in current_syllable
                elif letter in vowels:                                           #and will be appended to list_of_syllables 4 lines below)
                    current_syllable += letter         
                    cluster_processed = False
                list_of_syllables.append(current_syllable)
                if ambiGuous == True:
                    ambiguousEntry = []
                    ambiguousEntry.append(word)
                    ambiguousEntry.append(list_of_syllables)
                    ambiguousList.append(ambiguousEntry)
                    ambiguousJustWords.append(word)
                return list_of_syllables

            elif letter in consonants:              #IT'S A CONSONANT                                
                prev_vowels_make_cluster = False
                if word[counter - 1] in vowels and word[counter + 1] in vowels:     #if there is a vowel before and after the consonant
                    list_of_syllables.append(current_syllable)
                    current_syllable = letter
                elif word[counter + 1] in consonants:   
                    if cluster_processed != True:
                        cons_cluster = letter
                        next_is_cons = True
                        cons_counter = counter
                        while next_is_cons == True:
                            cons_cluster += word[cons_counter + 1]
                            cons_counter += 1
                            next_is_cons = (cons_counter + 1) != len(word) and word[cons_counter + 1] in consonants
                        if cons_counter == len(word) - 1: #if the just handled cons_cluster is at the end of the word (eg 'tanks')
                            current_syllable += cons_cluster                                                   
                        elif cons_cluster[0:2] in accept_cons_clust: #if a word starts with the first two consonants of the cluster 
                            if counter != 0:                #(so that it doesn't put again the final syllable of the previous word)
                                list_of_syllables.append(current_syllable)
                            current_syllable = cons_cluster                            
                        else:
                            current_syllable += letter
                            list_of_syllables.append(current_syllable)
                            current_syllable = cons_cluster[1:]
                        cluster_processed = True
                            
            elif letter in vowels:    #IT'S A VOWEL
                cluster_processed = False
                current_syllable += letter
                if word[counter + 1] in vowels:
                    check = letter + word[counter +1]
                    if  check in ambiguous:
                        ambiGuous = True
                    if not vowels_together(word, counter) or prev_vowels_make_cluster:
                        list_of_syllables.append(current_syllable)                             
                        current_syllable = ''                                                  
                        prev_vowels_make_cluster = False                                      
                    else:                                                                      
                        prev_vowels_make_cluster = True
                        
def syllabifyLexicon(filename, ambiguityFile = True):
    '''(filename) - > file (syllables.txt)
        boolean: True -> create file with ambiguously syllabified entries

    Syllabifies a database and adds two new columns, the syllables of each word and their number.
    The input file needs to have the words at the first column. The program will ignore anything else.
    Assumes  headers on the first line.    
    '''
    lexicon = []
    with open(filename, 'r') as file: 
        for line in file.readlines()[1:]:
            lexicon.append(re.split(r'\t',line.rstrip())[0])           
    overall_list = [] 
    for word in lexicon:
        list_of_syllables = parser(word)
        overall_list.append(list_of_syllables)        
    with open('syllables.txt', 'w') as f:
        if ambiguityFile:
            ambiguities = open('ambiguous.txt', 'w')
            ambiguities.write( 'Word	syll	syll num' + '\r\n')
        f.write( 'Word	syll	syll num' + '\r\n')
        lengths = []
        for item in range(0, len(lexicon)):
            syllables=''
            if type(overall_list[item]) != str:
                length = len(overall_list[item])
                for syllable in overall_list[item]:
                    syllables = syllables + syllable + '-'
                syllables = syllables.rstrip('-')
            else:
                syllables = overall_list[item]
                length=1
            f.write(lexicon[item] + '\t' + syllables + '\t' + str(length) + '\r\n')
            if ambiguityFile and (lexicon[item] in ambiguousJustWords):
                ambiguities.write(lexicon[item] + '\t' + syllables + '\t' + str(length) +  '\n')
        if ambiguityFile:    
            ambiguities.close()
   
if not os.path.isfile('init_cons_clusters.pickle'):
    legal_cons_clust()
with codecs.open('init_cons_clusters.pickle', 'rb') as f:
    accept_cons_clust = pickle.load(f)
