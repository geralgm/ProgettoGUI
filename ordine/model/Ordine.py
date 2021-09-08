

class Ordine:
    def __init__(self, cod_fattura, stato,numero_tavola, data_ordine, importo_totale, quantita_totale):
        super(Ordine, self).__init__()

        self.cod_fattura = cod_fattura
        self.stato = stato
        self.numero_tavola=numero_tavola
        self.data_ordine = data_ordine
        self.importo_totale = importo_totale
        self.quantita_totale = quantita_totale
