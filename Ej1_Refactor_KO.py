# Sistema de venta de billetes de avión

class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, fecha, salida, llegada, precio):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.salida = salida
        self.llegada = llegada
        self.precio = precio

class Pasajero:
    def __init__(self, nombre, apellido, edad, telefono, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.correo = correo

class Informacion:
    def __init__(self, vuelo, pasajero, asientos):
        self.vuelo = vuelo
        self.pasajero = pasajero
        self.asientos = asientos

def mostrar_vuelos_disponibles(vuelos):
    print("Vuelos disponibles:")
    for vuelo in vuelos:
        print(f"- Vuelo: {vuelo.numero_vuelo}, {vuelo.origen} - {vuelo.destino}, Fecha: {vuelo.fecha}, Salida: {vuelo.salida}, Llegada: {vuelo.llegada}, Precio: {vuelo.precio:.2f} €")

def solicitar_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingresa un número válido.")

def reservar_vuelo(vuelos, numero_vuelo, pasajero, cantidad):
    for vuelo in vuelos:
        if vuelo.numero_vuelo == numero_vuelo:
            if cantidad <= 0:
                print("La cantidad de asientos debe ser mayor que cero.")
                return
            if cantidad > 10:
                print("No se pueden reservar más de 10 asientos.")
                return
            reserva = Informacion(vuelo, pasajero, cantidad)
            print(f"\n¡Reserva confirmada para el vuelo {vuelo.numero_vuelo}!")
            print(f"Pasajero: {pasajero.nombre} {pasajero.apellido}")
            print(f"Asientos reservados: {cantidad}")
            return
    print("No se encontró ningún vuelo con ese número.")


def main():
    vuelos = [
        Vuelo("AA123", "Nueva York", "Los Angeles", "2024-05-15", "08:00", "11:00", 250.00),
        Vuelo("AA456", "Los Angeles", "Chicago", "2024-05-20", "10:00", "13:00", 200.00),
        Vuelo("AA789", "Chicago", "Miami", "2024-05-25", "12:00", "15:00", 300.00)
    ]

    print("Bienvenido al sistema de venta de billetes de avión.")
    opcion = input("Seleccione una opción:\n1. Ver vuelos disponibles\n2. Reservar vuelo\nIngrese su opción: ")

    if opcion == '1':
        mostrar_vuelos_disponibles(vuelos)
    elif opcion == '2':
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = solicitar_entero("Edad: ")
        telefono = input("Teléfono: ")
        correo = input("Correo electrónico: ")

        pasajero = Pasajero(nombre, apellido, edad, telefono, correo)

        numero_vuelo = input("Número de vuelo a reservar: ")
        cantidad = solicitar_entero("Cantidad de asientos (máx. 10): ")

        reservar_vuelo(vuelos, numero_vuelo, pasajero, cantidad)
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
