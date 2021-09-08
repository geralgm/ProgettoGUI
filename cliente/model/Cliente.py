class Cliente():
    def __init__(self, id, nome, cognome, cf, datanascita, email, telefono, indirizzo):
        super(Cliente, self).__init__()
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.datanascita = datanascita
        self.email = email
        self.telefono = telefono
        self.indirizzo = indirizzo
        self.disponibile = True

    def is_disponibile(self):
        return self.disponibile

    def prenota(self):
        self.disponibile = False