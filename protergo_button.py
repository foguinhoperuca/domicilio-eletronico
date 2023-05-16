from kivy.uix.boxlayout import BoxLayout


class ProtergoButton(BoxLayout):
    def __init__(self, **kwargs):
        super(ProtergoButton, self).__init__(**kwargs)

    # def build(self):
    #     # self.layout = BoxLayout(orientation='vertical')
    #     # self.button = Button(text='Solicitar Ajuda GCM!', background_color=self.actual_color, size_hint=(1, .5))
    #     # self.button.bind(on_press=self.on_press_button)

    #     # self.label = Label(text='Em caso de *EMERGÊNCIA* solicitar o apoio da GCM')

    #     # self.layout.add_widget(self.label)
    #     # self.layout.add_widget(self.button)

    #     # return self.layout

PAREI usando kvlang pra definir um objeto com id e pegar ele no codigo python. Depois modificar o formato do botao para redondo vermelho. Por fim enviar uma requisição HTTP para um backend.
    def on_release_button(self):
        print("Button released...")
        # self.layout.clear_widgets()
        self.ids.lbl_status.text = 'Solicitando apoio...'
