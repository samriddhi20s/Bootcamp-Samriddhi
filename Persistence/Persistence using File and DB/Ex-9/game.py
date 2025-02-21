import pickle

class Game:
    def __init__(self, player_name, level=1, score=0, inventory=None):
        self.player_name = player_name
        self.level = level
        self.score = score
        self.inventory = inventory if inventory else []

    def save_state(self, filename="game_save.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self, file)
        print(f"Game state saved to {filename}")

    @classmethod
    def load_state(cls, filename="game_save.pkl"):
        try:
            with open(filename, "rb") as file:
                game = pickle.load(file)
            print(f"Game state loaded from {filename}")
            return game
        except FileNotFoundError:
            print("No saved game found. Starting a new game.")
            return cls("New Player")  

    def __repr__(self):
        return f"Game(player_name={self.player_name}, level={self.level}, score={self.score}, inventory={self.inventory})"
