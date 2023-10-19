def most(x,y):
    if(x>y):
        return x
    else:
        return y
def least(x,y):
    if(x<y):
        return x
    else:
        return y

x = int(input("Un numero: "))
y = int(input("Otro Numero: "))
print(most(x-3,least(x+2, y-5)))