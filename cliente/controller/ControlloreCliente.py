class ControlloreCliente():
    def __init__(self, cliente):
        self.model = cliente

    def get_id_cliente(self):
        return self.model.id

    def get_nome_cliente(self):
        return self.model.nome

    def get_cognome_cliente(self):
        return self.model.cognome

    def get_cf_cliente(self):
        return self.model.cf

    def get_datanascita_cliente(self):
        return self.model.datanascita

    def get_email_cliente(self):
        return self.model.email

    def get_telefono_cliente(self):
        return self.model.telefono

    def get_indirizzo_cliente(self):
        return self.model.indirizzo

    def get_servizio_disponibile(self):
        if self.model.is_disponibile():
            return "Disponibile"
        else:
            return "Non Disponibile"
