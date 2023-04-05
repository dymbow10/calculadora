def soma(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    if (b != 0):
        return a/b
    else:
        return "Error"

def pow(a,b):
    return a**b
    
def mod(a,b):
    return a%b

def fac(a):
    if (a<0):
        return "Error"
    elif (a==1 or a==0):
        return 1
    else:
        return a * fac(a-1)