from tkinter import ttk


class CustomUI:
    def __init__(self, root):
        self._root = root
        self.entry_width = None
        self.entry_height = None
        self.entry_mines = None
        self.width = 0
        self.height = 0
        self.mines = 0
        self.valid = 0

        self.min_params = 10
        self.max_params = 50

    def start(self):
        label_heading = ttk.Label(master=self._root, text="Custom grid parameters:")

        label_width = ttk.Label(master=self._root, text="Grid width (" + str(self.min_params) + "-" + str(self.max_params) + "):")
        self.entry_width = ttk.Entry(master=self._root)

        label_height = ttk.Label(master=self._root, text="Grid height (" + str(self.min_params) + "-" + str(self.max_params) + ")")
        self.entry_height = ttk.Entry(master=self._root)

        label_mines = ttk.Label(master=self._root, text="Mines:")
        self.entry_mines = ttk.Entry(master=self._root)

        button_start = ttk.Button(
            master=self._root,
            text="Start",
            command=self._handle_button_start
        )

        label_heading.grid(row=0, columnspan=2, padx=5, pady=5)

        label_width.grid(row=1, column=0, padx=5, pady=5)
        self.entry_width.grid(row=1, column=1, padx=5, pady=5)

        label_height.grid(row=2, column=0, padx=5, pady=5)
        self.entry_height.grid(row=2, column=1, padx=5, pady=5)

        label_mines.grid(row=3, column=0, padx=5, pady=5)
        self.entry_mines.grid(row=3, column=1, padx=5, pady=5)

        button_start.grid(row=4, columnspan=2, padx=5, pady=10)

    def _handle_button_start(self):
        self.valid = self._check_valid_inputs()
        self._root.destroy()

    def _check_valid_inputs(self):
        try:
            self.width = int(self.entry_width.get())
            self.height = int(self.entry_height.get())
            self.mines = int(self.entry_mines.get())
        except ValueError:
            return -1

        if self.width < self.min_params or self.width > self.max_params or self.height < self.min_params or self.height > self.max_params:
            return -1

        max_mines = self.width * self.height - 1
        if self.mines < 1 or self.mines > max_mines:
            return -1

        return 1
