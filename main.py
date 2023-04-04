import random

import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout


red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]

class HBoxLayoutApp(App):
    def build(self):
        return Button()

    def on_press_button(self):
        print('Using kv language!!')


class MainApp(App):
    def build(self):
        layout = BoxLayout(padding=10)
        colors = [red, green, blue, purple]

        for i in range(3):
            btn = Button(text="Button #%s" % (i + 1), background_color=random.choice(colors))
            btn.bind(on_press=self.on_press_button)
            layout.add_widget(btn)

        label = Label(text='Central do Cidadão', size_hint=(.5, .5), pos_hint={'center_x': .5, 'center_y': .5})
        layout.add_widget(label)

        img = Image(source='assets/images/brasao_sorocaba.png', size_hint=(1, .5), pos_hint={'center_x': .25, 'center_y': .25})
        layout.add_widget(img)

        return layout

    def on_press_button(self, instance):
        print('You pressed the button!!')


if __name__ == '__main__':
    # app = HBoxLayoutApp()
    app = MainApp()
    app.run()
