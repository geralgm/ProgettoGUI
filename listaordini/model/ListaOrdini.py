import json
import os
import pickle

from ordine.model.Ordine import Ordine


class ListaOrdini():

    def __init__(self):
        super(ListaOrdini, self).__init__()
        self.lista_ordini = []


        if os.path.isfile('listaordini/data/DatabaseOrdini.pickle'):
            with open('listaordini/data/DatabaseOrdini.pickle', 'rb') as f:

                try:
                   self.lista_ordini = pickle.load(f)
                except EOFError:
                   return
        else:
            with open('listaordini/data/DatabaseOrdini.json') as f:
                lista_ordine_json = json.load(f)
                for ordine_da_caricare in lista_ordine_json:
                    self.lista_ordini.append(Ordine(ordine_da_caricare['cod_fattura'],  ordine_da_caricare['stato'],
                                                                ordine_da_caricare['numero_tavola'],
                                                                ordine_da_caricare['data_ordine'],
                                                                ordine_da_caricare['importo_totale'],
                                                                ordine_da_caricare["quantita_totale"]))


    def aggiungi_ordine(self, ordine):
        self.lista_ordini.append(ordine)

    def elimina_ordine_by_codice(self, cod_fattura):
        def is_selected_ordine(ordine):
            if ordine.cod_fattura == cod_fattura:
                return True
            return False
        self.lista_ordini.remove(list(filter(is_selected_ordine, self.lista_ordini))[0])

    def get_ordine_by_index(self, index):
        return self.lista_ordini[index]

    def get_lista_ordini(self):
        return self.lista_ordini

    def save_data(self):
        with open('listaordini/data/DatabaseOrdini.pickle', 'wb') as handle:
            pickle.dump(self.lista_ordini, handle, pickle.HIGHEST_PROTOCOL)

