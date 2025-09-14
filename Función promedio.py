def calcular_promedio_temperaturas(datos_ciudades: dict) -> None:
    """
    Calcula y muestra el promedio de temperaturas de varias ciudades a lo largo de 4 semanas.

    Args:
        datos_ciudades (dict): Un diccionario que contiene listas de datos de temperaturas.
                               Las claves son los nombres de las ciudades y los valores son
                               listas de temperaturas diarias en grados Fahrenheit (°F).
    """

    for ciudad, semanas_de_datos in datos_ciudades.items():
        print(f"Calculando promedio para: {ciudad}")
        temperaturas_totales = []

        # Iterar a través de las 4 semanas y recolectar todas las temperaturas
        for semana in semanas_de_datos:
            # Asegurarse de que cada día de la semana sea un diccionario con la clave 'temp'
            if isinstance(semana, list):
                for dia in semana:
                    if isinstance(dia, dict) and 'temp' in dia:
                        temperaturas_totales.append(dia['temp'])

        # Calcular el promedio en Fahrenheit si hay datos
        if temperaturas_totales:
            promedio_fahrenheit = sum(temperaturas_totales) / len(temperaturas_totales)

            # Convertir de Fahrenheit a Celsius
            promedio_celsius = (promedio_fahrenheit - 32) * 5 / 9

            print(f"Temperatura promedio en {ciudad} durante las 4 semanas: {promedio_celsius:.2f}°C")
            print("-" * 50)
        else:
            print(f"No hay datos de temperatura válidos para {ciudad}.")
            print("-" * 50)

# Datos de temperaturas de las ciudades proporcionados
datos_temperaturas = {
    "Tabacundo": [
        [{"day": "Lunes", "temp": 50}, {"day": "Martes", "temp": 48}, {"day": "Miércoles", "temp": 45},
         {"day": "Jueves", "temp": 51}, {"day": "Viernes", "temp": 50}, {"day": "Sábado", "temp": 46},
         {"day": "Domingo", "temp": 49}],
        [{"day": "Lunes", "temp": 51}, {"day": "Martes", "temp": 50}, {"day": "Miércoles", "temp": 53},
         {"day": "Jueves", "temp": 50}, {"day": "Viernes", "temp": 57}, {"day": "Sábado", "temp": 49},
         {"day": "Domingo", "temp": 53}],
        [{"day": "Lunes", "temp": 48}, {"day": "Martes", "temp": 50}, {"day": "Miércoles", "temp": 52},
         {"day": "Jueves", "temp": 49}, {"day": "Viernes", "temp": 51}, {"day": "Sábado", "temp": 47},
         {"day": "Domingo", "temp": 49}],
        [{"day": "Lunes", "temp": 56}, {"day": "Martes", "temp": 58}, {"day": "Miércoles", "temp": 50},
         {"day": "Jueves", "temp": 48}, {"day": "Viernes", "temp": 39}, {"day": "Sábado", "temp": 49},
         {"day": "Domingo", "temp": 51}]
    ],
    "Cayambe": [
        [{"day": "Lunes", "temp": 40}, {"day": "Martes", "temp": 44}, {"day": "Miércoles", "temp": 48},
         {"day": "Jueves", "temp": 41}, {"day": "Viernes", "temp": 43}, {"day": "Sábado", "temp": 45},
         {"day": "Domingo", "temp": 49}],
        [{"day": "Lunes", "temp": 43}, {"day": "Martes", "temp": 46}, {"day": "Miércoles", "temp": 40},
         {"day": "Jueves", "temp": 42}, {"day": "Viernes", "temp": 39}, {"day": "Sábado", "temp": 47},
         {"day": "Domingo", "temp": 41}],
        [{"day": "Lunes", "temp": 41}, {"day": "Martes", "temp": 45}, {"day": "Miércoles", "temp": 48},
         {"day": "Jueves", "temp": 40}, {"day": "Viernes", "temp": 42}, {"day": "Sábado", "temp": 46},
         {"day": "Domingo", "temp": 40}],
        [{"day": "Lunes", "temp": 44}, {"day": "Martes", "temp": 47}, {"day": "Miércoles", "temp": 49},
         {"day": "Jueves", "temp": 41}, {"day": "Viernes", "temp": 44}, {"day": "Sábado", "temp": 47},
         {"day": "Domingo", "temp": 40}]
    ],
    "Ayora": [
        [{"day": "Lunes", "temp": 36}, {"day": "Martes", "temp": 35}, {"day": "Miércoles", "temp": 40},
         {"day": "Jueves", "temp": 39}, {"day": "Viernes", "temp": 38}, {"day": "Sábado", "temp": 35},
         {"day": "Domingo", "temp": 32}],
        [{"day": "Lunes", "temp": 39}, {"day": "Martes", "temp": 31}, {"day": "Miércoles", "temp": 33},
         {"day": "Jueves", "temp": 40}, {"day": "Viernes", "temp": 47}, {"day": "Sábado", "temp": 44},
         {"day": "Domingo", "temp": 41}],
        [{"day": "Lunes", "temp": 34}, {"day": "Martes", "temp": 33}, {"day": "Miércoles", "temp": 35},
         {"day": "Jueves", "temp": 32}, {"day": "Viernes", "temp": 39}, {"day": "Sábado", "temp": 36},
         {"day": "Domingo", "temp": 33}],
        [{"day": "Lunes", "temp": 38}, {"day": "Martes", "temp": 40}, {"day": "Miércoles", "temp": 32},
         {"day": "Jueves", "temp": 39}, {"day": "Viernes", "temp": 41}, {"day": "Sábado", "temp": 40},
         {"day": "Domingo", "temp": 39}]
    ]
}

# Llamar a la función con los datos
calcular_promedio_temperaturas(datos_temperaturas)