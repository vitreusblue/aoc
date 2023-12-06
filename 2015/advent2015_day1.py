# FINISH DATE: Dec/3/2023

floor = 0
while True:
    code = input('enter the code\n')
    for i in range(0, len(code)):
        if code[i] == ('('):
            floor += 1
        if code[i] == (')'):
            floor -= 1
    print(floor)


