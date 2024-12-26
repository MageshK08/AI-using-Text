'''Prime number'''
Num=int(input("Enter a number:"))
if Num<2:
    print("Not prime")
else:
    c=2
    while c*c<=Num:
        if Num%c==0:
            print("Not Prime")
            break
        c+=1
    else:
        print("Prime")
