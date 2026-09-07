import re

texto = '''Hola, ¿cómo están todos? Mi nombre es Juan_Perez.
Bienvenido al sistema de logs (v1.0) - Fecha: 2026-09-06.
Esta es la primera sección de prueba. Código ID: 01.
Esta es la segunda línea del bloque B. Código ID: 202.
Esta es la tercera línea del bloque C. Código ID: 3004.

Soporte técnico: contacto@ejemplo.com o admin_2@red.org
Precios de oferta: $15.50, $200 y $1500 USD.
Servidores activos: 192.168.1.1 y 10.0.0.254.
Fin del documento.'''

# --- BÚSQUEDAS BÁSICAS DE CARACTERES ---

# \d -> Busca todos los dígitos individuales (0-9)
digitos = re.findall(r"\d", texto)

# \w -> Caracteres alfanuméricos (letras, números y guion bajo _)
alfanumericos = re.findall(r"\w+", texto) # Usamos + para juntar las palabras

# \W -> Símbolos, puntos, comas, signos de interrogación y espacios
simbolos = re.findall(r"\W", texto)

# \. -> Puntos literales en el texto (ej. en IPs, versiones, correos)
puntos = re.findall(r"\.", texto)

# --- BÚSQUEDAS DE CUANTIFICADORES Y RANGOS ---

# \d{2} -> Números de exactamente 2 dígitos (ej. '06', '01')
dos_digitos = re.findall(r"\b\d{2}\b", texto)

# \d{3,4} -> Números entre 3 y 4 dígitos (ej. '202', '3004', '1500')
tres_a_cuatro_digitos = re.findall(r"\b\d{3,4}\b", texto)

# --- INICIO Y FIN DE LÍNEA ---

# ^Esta -> Líneas que COMIENZAN con la palabra 'Esta' (usando flag re.M para multilínea)
inicio_esta = re.findall(r"^Esta", texto, flags=re.M)

# \d+\.$ -> Líneas que TERMINAN en un punto precedido de números
fin_punto = re.findall(r"\.$", texto, flags=re.M)

# --- CASOS PRÁCTICOS DE LA VIDA REAL ---

# Buscar correos electrónicos
correos = re.findall(r"[\w.-]+@[\w.-]+\.\w+", texto)

# Buscar fechas en formato YYYY-MM-DD
fechas = re.findall(r"\d{4}-\d{2}-\d{2}", texto)

# Buscar precios con signo $
precios = re.findall(r"\$\d+(?:\.\d+)?", texto)

# --- IMPRESIÓN DE RESULTADOS ---

print("--- RESULTADOS DE BÚSQUEDA ---")
print("1. Muestra de palabras alfanuméricas (primeras 5):", alfanumericos[:5])
print("2. Puntos encontrados:", len(puntos))
print("3. Números de 2 dígitos exactos:", dos_digitos)
print("4. Números de 3 a 4 dígitos:", tres_a_cuatro_digitos)
print("5. Líneas que empiezan con 'Esta':", len(inicio_esta))
print("\n--- CASOS PRÁCTICOS ---")
print("6. Correos encontrados:", correos)
print("7. Fechas detectadas:", fechas)
print("8. Precios detectados:", precios)