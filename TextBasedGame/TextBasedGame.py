# dictionary imports

# A dictionary for the simplified dragon text game
rooms = {
        'Start': {'Start': 'Great Hall', 'Item': 'None'},
        'Great Hall': {'North': 'Kitchen', 'Item': 'None'},
        'Kitchen': {'South': 'Great Hall', 'Item': 'Whip'}
    }

# start inventory/collection
collection = []


def move_rooms(current_room, user_input):

    # possible directions
    navigation = ['Go North', 'Go South', 'Go East', 'Go West', 'Exit', 'Start']
    # what to print if incorrect command
    invalid_command = 'Please enter a valid command.'
    # what to print if direction not available for current room
    wrong_way = 'You bumped into a wall.'
    # define the room player is moving to 
    print('\n * * * * * * * * * * * * * * \n')

    if rooms[current_room]['Item'] != 'None':
        if rooms[current_room]['Item'] not in collection:
            print('You see {}.'.format(rooms[current_room]['Item']))
        else:
            pass
    else:
        pass
    user_input = input('What would you like to do? \n').title().split()
    if len(user_input) > 1:
        action = user_input[0]
        movement = user_input[1]
        if action == 'Get':
            action = 'Item'
            item_to_collect = movement
            get_item(current_room, action, item_to_collect)
        elif action == 'Go':
            if movement in rooms[current_room]:
                current_room = rooms[current_room][movement]
                print('You moved to the {}.'.format(current_room))
                return current_room
            elif movement not in rooms[current_room]:
                print(wrong_way)
            elif user_input not in navigation:
                print(invalid_command)
    else:
        print(invalid_command)
            
        return current_room


def get_item(current_room, action, item_to_collect):
    # list of items in the game
    items_list = ['Whip', 'Mead', 'Potion']
    # define new list elements if list length is greater than 1
    no_item = 'There are no item to pick up in this room.'
    not_in_game = 'This item does not exist in this game.'
    not_in_room = 'This item is not in your current room.'
    already_collected = 'You have already collected this item.'
    if action not in rooms[current_room]:
        print(no_item)
    elif item_to_collect not in rooms[current_room][action]:
        print(not_in_room)
    elif item_to_collect not in items_list:
        print(not_in_game)
    elif item_to_collect in collection:
        print(already_collected)
    elif item_to_collect not in collection:
        collection.append(item_to_collect)
        print('You added {} to your collection.'.format(item_to_collect))

    return move_rooms(current_room, user_input='')


def main():
    # Print intro
    print('Welcome to the Castle Keep Adventure! You are tasked with protecting the keep. \n')
    print('To move between rooms, enter a direction (North, South, East, West)! To exit the game, enter Exit.')
    
    # player start location
    current_room = 'Great Hall'
    print('You are in the {}.'.format(current_room))

    # While input is not equal to Exit game LOOP
    user_input = 'Start'
    while user_input != 'Exit':
        next_room = move_rooms(current_room, user_input)
        current_room = next_room

    print('Thanks for playing!')


if __name__ == "__main__":
    main()

