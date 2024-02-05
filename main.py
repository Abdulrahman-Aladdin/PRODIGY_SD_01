import customtkinter as ctk
from CustomFrame import CustomFrame
from Converter import Converter
from settings import *


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f'{WINDOW_SIZE}x{WINDOW_SIZE}')
        self.resizable(RESIZABLE, RESIZABLE)
        self.title(TITLE)
        self.configure(fg_color=WINDOW_COLOR)

        self.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')
        self.columnconfigure(0, weight=1, uniform='b')

        self.title_label = ctk.CTkLabel(master=self, text=TITLE,
                                        font=ctk.CTkFont(size=LARGE_FONT_SIZE, family=FONT, weight='bold'),
                                        text_color=TITLE_COLOR)
        self.title_label.grid(row=0, column=0, stick='nsew')

        self.celsius = ctk.DoubleVar(value=0)
        self.celsius.trace('w', self.update_temperature_c)
        self.celsius_frame = CustomFrame(self, fg_color=FRAME_COLOR, float_var=self.celsius, unit=CELSIUS_UNIT)
        self.celsius_frame.grid(row=1, column=0, stick='nsew', padx=15, pady=10)

        self.fahrenheit = ctk.DoubleVar(value=32.0)
        self.fahrenheit.trace('w', self.update_temperature_f)
        self.fahrenheit_frame = CustomFrame(self, fg_color=FRAME_COLOR, float_var=self.fahrenheit, unit=FAHRENHEIT_UNIT)
        self.fahrenheit_frame.grid(row=2, column=0, stick='nsew', padx=15, pady=10)

        self.kelvin = ctk.DoubleVar(value=273.15)
        self.kelvin.trace('w', self.update_temperature_k)
        self.kelvin_frame = CustomFrame(self, fg_color=FRAME_COLOR, float_var=self.kelvin, unit=KELVIN_UNIT)
        self.kelvin_frame.grid(row=3, column=0, stick='nsew', padx=15, pady=10)

        self.update = True
        self.converter = Converter()

        self.mainloop()

    def update_temperature_c(self, *args):
        if self.update:
            self.update = False
            self.fahrenheit.set(round(self.converter.celsius_to_fahrenheit(self.celsius.get()), 2))
            self.kelvin.set(round(self.converter.celsius_to_kelvin(self.celsius.get()), 2))
            self.update_screen()
            self.update = True

    def update_temperature_f(self, *args):
        if self.update:
            self.update = False
            self.celsius.set(round(self.converter.fahrenheit_to_celsius(self.fahrenheit.get()), 2))
            self.kelvin.set(round(self.converter.fahrenheit_to_kelvin(self.fahrenheit.get()), 2))
            self.update_screen()
            self.update = True

    def update_temperature_k(self, *args):
        if self.update:
            self.update = False
            self.celsius.set(round(self.converter.kelvin_to_celsius(self.kelvin.get()), 2))
            self.fahrenheit.set(round(self.converter.kelvin_to_fahrenheit(self.kelvin.get()), 2))
            self.update_screen()
            self.update = True

    def update_screen(self):
        self.celsius_frame.text_var.set(f'{self.celsius_frame.float_var.get()} {self.celsius_frame.unit}')
        self.fahrenheit_frame.text_var.set(f'{self.fahrenheit_frame.float_var.get()} {self.fahrenheit_frame.unit}')
        self.kelvin_frame.text_var.set(f'{self.kelvin_frame.float_var.get()} {self.kelvin_frame.unit}')


if __name__ == '__main__':
    App()
