

board =[" " for x in range (10)]
def insertletters(letter,pos):
    board[pos]=letter

def spaceIsFree(pos):
    return board[pos]==" "

def printBoard(board): #printing board
    print('   |   |')
    print(' '+ board[1] +' | '+ board[2] +' | '+ board[3])
    print('   |   |')
    print('-----------')
    print(' '+ board[4] +' | '+ board[5] +' | '+ board[6])
    print('   |   |')
    print('-----------')
    print(' '+ board[7] +' | '+ board[8] +' | '+ board[9])
    print('   |   |')

def IsWinner (bo, le):
    return (bo[7]==le and bo[8]==le and bo[9]==le)or(bo[4]==le and bo[5]==le and bo[6]==le)or(bo[1]==le and bo[2]==le and bo[3]==le)or(bo[1]==le and bo[4]==le and bo[7]==le)or(bo[2]==le and bo[5]==le and bo[8]==le)or(bo[3]==le and bo[6]==le and bo[9]==le)or(bo[1]==le and bo[5]==le and bo[9]==le)or(bo[3]==le and bo[5]==le and bo[7]==le)


def IsBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def playerMove():
    run = True
    while run:
        move= input('Please select a position to place an \'X\' (1-9): ')
        try:
            move=int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertletters('X',move)
                else:
                    print("space is occupied")
            else:
                print("Please type a number within range ")

        except:
            print("Please type a number")


def compMove():
    PossibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x!=0]
    move = 0

    for let in ['O','X']:
        for i in PossibleMoves:
            boardCopy = board[:]
            boardCopy[i]=let
            if IsWinner(boardCopy,let):
                move=i
                return move
    
    cornerOpen =[]
    for i in PossibleMoves:
        if i in [1,3,7,9]: 
            cornerOpen.append(i)
    if len(cornerOpen)> 0:
        move = selectRandom(cornerOpen)
        return move
    if 5 in PossibleMoves:
        move = 5
        return move


    edgesOpen =[]
    for i in  PossibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen)> 0:
        move = selectRandom(edgesOpen)


def selectRandom(li):
    import random
    ln=len(li) 
    r = random.randrange(0,ln)
    return li[r]
    


def main():
    print("Welcome to Tic Tac Toe :)")
    printBoard(board)
    while not(IsBoardFull(board)):
        if not (IsWinner(board,'O')):
            playerMove()
            printBoard(board)
        else:
            print( "Sorry O\'s won this time!")
            break

        if not (IsWinner(board,'X')):
            move =compMove()
            if move == 0:
                print("Tie Game")
            else:
                insertletters('O',move)
                print('Computer placed an \'O\' in position',move,':')
                printBoard(board)
        else:
            print( "Sorry X\'s won this time, Good Job !")
            break


    if IsBoardFull(board):
        print("Tie Game")

main()