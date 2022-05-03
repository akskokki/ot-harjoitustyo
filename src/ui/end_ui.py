from tkinter import ttk


class EndUI:
    def __init__(self, root):
        self._root = root
        self.selection = 0

    def start(self, time):
        if time == -1:
            heading = "Oh no! You clicked on a mine :("
        else:
            heading = "Congratulations! You cleared all the mines :)"
            label_time = ttk.Label(master=self._root, text="Final time: " + str(time/1000) + " seconds.")

        label_heading = ttk.Label(master=self._root, text=heading)
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

        current_row = 0

        label_heading.grid(row=current_row, columnspan=3, padx=5, pady=5)
        current_row += 1

        if time >= 0:
            label_time.grid(row=current_row, columnspan=3, padx=5, pady=5)
            current_row += 1
        
        button_easy.grid(row=current_row, column=0, padx=5, pady=5)
        button_medium.grid(row=current_row, column=1, padx=5, pady=5)
        button_hard.grid(row=current_row, column=2, padx=5, pady=5)

    def _handle_button_restart(self):
        self.selection = 1
        self._root.destroy()

    def _handle_button_change_difficulty(self):
        self.selection = 2
        self._root.destroy()

    def _handle_button_quit(self):
        self.selection = 3
        self._root.destroy()
