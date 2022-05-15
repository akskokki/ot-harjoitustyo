from tkinter import ttk


class DifficultyUI:
    """Class for the difficulty UI displayed at the start of the game

    Attributes:
        root: the root window which the UI is being displayed on
        selection: the difficulty that the player has selected (1: easy, 2: medium, 3: hard, 4: custom)
    """

    def __init__(self, root):
        """Constructor which sets the root UI window

        Args:
            root: the root window which the UI is being displayed on
        """

        self._root = root
        self.selection = 0

    def start(self, scoreboard):
        """Creates and starts the UI after fetching the current high scores

        Args:
            scoreboard: Scoreboard-object to read the current high scores from
        """

        scores = scoreboard.get_scores()
        for i in range(3):
            if scores[i] == -1:
                scores[i] = "No time set"
            else:
                scores[i] = str(scores[i]/1000) + " s"

        label_heading = ttk.Label(master=self._root, text="Choose difficulty")
        button_easy = ttk.Button(master=self._root,
                                 text="Easy",
                                 command=self._handle_button_easy
                                 )
        button_medium = ttk.Button(master=self._root,
                                   text="Medium",
                                   command=self._handle_button_medium
                                   )
        button_hard = ttk.Button(
            master=self._root,
            text="Hard",
            command=self._handle_button_hard
        )
        button_custom = ttk.Button(
            master=self._root,
            text="Custom",
            command=self._handle_button_custom
        )
        label_easy_time = ttk.Label(master = self._root, text=str(scores[0]))
        label_medium_time = ttk.Label(master = self._root, text=str(scores[1]))
        label_hard_time = ttk.Label(master = self._root, text=str(scores[2]))

        label_heading.grid(row=0, columnspan=4, padx=5, pady=5)
        button_easy.grid(row=1, column=0, padx=5, pady=5)
        button_medium.grid(row=1, column=1, padx=5, pady=5)
        button_hard.grid(row=1, column=2, padx=5, pady=5)
        label_easy_time.grid(row=2, column=0, padx=5, pady=0)
        label_medium_time.grid(row=2, column=1, padx=5, pady=0)
        label_hard_time.grid(row=2, column=2, padx=5, pady=0)
        button_custom.grid(row=3, column=1, padx=5, pady=10)

    def _handle_button_easy(self):
        self.selection = 1
        self._root.destroy()

    def _handle_button_medium(self):
        self.selection = 2
        self._root.destroy()

    def _handle_button_hard(self):
        self.selection = 3
        self._root.destroy()

    def _handle_button_custom(self):
        self.selection=4
        self._root.destroy()
