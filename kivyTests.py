"""
Simple applications built with Kivy. Goal is to create an android application. 
"""

import kivy
from kivy.app import App
kivy.require("1.8.0")
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Line

class Widgets(Widget):
    #this is using the kivy layout
    pass

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        # test that super reacts like it should
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='username:'))
        self.username = TextInput(multiline = False)
        self.add_widget(self.username)

        self.add_widget(Label(text='password:'))
        self.password = TextInput(multiline = False, password = True) # inherited arguments - password blanks it as asterisks
        self.add_widget(self.password)


#inheriting from the basic App class
class SimpleKivy(App):
    def build(self):
        return Widgets()

# this is what determines the KV file to use - it will load the same one as the class name
class FloatingKivyApp(App):
    def build(self):
        return FloatLayout()

class TouchInput(Widget):
    def on_touch_down(self, touch):
        print(touch)
        with self.canvas:
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        print(touch)
        touch.ud['line'].points += (touch.x, touch.y)
    
    def on_touch_up(self, touch):
        print(touch)


class TouchingKivyApp(App):
    def build(self):
        return TouchInput()


if __name__ == "__main__":
    TouchingKivyApp().run()