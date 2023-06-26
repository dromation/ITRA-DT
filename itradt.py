# SOCV CAMERA using OPENCV module for Video Capture
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
import webbrowser
import sys, os, pathlib
from typing import Union
import socket
from time import time
from datetime import datetime
from os.path import dirname, join
import cv2 as cv
import numpy as np
import glob
from kivymd.toast import toast
from kivy.properties import ObjectProperty, NumericProperty, StringProperty, BooleanProperty,\
    ListProperty
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import cv2



class MainApp(MDApp):
    title = 'Thermo Vision'
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path
        )
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.material_style = "M3"
        main_layout = MDBoxLayout(orientation = 'vertical')
        menu = MDTopAppBar(id = 'toolbar',
                            use_overflow = True,
                            pos_hint = {"top": 1},
                            size_hint_x = 1,
                            left_action_items =  [["menu", lambda x: self.callback(x)],["file", lambda x: self.file_manager_open()]],
                            right_action_items =  [["tools", lambda x: self.display_settings()],["information", lambda x: self.app_timer()]],
                            md_bg_color =  self.theme_cls.primary_color
                            )


        bottom = MDBottomNavigation()



        #START OF CAMERA SCREEN
        item_camera = MDBottomNavigationItem(id = 'cameras',
                                            name = 'Cameras',
                                            text = "Camera Settings",
                                            icon = 'camera')

        cam_layout = MDBoxLayout(orientation = 'vertical',
                                    pos_hint = {"center_x": 0.5, "center_y": 0.5},
                                    size_hint_y = 0.8,
                                    )

        self.image = Image()
        # self.image.size_hint_y = None
        # self.image.height = 200
        self.image.allow_stretch = True
        cam_layout.add_widget(self.image)
        cam_layout.add_widget(MDRaisedButton(
            text = 'Low T template',
            pos_hint = {'center':.5 , 'center_y':.5},
            size_hint = (None,None),
            on_press = self.take_lowtemplate
        ))
        cam_layout.add_widget(MDRaisedButton(
            text = 'High T template',
            pos_hint = {'center':.5 , 'center_y':.5},
            size_hint = (None,None),
            on_press = self.take_hightemplate
        ))
        self.capture = cv2.VideoCapture(2)
        Clock.schedule_interval(self.load_video,1.0/30.0)
        item_camera.add_widget(cam_layout)

        #START OF MACHINE VISION ALGORITHMS
        item_vision = MDBottomNavigationItem(id = 'visions',
                                            name = 'Visions',
                                            text = "Machine Vision Settings",
                                            icon = 'camera-control')


        visions_layout = MDBoxLayout(orientation = 'vertical',
                                    pos_hint = {"center_x": 0.5, "center_y": 0.5},
                                    size_hint_y = 0.8,
                                    )
        self.template = Image()

        item_vision.add_widget(visions_layout)


        #bottom items together

        bottom.add_widget(item_camera)
        bottom.add_widget(item_vision)

        #MAIN WIDGETS
        main_layout.add_widget(menu)
        main_layout.add_widget(bottom)
        return main_layout
    def display_settings(settings):
        return True

    def selected(self, filename):
        try:
            self.ids.img.source = filename[0]
        except:
            pass

    def load_video(self, *args):
        gray = self.capture.read(cv2.IMREAD_GRAYSCALE)
        alpha = self.capture.read(cv2.IMREAD_UNCHANGED)
        depth = self.capture.read(cv2.IMREAD_ANYDEPTH)
    

        infern = cv2.applyColorMap(gray, cv2.COLORMAP_INFERNO)
        jetp = cv2.applyColorMap(infern, cv2.COLORMAP_JET)
        #virdis = cv2.applyColorMap(jetp, cv2.COLORMAP_VIRIDIS)
        invert = cv2.bitwise_not(jetp)

        frame = invert
        self.image_frame = frame
        buffer = cv2.flip(frame, 0).tobytes() # tostring is deprecated
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]))
        texture.blit_buffer(buffer, bufferfmt='ubyte')
        self.image.texture = texture

    def take_lowtemplate(self, *args):
        image_name = "tmpl/template_low.png"
        
        cv2.imwrite(image_name, self.image_frame)
    def take_hightemplate(self, *args):
        image_name = "tmph/template_high.png"
        cv2.imwrite(image_name, self.image_frame)

    def on_save(self, instance, value):
        print(instance, value)

    def on_cancel(self, instance, value):
        print(instance, value)
    def callback(self, button):
        self.menu.caller = button
        self.menu.open()

    def home_callback(self, text_item):
        self.menu.dismiss()
        Snackbar(text=text_item).open()

    def menu_callback(self, text_item):
        self.menu.dismiss()
        Snackbar(text=text_item).open()


    def on_pause(self):
        return True

    def on_resume(self):
        pass

    #IMAGE LOAD command
    def load_image(self, *args):
        self.cv2.imread()

    #HELP commands
    def help(self):
        webbrowser.open('https://docs.opencv.org/4.x/')
    #FILE MANAGER COMMANDS
    def file_manager_open(self):
        self.file_manager.show(os.path.expanduser("~"))  # output manager to the screen
        self.manager_open = True

    def select_path(self, path: str):
        '''
        It will be called when you click on the file name
        or the catalog selection button.

        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

if __name__ == '__main__':
    MainApp().run()
