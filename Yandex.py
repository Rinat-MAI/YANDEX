N = int(input())
A = []
def SummaDigit(s):
    summadig = 0
    for c in s:
        summadig += int(c)
    return summadig
for i in range(N):
    surname, name, patronymic, day, month, year = input().split(',')
    summa = len(set(surname+name+patronymic)) + SummaDigit(day+month)*64 + (ord(surname[0]) - 64)*256
    s = hex(summa).upper()
    if len(s) >= 3:
        s = s[-3:]
    else:
        s = '0'*(3-len(s)) + s
    A.append(s)
print(*A)