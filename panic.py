from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.gridlayout import GridLayout

from protergo_button import ProtergoButton
from util import red, green, blue, purple, colors


class PanicApp(App):
    def __init__(self):
        super(PanicApp, self).__init__()
        # choosen_colors = choice(colors)
        # colors.remove(choosen_colors)
        # self.actual_color = choosen_colors
        self.actual_color = red
        # self.label = Label(text='Em caso de *EMERGÊNCIA* solicitar o apoio da GCM')

        # self.layout.add_widget(self.label)

    # def build(self):
    #     self.layout = ProtergoButton()

    #     return self.layout
