from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MoMoApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        layout.add_widget(Label(text='My MoMo App', font_size=32, bold=True))
        layout.add_widget(Label(text='Welcome from Bamenda!', font_size=20))
        self.amount = TextInput(hint_text='Enter amount e.g 5000', multiline=False, font_size=20)
        layout.add_widget(self.amount)
        btn = Button(text='Check Balance', font_size=22, size_hint_y=None, height=60)
        btn.bind(on_press=self.check)
        layout.add_widget(btn)
        self.result = Label(text='', font_size=20)
        layout.add_widget(self.result)
        return layout

    def check(self, instance):
        amt = self.amount.text
        if amt:
            self.result.text = f'You wan send {amt} FCFA\nGood luck!'
        else:
            self.result.text = 'Please enter amount first'

MoMoApp().run()
