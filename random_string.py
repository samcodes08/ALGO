import string
import random
Q=[]
with open('questions.txt','r') as f:
    for line in f:
        for word in line.split(';'):
           Q.append(word)
del(Q[-1])
#print(Q)
def id_generator(size, list1):
    s=''
    for i in range(size):
        character=random.choice(list1)
        list1.remove(character)
        s+=character
    #return ''.join(random.choice(list1) for _ in range(size))
    return(s)
p=['.',':','?',';','!','+','@','#']
n=['0','1','2','3','4','5','6','7','8','9']
l=[]
q1=random.choice(Q)
Q.remove(q1)
print(q1)
q1=input()
'''for i in range(len(q1)):
    l.append(q1[i])'''
l.append(q1)
q2=random.choice(Q)
Q.remove(q2)
print(q2)
q2=input()
'''for i in range(len(q2)):
    l.append(q2[i])'''
l.append(q2)

q3=random.choice(Q)
Q.remove(q3)
print(q3)
q3=input()
'''for i in range(len(q3)):
    l.append(q3[i])'''
l.append(q3)
for i in range(3):
    n1=random.choice(n)
    n.remove(n1)
    p1=random.choice(p)
    p.remove(p1)
    l.append(n1)
    l.append(p1)
l=list(set(l))
#print(l)
s=id_generator(6,l)
print("Password",s)
