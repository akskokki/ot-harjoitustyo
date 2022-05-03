from tkinter import ttk


class ErrorUI:
    def __init__(self, root):
        self._root = root
    
    def start(self):
        label_heading = ttk.Label(master=self._root, text="Please enter valid grid parameters!")
        button_ok = ttk.Button(master=self._root, text = "OK", command=self._handle_button_ok)

        label_heading.grid(row=0, column=0, padx=5, pady=5)
        button_ok.grid(row=1, column=0, padx=5, pady=5)
    
    def _handle_button_ok(self):
        self._root.destroy()
