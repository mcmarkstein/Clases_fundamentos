class Drinks:
    def __init__(self, title,strAlcoholic, strInstructions):
        self.title = title
        self.strAlcoholic =strAlcoholic
        self.strInstructions = strInstructions

    def __str__(self):
        return f"El nombre {self.title}" \
                f"Es alcoholico: {self.strAlcoholic}" \
                f"Las intrucciones en ingles: {self.strInstructions}

