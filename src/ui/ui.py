from tkinter import ttk


class UI:
    def __init__(self, root):
        self._root = root
        self.selection = 0

    def start(self):
        heading_label = ttk.Label(master=self._root, text="Choose difficulty")
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

        heading_label.grid(row=0, columnspan=3, padx=5, pady=5)
        button_easy.grid(row=1, column=0, padx=5, pady=5)
        button_medium.grid(row=1, column=1, padx=5, pady=5)
        button_hard.grid(row=1, column=2, padx=5, pady=5)

    def _handle_button_easy(self):
        self.selection = 1
        self._root.destroy()

    def _handle_button_medium(self):
        self.selection = 2
        self._root.destroy()

    def _handle_button_hard(self):
        self.selection = 3
        self._root.destroy()
