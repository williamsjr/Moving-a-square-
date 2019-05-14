from tkinter import *
from time import *

class my_frame(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.myCanvas = Canvas(width = 250, height = 250, bg = 'white')
        self.myCanvas.grid()

        my_rect = self.myCanvas.create_rectangle(10, 10, 50, 50)
        self.myCanvas.update()
        
        for x in range(11):
            my_count = 10*x
            self.myCanvas.coords(my_rect, my_count + 10,
                                           my_count + 10, my_count +
                                           50, my_count + 50)
            self.myCanvas.update()
            sleep(1)

frame = my_frame()
frame.mainloop()
