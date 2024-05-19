import re

def procesar_codigo_cpp(codigo):
    # Dividir el código en líneas
    lineas = codigo.split('\n')
    
    # Tabla hash para almacenar las palabras y signos con sus posiciones
    tabla_hash = {}
    
    # Expresiones regulares para detectar palabras y operadores
    token_regex = re.compile(r'\b\w+\b|[=;+\-*/]')
    
    # Procesar cada línea
    for num_linea, linea in enumerate(lineas, start=-1):
        # Buscar todas las palabras y signos en la línea
        tokens = token_regex.finditer(linea)
        for token in tokens:
            texto_token = token.group()
            # La posición inicial del token en la línea (columna)
            columna = token.start()
            # Usar la posición (línea, columna) como clave
            clave = (num_linea, columna)
            # Almacenar en la tabla hash
            tabla_hash[clave] = texto_token
    
    return tabla_hash

# Ejemplo de código C++ para analizar
codigo_cpp = """
int suma = 0;
suma = 54 + 20;
int resta = 0;
resta = 20 - 10;
"""

# Procesar el código y obtener la tabla hash
tabla_hash = procesar_codigo_cpp(codigo_cpp)

# Imprimir la tabla hash
for clave, token in sorted(tabla_hash.items()):
    print(f"Clave: {clave}, Token: {token}")
