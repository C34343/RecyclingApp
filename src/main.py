import kivy

kivy.require("2.2.1") 

from kivy.app import App
import random
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


class MainApp(App):
    def build(self):
        self.layout = BoxLayout(size_hint = (1, 1),
                           pos_hint={'center_x': 0.5, 'center_y': 0.5})
        # colors = [red, green, blue, purple]
        self.picBtn = Button(color =(1, 1, 1, 1),
                    background_normal = 'pictureIcon.png',
                    background_down ='pictureIcon.png',
                    size_hint = (None, 0.2),
                    pos_hint = {"center_x": 0.5, "center_y": 0.5})
        self.picBtn.bind(on_press = self.takePic)

        self.layout.add_widget(self.picBtn)
        return self.layout
    
    def takePic(self, instance):
        print("Picture taken")

if __name__ == '__main__':
    Window.clearcolor = (1, 1, 1, 1)
    app = MainApp()
    app.run()