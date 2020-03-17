import tkinter as tk

win = tk.Tk()

text = tk.Label(win, text="Hello, Tk "+str(tk.TkVersion)+"!") # The text is something like "Hello, Tk 8.6!"
text.pack()

win.mainloop()
