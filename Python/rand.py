import random, sys 

for i in range(0, 9999) : 
    random.seed(i)
    myRandom = ""

    for j in range(0, 10) : 
        myRandom += str(random.randint(0, 9))
        if(myRandom == "6408348426") :
            print("seed =" + str(i))
            sys.exit(0)