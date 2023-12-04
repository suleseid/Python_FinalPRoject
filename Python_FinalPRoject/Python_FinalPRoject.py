
class Player:
    def __init__(self, name, number):
          self.name = name
          self.number = number
# Global collection of players
players = []  
def populate_players():
    players.append(Player("Lamar Jackson", 8)) 
    players.append(Player("Russel Wilson", 3))
    players.append(Player("Leonel Messi", 10))
    players.append(Player("Cristano Ronaldo", 7))
    players.append(Player("Patrick Mahomes", 15))
 
def display_all_players():
    print("\nAll Players:") 
    for player in players:   
        print(f"Name: {player.name}, Number: {player.number}")
           
def display_players_with_odd_number():
    print("\nAll players with odd numbers:") 
    for player in players:
        if player.number % 2 != 0:
           print(f"Name: {player.name}, Number: {player.number}")   
           
def desplay_player_with_spacific_latter(letter):
    print(f"\nPlayers withNames Starting with '{letter}':")
    for player in players:
        if player.name.lower().startswith(letter.lower()):
            print(f"Name: {player.name}, number: {player.number}")
            
def add_player():
    name = input("Enter player name: ")
    number = int(input("Enter player number: "))
    players.append(Player(name, number))
    print(f"Player {name} added succcessfully!")
    

def main():
    populate_players()
    while True:
        print("\nMenu:")
        print("1. Display all players")
        print("2. Display players with odd numbers")
        print("3. Display players with names starting with a letter")
        print("4. Add player")
        print("5. Exit")
        
        choice = int(input("Enter your choice(1-5): "))
        
        if choice == 1:
           display_all_players()
        elif choice == 2:
           display_players_with_odd_number()
        elif choice == 3:
           letter = input("Enter the letter: ")
           display_players_with_specific_letter(letter)
        elif choice == 4:
           add_player()
        elif choice == 5:
           break
        else:
           print("You Entered Invalid choice. Please tyr it again.Thank you!!. ")
            
if __name__ == "__main__":
     main()

     
                 
    