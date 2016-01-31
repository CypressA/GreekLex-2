#############################################################
#############################################################
#                                                           #
# This script determines whether a consonant cluster        #
# is a legal one according to the rules by                  #
# Tzakosta & Karra (2007; 2010)                             #
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

import sys


consonants = 'bdgGptkcvDzJjfTsxXZSmnMNlrLh'
nasalsAndLiquids = 'mnMNlrL'
nasals = 'mnMN'
liquids = 'lrL'
outsideRules = ['zb', 'fk', 'fc', 'zv', 'fx', 'fX', 'vJ', 'vj', 'zJ', 'zj']
#consonant clusters that would be erroneously judged as non-acceptable by
#the algorithm yet are reported as acceptable in Botinis (2011)




###Sonority Scale 1
###Manner of Articulation
MoA = {'b': 'stop','d': 'stop', 'g': 'stop', 'G': 'stop', 'p': 'stop',
       't': 'stop', 'k': 'stop', 'c':'stop',
       'v': 'fricative', 'D': 'fricative', 'z': 'fricative', 'J': 'fricative',
       'j': 'fricative', 'f': 'fricative', 'T': 'fricative', 's': 'fricative',
       'x': 'fricative', 'X': 'fricative',
       'Z': 'affricate', 'S': 'affricate',
       'm': 'nasal', 'n': 'nasal', 'M': 'nasal', 'N': 'nasal', 'h': 'nasal', 
       'l': 'liquid', 'r': 'liquid', 'L': 'liquid'}

###Sonority Scale 2
###Place of Articulation       
PoA = {'h': 'velar', 'k': 'velar', 'g': 'velar', 'x': 'velar', 'J':'velar',
       'm': 'labial', 'p': 'labial', 'b': 'labial', 'f': 'labial', 'v': 'labial',
       'M': 'labial',
       'T': 'coronal', 'D': 'coronal', 't': 'coronal', 'd': 'coronal',
       'n': 'coronal', 's': 'wildcard', 'z': 'coronal', 'r': 'coronal',
       'l': 'coronal', 'L': 'coronal', 'c': 'coronal', 'X': 'coronal',
       'G': 'coronal', 'j': 'coronal', 'N': 'coronal'}

###Sonority Scale 3
###Voicing
voicing = {'p': 'voiceless', 't': 'voiceless', 'k': 'voiceless', 'c': 'voiceless',
           'f': 'voiceless', 'T': 'voiceless', 's': 'voiceless', 'x': 'voiceless',
           'X': 'voiceless', 'b': 'voiced', 'd': 'voiced', 'g': 'voiced', 'G': 'voiced',
           'v': 'voiced', 'D': 'voiced', 'z': 'voiced', 'J': 'voiced', 'j': 'voiced',
           'm': 'voiced', 'n': 'voiced', 'N': 'voiced', 'l': 'voiced', 'r': 'voiced',
           'L': 'voiced', 'h': 'voiced'} 




MoAScale = {'stop': 1, 'fricative': 2, 'affricate': 3, 'nasal' : 4, 'liquid': 5}
PoAScale = {'wildcard': 0, 'velar': 1, 'labial': 2, 'coronal': 3}
voicingScale = {'voiceless': 1, 'voiced': 2 }


def clusterOK(cluster = ''):
    ''' string -> boolean

    Returns False and prints a warning if the cluster contains anything
    but the adjusted consonant phonetic symbols or less than two characters
'''
    if len(cluster) < 2:
        sys.exit('The function expects at least a two-consonant string')
    for symbol in cluster:
              if symbol not in consonants:
                  print('Input ' + cluster + ' not acceptable')
                  sys.exit('The phonetic symbol list is ' + consonants)
    return True



def decidePoA(cluster = ''):
    ''' string (boolean) -> string

    Decides if a consonant cluster is perfect, acceptable or not 
    acceptable regarding Place of Articulation

'''
    
    outcomes = []
    for i in range(len(cluster)-1):
    
        if PoAScale[PoA[cluster[i]]] < PoAScale[PoA[cluster[i+1]]]:
            outcomes.append('perfect')
        elif PoAScale[PoA[cluster[i]]] == PoAScale[PoA[cluster[i+1]]]:
            outcomes.append('acceptable')
        elif PoAScale[PoA[cluster[i]]] > PoAScale[PoA[cluster[i+1]]]:
            outcomes.append('notAcceptable')
        else:
            print('no outcome')

    if 'notAcceptable' in outcomes:
        return 'notAcceptable'
    elif 'acceptable' in outcomes:
        return 'acceptable'
    else:
        return 'perfect'



