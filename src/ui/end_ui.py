from tkinter import ttk


class EndUI:
    def __init__(self, root):
        self._root = root
        self.selection = 0

    def start(self, result):
        if result == "win":
            heading = "Congratulations! You cleared all the mines :)"
        elif result == "loss":
            heading = "Oh no! You clicked on a mine :("

        heading_label = ttk.Label(master=self._root, text=heading)
        button_easy = ttk.Button(master=self._root,
                                 text="Restart",
                                 command=self._handle_button_restart
                                 )
        button_medium = ttk.Button(master=self._root,
                                   text="Change difficulty",
                                   command=self._handle_button_change_difficulty
                                   )
        button_hard = ttk.Button(
            master=self._root,
            text="Quit",
            command=self._handle_button_quit
        )

        heading_label.grid(row=0, columnspan=3, padx=5, pady=5)
        button_easy.grid(row=1, column=0, padx=5, pady=5)
        button_medium.grid(row=1, column=1, padx=5, pady=5)
        button_hard.grid(row=1, column=2, padx=5, pady=5)

    def _handle_button_restart(self):
        self.selection = 1
        self._root.destroy()

    def _handle_button_change_difficulty(self):
        self.selection = 2
        self._root.destroy()

    def _handle_button_quit(self):
        self.selection = 3
        self._root.destroy()
