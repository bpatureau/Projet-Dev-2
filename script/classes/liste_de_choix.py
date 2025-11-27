class ListeDeChoix:
    """Classe représentant un node de l'histoire avec ses choix"""
    
    def __init__(self, id_node, description):
        self.id = id_node
        self.description = description
        self.propositions = []
