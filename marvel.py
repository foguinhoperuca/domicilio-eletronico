from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
from kivy.uix.label import Label


class Marvel(BoxLayout):

    def __init__(self, **kwargs):
        super(Marvel, self).__init__(**kwargs)
        # self.orientation = 'vertical'
        # self.label = Label(text='Em caso de *EMERGÊNCIA* solicitar o apoio da GCM')
        # self.add_widget(self.label)

    def hulk_smash(self):
        self.ids.hulk.text = "hulk: puny god!"
        self.ids["loki"].text = "loki: >_<!!!"  # alternative syntax
