while True:
    FirstSym = []
    SecondSym = []
    Znak = []
    print("Введите выражение")
    stroka = (input())
    for i in range(len(stroka)):
        if stroka[i] == '*' or stroka[i] == '/' or stroka[i] == '+' or stroka[i] == '-':
            Znak = stroka[i]
            break
        FirstSym.append(stroka[i])
    FirstChislo = int(''.join((str(j) for j in FirstSym)))

    for i in range(stroka.find(Znak), len(stroka)):
        SecondSym.append(stroka[i])
    SecondChislo = int(''.join((str(j) for j in SecondSym))) 

    if Znak == '+':
        print(FirstChislo + SecondChislo)
    if Znak == '-': 
        print(FirstChislo - SecondChislo)
    if Znak == '*':
        print(FirstChislo * SecondChislo)
    if Znak == '/':
        print(FirstChislo / SecondChislo)
    print("Хотите выйти? (да/нет)")
    answer = input(str())
    if answer == "да":
        break