from random import randint
def answer(num):
    if(num==1):
        return 'its certain'
    elif(num==2):
        return 'listen to your heart'
    elif(num==3):
        return 'ask again need to think '
    elif(num==4):
        return 'no action is the best action '
    elif(num==5):
        return 'sleep over it '
    elif(num==6):
        return 'no dont are you mad!!!'
    elif(num==7):
        return 'Whatever the heart says'
    
i=0
while(i<2):
    print('Ready to know your fate ?\n type your question !!:')
    x=input()
    r=randint(1,7)
    print(answer(r))
    print("\n To ask again press 1 :  \n To quit press two ")
    i=int(input())
