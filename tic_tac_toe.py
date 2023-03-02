class game:    
    def __init__(self): 
        user1 = input("What's player #1 name: ")
        user2 = input("What's player #2 name: ")
        listOfgrid =[["|",1,"|",2,"|",3,"|"],
                    ["|",4,"|",5,"|",6,"|"],
                    ["|",7,"|",8,"|",9,"|"]]
        def printGrid():
            for i in range(len(listOfgrid[0])):
                print(listOfgrid[0][i],end='')
            print('\r')
            for i in range(len(listOfgrid[0])):
                print(listOfgrid[1][i],end='')
            print('\r')
            for i in range(len(listOfgrid[0])):
                print(listOfgrid[2][i],end='')
            print('\r')
        def user1Input():
            inputStr = user1 + ", please choose your number to play:"
            a = input(inputStr)
            a = int(a)
            if a > 9 or a < 1:
                print(a,"is not a valid number!")
                user1Input()
            else:
                for i in range(len(listOfgrid)):
                    if a in listOfgrid[i]:
                        listOfgrid[i][listOfgrid[i].index(a)] = 'X' 
        def user2Input():
            inputStr = user2 + ", please choose your number to play:"
            a = input(inputStr)
            a = int(a)
            if a > 9 or a < 1:
                print(a,"is not a valid number!")
                user2Input()
            else:
                for i in range(len(listOfgrid)):
                    if a in listOfgrid[i]:
                        listOfgrid[i][listOfgrid[i].index(a)] = 'O' 
        def main():
            printGrid()
            x = 0
            while x < 5:
                user1Input()
                printGrid()
                if listOfgrid[0][1] == 'X' and listOfgrid[0][3] == 'X' and listOfgrid[0][5] == 'X':
                    print("CONGRATULATIONS",user1,"! You WON!")
                    break
                elif listOfgrid[1][1] == 'X' and listOfgrid[1][3] == 'X' and listOfgrid[1][5] == 'X':
                    print("CONGRATULATIONS",user1,"! You WON!")
                    break
                elif listOfgrid[2][1] == 'X' and listOfgrid[2][3] == 'X' and listOfgrid[2][5] == 'X':
                    print("CONGRATULATIONS",user1,"! You WON!")
                    break
                elif listOfgrid[0][1] == 'X' and listOfgrid[1][1] == 'X' and listOfgrid[2][1] == 'X':
                    print("CONGRATULATIONS",user1,"! You WON!")
                    break
                elif listOfgrid[0][3] == 'X' and listOfgrid[1][3] == 'X' and listOfgrid[2][3] == 'X':
                    print("CONGRATULATIONS",user1,"! You WON!")
                    break
                elif listOfgrid[0][5] == 'X' and listOfgrid[1][5] == 'X' and listOfgrid[2][5] == 'X':
                    print("CONGRATULATIONS",user1,"! You WON!")
                    break
                elif listOfgrid[0][1] == 'X' and listOfgrid[1][3] == 'X' and listOfgrid[2][5] == 'X':
                    print("CONGRATULATIONS",user1,"! You WON!")
                    break
                elif listOfgrid[0][5] == 'X' and listOfgrid[1][3] == 'X' and listOfgrid[2][1] == 'X':
                    print("CONGRATULATIONS",user1,"! You WON!")
                    break
                if x == 4:
                    print("It's a tie! Nobody is winner!")
                    break
                user2Input()
                printGrid()
                if listOfgrid[0][1] == 'O' and listOfgrid[0][3] == 'O' and listOfgrid[0][5] == 'O':
                    print("CONGRATULATIONS",user2,"! You WON!")
                    break
                elif listOfgrid[1][1] == 'O' and listOfgrid[1][3] == 'O' and listOfgrid[1][5] == 'O':
                    print("CONGRATULATIONS",user2,"! You WON!")
                    break
                elif listOfgrid[2][1] == 'O' and listOfgrid[2][3] == 'O' and listOfgrid[2][5] == 'O':
                    print("CONGRATULATIONS",user2,"! You WON!")
                    break
                elif listOfgrid[0][1] == 'O' and listOfgrid[1][1] == 'O' and listOfgrid[2][1] == 'O':
                    print("CONGRATULATIONS",user2,"! You WON!")
                    break
                elif listOfgrid[0][3] == 'O' and listOfgrid[1][3] == 'O' and listOfgrid[2][3] == 'O':
                    print("CONGRATULATIONS",user2,"! You WON!")
                    break
                elif listOfgrid[0][5] == 'O' and listOfgrid[1][5] == 'O' and listOfgrid[2][5] == 'O':
                    print("CONGRATULATIONS",user2,"! You WON!")
                    break
                elif listOfgrid[0][1] == 'O' and listOfgrid[1][3] == 'O' and listOfgrid[2][5] == 'O':
                    print("CONGRATULATIONS",user2,"! You WON!")
                    break
                elif listOfgrid[0][5] == 'O' and listOfgrid[1][3] == 'O' and listOfgrid[2][1] == 'O':
                    print("CONGRATULATIONS",user2,"! You WON!")
                    break
                if x == 4:
                    print("Tie!")
                    break
                x = x + 1
        main()
playAgain = "1"
while playAgain == "1":
    newGame = game()
    playAgain = input("Would you like to play this game again?\n[1] yes \n[2] no \nEnter your choice:")
    if playAgain == "1":
        continue
    elif playAgain == "2":
        print("Thank you and see you later!")
        break