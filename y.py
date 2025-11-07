x=[1,2,3,4,5]
y=[6,7,8,9,10]
a=0
b=0
for i in x:
    for j in y:
        print(x[a],y[b])
        b+=1
    a+=1
    b=0