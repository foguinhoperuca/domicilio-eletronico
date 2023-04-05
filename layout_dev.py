from random import choice, randint

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


class HBoxLayoutApp(App):
    def build(self):
        return Button()

    def on_press_button(self):
        print('Using kv language!!')


class BoxLayoutApp(App):
    def build(self):
        self.layout = BoxLayout(padding=10)

        self.label = Label(text='Central do Cidadão', size_hint=(.5, .5), pos_hint={'center_x': .5, 'center_y': .5})
        self.layout.add_widget(self.label)

        for i in range(2):
            btn = Button(text="Button #%s" % (i + 1), background_color=choice([red, green, blue, purple]))
            btn.bind(on_press=self.on_press_button)
            self.layout.add_widget(btn)

        self.img = Image(source='assets/images/brasao_sorocaba.png', size_hint=(1, .5), pos_hint={'center_x': .25, 'center_y': .25})
        self.layout.add_widget(self.img)

        return self.layout

    def on_press_button(self, instance):
        print('You pressed the button!!')
        if self.label.text == 'CHANGED!!':
            self.label.text = 'Central do Cidadão'
        else:
            self.label.text = 'CHANGED!!'

        instance.background_color = choice([red, green, blue, purple])


class GridLayoutApp(App):
    def build(self):
        self.layout = GridLayout(padding=10, cols=1, rows=2)

        # self.label = Label(text='Central do Cidadão', size_hint=(.5, .5), pos_hint={'center_x': .5, 'center_y': .5})
        self.label = Label(text='Central do Cidadão', size_hint_x=100, width=100)
        self.layout.add_widget(self.label)

        self.btn = Button(text="Change Label", background_color=choice([red, green, blue, purple]))
        self.btn.bind(on_press=self.on_press_button)
        self.layout.add_widget(self.btn)

        return self.layout

    def on_press_button(self, instance):
        print('You pressed the button!!')
        if self.label.text == 'CHANGED!!':
            self.label.text = 'Central do Cidadão'
        else:
            self.label.text = 'CHANGED!!'

        instance.background_color = choice([red, green, blue, purple])

if __name__ == '__main__':
    # app = HBoxLayoutApp()
    # app = BoxLayoutApp()
    # app = GridLayoutApp()
    app = NewsFeedApp()
    app.run()
