#Recursividad
class Human:
    def __init__(self):
        self.name = 'Guido'
        self.head = self.createHead()

    def createHead(self):
        return Human.Head(self)

    class Head:
        def __init__(self, human):
            self.human = human

        def talk(self):
            return 'talking...', self.human.name


# Let's try:
guido = Human()
print(guido.name)
# 'Guido'
print(guido.head.talk())
# ('talking...', 'Guido')
guido.name = "Power Guido"
print(guido.head.talk())
# ('talking...', 'Power Guido')