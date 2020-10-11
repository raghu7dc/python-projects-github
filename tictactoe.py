theBoard={
    "9":" ","8":" ","7":" ",
    "6":" ","5":" ","4":" ",
    "3":" ","2":" ","1":" "
}

def drawboard(board):
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print('-+-+-')
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print('-+-+-')
    print(board['1']+'|'+board['2']+'|'+board['3'])


board_key=[]
for key in theBoard:
    board_key.append(key)

def game():
    turn='x'
    count=0

    for i in range(10):
        drawboard(theBoard)
        print("it's your move "+turn+"choose your loaction")
        move=input('choose location: ')

        if theBoard[move]==' ':
            theBoard[move]=turn
            count+=1
        else:
            print("the  location is  already filled \n choose another")
            continue

        if count>=5:
            if theBoard['7']==theBoard['8']==theBoard['9']!=' ':
                drawboard(theBoard)
                print("game over \n player"+ turn + "has won")
                break
            elif theBoard['4']==theBoard['5']==theBoard['6']!=' ':
                drawboard(theBoard)
                print("game over \n player"+ turn + "has won")
                break
            elif theBoard['1']==theBoard['2']==theBoard['3']!=' ':
                drawboard(theBoard)
                print("game over \n player"+ turn + "has won")
                break
            elif theBoard['7']==theBoard['4']==theBoard['1']!=' ':
                drawboard(theBoard)
                print("game over \n player"+ turn + "has won")
                break
            elif theBoard['5']==theBoard['8']==theBoard['2']!=' ':
                drawboard(theBoard)
                print("game over \n player"+ turn + "has won")
                break
            elif theBoard['3']==theBoard['6']==theBoard['9']!=' ':
                drawboard(theBoard)
                print("game over \n player"+ turn + "has won")
                break
            elif theBoard['7']==theBoard['5']==theBoard['3']!=' ':
                drawboard(theBoard)
                print("game over \n player"+ turn + "has won")
                break
            elif theBoard['9']==theBoard['5']==theBoard['1']!=' ':
                drawboard(theBoard)
                print("game over \n player"+ turn + "has won")
                break

        if count==9:
            print('game over \n it is a tie')

        if turn=='x':
            turn='0'
        else:
            turn='x'

    restart=input('do you wanna start again:(y/n): ')
    if restart=="y":
        for key in board_key:
            theBoard[key]=" "

        game()
    else:
        exit()

game()

