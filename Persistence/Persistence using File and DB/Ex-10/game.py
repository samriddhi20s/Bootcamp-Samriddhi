import pickle

class Game:
    VERSION = 2  # Current class version

    def __init__(self, player_name, level=1, score=0, inventory=None, difficulty="Normal"):
        self.version = Game.VERSION  # Store version info
        self.player_name = player_name
        self.level = level
        self.score = score
        self.inventory = inventory if inventory else []
        self.difficulty = difficulty  # New attribute in version 2

    def save_state(self, filename="game_save.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self, file)
        print(f"Game state (version {self.VERSION}) saved to {filename}")

    @classmethod
    def load_state(cls, filename="game_save.pkl"):
        try:
            with open(filename, "rb") as file:
                game = pickle.load(file)

            # Handle version differences
            if not hasattr(game, "version"):
                print(" Old version detected! Migrating data...")
                game.version = 1  # Assume it was version 1
                game.difficulty = "Normal"  # Default difficulty for old versions

            if game.version < cls.VERSION:
                print(f" Upgrading save file from version {game.version} to {cls.VERSION}")
                game.version = cls.VERSION  # Update version

            return game

        except FileNotFoundError:
            print("No saved game found. Starting a new game.")
            return cls("New Player")  # Default state

    def __repr__(self):
        return (f"Game(player_name={self.player_name}, level={self.level}, score={self.score}, "
                f"inventory={self.inventory}, difficulty={self.difficulty})")
