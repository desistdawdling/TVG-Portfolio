# dictionary imports
import game_rooms
import game_items

# A dictionary for the simplified dragon text game

# start inventory/collection
collection = []

def move_rooms(current_room, movement):
    # possible directions
    navigation = ['Go North', 'Go South', 'Go East', 'Go West', 'Exit', 'Start Over']
    # what to print if incorrect command
    invalid_command = 'Please enter a valid command.'
    # what to print if direction not available for current room
    wrong_way = "You bumped into a wall.
    # define the room player is moving to 
    next_room = current_room
    print('You are in the {}.'.format(current_room))
    if 'Item' in rooms[current_room]:
        print('You see {}.'.format(rooms[current_room['Item']))
    else:
        pass
    user_input = input('What would you like to do?').split().title()
    if len(user_input) > 1:
        action = user_input[0]
        movement = user_input[1]
        if action == 'Get':
            movement == item_to_collect
            get_item(current_room, item_to_collect)
        elif action == 'Go':
            if movement in rooms[current_room]:
                next_room = rooms[current_room][movement]
                print('You moved to the {}.'.format(next_room))
                print('* * * * * * * * * * * * * * * * * * * *')
            elif movement not in navigation:
                print(invalid_command)
            elif movement not in rooms[current_room]:
                print(wrong_way)


def get_item(current_room, item_to_collect)
    # define new list elements if list length is greater than 1
    no_item = 'There are no item to pick up in this room.'
    not_in_game = 'This item does not exist in this game.'
    not_in_room = 'This item is not in your current room.'
    already_collected = 'You have already collected this item.'
    if 'Item' not in rooms[current_room]:
        print(no_item)
    elif item_to_collect not in rooms[current_room['Item']]:
        print(not_in_room)
    elif item_to_collect not in items_list:
        print(not_in_game)
    elif item_to_collect in collection:
        print(already_collected)
    elif item_to_collect not in collection:
        collection.append('item_to_collect')
        print('You added {} to your collection.'.format(item_to_collect))
    return move_rooms(current_room, movement)      


def main():
    # Print intro
    print('Welcome to the Castle Keep Adventure! You are tasked with protecting the keep. \n')
    print('To move between rooms, enter a direction (North, South, East, West)! To exit the game, enter Exit.')
    
    # player start location
    current_room = 'Great Hall'
    print('You are in the {}'.format(current_room))
    
    # While input is not equal to Exit game LOOP
    user_input = ''
    while user_input != 'Exit':
        current_room = move_rooms(current_room, user_input)

    print('Thanks for playing!')


# main program
if __name__ == "__main__":
    main()
