from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class NameListerApp(App):
    def __init__(self):
        super().__init__()
        self.names = ["Bob", "Bill", "Alex", "Luke"]

    def build(self):
        self.title = "Name Lister"
        self.root = Builder.load_file("name_lister.kv")
        return self.root

    def list_names(self):
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.list_box.add_widget(temp_label)

    def clear_names(self):
        self.root.ids.list_box.clear_widgets()


NameListerApp().run()
