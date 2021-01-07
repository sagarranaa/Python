available_candy = 5
x = int(input("How much candy you want ?:"))
i = 1
while i < x:
    if i > available_candy:
        print("Sorry sir we are out of stuck!")
        break
    print("Candy")
    i = i + 1

print("Byyeee visit again nice to meet you sir !")
