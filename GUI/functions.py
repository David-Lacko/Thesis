import cv2
import customtkinter
import tkinter as tk
from PIL import Image, ImageTk
from Main_cam import *
from Kamera.camera_setup import setup

class VideoPlayer(tk.Frame):
    def __init__(self, master=None, camera=0):
        super().__init__(master)
        super().__init__(master)
        self.master = master
        self.video = cv2.VideoCapture(camera) # change the index to select a different camera or file
        self.video.set(3, height)
        self.video.set(4, width)
        self.canvas = tk.Canvas(self.master, width=self.video.get(cv2.CAP_PROP_FRAME_HEIGHT), height=self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.canvas.pack()
        self.run = True

    def update_frame(self):
        ret, frame = self.video.read()
        if ret:
            image = setup(frame)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(image))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        if self.run == True:
            self.master.after(15, self.update_frame)


    def stop(self):
        self.run=False
        self.video.release()
        self.canvas.destroy()


camera = 0
camera_runing = False
def set_camera(cam):
    global camera
    camera = int(cam[-1])

def start_setup(root,button,app):
    button_2 = customtkinter.CTkButton(root, text="Stop", command=lambda: stop_setup(root, video_player,app))
    button_2.pack(pady=10, padx=10)

    video_player = VideoPlayer(root,camera)
    video_player.update_frame()
    for i in button:
        i.destroy()

def stop_setup(root,video_player,app):
    video_player.stop()
    root.destroy()
    start_GUI(app)

def start_GUI(app):
    frame_1 = customtkinter.CTkFrame(master=app)
    frame_1.pack(pady=20, padx=60, fill="both")

    cameras = all_cameras()
    optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=cameras, command=set_camera)
    #place to middle
    optionmenu_1.pack(pady=10, padx=10)
    optionmenu_1.set(cameras[0])
    camera = 0

    button_1 = customtkinter.CTkButton(frame_1, text="Start", command=lambda: start_setup(frame_1,[button_1,optionmenu_1],app))
    button_1.pack(pady=10, padx=10)



