# in decorators we can change behaviours of existing function in run time or compile time

def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        # then apply over here logic
        if a<b:
            a,b=b,a
            return func(a,b)
    return inner



div=smart_div(div)

div(2,4)