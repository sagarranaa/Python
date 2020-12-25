# there are threee type of exception
# Runtime error
# compile time
# logical error


a=5
b=9
try:
    print(a/b)
    print("resource open")
except Exception as e:  # expception block will not when above block is correct  else it will show you below statement
    print(a+b)
    print("resource is close")
finally: # finally block will run if you above statement is correct or not
    print(a%b)