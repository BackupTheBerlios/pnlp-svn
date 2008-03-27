#!/usr/bin/env python

import Tkinter as tk

root = tk.Tk()
tk.Label(root, text="Hello PNLP").pack()
tk.Button(root, text="Quit", command=root.quit).pack()
root.mainloop()
