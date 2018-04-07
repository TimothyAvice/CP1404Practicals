from kivy.app import App
from kivy.lang import Builder


class ConverterApp(App):
    def build(self):
        self.root = Builder.load_file("my_convert_m_km.kv")
        return self.root

    def handle_increment(self, value):
        try:
            number = int(self.root.ids.user_input.text)
            number += value
            self.root.ids.user_input.text = str(number)
            self.root.ids.output_text.text = ''
        except ValueError:
            self.root.ids.user_input.text = '0'
            self.root.ids.output_text.text = "Cannot increment non-numeric input"

    def clear(self):
        self.root.ids.user_input.text = ''
        self.root.ids.output_text.text = ''

    def convert_to_km(self, number):
        try:
            number = int(number)
            result = number * 1.60934
            self.root.ids.output_text.text = "{} miles is equivalent to {} km".format(number, result)
        except ValueError:
            self.root.ids.user_input.text = '0'
            self.root.ids.output_text.text = "Cannot convert non-numeric input"

    def convert_to_miles(self, number):
        try:
            number = int(number)
            result = number * 0.621371
            self.root.ids.output_text.text = "{} km is equivalent to {} miles".format(number, result)
        except ValueError:
            self.root.ids.user_input.text = '0'
            self.root.ids.output_text.text = "Cannot convert non-numeric input"


ConverterApp().run()