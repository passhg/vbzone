from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        txt = TextInput(
            hint_text="이름을 입력하세요",
            multiline=False
        )

        btn = Button(
            text="확인",
            size_hint_y=None,
            height=50
        )

        result = Label(
            text="결과가 여기에 표시됩니다."
        )

        def button_click(instance):
            result.text = "입력한 이름: " + txt.text

        btn.bind(on_press=button_click)

        layout.add_widget(txt)
        layout.add_widget(btn)
        layout.add_widget(result)

        return layout


MyApp().run()