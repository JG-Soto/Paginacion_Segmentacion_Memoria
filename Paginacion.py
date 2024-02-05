class Pagina:
    def __init__(self, numero_pagina, contenido):
        self.numero_pagina = numero_pagina
        self.contenido = contenido

class TablaPaginas:
    def __init__(self, tamano_tabla):
        self.tamano_tabla = tamano_tabla
        self.paginas = [None] * tamano_tabla

    def agregar_pagina(self, pagina):
        if pagina.numero_pagina < self.tamano_tabla:
            self.paginas[pagina.numero_pagina] = pagina
        else:
            print(f"Error: El número de página {pagina.numero_pagina} excede el tamaño de la tabla de páginas.")

    def obtener_contenido_pagina(self, numero_pagina):
        if numero_pagina < self.tamano_tabla and self.paginas[numero_pagina] is not None:
            return self.paginas[numero_pagina].contenido
        else:
            print(f"Error: La página {numero_pagina} no está en la tabla de páginas.")

class MemoriaFisica:
    def __init__(self, tamano_memoria):
        self.tamano_memoria = tamano_memoria
        self.memoria = [None] * tamano_memoria

    def cargar_pagina(self, pagina, direccion_memoria):
        if direccion_memoria < self.tamano_memoria:
            self.memoria[direccion_memoria] = pagina
        else:
            print(f"Error: La dirección de memoria {direccion_memoria} excede el tamaño de la memoria física.")

# Ejemplo de uso
tabla_paginas = TablaPaginas(tamano_tabla=10)
memoria_fisica = MemoriaFisica(tamano_memoria=30)

# Crear páginas y agregarlas a la tabla de páginas
pagina1 = Pagina(numero_pagina=0, contenido="Contenido de la página 0")
pagina2 = Pagina(numero_pagina=1, contenido="Contenido de la página 1")

tabla_paginas.agregar_pagina(pagina1)
tabla_paginas.agregar_pagina(pagina2)

# Simular carga de páginas en la memoria física
memoria_fisica.cargar_pagina(pagina1, direccion_memoria=0)
memoria_fisica.cargar_pagina(pagina2, direccion_memoria=10)

# Acceder al contenido de una página a través de la tabla de páginas
contenido_pagina = tabla_paginas.obtener_contenido_pagina(numero_pagina=1)
print(contenido_pagina)