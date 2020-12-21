def person(name,**data):
    print(name)

    for i,j in data.items():
        print(i,j)


person("sagar",age=23,city="Mumbai",mobile=7448230086)