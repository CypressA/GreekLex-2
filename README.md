# GreekLex-2
Python scripts for the development of GreekLex 2, a psycholinguistic database for Greek language

##Examples for running the scripts
***GreekSyllabicParser.py***


    >>> parser('κανονικός')

['κα', 'νο', 'νι', 'κός']

    >>> parser('άνθρωπος')

['άν', 'θρω', 'πος']

<br><br>
*Alternatively, an entire database can be parsed but it needs to have the following structure:*

word&nbsp;&nbsp;&nbsp;&nbsp;var1&nbsp;&nbsp;&nbsp;&nbsp;var2

αρχή&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;..&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;..

ζωή&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
..&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;..



    >>> syllabifyLexicon('database.txt', False)


*The output will look like:*


Word&nbsp;&nbsp;&nbsp;&nbsp;syll&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;syll num

αρχή&nbsp;&nbsp;&nbsp;&nbsp;αρ-χή&nbsp;&nbsp;&nbsp;&nbsp;2

ζωή&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ζω-ή&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2


<br><br>
***GPconverter.py***

    >>> convert('φτώχεια','φτώ-χεια')

'ftόXa'

    >>> convert('αδειανός','α-δεια-νός')

'aDjanόs'


*The second argument needs to be the syllabified orthographic form. The previous script can be used for this.*

<br><br>
*Whole databases can be processed here as well. Example:*


Word&nbsp;&nbsp;&nbsp;&nbsp;syll&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;syll num

αρχή&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;αρ-χή&nbsp;&nbsp;&nbsp;&nbsp;2

ζωή&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ζω-ή&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2


    >>> convertLexicon('database.txt')

*The output will look like:*

Word&nbsp;&nbsp;&nbsp;&nbsp;syll&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;phones&nbsp;&nbsp;&nbsp;&nbsp;phonSyl

αρχή&nbsp;&nbsp;&nbsp;&nbsp;αρ-χή&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;arXί&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ar-Xί	

ζωή&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ζω-ή&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;zoί&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;zo-ί	

*Note that the syllabified output will entail the orthographic syllables, not the phonological ones.*

<br><br>
***GreekPhonSyllabicParser.py***

    >>> parser('aDjanόs')

'a-Dja-nόs'

    >>> parser('άnTropos')

'άn-Tro-pos'


<br><br>
*Database example:*

phonTranscriptions&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;var1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;var2

eksoraizmόs&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...	

eksostrefίs&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...


    >>> syllabifyLexicon('test.txt')

*The output will look like:*

Word&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;syll&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;syll num

eksoraizmόs&nbsp;&nbsp;&nbsp;e-kso-ra-i-zmόs&nbsp;&nbsp;5

eksostrefίs&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e-kso-stre-fίs&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4

<br><br>
*For any questions or bug reports, contact* ***Antonios Kyparissiadis*** *at:*

**antonios.kyparissiadis@nottingham.ac.uk** or **kyparissiadis@gmail.com**

<br><br>
*If you use these scripts, please cite by using this reference.*

Kyparissiadis, A., van Heuven, W.J.B., Pitchford, N.J., & Ledgeway, T. (submitted). *GreekLex 2: A comprehensive database with syllabic, phonological and part-of-speech information.*

<br><br>
***GreekLex 2*** *database is available [here](http://www.psychology.nottingham.ac.uk/GreekLex/).*

*The reference list provides sources that the development of the scripts was based on.*
<br><br>

**References**

Babiniotis, G. (2008). *Orthografiko Lexiko tis Neas Elinikis Glossas (Orthographic Dictionary of Modern Greek Language)*. Athens, Greece: Kentro Lexikologias.

Botinis, A. (2011). *Fonitiki tis Ellinikis (Greek phonetics).* Athens, Greece: ISEL Editions.

Tzakosta,  M. (2010). The importance of being voiced: Cluster formation in dialectal variants of Greek. In A. Ralli, B. D. Joseph,  M. Janse, and A. Karasimos, (Eds), *Electronic Proceedings of the 4th International Conference of modern Greek Dialects and Linguistic Theory* (pp. 213-223). Patras, Greece: University of Patras.

Tzakosta, M. (2011). Consonantal interactions in dialectal variants of Greek: a typological approach of three-member consonant clusters. In C. Basea-Bezadakou, I. Manolessou, A. Afroudakis, G. Katsouda & S. Beis (Eds.), *Modern Greek Dialectology vol. 6.* (pp. 463-483). Athens, Greece: Academy of Athens – Research Center for Modern Greek Dialects. 

Tzakosta, M., & Karra, A. (2011). *A typological and comparative account of CL and CC clusters in Greek dialects.* In Μ. Janse, B. Joseph, P. Pavlou, A. Ralli & S. Armosti (Eds.), Studies in Modern Greek Dialects and Linguistic Theory I (pp. 95–105). Nicosia, Cyprus: Kykkos Cultural Research Centre.

