from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class CreditCalc(MDApp):
    def build(self):
        return MDLabel(text="Hello, Credit Calculator", halign="center")


if __name__ == '__main__':
    CreditCalc().run()
