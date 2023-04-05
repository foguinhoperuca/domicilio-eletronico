from random import choice, randint

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]
colors = [red, green, blue, purple]

job_descriptions = [
    ("Técnico em Enfermagem", "3.571,21"),
    ("Mecânico de Autos", "2.198,66"),
    ("Vendedor Externo", "1.522,95"),
    ("Balconista/Recepcionista", "1.392,82"),
    ("Atendente de Telemarketing", "2.540,61"),
    ("Jardineiro", "1.388,66"),
    ("Porteiro", "1.982,46"),
    ("Motorista", "2.177,42")
]


class NewsFeedApp(App):
    def __init__(self):
        super(NewsFeedApp, self).__init__()
        choosen_colors = choice(colors)
        colors.remove(choosen_colors)
        self.actual_color = choosen_colors

    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.button = Button(text='Atualizar Lista de Vagas', background_color=self.actual_color, size_hint=(1, .1))
        self.button.bind(on_press=self.on_press_button)

        self.label = Label(text='Lista de Vagas de Emprego do PAT')

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)

        return self.layout

    def on_press_button(self, instance):

        avaliable_jobs = job_descriptions.copy()
        self.layout.clear_widgets()

        header_grid = GridLayout(padding=20, cols=3, rows=1, size_hint_y=.3)
        lbl_header_job_code = Label(text="Código", size_hint_x=.1)
        lbl_header_job_descr = Label(text="Descrição")
        lbl_header_job_wage = Label(text="Salário", size_hint_x=.2)
        header_grid.add_widget(lbl_header_job_code)
        header_grid.add_widget(lbl_header_job_descr)
        header_grid.add_widget(lbl_header_job_wage)
        self.layout.add_widget(header_grid)

        for i in range(randint(1, len(job_descriptions))):
            grid = GridLayout(padding=10, cols=3, rows=1)
            job = avaliable_jobs.pop(randint(0, len(avaliable_jobs) - 1))

            lbl_number = Label(text="Vaga #%s" % (i + 1), size_hint_x=.1)
            lbl_descr = Label(text=f"{job[0]}")
            lbl_wage = Label(text=f"R$ {job[1]}", size_hint_x=.2)
            grid.add_widget(lbl_number)
            grid.add_widget(lbl_descr)
            grid.add_widget(lbl_wage)

            self.layout.add_widget(grid)

        new_button_color = choice(colors)
        colors.remove(new_button_color)
        colors.append(self.actual_color)
        self.actual_color = new_button_color

        button = Button(text='Atualizar Lista de Vagas', background_color=self.actual_color, size_hint_y=.2)
        button.bind(on_press=self.on_press_button)

        self.layout.add_widget(button)


if __name__ == '__main__':
    app = NewsFeedApp()
    app.run()
