import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("I AM A TITLE RAWR FEAR ME")
        self.geometry("1280x720")

        self.button = tk.Button(self, text="Kill me", command=self.pressMePls)
        self.button.place(x=10,y=10)
    
    def pressMePls(self):
        print("I HATH BEEN PRESETHED. I AM KILLED.")

app = App()
app.mainloop()