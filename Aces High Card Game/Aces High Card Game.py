

import cards 

RULES = '''
Aces High Card Game:
     Tableau columns are numbered 1,2,3,4.
     Only the card at the bottom of a Tableau column can be moved.
     A card can be moved to the Foundation only if a higher ranked card 
        of the same suit is at the bottom of another Tableau column.
     To win, all cards except aces must be in the Foundation.'''

MENU = '''     
Input options:
    D: Deal to the Tableau (one card on each column).
    F x: Move card from Tableau column x to the Foundation.
    T x y: Move card from Tableau column x to empty Tableau column y.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
'''


def init_game():
   

    stock = cards.Deck()
    tableau = [[], [], [], []]
    

    stock.shuffle()
    for col in tableau:
        card1 = stock.deal()
        col.append(card1)

    return stock, tableau, 


def deal_to_tableau(stock, tableau):
    

    tableau[0].append(stock.deal())
    tableau[1].append(stock.deal())
    tableau[2].append(stock.deal())
    tableau[3].append(stock.deal())

def display(stock, tableau, foundation):
   

    print("\n{:<8s}{:^13s}{:s}".format("stock", "tableau", "  foundation"))

    max_rows = 0
    for col in tableau:
        if len(col) > max_rows:
            max_rows = len(col)

    for i in range(max_rows):

        if i == 0:
            display_char = "" if stock.is_empty() else "XX"
            print("{:<8s}".format(display_char), end='')
        else:
            print("{:<8s}".format(""), end='')


        for col in tableau:
            if len(col) <= i:
                print("{:4s}".format(''), end='')
            else:
                print("{:4s}".format(str(col[i])), end='')

        if i == 0:
            if len(foundation) != 0:
                print("    {}".format(foundation[-1]), end='')

        print()


def get_option():
   
    command = input("\nInput an option (DFTRHQ): ")
    option = command.strip().split()

    if not option:
        print("Invalid option.")
        return
    elif len(option) == 1:

        if option[0].upper() not in 'DRHQ':
            print("Error in option:", command)
            print("Invalid option.")
            return
    elif len(option) == 2:

        if option[0].upper() != 'F':
            print("Error in option:", command)
            print("Invalid option.")
            return

        if not option[1].isdigit():
            print("Error in option:", command)
            print("Invalid option.")
            return

        if not 1 <= int(option[1]) <= 4:
            print("Error in option:", command)
            print("Invalid option.")
            return
    elif len(option) == 3:

        if option[0].upper() != 'T':
            print("Error in option:", command)
            print("Invalid option.")
            return

        if not option[1].isdigit() or not option[2].isdigit():
            print("Error in option:", command)
            print("Invalid option.")
            return

        if not 1 <= int(option[1]) <= 4 or not 1 <= int(option[2]) <= 4:
            print("Error in option:", command)
            print("Invalid option.")
            return
    else:
        print("Error in option:", command)
        print("Invalid option.")
        return

    return option


def validate_move_to_foundation(tableau, from_col):
    

    if not isinstance(from_col, int):
        return False
    if not 1 <= from_col <= 4:
        return False

    if not tableau[from_col - 1]:
        print("Error, empty column:", from_col)
        return False
    
    card_move = tableau[from_col - 1][-1]
    if card_move.rank() == 1:
        print("Error, cannot move {}.".format(card_move))
        return False

    for column in range(1, 5):
        if column == from_col:
            continue
    
        if not tableau[column - 1]:
            continue
        card1 = tableau[column - 1][-1]
        
        if not card1.suit() == card_move.suit():
            continue
        
        if card1.rank() == 1:
            return True
        elif card1.rank() > card_move.rank():
            return True

    print("Error, cannot move {}.".format(card_move))
    return False


def move_to_foundation(tableau, foundation, from_col):

    valid_bool = validate_move_to_foundation(tableau, from_col)
    if valid_bool:
        
        card1 = tableau[from_col - 1].pop()
        foundation.append(card1)


def validate_move_within_tableau(tableau, from_col, to_col):
    

    if not type(from_col) == int or not type(to_col) == int:
        return False

    if not 1 <= from_col <= 4 or not 1 <= to_col <= 4:
        return False



    to_ = tableau[to_col - 1]
    if to_:
        print("Invalid move")
        return False

    from_ = tableau[from_col - 1]
    if not from_:
        print("Error, empty column:", from_col)
        return False

    return True


def move_within_tableau(tableau, from_col, to_col):
   

    valid_bool = validate_move_within_tableau(tableau, from_col, to_col)
    if valid_bool:
        card = tableau[from_col - 1].pop()
        tableau[to_col - 1].append(card)


def check_for_win(stock, tableau):
    
  
    if stock.is_empty():
      
        win = True
        for column in tableau:
            if not len(column) == 1 or not column[0].rank() == 1:
                win = False
                break
        return win
    return False


def main():
   

    stock, tableaun = init_game()

    print(MENU)
    display(stock, tableau )

    while True:

        option = get_option()
        if not option:
            display(stock, tableau)
            continue
        cmd = option[0].upper()
        if cmd == 'D':

            deal_to_tableau(stock, tableau)
        elif cmd == 'F':

            from_col = int(option[1])
            move_to_foundation(tableau,  from_col)
        elif cmd == 'T':

            from_col = int(option[1])
            to_col = int(option[2])
            move_within_tableau(tableau, from_col, to_col)
        elif cmd == 'R':

            print("=========== Restarting: new game ============")
            
            stock, tableau = init_game()
            print(RULES)
            print(MENU)
            display(stock, tableau, )
            continue
        elif cmd == 'H':
           
            print(MENU)
        elif cmd == 'Q':
            print("You have chosen to quit.")
            break

        win = check_for_win(stock, tableau)
        if win:
            print("You won!")
            break
        display(stock, tableau, foundation)


if __name__ == "__main__":
    main()
