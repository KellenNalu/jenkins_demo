from tkinter import *

frame = Tk()
frame.title('Sharing Group Demo')
text = Label(frame, text="This is a demo, click button to close")
text.pack()
button = Button(frame, text="Close", width=25, command=frame.destroy)
button.pack()
frame.mainloop()
    