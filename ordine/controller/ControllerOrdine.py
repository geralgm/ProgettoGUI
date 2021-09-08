class ControllerOrdine:
    def __init__(self, ordine):
        self.model = ordine

    def get_cod_fattura(self):
        return self.model.cod_fattura

    def get_stato(self):
        return self.model.stato

    def get_numero_tavola(self):
        return self.model.numero_tavola

    def get_data_ordine(self):
       return self.model.data_ordine

    def get_importo_totale(self):
         return self.model.importo_totale

    def get_quantita_totale(self):
        return self.model.quantita_totale
