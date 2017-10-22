class Retangulo:
    b = None
    a = None
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def area(self):
        return self.a*self.b

class Quadrado(Retangulo):
    def __init__(self, lado):
        super(Quadrado, self).__init__(lado, lado)

quadrado = Quadrado(10)
print()
print(quadrado.area())

def div(f):
    def funf(x):
        return "<div>{}</div>".format(f(x))
    return funf

@div
def print_hmtl(nome):
    return "nome" 

print
print(print_hmtl("nome"))

