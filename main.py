from gui_window import guiWindow
from text import  paragraphs
import random

timer_id = None
is_finished = False

def startTimer(seconds=5):
    global timer_id
    if seconds == 60:
        secs = "60"
    else:
        mins, secs = divmod(seconds,60)
        if secs < 10:
            secs = "0" + str(secs)
    guiSpeedtest.labelTime.config(text = f"Time remaining: {secs} s")
    timer_id = guiSpeedtest.after(1000, startTimer, seconds-1)

    if int(secs) < 1:
        stopTimer()
        guiSpeedtest.inputText.config(state="disabled", bg="#F7F7F8")

def startTyping():
    global is_finished
    is_finished = False
    randomParagraph = random.choice(paragraphs)
    guiSpeedtest.randomText.config(text = randomParagraph)
    guiSpeedtest.inputText.config(state="normal", bg = "white")
    guiSpeedtest.inputText.delete("1.0","end")
    stopTimer()
    startTimer()

def stopTyping():
    stopTimer()
    guiSpeedtest.inputText.config(state="disabled", bg="#F7F7F8")
    guiSpeedtest.labelTime.config(text=f"Time remaining: 00")

def stopTimer():
    global timer_id, is_finished
    if timer_id is not None:
        guiSpeedtest.after_cancel(timer_id)
        timer_id = None
        is_finished = True
    calculateErrors()

def calculateErrors():
    global is_finished
    if is_finished:
        content = guiSpeedtest.inputText.get("1.0","end")
        words_written = [word for word in content.split(" ")]
        words_written[-1] = words_written[-1].strip()

        print(words_written)

guiSpeedtest = guiWindow()
guiSpeedtest.inputText.config(state = "disabled", bg = "#F7F7F8")
guiSpeedtest.startButton.config(command=startTyping)
guiSpeedtest.stopButton.config(command=stopTyping)

guiSpeedtest.mainloop()


