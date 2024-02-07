inventory = []
currentRoom = 'Hall'
rooms = {

            'Hall' : { 
                  'south' : 'Kitchen'
                },

            'Kitchen' : {
                  'north' : 'Hall'
                }

         }


def showInstructions():
  #print a main menu and the commands
  print('''
    Welcome to your own RPG Game
    ============================

    Get to the Garden with a key and a potion.
    Avoid the monsters!

    Commands:
    go [direction]
    get [item]
    ''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")
  
showInstructions()