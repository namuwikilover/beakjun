import string

letter_count = dict((letter, -1) for letter in string.ascii_uppercase);

letter_count['A']=3; letter_count['B']=3; letter_count['C']=3
letter_count['D']=4; letter_count['E']=4; letter_count['F']=4
letter_count['G']=5; letter_count['H']=5; letter_count['I']=5
letter_count['J']=6; letter_count['K']=6; letter_count['L']=6
letter_count['M']=7; letter_count['N']=7; letter_count['O']=7
letter_count['P']=8; letter_count['Q']=8; letter_count['R']=8; letter_count['S']=8
letter_count['T']=9; letter_count['U']=9; letter_count['V']=9
letter_count['W']=10; letter_count['X']=10; letter_count['Y']=10; letter_count['Z']=10

l=input(); s=0
for i in l:
    s+=letter_count[i]
print(s)




