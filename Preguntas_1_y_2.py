import re

texto1 = """
Juan: 987654321
María: 912345678
Pedro: 998877665
Ana: 923456789
"""

numeros = re.findall(r"\d+", texto1)
print("Números encontrados:", numeros)
cantidad_total = len(numeros)
print("Total de números:", cantidad_total)




import re

texto2 = """
correo1@gmail.com
ventas@empresa.pe
contacto@universidad.edu.pe
soporte@hotmail.com
"""


patron_correos = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
correos = re.findall(patron_correos, texto2)
print("Correos encontrados:", correos)
cantidad_total = len(correos)
print("Total de correos:", cantidad_total)