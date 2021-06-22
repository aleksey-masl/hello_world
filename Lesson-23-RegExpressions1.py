import re

mytext = "Vasya aaaaaaaaaaa 1972, Kolya - 1972, Olesya 1981, Petya gggggggggggggg," \
         "bbbbbbbbbbbbbb@intel.com, 1972, ccccccccc@gmail.com,   " \
         "Vladimir 1977, Irina, 2001, lex230323@mail.ru, Kolbasa Varenaya,"\
         "lex230323@yandex.ru, yandex.ru"
'''
\d = Any Digit 0-9
\D = Any nonDigit
\w = Any Alphabet symbol [A-Za-z]
\W = Any non Alphabet symbol
\s - space
\S - Non space

'''

textlookfor = r'\w+\.+'
allresults = re.findall(textlookfor, mytext)
print(allresults)
