import tkinter as tk

def say_hello():
    label.config(text="Hello, World!")

app = tk.Tk()
app.title("Lightweight App")

label = tk.Label(app, text="Welcome!")
label.pack()

button = tk.Button(app, text="Say Hello", command=say_hello)
button.pack()

app.mainloop()
