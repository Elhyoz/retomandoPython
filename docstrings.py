class Punto:
    'Representa un punto en coordenadas geométrica bidimensionales'
    def __init__(self, x=0, y=0):
        '''Inicializa la posición de un nuevo punto. Las coordenadas de X e Y pueden ser especificadas. Sino lo son
        el punto por defecto será el de origen'''
        self.mover(x, y)

    def mover(self, x, y):
        "Mueve el punto a una nueva localización en un plano bidimensional"
        self.x = x
        self.y = y

    def reiniciar(self):
        'Reinicia el punto al origen geométrico 0,0'
        self.mover(0,0)

    def calcular_distancia(self, otro_punto):
        ''' Calcula la distancia de este punto a un segundo punto pasado como parámetro.
        Esta función utiliza el teorema de pitágoras para calcular la distancia entre dos puntos.
        La distancia es devuelta como flotante (float) '''
        return math.sqrt(
			(self.x - otro_punto.x)**2 +
            (self.y - otro_punto.y)**2)
