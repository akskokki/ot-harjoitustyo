from tkinter import Tk

from ui.difficulty_ui import DifficultyUI
from ui.custom_ui import CustomUI
from ui.error_ui import ErrorUI
from ui.game_ui import GameUI
from ui.end_ui import EndUI


class UI:
    def __init__(self):
        """Constructor which initialises the functionality of the main UI
        """
        self.running = True
        self.view = "difficulty"
        self.game_difficulty = 0
        self.custom_width = 0
        self.custom_height = 0
        self.custom_mines = 0
        self.game_time = 0

    def start(self):
        """Starts a simple loop that changes the view each time the previous view's functionality is completed
        """
        while self.running:
            self._handle_view()

    def _handle_view(self):
        """Opens a new view according to which one the current view is set to
        """
        if self.view == "difficulty":
            self._handle_difficulty_ui()
        elif self.view == "custom":
            self._handle_custom_ui()
        elif self.view == "error":
            self._handle_error_ui()
        elif self.view == "game":
            self._handle_game_ui()
        elif self.view == "end":
            self._handle_end_ui()

    def _handle_difficulty_ui(self):
        """Creates a difficulty selection UI and uses the selection that has been made to open the game
        """
        window = Tk()
        window.title("Minesweeper")

        difficulty_ui = DifficultyUI(window)
        difficulty_ui.start()

        window.resizable(False, False)
        window.mainloop()

        self.game_difficulty = difficulty_ui.selection

        if self.game_difficulty == 4:
            self.view = "custom"
        else:
            self.view = "game"
    
    def _handle_custom_ui(self):
        """Creates a custom game creation UI and passes the selected perimeters back to the main UI
        """
        window = Tk()
        window.title("Custom game")

        custom_ui = CustomUI(window)
        custom_ui.start()

        window.resizable(False, False)
        window.mainloop()

        if custom_ui.valid == 1:
            self.custom_width = custom_ui.width
            self.custom_height = custom_ui.height
            self.custom_mines = custom_ui.mines
            self.view = "game"
        elif custom_ui.valid == -1:
            self.view = "error"
        else:
            self.running = False

    def _handle_error_ui(self):
        """Creates an error handling UI for invalid parameters given in custom game creation
        """
        window = Tk()
        window.title("Error")

        error_ui = ErrorUI(window)
        error_ui.start()

        window.resizable(False, False)
        window.mainloop()

        self.view = "custom"


    def _handle_game_ui(self):
        """Creates a new game UI and passes the currently selected difficulty parameters to it
        """
        if self.game_difficulty == 0:
            self.running = False
            return

        game_ui = GameUI(self.custom_width, self.custom_height, self.custom_mines)
        self.game_time = game_ui.start(self.game_difficulty)
        if self.game_time == 0:
            self.running = False

        self.view = "end"

    def _handle_end_ui(self):
        """Creates an ending UI when the current game has been finished, and allows the user to start a new game
        """
        window = Tk()
        window.title("Game Over")

        end_ui = EndUI(window)
        end_ui.start(self.game_time)

        window.resizable(False, False)
        window.mainloop()

        if end_ui.selection == 1:
            self.view = "game"
        elif end_ui.selection == 2:
            self.view = "difficulty"
        else:
            self.running = False
