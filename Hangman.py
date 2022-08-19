#Hangman
print("\t\tWelcome to HANGMAN\n Guess each letter to build up your word. 10 trials lead to an excecution")
a='y'
words={0:'supercalifragilisticexpialidocious',8:'mozambique',2:'execution',4:'skyscraper',3:'aerodynamic',5:'clueless',6:'mythological',7:'rythmic',1:'avacado'}
while a.lower()=='y':
   c=int(input("Enter choice of level(1-8 or a bonus level 0) : "))
   while c not in range(0,9):
       c=int(input("Enter a valid level : "))
   ans=words[c]
   guessed=[]
   wrong=0
   while True:
    if guessed==[]:
        for i in ans:
            print('_',end=' ')
    if wrong==10:
        print("\n\t\tGAME OVER\n The word was ",ans)
        break
    g=input('\n\nEnter a letter : ').lower()
    while g in guessed:
        g=input("Enter another letter, you already tried that : ").lower()
    while not(g.isalpha()) or len(g)!=1:
       g=input("Enter a letter only : ")
    if g not in ans:
        wrong+=1
    guessed.append(g)
    print('wrong guesses :',wrong)
    if wrong==1:
        print("""












             _____________""")
    elif wrong==2:
        print("""   
                   |
                   |
                   |
                   |
                   |
                   |
                   |
                   |
                   |
                   | 
                   |
             ______|_______""")
    elif wrong==3:
        print("""
                    ____________
                   |
                   |
                   |
                   |
                   |
                   |
                   |
                   |
                   |
                   | 
                   |
             ______|_______""")
    elif wrong==4:
        print("""
                    ____________
                   |            |
                   |            |
                   |           
                   |
                   |
                   |
                   |
                   |
                   |
                   | 
                   |
             ______|_______""")
    elif wrong==5:
        print("""
                    ____________
                   |            |
                   |            |
                   |           ( )
                   |            |
                   |
                   |
                   |
                   |
                   |
                   | 
                   |
             ______|_______""")
    elif wrong==6:
        print("""
                    ____________
                   |            |
                   |            |
                   |           ( )
                   |            |
                   |           /|
                   |
                   |
                   |
                   |
                   | 
                   |
             ______|_______""")
    elif wrong==7:
        print("""
                    ____________
                   |            |
                   |            |
                   |           ( )
                   |            |
                   |           /|\\
                   |
                   |
                   |
                   |
                   | 
                   |
             ______|_______""")
    elif wrong==8:
        print("""
                    ____________
                   |            |
                   |            |
                   |           ( )
                   |            |
                   |           /|\\
                   |            | 
                   |
                   |
                   |
                   | 
                   |
             ______|_______""")
    elif wrong==9:
        print("""
                    ____________
                   |            |
                   |            |
                   |           ( )
                   |            |
                   |           /|\\
                   |            | 
                   |           /
                   |
                   |
                   | 
                   |
             ______|_______""")
    elif wrong==10:
        print("""
                    ____________
                   |            |
                   |            |
                   |           ( )
                   |            |
                   |           /|\\
                   |            | 
                   |           / \\
                   |
                   |
                   | 
                   |
             ______|_______""")
   
    count=0
    print()
    for i in ans:
        if i in guessed:
            print(i,end=' ')
            count+=1
        else:
            print('_',end=' ')
    print()
    if count==len(ans):
        print("\n\t\tYou won!\n\t")
        break
   a=input("\nDo you want to play again? (y/n) ")
else:
     print("\n\n\t\tGAME DESIGNED BY\n\t\tSumitha Harshita Tara")
     endtemp = str(input("Press the Enter key to exit"))
