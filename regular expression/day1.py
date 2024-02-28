# =====regular expression======

#  "\d" -------   0 to 9
#  "\D" ------    any non - digit
#  "\w" ------    (A to Z , a to z , 0 - 9)
#  "\W" ------     Reresents non - alphanumeric


# program 1
import re

rhyme = "Fun,Bun,Son,Mom,Run,Gun"

A = re.search(r'M\w\w', rhyme)
if A:
    print(A.group())
else:
    print("Not Found")

# program 2:

rhyme2 = "cat rat sat fan can"

B = re.search(r'\wat', rhyme2)
if B:
    print(B.group())
else:
    print("Not Found")

# program 3 :

rhyme3 = "Fun,Bun,Son,Mom,Run,Gun"

C = re.findall(r'\wu\w', rhyme3)
print(C)  # ['Fun', 'Bun', 'Run', 'Gun']

# program 4 :

rhyme4 = " bed spread fed ahead bled"

D = re.findall(r'\Ded', rhyme4)
print(D)  # ['bed', 'fed', 'led']

# program 5 :

rhyme5 = "Cook Book Took Look Hook"
E = re.match(r'C\w\w\w', rhyme5)
print(E)
if E:
    print(E.group())
else:
    print('not found')

# program 6
# non - alphanumeric

rhyme6 = "This is core java class and i am learning same"
F = re.split(r'\W', rhyme6)
print(F)  # return list   ===> ['This', 'is', 'core', 'java', 'class', 'and', 'i', 'am', 'learning', 'same']

# program 7
rhyme7 = "I am learning python"

G = re.sub(r'\wython', "java", rhyme7)
print(G)

rhyme8 = "i love you mom"
p = re.sub(r'\wom', "dad", rhyme8)
print(p)  # i love you dad
