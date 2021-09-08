"""
    Main procedure of the pokemon game
"""
import csv
from random import randint
from random import seed
from copy import deepcopy

from pokemon import Pokemon
from pokemon import Move

seed(1)  # Set the seed so that the same events always happen

# DO NOT CHANGE THIS!!!
# =============================================================================
element_id_list = [None, "normal", "fighting", "flying", "poison", "ground", "rock",
                   "bug", "ghost", "steel", "fire", "water", "grass", "electric",
                   "psychic", "ice", "dragon", "dark", "fairy"]


# Element list to work specifically with the moves.csv file.
#   The element column from the moves.csv files gives the elements as integers.
#   This list returns the actual element when given an index
# =============================================================================

def read_file_moves(fp):
    '''
        takes in the file pointer created from opening the moves.csv file and
        returns a list of move objects
    '''
    moves = list()
    reader = csv.reader(fp)     # readin csv datas
    header = None
    for row in reader:
        if not row[0].isdigit():
            header = row    # ignore the first row
        else:
            # ignore rules
            if row[header.index("generation_id")] != "1":
                continue
            if row[header.index("damage_class_id")] == "1":
                continue
            if not row[header.index("power")]:
                continue
            if not row[header.index("accuracy")]:
                continue

            # add move
            name = row[header.index("identifier")]  # name
            element = row[header.index("type_id")]  # element
            element = element_id_list[int(element)]
            power = int(row[header.index("power")])  # power
            accuracy = int(row[header.index("accuracy")])  # accuracy
            attack_type = int(row[header.index("damage_class_id")])  # attack_type
            moves.append(Move(name, element, power, accuracy, attack_type))
    return moves


def read_file_pokemon(fp):
    '''
        takes in the file pointer created from opening the pokemon.csv file and
        returns a list of pokemon objects
    '''
    pokemons = list()
    reader = csv.reader(fp)
    header = None
    ids = set()     # avoid repeated id
    for row in reader:
        if not row[0].isdigit():
            header = row    # ignore the first row
        else:
            # ignore rules
            if row[header.index("Generation")] != "1":
                continue
            id = row[header.index("#")]
            if id in ids:
                continue
            else:
                ids.add(id)
            # add to pokemons
            name = row[header.index("Name")].lower()  # name in lower case
            element1 = row[header.index("Type 1")].lower()  # element in lower case
            element2 = row[header.index("Type 2")].lower()
            hp = int(row[header.index("HP")])   # hp
            patt = int(row[header.index("Attack")])   # patt
            pdef = int(row[header.index("Defense")])   # pdef
            satt = int(row[header.index("Sp. Atk")])   # satt
            sdef = int(row[header.index("Sp. Def")])   # sdef
            pokemons.append(Pokemon(name, element1, element2, moves=None, hp=hp,
                                    patt=patt, pdef=pdef, satt=satt, sdef=sdef))
    return pokemons


def choose_pokemon(choice, pokemon_list):
    '''
        takes in user input (called choice) as a string and the list of available
        pokemon
    '''
    if type(choice) == int:
        if choice > len(pokemon_list):  # out of range
            return None
        return deepcopy(pokemon_list[choice - 1])
    else:
        if choice.isdigit():
            choice = int(choice)
            if choice > len(pokemon_list):  # out of range
                return None
            return deepcopy(pokemon_list[choice - 1])

        for pokemon in pokemon_list:
            if pokemon.get_name() == choice.lower():
                return deepcopy(pokemon)
        else:
            return None


def add_moves(pokemon, moves_list):
    '''
        first adds one random move to the pokemon’s move list
        then adds three more moves that match one of the elements of this pokemon
    '''
    # add first random move
    index = randint(0, len(moves_list) - 1)
    pokemon.add_move(moves_list[index])
    # try 200 attempts
    for _ in range(200):
        index = randint(0, len(moves_list) - 1)
        move = moves_list[index]
        element = move.get_element()
        if move not in pokemon.get_moves() and element in [pokemon.element1, pokemon.element2]:
            pokemon.add_move(move)
            if pokemon.get_number_moves() == 4:
                return True
    return False


def turn(player_num, player_pokemon, opponent_pokemon):
    '''
        Player_num is an int for printing which player: 1 or 2
    '''
    oppo = 1 if player_num == 2 else 2

    print("Player {}'s turn".format(player_num))
    print(player_pokemon)
    while True:
        print("Show options: 'show ele', 'show pow', 'show acc'")
        ch = input("Select an attack between 1 and {} or show option or 'q': ".format(
            player_pokemon.get_number_moves()))
        if ch.lower() == 'q':
            print("Player {} quits, Player {} has won the pokemon battle!".format(player_num, oppo))
            return False
        elif ch.lower() == "show ele":
            player_pokemon.show_move_elements()
        elif ch.lower() == "show pow":
            player_pokemon.show_move_power()
        elif ch.lower() == "show acc":
            player_pokemon.show_move_accuracy()
        else:
            move = player_pokemon.choose(int(ch) - 1)
            print("selected move:", move)
            print()
            print("{} hp before:{}".format(opponent_pokemon.get_name(), opponent_pokemon.get_hp()))
            player_pokemon.attack(move, opponent_pokemon)
            print("{} hp after:{}".format(opponent_pokemon.get_name(), opponent_pokemon.get_hp()))
            print()
            if opponent_pokemon.get_hp() <= 0:
                print("Player {}'s pokemon fainted, Player {} has won the pokemon battle!".format(
                    oppo, player_num))
                return False
            return True


def main():
    # read in datas
    moves_list = read_file_moves(open("moves.csv", "r", encoding="utf-8"))
    pokemon_list = read_file_pokemon(open("pokemon.csv", "r", encoding="utf-8"))

    # prompt
    usr_inp = input("Would you like to have a pokemon battle? ").lower()
    while True:
        while usr_inp != 'n' and usr_inp != 'q' and usr_inp != 'y':
            usr_inp = input("Invalid option! Please enter a valid choice: Y/y, N/n or Q/q: ").lower()

        if usr_inp != 'y':
            # quit
            print("Well that's a shame, goodbye")
            return
        else:
            # prepare battle
            player_num = 1
            player_pokemon = None
            while not player_pokemon:
                ch = input("Player {}, choose a pokemon by name or index: ".format(player_num))
                print("pokemon{}:".format(player_num))
                player_pokemon = choose_pokemon(ch, pokemon_list)
            print(str(player_pokemon))
            flag = add_moves(player_pokemon, moves_list)
            if not flag:
                return

            opponent_num = 2
            opponent_pokemon = None
            while not opponent_pokemon:
                ch = input("Player {}, choose a pokemon by name or index: ".format(opponent_num))
                print("pokemon{}:".format(opponent_num))
                opponent_pokemon = choose_pokemon(ch, pokemon_list)
            print(str(opponent_pokemon))
            flag = add_moves(opponent_pokemon, moves_list)
            if not flag:
                return

            # start battle
            go = True
            while go:
                if not turn(player_num, player_pokemon, opponent_pokemon):
                    break

                if not turn(opponent_num, opponent_pokemon, player_pokemon):
                    break

                print("Player {} hp after: {}".format(player_num, player_pokemon.get_hp()))
                print("Player {} hp after: {}\n".format(opponent_num, opponent_pokemon.get_hp()))

            usr_inp = input("Battle over, would you like to have another? ").lower()


if __name__ == "__main__":
    main()