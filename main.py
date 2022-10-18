import json
import webbrowser

a = []
n = 1
while(n != 0):
    with open('1.json') as json_file:
        data = json.load(json_file)
        d = data["results"]
        d = list(d)
        for i in range(len(d)):
            c = d[i]
            r = c["issue_cwe"]
            k = r["id"]
            a.append(k)

    b = set(a)
    c = list(b)
    print("Идентификаторы уязвимостей")
    for i in c:
        print(i)

    ans = ["да", "нет"]
    ans_n = "/".join(ans)
    print(f"Хотите ли вы узнать информацию о какой-нибудь уязвимости? {ans_n}")
    s = str(input())
    if (s == "да"):
        n = int(input("Введите идентификатор уязвимости для поиска информации:"))
        if (n in c):
            webbrowser.open(f"https://cwe.mitre.org/data/definitions/{n}.html")
        else:
            print("Такой уязвимости нет!")
    elif (s == "нет"):
        print("ОК!")
    else:
        print("???????")

    ans1 = ["да", "нет"]
    ans1_n = "/".join(ans1)
    print(f"Хотите ли вы продолжить работу с данным ПО?{ans1_n}")
    s = str(input("Введите ответ:"))
    if (s == ans1[0]):
        n += 1
    elif (s == ans1[1]):
        break
    else:
        print("Ничего непонятно")

print("Спасибо, что выбрали меня!")