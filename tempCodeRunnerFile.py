import random
ll=int(input("enter lower limit here:"))
ul=int(input("enter upper limit here:"))
count=1
num=random.randrange(ll,ul)



while count<=7:
    num1=int(input("enter your guessed number here:"))
    if num1>num :
        print("AAiya,you guessed too high!,try again.")
    elif num1<num :
        print("AAiya,you guessed too low!,try again,")
    else:
        print("Hurrayh!you guessed it right.")
        break
    
    count+=1