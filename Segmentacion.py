class MemoriaSegmentada:
    def __init__(self, tamano_total):
        self.tamano_total = tamano_total
        self.segmentos = []

    def asignar_segmento(self, tamano):
        if self.tamano_disponible() >= tamano:
            self.segmentos.append(tamano)
            print(f"Segmento de {tamano} asignado.")
        else:
            print("No hay suficiente espacio disponible.")

    def tamano_disponible(self):
        return self.tamano_total - sum(self.segmentos)

    def liberar_segmento(self, indice):
        if 0 <= indice < len(self.segmentos):
            tamano_liberado = self.segmentos.pop(indice)
            print(f"Segmento de {tamano_liberado} liberado.")
        else:
            print("Índice de segmento no válido.")

# Ejemplo de uso
memoria = MemoriaSegmentada(tamano_total=1000)
memoria.asignar_segmento(200)
memoria.asignar_segmento(300)
memoria.asignar_segmento(150)

print(f"Espacio disponible: {memoria.tamano_disponible()}")

memoria.liberar_segmento(1)

print(f"Espacio disponible después de liberar un segmento: {memoria.tamano_disponible()}")