def decideMoA(cluster = ''):
    ''' string -> string

    Decides if a consonant cluster is perfect, acceptable or not 
    acceptable regarding Manner of Articulation

'''
    outcomes = []
    for i in range(len(cluster)-1):
    
        if MoAScale[MoA[cluster[i]]] < MoAScale[MoA[cluster[i+1]]]:
            outcomes.append('perfect')
        elif MoAScale[MoA[cluster[i]]] == MoAScale[MoA[cluster[i+1]]]:
            outcomes.append('acceptable')
        elif MoAScale[MoA[cluster[i]]] > MoAScale[MoA[cluster[i+1]]]:
            outcomes.append('notAcceptable')
        else:
            print('no outcome')

    if 'notAcceptable' in outcomes:
        return 'notAcceptable'
    elif 'acceptable' in outcomes:
        return 'acceptable'
    else:
        return 'perfect'

def decideVoicing(cluster = ''):
    ''' string -> string

    Decides if a consonant cluster is perfect, acceptable or not 
    acceptable regarding the voicing scale

'''
    outcomes = []
    for i in range(len(cluster)-1):
        
        if voicingScale[voicing[cluster[i]]] > voicingScale[voicing[cluster[i+1]]]:
            outcomes.append('notAcceptable')
        else:
            return 'passes'
        
    if 'notAcceptable' in outcomes:
        return 'notAcceptable'
    else:
        return 'passes'



def decideCluster(cluster = '', liberal = False, details = True):
    ''' string, (boolean), (boolean) -> boolean

    Decides if a two-consonant cluster is legal or not.
    'liberal = True' will not assess nasals and liquids for Manner of Articulation
    'liberal = False' will assess nasals and liquids for Manner of Articulation as any other consonant

'''
    if not clusterOK(cluster):
        return

    if cluster in outsideRules:
        if details:
           print('external rules')
        return True
  
    if cluster[0] in liquids:
        if details:
            print('initial is liquid')
        return False
    elif decideVoicing(cluster) == 'notAcceptable':
        if details:
            print('voicing violated')
        return False
    elif cluster[0] in nasals and cluster[1] in liquids:
        if details:
            print('nasal-liquid')
        return False

    if liberal and any(n in nasalsAndLiquids for n in cluster):
        mannerPlace = ['notAssessed', decidePoA(cluster)]       
    else:
        mannerPlace = [decideMoA(cluster), decidePoA(cluster)]

        
    if details:

        print('MoA: ' + mannerPlace[0])
        print('PoA: ' + mannerPlace[1])


    if 'perfect' in mannerPlace:
        return True
    elif 'acceptable' in mannerPlace and 'notAcceptable' not in mannerPlace: 
        return True
    elif 'notAcceptable' in mannerPlace and 'perfect' not in mannerPlace: 
        return False
    else:
        print('Cannot handle cluster ' + cluster)


 
##Botinis, A. (2011). Fonitiki tis Ellinikis (Greek phonetics). Athens, Greece: ISEL Editions


##Tzakosta, M., & Karra, A. (2007). A typological and comparative account of CL and CC clusters
##in Greek dialects. 3rd International Conference on Modern Greek, Dialects and Linguistic Theory,
##Nicosia, Cyprus. Retrieved from http://speech.ilsp.gr/iplr/TzakostaKarra_2007_MGD3.pdf

##Tzakosta,  M. (2010). The importance of being voiced: Cluster formation in dialectal variants of Greek,
##in A. Ralli, B. Joseph,  M. Janse, and A. Karasimos, (Eds), Electronic Proceedings of the 4th
##International Conference of modern Greek Dialects and Linguistic Theory (pp.213-223) University
##of Patras.

##Tzakosta, M. (2011). Consonantal interactions in dialectal variants of Greek: a typological approach
##of three-member consonant clusters. In C. Basea-Bezadakou, , et al. (Eds.) Modern Greek Dialectology
##vol. 6. (463-483). Athens: Academy of Athens – Research Center for Modern Greek Dialects. 
