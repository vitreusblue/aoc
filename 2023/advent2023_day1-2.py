print("paste the code here, type () to finish\n")
code = []
code2 = []
code3 = []
sum = 0
wordlist = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

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
    f = 0
    while f < len(p):
        if p[f].isnumeric() == True: #if the character is an number
            code2[i] += p[f]
        else: #CODE FOR FINDING WORDS
            l = 1
            solved = False
            while l < len(wordlist) and solved == False:
                r = wordlist[l]
                if p[f] == r[0]:
                    truths = 0
                    for j in range(0, len(r)): #this reads still but closer this time
                        if f+j < len(p):
                            if p[f+j] == r[j]:
                                truths += 1
                    if truths == len(r): # true when word matches the word list
                        code2[i] += str(l)
                        # f += j
                        solved = True # ends the truth checker
                l += 1
        f+=1

                    



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


