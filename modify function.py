def div(a,b):
    if(b==0):
       return print("this is not possible")
    else:
       c=a/b
       return print(c)

a = input('enter any value')
b = input("enter the second value")
div(int(a),int(b))
