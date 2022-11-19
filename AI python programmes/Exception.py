a = 'ha'

try:
    if a%2 == 0:
        print("Good marks")
    else:
        print("Bad marks")
except:
    print("Invalid Input")



n = [10,20,30]

try:
    print("Third element in the list : %d" %(n[2]))

    print("Fourth element in the list : %d" %(n[3]))

except:
    print("Exception caught")
