# Sistema de recomendación de productos
# Proyecto de Inteligencia Artificial 2.0

productos = [
    {"nombre": "Laptop", "categoria": "tecnologia", "precio": 500000},
    {"nombre": "Audifonos", "categoria": "tecnologia", "precio": 50000},
    {"nombre": "Polera", "categoria": "ropa", "precio": 20000},
    {"nombre": "Zapatillas", "categoria": "ropa", "precio": 60000},
    {"nombre": "Libro", "categoria": "educacion", "precio": 15000}
]

preferencias = {
    "categoria": "tecnologia"
}


def recomendar_productos(productos, preferencias):
    recomendaciones = []

    for producto in productos:
        if producto["categoria"] == preferencias["categoria"]:
            recomendaciones.append(producto["nombre"])

    return recomendaciones


recomendaciones = recomendar_productos(productos, preferencias)

print("Sistema de recomendacion")
print("------------------------")
print("Tus preferencias:", preferencias)
print("Productos recomendados:")

for producto in recomendaciones:
    print("-", producto)