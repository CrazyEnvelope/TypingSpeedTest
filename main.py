from gui_window import guiWindow
from text import  paragraphs
import random

timer_id = None

def startTimer(seconds=60):
    global timer_id
    if seconds == 60:
        secs = "60"
    else:
        mins, secs = divmod(seconds,60)
        if secs < 10:
            secs = "0" + str(secs)
    guiSpeedtest.labelTime.config(text = f"Time remaining: {secs}")
    timer_id = guiSpeedtest.after(1000, startTimer, seconds-1)

def startTyping():
    randomParagraph = random.choice(paragraphs)
    guiSpeedtest.randomText.config(text = randomParagraph)
    guiSpeedtest.inputText.config(state="normal", bg = "white")
    startTimer()

def stopTyping():
    global timer_id
    if timer_id is not None:
        guiSpeedtest.after_cancel(timer_id)
        timer_id = None
    guiSpeedtest.inputText.config(state="disabled", bg="#F7F7F8")

guiSpeedtest = guiWindow()
guiSpeedtest.inputText.config(state = "disabled", bg = "#F7F7F8")
guiSpeedtest.startButton.config(command=startTyping)
guiSpeedtest.stopButton.config(command=stopTyping)

guiSpeedtest.mainloop()


