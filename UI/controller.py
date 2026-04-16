import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def addAnni(self):
        self._view.annoSelezionato.options.append(
            ft.dropdown.Option(key=None, text="Nessun filtro")
        )
        for i in self._model.getAllAnni():
            self._view.annoSelezionato.options.append(
                ft.dropdown.Option(key=i["anno"], text=str(i["anno"]))
            )


    def addBrand(self):
        self._view.brandSelezionato.options.append(
            ft.dropdown.Option(key=None, text="Nessun filtro")
        )
        for i in self._model.getAllBrand():
            self._view.brandSelezionato.options.append(
                ft.dropdown.Option(key=i["brand"], text=str(i["brand"]))
            )

    def addRetailer(self):
        self._view.retailerSelezionato.options.append(
            ft.dropdown.Option(key=None, text="Nessun filtro")
        )
        for i in self._model.getAllRetailer():
            self._view.retailerSelezionato.options.append(
                ft.dropdown.Option(key=i["name"], text=str(i["name"]))
            )

    def showTopVendite(self, e):
        self._view.txt_result.controls.clear()
        anno = self._view.annoSelezionato.value
        brand = self._view.brandSelezionato.value
        retailer = self._view.retailerSelezionato.value

        for i in self._model.getAllRicavi(anno,brand,retailer):
            if anno is None or anno=="Nessun filtro":
                self._view.txt_result.controls.append(
                    ft.Text(
                        f"data : {i['Date']}; ricavo : {i['ricavo']}; retailer : {i['Retailer_code']}; Product : {i['Product_number']}")
                )
            elif int(anno) == i["Date"].year and brand is None or brand=="Nessun filtro":
                self._view.txt_result.controls.append(
                    ft.Text(
                        f"data : {i['Date']}; ricavo : {i['ricavo']}; retailer : {i['Retailer_code']}; Product : {i['Product_number']}")
                )
            elif int(anno) == i["Date"].year and brand==i["Product_brand"] and retailer==i["Retailer_name"]:
                self._view.txt_result.controls.append(
                    ft.Text(
                        f"data : {i['Date']}; ricavo : {i['ricavo']}; retailer : {i['Retailer_code']}; Product : {i['Product_number']}")
                )



        self._view.update_page()

    def analizzaVendite(self, e):
        self._view.txt_result.controls.clear()
        anno = self._view.annoSelezionato.value
        brand = self._view.brandSelezionato.value
        retailer = self._view.retailerSelezionato.value

        risultati = self._model.getAllVendite(anno, brand, retailer)

        if len(risultati) == 0:
            self._view.create_alert("Nessun risultato trovato")
            return

        i = risultati[0]
        self._view.txt_result.controls.append(ft.Text("Statistiche vendite:"))
        self._view.txt_result.controls.append(ft.Text(f"Giro d'affari: {i['volume']}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero vendite: {i['num_vendite']}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero retailers coinvolti: {i['num_retailer']}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero prodotti coinvolti: {i['num_prodotti']}"))
        self._view.update_page()


