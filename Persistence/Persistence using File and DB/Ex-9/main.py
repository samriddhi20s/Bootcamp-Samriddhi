from game import Game

# Step 1: Create a Game object
game1 = Game("Player1", level=5, score=1200, inventory=["sword", "shield", "potion"])

# Step 2: Save the current game state
game1.save_state()

# Step 3: Load the game state from file
loaded_game = Game.load_state()
print("\nRestored Game State:", loaded_game)
