from flet import Column, Icons, ElevatedButton, Text, Row, Colors
from flet.core.text_style import TextThemeStyle
from flet.core.types import MainAxisAlignment, CrossAxisAlignment, TextAlign

from core.navigation import Navigator


class MainView(Column):
    def __init__(self, navigator: Navigator):
        super().__init__()
        self.navigator: Navigator = navigator
        self.alignment = MainAxisAlignment.CENTER
        self.horizontal_alignment = CrossAxisAlignment.CENTER
        self.spacing = 30
        self.BuildUI()

    def BuildUI(self):
        self.title: Text = Text(
            value='Isolation Coordination Method',
            text_align=TextAlign.CENTER,
            size=36,
            theme_style=TextThemeStyle.TITLE_MEDIUM,
            color=Colors.RED_500,
        )

        self.subtitle: Text = Text(
            value='Please choose the method:',
            text_align=TextAlign.CENTER,
            size=24,
            theme_style=TextThemeStyle.LABEL_MEDIUM,
            color=Colors.RED_300,
        )

        self.iec_btn: ElevatedButton = ElevatedButton(
            text='IEC 60071',
            icon=Icons.ELECTRICAL_SERVICES,
            width=250,
            height=50,
            on_click=lambda e: self.navigator.NavigateTo('/iec')
        )

        self.conventional_btn: ElevatedButton = ElevatedButton(
            text='Conventional Method',
            icon=Icons.CALCULATE,
            width=250,
            height=50,
            on_click=lambda e: self.navigator.NavigateTo('/conventional')
        )

        self.controls = [
            self.title,
            self.subtitle,
            Row(
                controls=[
                    self.iec_btn,
                    self.conventional_btn
                ],
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=CrossAxisAlignment.CENTER
            ),
        ]
