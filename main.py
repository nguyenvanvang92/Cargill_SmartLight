from logging import error, root
from kivy.core import window
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
from kivy.core.window import Window
from kivymd.uix.picker import MDDatePicker

x = 516
#Window.size = (x,16*x/9) 

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
Builder.load_file("design_gui_content.kv")

flag_btn_phongnhapxa = [False,False,False,False,False,False,False,False,False,False,False,False]
status_light = ["", "", "", "", "", "", "", "", "", "", "", ""]

class Content_pnx(MDBoxLayout):
    pass


class Content_knl(MDBoxLayout):
    pass

class HomeScreen(Screen):
    number_light = ""
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.ids.scroll_controll.add_widget(
            MDExpansionPanel(
                icon = "NhaNhapXa.png",
                content=Content_pnx(),
                panel_cls=MDExpansionPanelOneLine(
                text="Ph??ng Nh???p X??",
                )
            )
        )
        self.ids.scroll_controll.add_widget(
            MDExpansionPanel(
                icon = "NhaKho.png",
                content=Content_knl(),
                panel_cls=MDExpansionPanelOneLine(
                text="Kho Nguy??n Li???u",
                )
            )
        )
        self.ids.scroll_controll.add_widget(
            MDExpansionPanel(
                icon = "PhongLoHoi.png",
                content=Content_knl(),
                panel_cls=MDExpansionPanelOneLine(
                text="Ph??ng L?? H??i",
                )
            )
        )
        self.ids.scroll_controll.add_widget(
            MDExpansionPanel(
                icon = "PhongKhiNen.png",
                content=Content_knl(),
                panel_cls=MDExpansionPanelOneLine(
                text="Ph??ng Kh?? N??n",
                )
            )
        )
        self.ids.scroll_controll.add_widget(
            MDExpansionPanel(
                icon = "PhongBaoTri.png",
                content=Content_knl(),
                panel_cls=MDExpansionPanelOneLine(
                text="Ph??ng B???o Tr??",
                )
            )
        )
        self.ids.scroll_controll.add_widget(
            MDExpansionPanel(
                icon = "ThapSanXuat.png",
                content=Content_knl(),
                panel_cls=MDExpansionPanelOneLine(
                text="Th??p S???n Xu???t\nT???ng 1",
                )
            )
        )
        self.ids.scroll_controll.add_widget(
            MDExpansionPanel(
                icon = "ThapSanXuat.png",
                content=Content_knl(),
                panel_cls=MDExpansionPanelOneLine(
                text="Th??p S???n Xu???t\nT???ng 2",
                )
            )
        )
        self.ids.scroll_controll.add_widget(
            MDExpansionPanel(
                icon = "ThapSanXuat.png",
                content=Content_knl(),
                panel_cls=MDExpansionPanelOneLine(
                text="Th??p S???n Xu???t\nT???ng 3",
                )
            )
        )
        self.ids.scroll_controll.add_widget(
            MDExpansionPanel(
                icon = "ThapSanXuat.png",
                content=Content_knl(),
                panel_cls=MDExpansionPanelOneLine(
                text="Th??p S???n Xu???t\nT???ng 4",
                )
            )
        )
        self.ids.scroll_controll.add_widget(
            MDExpansionPanel(
                icon = "ThapSanXuat.png",
                content=Content_knl(),
                panel_cls=MDExpansionPanelOneLine(
                text="Th??p S???n Xu???t\nT???ng 5",
                )
            )
        )
        self.ids.scroll_controll.add_widget(
            MDExpansionPanel(
                icon = "ThapSanXuat.png",
                content=Content_knl(),
                panel_cls=MDExpansionPanelOneLine(
                text="Th??p S???n Xu???t\nT???ng 6",
                )
            )
        )
        self.ids.scroll_controll.add_widget(
            MDExpansionPanel(
                icon = "ThapSanXuat.png",
                content=Content_knl(),
                panel_cls=MDExpansionPanelOneLine(
                text="Th??p S???n Xu???t\nT???ng 7",
                )
            )
        )
        self.ids.scroll_controll.add_widget(
            MDExpansionPanel(
                icon = "ThapSanXuat.png",
                content=Content_knl(),
                panel_cls=MDExpansionPanelOneLine(
                text="Th??p S???n Xu???t\nT???ng 8",
                )
            )
        )
        self.ids.scroll_controll.add_widget(
            MDExpansionPanel(
                icon = "DanThaoTac.png",
                content=Content_knl(),
                panel_cls=MDExpansionPanelOneLine(
                text="D??n Thao T??c Ngo??i Tr???i",
                )
            )
        )
        self.ids.scroll_controll.add_widget(
            MDExpansionPanel(
                icon = "TangHam.png",
                content=Content_knl(),
                panel_cls=MDExpansionPanelOneLine(
                text="Th??p S???n Xu???t\nT???ng H???m 1",
                )
            )
        )
        self.ids.scroll_controll.add_widget(
            MDExpansionPanel(
                icon = "TangHam.png",
                content=Content_knl(),
                panel_cls=MDExpansionPanelOneLine(
                text="Th??p S???n Xu???t\nT???ng H???m 2",
                )
            )
        )
        self.ids.scroll_controll.add_widget(
            MDExpansionPanel(
                icon = "TangTret.png",
                content=Content_knl(),
                panel_cls=MDExpansionPanelOneLine(
                text="T???ng Tr???t",
                )
            )
        )
        self.ids.scroll_controll.add_widget(
            MDExpansionPanel(
                icon = "PhongCanThuoc.png",
                content=Content_knl(),
                panel_cls=MDExpansionPanelOneLine(
                text="Ph??ng C??n Thu???c",
                )
            )
        )
        self.ids.scroll_controll.add_widget(
            MDExpansionPanel(
                icon = "CangXuatHang.png",
                content=Content_knl(),
                panel_cls=MDExpansionPanelOneLine(
                text="C???ng Xu???t H??ng",
                )
            )
        )
    
    def on_enter(self, *args):
        self.ids.nav._refresh_tabs()

    def event_btn(self, *args):
        global flag_btn_phongnhapxa
        flag_btn_phongnhapxa[int(self.number_light) - 1] = True

class DemoApp(MDApp):
    height = Window.height
    width = Window.width
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name='homescreen'))
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.primary_hue = '900'
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

