from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

class MeuApp(App):

    def build(self):
        self.layout = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=20
        )

        # Fundo azul
        with self.layout.canvas.before:
            Color(0, 0, 1, 1)
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)

        self.layout.bind(size=self.update_rect, pos=self.update_rect)

        # Caixa dinheiro
        self.dinheiro = TextInput(
            hint_text='Dinheiro',
            multiline=False,
            font_size=24,
            size_hint=(1, 0.15)
        )

        # Caixa meses
        self.meses = TextInput(
            hint_text='Meses',
            multiline=False,
            input_filter='int',
            font_size=24,
            size_hint=(1, 0.15)
        )

        # Botão calcular
        self.botao = Button(
            text='Valor',
            font_size=24,
            background_color=(0, 1, 0, 1),  # Verde
            size_hint=(1, 0.15)
        )

        self.botao.bind(on_press=self.calcular)

        # Resultado
        self.resultado = Label(
            text='',
            font_size=28,
            color=(1, 1, 1, 1),
            size_hint=(1, 0.2)
        )

        # Botão X
        self.botao_x = Button(
            text='X',
            font_size=24,
            background_color=(1, 0, 0, 1),
            size_hint=(1, 0.15)
        )

        self.botao_x.bind(on_press=self.voltar_inicio)

        # Adicionar elementos
        self.layout.add_widget(self.dinheiro)
        self.layout.add_widget(self.meses)
        self.layout.add_widget(self.botao)
        self.layout.add_widget(self.resultado)
        self.layout.add_widget(self.botao_x)

        return self.layout

    def update_rect(self, *args):
        self.rect.pos = self.layout.pos
        self.rect.size = self.layout.size

    def calcular(self, instance):
        try:
            valor = float(self.dinheiro.text)
            meses = int(self.meses.text)

            dias = meses * 30

            if dias > 0:
                por_dia = valor / dias
                self.resultado.text = f'R$ {por_dia:.2f} por dia'
            else:
                self.resultado.text = 'Digite meses válidos'

        except:
            self.resultado.text = 'Preencha corretamente'

    def voltar_inicio(self, instance):
        self.dinheiro.text = ''
        self.meses.text = ''
        self.resultado.text = ''

MeuApp().run()