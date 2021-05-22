from logging import root
from kivymd.app import MDApp
from kivy.clock import Clock 
from kivy.uix.screenmanager import Screen,ScreenManager,FadeTransition,SwapTransition, FallOutTransition,RiseInTransition
from kivy.lang import Builder 
from kivy.config import Config 
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.picker import MDTimePicker
import pyrebase
from threading import Thread   
from time import sleep
from firebase import firebase
from kivymd.toast import toast 
from kivy.utils import platform 
from plyer import notification
import pyowm
from datetime import datetime
from getpass import getpass


app = firebase.FirebaseApplication("https://datakivyapp.firebaseio.com/", None)

config = {
    "apiKey": "AIzaSyBdvqAiomZTykWb5nzHJxG825_l_mcothI",
    "authDomain": "datakivyapp.firebaseapp.com",
    "databaseURL": "https://datakivyapp.firebaseio.com",
    "projectId": "datakivyapp",
    "storageBucket": "datakivyapp.appspot.com",
    "messagingSenderId": "234264719688",
    "appId": "1:234264719688:web:dace06f06b1244d613c37d",
    "measurementId": "G-RFVXG3FXNK"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()

Builder.load_file("design_gui.kv")
Builder.load_file("gui_infor_pnx.kv")

flag_btn_phongnhapxa = [False,False,False,False,False,False,False,False,False,False,False,False]
status_light = ["", "", "", "", "", "", "", "", "", "", "", ""]

class Infor_pnx(Screen):
    pass    

class HomeScreen(Screen):
    number_light = ""
    
    def on_enter(self, *args):
        self.ids.nav._refresh_tabs()

    def event_btn(self, *args):
        global flag_btn_phongnhapxa
        #flag_btn_phongnhapxa[int(self.number_light) - 1] = True

    def event_btn_infor(self, *args):
        self.manager.current = "infor_pnx"

class DemoApp(MDApp):
    height = 200
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name='homescreen'))
        self.sm.add_widget(Infor_pnx(name="infor_pnx"))
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.primary_hue = '600'
        self.theme_cls.theme_style = 'Light'
        return self.sm

def send_data():
    global flag_btn_phongnhapxa, database
    while True:
        for i in range(0,12,1):
            if flag_btn_phongnhapxa[i]: 
                print(i)
                data_phongnhapxa = database.child("Phong Nhap Xa")
                flag_btn_phongnhapxa[i] = False
                if i == len(flag_btn_phongnhapxa) - 2:
                    data_send =  "pnx_" + str(len(flag_btn_phongnhapxa)) + "_1"
                    data_phongnhapxa.child("multi_led").update({"multi_setup":data_send})
                    print(data_send)
                else:
                    data_send = "pnx_" + str(i) + "_1"
                    data_phongnhapxa.child("led_" + str(i+1)).update({"sign_app":data_send})
                print("sent data")
                print(status_light[i])
        sleep(0.05)

#Thread(target=send_data).start()
DemoApp().run()

