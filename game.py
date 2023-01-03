import random
firstnum=1
lastnum=99
hads = int(random.randint(firstnum,lastnum))
print (hads)
javab=input("user guid: ")
while javab != 'd':
    #print("ghalate")
    #hads = int(random.randint(firstnum,lastnum))
    if javab=='b':
        #print("my number is bozorgtar")
        print("incorrect!! my number is higher than your guess :\) ")
        firstnum=hads
        hads=int(random.randint(firstnum,lastnum))
        print(hads)
        javab=input("user guid: ")
    #print(hads)
    elif(javab=='k'):
        print("incorrect!! my number is less than your guess :\) ")
        lastnum=hads
        hads=int(random.randint(firstnum,lastnum))
        print(hads)
        javab=input("user guid: ")
    #     print("Your Guss is Kochiktar")
    # firstnum=hads
    #hads=int(random.randint(firstnum,lastnum))
    elif(javab!='k' or javab!='b') :
        print('please just enter b or k or d!!')
        javab=input("user guid: ")

print('Hooooraaaa!!')