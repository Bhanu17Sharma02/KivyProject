from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.properties import ObjectProperty


Window.size=(300,500)

class Login(Screen):
    def on_login(self):
        print("rthgjhjjghj")
        #sm.current="option"
        pass
    def on_forget(self):
        pass


class Option(Screen):
    pass

class SmartFarming(Screen):
    pass

class Stlp(Screen):
    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        date_dialog.open()
    pass
class B_view(Screen):

    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        date_dialog.open()
    pass

class buss_by_area(Screen):

    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        date_dialog.open()
        pass

sm=ScreenManager()
sm.add_widget(Login(name="log"))
sm.add_widget(Option(name="option"))
sm.add_widget(SmartFarming(name='sf'))
sm.add_widget(Stlp(name="stlp"))
sm.add_widget(B_view(name="b_view"))
sm.add_widget(buss_by_area(name="buss"))

class Mainapp(MDApp):
    def __init__(self,**kwargs):
        super(Mainapp, self).__init__(**kwargs)
        self.screen1=ObjectProperty(None)



    def build(self):
        self.theme_cls.primary_palette="Green"
        self.theme_cls.theme_style="Dark"
        self.theme_cls.theme_hue="A100"
        self.screen1=Builder.load_file("main.kv")
        table = MDDataTable(pos_hint={"center_x": .5, "center_y": .35}, size_hint=(.8, .6),
                            column_data=[("Column1", dp(20)),
                                         ("Column2", dp(20)),
                                         ("Column3", dp(20)),
                                         ("Column4", dp(20)),
                                         ("Column5", dp(20)),
                                         ("Column6", dp(20))],
                            row_data=[(1, 2, 3, 4, 5, 6),
                                      (1, 2, 3, 4, 5, 6),
                                      (1, 2, 3, 4, 5, 6),
                                      (1, 2, 3, 4, 5, 6),
                                      (1, 2, 3, 4, 5, 6),
                                      (1, 2, 3, 4, 5, 6)],

                            )
        self.screen1.get_screen("buss").add_widget(table)
        return self.screen1

if __name__=="__main__":
    Mainapp().run()