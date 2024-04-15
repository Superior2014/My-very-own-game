import random

def prompt(message):
    """Display a prompt and return user input."""
    return input(message)

def display(message):
    """Display a message to the player."""
    print(message)

def forest_adventure():
    display("Welcome to the Enchanted Forest!")

    name = prompt('Enter your Name: ')
    display(f"Welcome, {name}!")

    display("You find yourself in a dense forest. Which direction do you want to go?")
    direction = prompt("(north, east, south, west): ").lower()

    if direction == 'north':
        encounter_mansion()
    elif direction == 'east':
        encounter_cliff()
    elif direction == 'west':
        encounter_castle()
    elif direction == 'south':
        display("You venture deeper into the forest but encounter a ferocious troll. It attacks you! Game Over.")
    else:
        display("Invalid direction. Please choose again.")
        forest_adventure()

def encounter_mansion():
    display("You find yourself outside a mysterious mansion.")
    action = prompt("Do you want to explore or go around? ").lower()

    if action == 'explore':
        explore_mansion()
    elif action == 'go around':
        display("You decide to go around the mansion.")
        forest_adventure()
    else:
        display("Invalid action. Please choose again.")
        encounter_mansion()

def explore_mansion():
    display("As you explore the mansion, you encounter a ghostly figure.")
    choice = prompt("Do you talk to the ghost or run away? ").lower()

    if choice == 'talk':
        display("The ghost reveals a hidden treasure in the mansion.")
        display("Congratulations! You found the treasure and won the game!")
    elif choice == 'run away':
        print("You run away in fear and return to the forest and fall in a ditch.")
        
    else:
        display("Invalid choice. Please try again.")
        explore_mansion()

def encounter_cliff():
    display("You stumble upon a cliff with a dramatic scene unfolding, a dog and a woman are hanging from a cliff, what do you do.")
    if choice == 'save dog':
      print("Shame, a dog over a human")
    elif choice == 'save woman":
      print("Shame, a human over a dog")
    elif choice == 'both':
      print("Now your using your head, You win")
    else:
        display("Invalid choice. Try again")
        encounter_cliff()
def encounter_castle():
    display("You arrive at a majestic castle.")
    if choice == 'enter':
      print("Harry potter ending")
      forest_adventure()
    if choice == 'Leave'
      forrest_adventure()

# Main game loop
forest_adventure()
