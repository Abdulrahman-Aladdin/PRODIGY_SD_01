import customtkinter as ctk
from settings import *


class CustomFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, fg_color=kwargs['fg_color'], corner_radius=CORNER_RADIUS)
        self.rowconfigure(0, weight=1, uniform='c')
        self.columnconfigure((0, 4), weight=2, uniform='d')
        self.columnconfigure((1, 3), weight=1, uniform='d')
        self.columnconfigure(2, weight=3, uniform='d')

        medium_font = ctk.CTkFont(size=MEDIUM_FONT_SIZE, family=FONT, weight='bold')
        large_font = ctk.CTkFont(size=LARGE_FONT_SIZE, family=FONT, weight='bold')

        self.large_increase = ctk.CTkButton(master=self, text='+', font=large_font, text_color=BUTTON_TEXT_COLOR,
                                            hover_color=BUTTON_HOVER_COLOR, fg_color=BUTTON_COLOR,
                                            corner_radius=CORNER_RADIUS,
                                            command=lambda: self.update_amount('+', LARGE_AMOUNT))
        self.large_increase.bind('<B1-Motion>', lambda e: self.update_amount('+', LARGE_AMOUNT))

        self.small_increase = ctk.CTkButton(master=self, text='+', font=medium_font, text_color=BUTTON_TEXT_COLOR,
                                            hover_color=BUTTON_HOVER_COLOR, fg_color=BUTTON_COLOR,
                                            corner_radius=CORNER_RADIUS,
                                            command=lambda: self.update_amount('+', SMALL_AMOUNT))
        self.small_increase.bind('<B1-Motion>', lambda e: self.update_amount('+', SMALL_AMOUNT))

        self.large_decrease = ctk.CTkButton(master=self, text='-', font=large_font, text_color=BUTTON_TEXT_COLOR,
                                            hover_color=BUTTON_HOVER_COLOR, fg_color=BUTTON_COLOR,
                                            corner_radius=CORNER_RADIUS,
                                            command=lambda: self.update_amount('-', LARGE_AMOUNT))
        self.large_decrease.bind('<B1-Motion>', lambda e: self.update_amount('-', LARGE_AMOUNT))

        self.small_decrease = ctk.CTkButton(master=self, text='-', font=medium_font, text_color=BUTTON_TEXT_COLOR,
                                            hover_color=BUTTON_HOVER_COLOR, fg_color=BUTTON_COLOR,
                                            corner_radius=CORNER_RADIUS,
                                            command=lambda: self.update_amount('-', SMALL_AMOUNT))
        self.small_decrease.bind('<B1-Motion>', lambda e: self.update_amount('-', SMALL_AMOUNT))

        self.large_decrease.grid(row=0, column=0, stick='nsew', padx=12, pady=12)
        self.small_decrease.grid(row=0, column=1, stick='nsew', padx=2, pady=20)
        self.small_increase.grid(row=0, column=3, stick='nsew', padx=2, pady=20)
        self.large_increase.grid(row=0, column=4, stick='nsew', padx=12, pady=12)

        self.float_var = kwargs['float_var']
        self.unit = kwargs['unit']
        self.text_var = ctk.StringVar(value=f'{self.float_var.get()} {self.unit}')

        self.text_label = ctk.CTkLabel(master=self, textvariable=self.text_var,
                                       font=medium_font, text_color=RESULT_COLOR)
        self.text_label.grid(row=0, column=2, stick='nsew', padx=5, pady=5)

    def update_amount(self, sign, amount):
        if sign == '+':
            self.float_var.set(round(self.float_var.get() + amount, 2))
        else:
            self.float_var.set(round(self.float_var.get() - amount, 2))
        self.text_var.set(f'{self.float_var.get()} {self.unit}')
