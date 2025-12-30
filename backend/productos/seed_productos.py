from productos.models import Producto

def run():
    productos = [
        {
            "nombre": "CAVIAR HIDRO NUTRITIVO",
            "descripcion": "Tratamiento capilar con extracto de caviar que nutre profundamente el cabello.",
            "precio": 15000,
            "disponible": True,
            "imagen": "productos/caviar.png"
        },
        {
            "nombre": "Crema Ácida",
            "descripcion": "Crema ácida para alisado, reduce frizz y mejora la manejabilidad.",
            "precio": 0,
            "disponible": False,
            "imagen": "productos/cremaacida.png"
        },
        {
            "nombre": "Máscara Capilar Almendras",
            "descripcion": "Nutre y repara el cabello seco y dañado.",
            "precio": 13000,
            "disponible": True,
            "imagen": "productos/mascaracapilaralmendras.png"
        },
        {
            "nombre": "Máscara Capilar Coco & Vainilla",
            "descripcion": "Hidrata profundamente y deja aroma delicioso.",
            "precio": 13000,
            "disponible": True,
            "imagen": "productos/mascaracapilarcocovainilla.png"
        },
        {
            "nombre": "Shampoo Extra Ácido & Acondicionador",
            "descripcion": "Limpia profundamente y aporta brillo saludable.",
            "precio": 17000,
            "disponible": True,
            "imagen": "productos/shampooacondicionador.png"
        },
        {
            "nombre": "Máscara Capilar Keratina",
            "descripcion": "Fortalece y repara el cabello dañado.",
            "precio": 13000,
            "disponible": True,
            "imagen": "productos/mascaracapilarkeratina.png"
        }
    ]

    for p in productos:
        Producto.objects.get_or_create(
            nombre=p["nombre"],
            defaults=p
        )

    print("✅ Productos iniciales cargados")
