from gui_window import guiWindow


def startTimer(seconds=60):
    if(seconds==60):
        secs = "60"
    else:
        mins, secs = divmod(seconds,60)
        if secs<10:
            secs = "0" + str(secs)
        guiSpeedtest.labelTime.config(text = f"Time remaining: {secs}")
    guiSpeedtest.after(1000,startTimer,seconds-1)

guiSpeedtest = guiWindow()
guiSpeedtest.startButton.config(command=startTimer)
guiSpeedtest.mainloop()


