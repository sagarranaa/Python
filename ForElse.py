num=[10,16,18,21,26,22]
for i in num:
    if(i%5==0):
        print(i)
        # we don't want print next divisible 5 use break statement
        break
else:
    print("Not Found")