import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite ", color="blue", size=24)
        self._page.controls.append(self._title)
        self._annoSelezionato=ft.Dropdown(label="anno",
                                          width=200)
        self._controller.addAnni()
        self._brandSelezionato=ft.Dropdown(label="brand",
                                       width=200)
        self._controller.addBrand()
        self._retailerSelezionato = ft.Dropdown(label="retailer",
                                             width=200,
                                                expand=True)
        self._controller.addRetailer()

        row1=ft.Row(controls=[self._annoSelezionato,self._brandSelezionato,self._retailerSelezionato])

        self._btnTopVendite=ft.ElevatedButton(content=ft.Text("Top Vendite"),
                                              on_click=self._controller.showTopVendite,
                                              width=200)

        self._btnAnalizzaVendite = ft.ElevatedButton(content=ft.Text("Analizza Vendite"),
                                                on_click=self._controller.analizzaVendite,
                                                width=200)
        row2=ft.Row(controls=[self._btnTopVendite,self._btnAnalizzaVendite],alignment='CENTER')
        self._page.add(row1,row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    @property
    def annoSelezionato(self):
        return self._annoSelezionato

    @property
    def brandSelezionato(self):
        return self._brandSelezionato

    @property
    def retailerSelezionato(self):
        return self._retailerSelezionato

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
