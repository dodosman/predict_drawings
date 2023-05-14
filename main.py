import sys

sys.path.append('C:/Users/Dominik/AppData/Local/Programs/Python/Python311/Lib')

import pickle
import os.path

import numpy as np
import PIL
import PIL.Image
import cv2

from tkinter import *
from tkinter import simpledialog

import tkinter.messagebox

from sklearn.svm import LinearSVC
from sklearn.gaussian_process import GaussianProcessRegressor as GP
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier


class DrawingClassifier:
    def __int__(self):
        self.class1, self.class2, self.class3 = None, None, None
        self.class1_counter, self.class2_counter, self.class3_counter = None, None, None
        self.csf = None
        self.proj_name = None
        self.root = None
        self.image1 = None

        self.status_label = None
        self.canvas = None
        self.draw = None

        self.brush_width = 15

        self.classes_prompt()
        self.init_gui()

    def classes_prompt(self):
        msg = Tk()
        msg.withdraw()

        self.proj_name = simpledialog.askstring("Project name", "Please enter your project name down below", parent=msg)
        if os.path.exists(self.proj_name):
            with open(f"{self.proj_name}/{self.proj_name}_data.pickle", "rb") as f:
                data = pickle.load(f)
            self.class1 = data['c1']
            self.class2 = data['c2']
            self.class3 = data['c3']
            self.class1_counter = data['c1c']
            self.class2_counter = data['c2c']
            self.class3_counter = data['c3c']
            self.clf = data['clf']
            self.proj_name = data['pname']
        else:
            self.class1 = simpledialog.askstring("Clas 1", "Whats is the first class called?", parent=msg)
            self.class2 = simpledialog.askstring("Clas 2", "Whats is the second class called?", parent=msg)
            self.class3 = simpledialog.askstring("Clas 3", "Whats is the third class called?", parent=msg)

            self.class1_counter = 1
            self.class2_counter = 1
            self.class3_counter = 1

            self.clf - LinearSVC()

            os.mkdir(self.proj_name)
            os.chdir(self.proj_name)
            os.mkdir(self.class1)
            os.mkdir(self.class2)
            os.mkdir(self.class3)
            os.chdir("..")

    def init_gui(self):
        WIDTH = 500
        HEIGHT = 500
        WHITE = (255, 255, 255)

        self.root = Tk()
        self.root.title(f"Drawing classifier - {self.proj_name}")

        self.canvas = Canvas(self.root, width=WIDTH - 10, height=HEIGHT - 10, background="white")
        self.canvas.pack(expand=YES, fill=BOTH)
        self.canvas.bind("<B1-Motion>", self.paint)

        self.image1 = PIL.Image.new("RGB", (WIDTH, HEIGHT), WHITE)
        self.draw = PIL.ImageDraw.Draw(self.image1)

        btn_frame = tkinter.Frame(self.root)
        btn_frame.pack(fill=X, side=BOTTOM)

        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)
        btn_frame.columnconfigure(2, weight=1)

        class1_btn = Button(btn_frame, text=self.class1, command=lambda: self.save(1))
        class1_btn.grid(row=0, column=0, sticky=W + E)

        class2_btn = Button(btn_frame, text=self.class2, command=lambda: self.save(2))
        class2_btn.grid(row=0, column=1, sticky=W + E)

        class3_btn = Button(btn_frame, text=self.class3, command=lambda: self.save(3))
        class3_btn.grid(row=0, column=2, sticky=W + E)

        bm_btn = Button(btn_frame, text="Brush-", command=self.brushminus)
        bm_btn.grid(row=1, column=0, sticky=W + E)

        clear_btn = Button(btn_frame, text="Clear", command=self.clear)
        bm_btn.grid(row=1, column=1, sticky=W + E)

        bp_btn = Button(btn_frame, text="Brush+", command=self.brushplus)
        bm_btn.grid(row=1, column=2, sticky=W + E)

        train_btn = Button(btn_frame, text="Train model", command=self.train_model)
        train_btn.grid(row=2, column=0, sticky=W + E)

        save_btn = Button(btn_frame, text="Save model", command=self.save_model)
        save_btn.grid(row=2, column=1, sticky=W + E)

        load_btn = Button(btn_frame, text="Load model", command=self.load_model)
        load_btn.grid(row=2, column=2, sticky=W + E)

        change_btn = Button(btn_frame, text="Change model", command=self.rotate_model)
        change_btn.grid(row=3, column=0, sticky=W + E)

        predict_btn = Button(btn_frame, text="Predict", command=self.predict)
        predict_btn.grid(row=3, column=1, sticky=W + E)

        save_everything_btn = Button(btn_frame, text="Save everything", command=self.save_everything)
        save_everything_btn.grid(row=3, column=2, sticky=W + E)

        self.status_label = Label(btn_frame, text=f"Current model: {type(self.clf).__name__}")
        self.status_label.config(font=("Arial", 10))
        self.status_label.grid(rom=4, column=1, sticky=W + E)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.attributes("-topmost", True)
        self.root.mainloop()

    def paint(self, event):
        pass

    def save(self, class_num):
        pass

    def brushminus(self):
        pass

    def clear(self):
        pass

    def brushplus(self):
        pass

    def train_model(self):
        pass

    def save_model(self):
        pass

    def load_model(self):
        pass


    def rotate_model(self):
        pass

    def predict(self):
        pass

    def save_everything(self):
        pass

    def on_closing(self):
        pass
