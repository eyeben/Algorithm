import re
txt = input()
li1 = re.split(r'[+-]+', txt)
li2 = re.split(r'\d+', txt)
li2 = [itm for itm in li2 if itm]

li = ['(', str(int(li1[0]))]
li1.pop(0)

for i in range(len(li2)):
    if li2[i] == '-':
        li.append(')')
        li.append('-')
        li.append('(')
        li.append(str(int(li1[i])))
    else:
        li.append('+')
        li.append(str(int(li1[i])))
li.append(')')
print(eval(''.join(li)))