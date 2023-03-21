from tkinter import *
from videoplayer import VideoThread


root= Tk()
root.geometry("1100x1400")
root.configure(bg='#023020')

frame = Frame(root, height=600, width=1100)
frame.pack(fill='both', expand=False)

wid = frame.winfo_id()

thread = VideoThread(wid)
thread.start()

root.mainloop()
thread.stop()