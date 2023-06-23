import pandas as pd

# Crear un DataFrame con datos imaginarios
data = {
    'Nombre': ['Juan', 'María', 'Carlos', 'Laura', 'Pedro'],
    'Edad': [28, 34, 29, 42, 36],
    'Ciudad': ['Buenos Aires', 'Madrid', 'Lima', 'Sao Paulo', 'México DF'],
    'Puntuación': [75, 82, 88, 95, 67]
}

df = pd.DataFrame(data)

# Mostrar el DataFrame completo
print(df)
print("##################################")
