# Tina Velez-Grey
# 14 October 2023

# Text Based Adventure Game: Protect the Keep!

# player inventory/collection
collection = []

# rooms dictionary
rooms = {
    'Training Room': {'south': 'Armory', 'Item': 'crossbow'},
    'Alchemy Lab': {'west': 'Library', 'Item': 'healing potion'},
    'Library': {'south': 'Main Hall', 'east': 'Alchemy Lab', 'Item': 'alarm'},
    'Main Hall': {'north': 'Library', 'west': 'Courtyard', 'east': 'Armory', 'south': 'Mess Hall'},
    'Armory': {'north': 'Training Room', 'west': 'Main Hall', 'Item': 'crossbow bolts'},
    'Mess Hall': {'west': 'Barracks', 'east': 'Kitchen', 'north': 'Main Hall', 'Item': 'mead'},
    'Barracks': {'north': 'Courtyard', 'east': 'Mess Hall', 'Item': 'armor'},
    'Kitchen': {'west': 'Mess Hall'},
    'Courtyard': {'exit': 'exit'}
}

# movement list and move error messages
navigation = ['north', 'south', 'east', 'west']
invalid_command = 'Please enter a valid command.'
wrong_way = 'You bumped into a wall.'

# items list and item error messages
items_list = ['crossbow', 'healing potion', 'crossbow bolts', 'alarm', 'mead', 'armor']
no_item = 'There are no items to pick up in this room.'
not_in_game = 'This item does not exist in this game.'
not_in_room = 'This item is not in your current room.'
already_collected = 'You have already collected this item.'


def move_rooms(current_room, movement):
    if movement in navigation:
        if movement not in rooms[current_room]:
            print(wrong_way)
        elif movement in rooms[current_room]:
            current_room = rooms[current_room][movement]
            print('You moved to the {}.'.format(current_room))
    else:
        print(invalid_command)

    return current_room


def get_item(current_room, item_to_collect):
    if item_to_collect not in items_list:
        print(not_in_game)
    elif 'Item' not in rooms[current_room]:
        print(no_item)
    elif item_to_collect not in rooms[current_room]['Item']:
        print(not_in_room)
    elif item_to_collect in collection:
        print(already_collected)
    elif item_to_collect not in collection:
        collection.append(item_to_collect)
        print('You added {} to your collection.'.format(item_to_collect))
        print('Your collection contains:', ', '.join(collection))
        print('You need', 6 - len(collection), 'more items before facing the Troll.')

    return current_room


def main():
    # Print intro & instructions
    print('Welcome to the Castle Keep Adventure! You are tasked with protecting the keep.')
    print('Collect 6 items before facing against the Troll Boss in the Courtyard or you will be defeated! \n')
    print('Move commands: go South, go North, go East, go West')
    print("Add to Collection: get 'item name'")
    print('To end the game, type Exit. \n')

    # player start location
    current_room = 'Kitchen'
    print('You are in the {}.'.format(current_room))
    # user input variable
    user_input = ''

    # Game LOOP
    while user_input != 'exit' and current_room != 'exit':
        # does the room have an item?
        if 'Item' in rooms[current_room]:
            # is the room's item already in the player's collection?
            if rooms[current_room]['Item'] in collection:
                pass
            else:
                print('You see {}.'.format(rooms[current_room]['Item']))
        else:
            pass
        # Line Break for ease of reading
        print('* - * - * - * - * - * - * ')
        user_input = input('What would you like to do? \n').lower().split()
        print()
        if user_input[0] == 'exit':
            break
        elif user_input[0] == 'go':
            current_room = move_rooms(current_room, user_input[1])
        elif user_input[0] == 'get':
            get_item(current_room, ' '.join(user_input[1:]))
        else:
            print(invalid_command)
        # Troll/Boss location and collection check
        if current_room == 'Courtyard':
            user_input = 'exit'
            if len(collection) < 6:
                # Line Break for ease of reading
                print('* - * - * - * - * - * - * ')
                print('You did not collect all of the items and the Troll smashed you!')
            else:
                print('You defeated the Troll and saved the keep!')
        else:
            pass

    # on user exit offer to play again, clear collection and restart
    user_exit = input('Do you want to play again? [Y/N] \n').lower()
    if user_exit == 'y':
        del collection[:]
        main()
    else:
        print('Thanks for playing!')


if __name__ == "__main__":
    main()
