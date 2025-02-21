from game import Game

# Step 1: Create and Save Game (New Version)
game1 = Game("Player1", level=5, score=1500, inventory=["sword", "shield"])
game1.save_state()

# Step 2: Load Game (Handles versioning automatically)
loaded_game = Game.load_state()
print("\nRestored Game State:", loaded_game)
