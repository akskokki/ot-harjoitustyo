from tkinter import ttk


class ErrorUI:
    """Class for the error UI which is displayed upon invalid custom grid parameters

    Attributes:
        root: the root window which the UI is being displayed on
    """

    def __init__(self, root):
        """Constructor which sets the root UI window

        Args:
            root: the root window which the UI is being displayed on
        """

        self._root = root

    def start(self):
        label_heading = ttk.Label(master=self._root, text="Please enter valid grid parameters!")
        button_ok = ttk.Button(master=self._root, text = "OK", command=self._handle_button_ok)

        label_heading.grid(row=0, column=0, padx=5, pady=5)
        button_ok.grid(row=1, column=0, padx=5, pady=5)

    def _handle_button_ok(self):
        self._root.destroy()
