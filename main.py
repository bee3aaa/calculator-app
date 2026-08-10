from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class Calculator(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        self.num1 = TextInput(
            hint_text="Enter number 1",
            input_filter="float"
        )

        self.num2 = TextInput(
            hint_text="Enter number 2",
            input_filter="float"
        )

        layout.add_widget(self.num1)
        layout.add_widget(self.num2)

        buttons = BoxLayout(spacing=5)

        for operator in ["+", "-", "*", "/", "%"]:
            button = Button(text=operator)
            button.bind(
                on_press=lambda btn: self.calculate(btn.text)
            )
            buttons.add_widget(button)

        layout.add_widget(buttons)

        self.result = Label(text="Result = ")
        layout.add_widget(self.result)

        return layout

    def calculate(self, operator):

        try:
            n1 = float(self.num1.text)
            n2 = float(self.num2.text)

            if operator == "+":
                result = n1 + n2

            elif operator == "-":
                result = n1 - n2

            elif operator == "*":
                result = n1 * n2

            elif operator == "/":
                result = n1 / n2

            elif operator == "%":
                result = n1 % n2

            self.result.text = f"Result = {result}"

        except ZeroDivisionError:
            self.result.text = "Cannot divide by zero"

        except ValueError:
            self.result.text = "Enter valid numbers"


Calculator().run()

