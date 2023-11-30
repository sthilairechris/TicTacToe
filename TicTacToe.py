import random
#importing a different code - random is a random set of intergers

def Place(board, symbol, x, y):
    if board[x][y] == ' ':
        board[x][y] = symbol
        return True
    else:
        return False

def Checkforwin(board, symbol):
    Correct_answers = [[0,0,1,1,2,2],[2,0,1,1,0,2],[0,0,0,1,0,2],[1,0,1,1,1,2],[2,0,2,1,2,2],[0,0,1,0,2,0],[0,1,1,1,2,1],[0,2,1,2,2,2]]
    for answer in Correct_answers:
        
        if board[answer[0]][answer[1]] == symbol and board[answer[2]][answer[3]] == symbol and board[answer[4]][answer[5]] == symbol:
            print('\n'*3)
            print_board(board)
            print(f'{symbol} WON!')
            exit()

def print_board(board):
    print('\n'*2)
    #Add print numbers
    #Use braces to get value from variable
    print('   1|    2|    3')
    print(f' {board[0][0]}  | {board[1][0]}   | {board[2][0]}') 
    #Where the functions are able to be input
    print('    |     |')
    print('-' *15)
    print('   4|    5|    6')
    print(f' {board[0][1]}  | {board[1][1]}   | {board[2][1]}')
    print('    |     |')
    print('-' *15)
    print('    |     |')
    print(f' {board[0][2]}  | {board[1][2]}   | {board[2][2]}')
    print('   7|    8|    9')
    
def Move(symbol, board):
    move_success = False

    #While for when we don't know how many times we're looping
    while not move_success:
        if symbol == 'X':
            user_input = input('Enter an option: 1 - 9 \nOr press x to exit:  ')
            if user_input == 'x':
                print()
                print('Goodbye!')
                exit()
        else:
            user_input = f'{random.randint(1,9)}'

        match user_input:
            case '1': 
               move_success = Place(board, symbol, 0,0)
            case '2': 
               move_success = Place(board, symbol, 1,0)
            case '3': 
               move_success = Place(board, symbol, 2,0)
            case '4': 
               move_success = Place(board, symbol, 0,1)
            case '5': 
               move_success = Place(board, symbol, 1,1)
            case '6': 
               move_success = Place(board, symbol, 2,1)
            case '7': 
               move_success = Place(board, symbol, 0,2)
            case '8': 
               move_success = Place(board, symbol, 1,2)
            case '9': 
               move_success = Place(board, symbol, 2,2)
            case _: 
                gamerunning = False

def single_player_game():
    gamerunning = True
    player_1 = 'X'
    computer = 'O'
    rows, cols = (3, 3)
    board = [[' ' for _ in range(cols)] for _ in range(rows)]

    while gamerunning:

        print_board(board)
        Checkforwin(board, player_1)
        Checkforwin(board, computer)
        #Would check every 2 turns
    
        Move(player_1, board)
                    
        Checkforwin(board, player_1)
        Checkforwin(board, computer)
        #Placed here so it checks for wins on every turn

        Move(computer, board)

Menu_options = ('1', 'x')


def main():
    while True:
        print()
        print('*** MENU ***')
        print('1 = 1 Player')
        print('x = Exit')

        print()
        user_input = input('Enter an option: ')

        if user_input not in Menu_options:
            print()
            print('OPTION NOT AVAILABLE')

        elif user_input == '1':
            print()
            single_player_game()

        elif user_input == 'x':
            print()
            print('Goodbye!')
            exit()


if __name__ == "__main__":
    main()
