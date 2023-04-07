import customtkinter as tk
from PIL import Image, ImageTk
from Main_cam import *
from Kamera.functions import *
from bot.can_moove import *
import time
from bot.config import *

class VideoPlayer(tk.CTkFrame):
    def __init__(self, master=None, camera=0):
        super().__init__(master)
        self.master = master
        self.video = cv2.VideoCapture(camera)
        self.video.set(3, height)
        self.video.set(4, width)
        self.canvas = tk.CTkCanvas(self.master, width=self.video.get(cv2.CAP_PROP_FRAME_HEIGHT),
                                height=self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.canvas.grid(row=0, column=1, columnspan=2)
        self.run = True

    def update_frame(self):
        ret, frame = self.video.read()
        if ret:
            image = locate_bord(frame)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(image))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        if self.run == True:
            self.master.after(15, self.update_frame)

    def stop(self):
        self.run = False
        self.video.release()
        self.canvas.destroy()

class GUI(tk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.camera = 0
        self.play = True

        self.title("Checkers")
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (width, height))
        self.start_GUI()

    def set_camera(self,cam):
        self.camera = int(cam[-1])


    def start_setup(self,root, button):
        back = tk.CTkButton(root, text="Stop", command=lambda: self.stop_setup(root, video_player))
        back.grid(row=0, column=0, pady=10, padx=10)

        next = tk.CTkButton(root, text="Next", command=lambda: self.finde_board(root, video_player))
        next.grid(row=0, column=3, pady=10, padx=10)

        video_player = VideoPlayer(root, self.camera)
        video_player.update_frame()
        for i in button:
            i.destroy()


    def stop_setup(self,root, video_player):
        video_player.stop()
        root.destroy()
        self.start_GUI()

    def finde_board(self,root, video_player):
        video_player.stop()
        root.destroy()
        self.setup_GUI()


    def start_GUI(self):

        frame_1 = tk.CTkFrame(self)
        frame_1.grid(row=0, column=0, padx=60, pady=20, sticky="nsew")
        cameras = all_cameras()
        select_camera = tk.CTkOptionMenu(frame_1, values=cameras, command=self.set_camera)
        select_camera.grid(row=1, column=0, pady=10, padx=50)
        select_camera.set(cameras[0])
        self.camera = 0
        start = tk.CTkButton(frame_1, text="Start",
                                           command=lambda: self.start_setup(frame_1, [start, select_camera]))
        start.grid(row=2, column=0, pady=10, padx=10)

        frame_1.place(relx=0.5, rely=0.5, anchor="center")

    def show_bord(self, root, bord):
        img = np.zeros((800, 800, 3), np.uint8)

        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    cv2.rectangle(img, (i * 100, j * 100), (i * 100 + 100, j * 100 + 100), (255, 255, 255), -1)
                else:
                    cv2.rectangle(img, (i * 100, j * 100), (i * 100 + 100, j * 100 + 100), (0, 0, 0), -1)
        imag = img.copy()
        w = cv2.imread("../Img/W.png")
        b = cv2.imread("../Img/B.png")
        wq = cv2.imread('../Img/WQ.png')
        bq = cv2.imread('../Img/BQ.png')
        # set image size
        w = cv2.resize(w, (80, 80))
        b = cv2.resize(b, (80, 80))
        wq = cv2.resize(wq, (80, 80))
        bq = cv2.resize(bq, (80, 80))
        # replace black pixels with white pixels
        w[np.where((w == [0, 0, 0]).all(axis=2))] = [255, 255, 255]
        b[np.where((b == [0, 0, 0]).all(axis=2))] = [255, 255, 255]
        wq[np.where((wq == [0, 0, 0]).all(axis=2))] = [255, 255, 255]
        bq[np.where((bq == [0, 0, 0]).all(axis=2))] = [255, 255, 255]

        for i in range(8):
            for j in range(8):
                if bord[i][j] == 1:
                    imag[i * 100 + 10:i * 100 + 80 + 10, j * 100 + 10:j * 100 + 80 + 10] = w
                elif bord[i][j] == 2:
                    imag[i * 100 + 10:i * 100 + 80 + 10, j * 100 + 10:j * 100 + 80 + 10] = b
                elif bord[i][j] == 3:
                    imag[i * 100 + 10:i * 100 + 80 + 10, j * 100 + 10:j * 100 + 80 + 10] = wq
                elif bord[i][j] == 4:
                    imag[i * 100 + 10:i * 100 + 80 + 10, j * 100 + 10:j * 100 + 80 + 10] = bq
        image = cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)
        photo = ImageTk.PhotoImage(image=Image.fromarray(image))
        tk.CTkLabel(root, image=photo, text="").grid(row=0, column=0,columnspan=9,rowspan=9)

    def calibrate_GUI(self,root,cap):

        bord = setup_bord

        # add button
        button_frame = tk.CTkFrame(root)
        self.show_bord(button_frame, bord)
        button_frame.grid(row=0, column=0, pady=10)
        back = tk.CTkButton(button_frame, text="Calibrate", command=lambda: self.set_colors(cap, root))
        back.grid(row=4, column=4)

    def set_colors(self,cap, root):
        get_color(cap, self.rows)
        root.destroy()
        self.start_position(cap)




    def setup_GUI(self):
        frame_1 = tk.CTkFrame(self)
        frame_1.grid(row=0, column=0, padx=60, pady=20, sticky="nsew")
        cap = load_webcam(self.camera)
        rows, black_rows = load_board(cap)
        if rows == None:
            self.destroy()
        self.rows = rows
        self.black_rows = black_rows
        self.calibrate_GUI(frame_1, cap)


    def start_position (self,cap):
        frame_1 = tk.CTkFrame(self)
        frame_1.grid(row=0, column=0, padx=60, pady=20, sticky="nsew")
        bord_s = board_start
        self.show_bord(frame_1, bord_s)
        frame_1.update()
        start = True
        while start:
            board = get_board(cap, self.rows, self.black_rows)
            frame_1.update()
            if np.array_equal(bord_s, board):
                start = False
        frame_1.destroy()
        self.play = True
        self.play_GUI(cap)

    def reset(self, cap):
        self.play = False



    def play_GUI(self,cap):
        frame_1 = tk.CTkFrame(self)
        frame_1.grid(row=1, column=0, padx=60, pady=20, sticky="nsew")
        bord = board_start
        self.show_bord(frame_1, bord)
        frame_1.update()
        time.sleep(1)
        figure = "w"
        back = tk.CTkButton(frame_1, text="Reset game", command=lambda: self.reset(cap))
        back.grid(row=9, column=4, pady=10)
        while self.play:
            #add text
            if figure == "w":
                text = tk.CTkLabel(self, text="White turn", font=("Helvetica", 30))
                text.grid(row=0, column=0, pady=10)
                board_temp = get_board(cap, self.rows, self.black_rows)
                if not np.array_equal(board_temp, empty_board):
                    if not np.array_equal(board_temp, bord):
                        if posible_move(copy.deepcopy(bord), "w", board_temp):
                            time.sleep(1)
                            bord = get_board(cap, self.rows,self.black_rows)
                            figure = "b"
                self.show_bord(frame_1, bord)
            else:
                text = tk.CTkLabel(self, text="Black turn", font=("Helvetica", 30))
                text.grid(row=0, column=0, pady=10)
                bord, moved = run(bord,figure)
                if bord is False:
                    break
                board_temp = get_board(cap, self.rows, self.black_rows)
                print(bord)
                figure = "w"
                self.show_bord(frame_1, bord)
                while not np.array_equal(board_temp, bord):
                    if self.play == False:
                        break
                    board_temp = get_board(cap, self.rows, self.black_rows)
                    frame_1.update()
            frame_1.update()
        frame_1.destroy()
        self.start_position(cap)


if __name__ == "__main__":
    camera_runing = False
    app = GUI()
    app.mainloop()
