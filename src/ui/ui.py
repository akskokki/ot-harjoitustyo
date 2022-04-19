from tkinter import Tk

from ui.difficulty_ui import DifficultyUI
from ui.game_ui import GameUI
from ui.end_ui import EndUI


class UI:
    def __init__(self):
        self.running = True
        self.view = "difficulty"
        self.game_difficulty = 0
        self.game_result = ""

    def start(self):
        while self.running:
            self._handle_view()

    def _handle_view(self):
        if self.view == "difficulty":
            self._handle_difficulty_ui()
        elif self.view == "game":
            self._handle_game_ui()
        elif self.view == "end":
            self._handle_end_ui()

    def _handle_difficulty_ui(self):
        window = Tk()
        window.title("Minesweeper")

        difficulty_ui = DifficultyUI(window)
        difficulty_ui.start()

        window.resizable(False, False)
        window.mainloop()

        self.game_difficulty = difficulty_ui.selection

        self.view = "game"

    def _handle_game_ui(self):
        if self.game_difficulty == 0:
            self.running = False
            return

        game_ui = GameUI()
        self.game_result = game_ui.start(self.game_difficulty)
        if self.game_result == "quit":
            self.running = False

        self.view = "end"

    def _handle_end_ui(self):
        window = Tk()
        window.title("Game Over")

        end_ui = EndUI(window)
        end_ui.start(self.game_result)

        window.resizable(False, False)
        window.mainloop()

        if end_ui.selection == 1:
            self.view = "game"
        elif end_ui.selection == 2:
            self.view = "difficulty"
        else:
            self.running = False
