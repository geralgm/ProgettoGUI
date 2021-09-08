class Prenotazione():
    def __init__(self, id, cliente, data):
        super(Prenotazione, self).__init__()
        self.id = id
        self.cliente = cliente
        #self.prodotto = prodotto
        self.data = data