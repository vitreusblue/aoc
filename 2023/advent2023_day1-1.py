print("paste the code here, type () to finish\n")
code = []
code2 = []
code3 = []
sum = 0

def report(var):
    for i in range(0, len(var)):
        print(var[i])  

# place into list (original code, i looked up a lot of dings)
while True:
    typed = input()
    if typed == "()":
        break
    else:
        code.append(typed)
print('\nYOU ENTERED:')
report(code)

# now to look for nyumbers :3
for i in range(0, len(code)):
    code2.append('')
    p = code[i]
    for f in range(0, len(p)):
        if p[f].isnumeric() == True:
            code2[i] += p[f]
print('\nNUMBER FILTERED:')
report(code2)

# finding the first and last numbers
for i in range(0, len(code2)):
    code3.append('')
    l = len(code2[i]) -1
    code3[i] = code2[i][0]
    code3[i] += code2[i][l]
print('\nFIRST AND LASTS')
report(code3)

# summing up
for i in range(0, len(code3)):
    sum += int(code3[i])

#final result
print('\n FINAL RESULT:' + str(sum))


