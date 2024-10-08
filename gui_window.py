import tkinter as tk

class guiWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Typing Speed Test")
        self.minsize(width = 800, height = 600)
        self.resizable(width=False, height=False)
        self.config( bg="#F7F7F8")

        #ContentFrame
        self.contentFrame = tk.Frame(self)
        self.contentFrame.config(width = 30, height = 10, bg="#F7F7F8")
        self.contentFrame.grid(row = 0, column = 1, padx = 20, pady = 20, sticky = "nsew")

        self.randomText = tk.Label(self.contentFrame, text = "Text will appear here!", font = ("Arial", 18), wraplength=1000, bg="#F7F7F8", anchor="w", justify="left")
        self.randomText.grid(row = 0, column = 0, pady = 10, sticky = "wn")

        self.inputText = tk.Text(self.contentFrame, font = ("Arial", 14, 'normal'))
        self.inputText.grid(row = 2, column = 0, pady = 10, sticky = "wn")

        #MenuFrame
        menuFrame = tk.Frame(self, padx=10,pady=10)
        menuFrame.config(bg="#402E7A")
        menuFrame.grid(row = 0, column = 0, sticky="nsw")

        labelTitle = tk.Label(menuFrame, text="TST", font=("Benett Sans Serif", 30, 'bold'), fg="white", bg="#402E7A")
        labelTitle.grid(row=0, column=0, pady=5, padx=(0,100), sticky="w")

        self.labelWPM = tk.Label(menuFrame,text ="WPM: 0" , font = ("MS Sans Serif", 10, 'normal') ,fg="white", bg="#402E7A")
        self.labelWPM.grid(row = 1, column = 0, pady = (60,5), sticky="w")

        self.labelErrors = tk.Label(menuFrame, text = "Entry errors: 0" , font=("MS Sans Serif", 10, 'normal'),fg="white",bg="#402E7A")
        self.labelErrors.grid(row=2, column=0, pady = 5, sticky="w")

        self.labelAccuracy = tk.Label(menuFrame,text = "Accuracy: 0 %", font=("MS Sans Serif", 10, 'normal'),fg="white",bg="#402E7A")
        self.labelAccuracy.grid(row=3, column=0, pady = 5, sticky="w")

        self.labelTime = tk.Label(menuFrame, text = "Time remaining: 00 s", font=("MS Sans Serif", 10, 'normal'), fg="white",bg="#402E7A")
        self.labelTime.grid(row=4, column=0, pady = 5, sticky="w")

        menuFrame.grid_rowconfigure(5,weight = 1)

        self.startButton = tk.Button(menuFrame, text = "Start", font = ("MS Sans Serif",10,"bold"), bg = "#47ff98", borderwidth=0)
        self.startButton.grid(row = 6, column=0, pady = 5, sticky ="wse")

        self.stopButton = tk.Button(menuFrame, text="Stop", font=("MS Sans Serif", 10,"bold"),bg = "#f95555")
        self.stopButton.grid(row=7, column=0, pady=5, sticky="wse")


