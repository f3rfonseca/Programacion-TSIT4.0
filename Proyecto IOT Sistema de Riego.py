import time
import random
import tkinter as tk

class DispositivoIoT:
    def __init__(self, nombre):
        self.nombre = nombre

    def leer_datos(self):
        pass

    def controlar(self, *args):
        pass

class SensorHumedad(DispositivoIoT):
    def __init__(self, nombre):
        super().__init__(nombre)

# Generar un valor aleatorio para simular la humedad del suelo
    def leer_datos(self):
        return random.randint(0, 100)

class SensorTemperatura(DispositivoIoT):
    def __init__(self, nombre):
        super().__init__(nombre)

# Generar un valor aleatorio para simular la temperatura ambiente
    def leer_datos(self):
        return random.randint(20, 30) 

class SensorCalidadAgua(DispositivoIoT):
    def __init__(self, nombre):
        super().__init__(nombre)

# Generar un valor aleatorio para simular la calidad del agua
    def leer_datos(self):
        calidad = random.choice(["Buena", "Regular", "Mala"])
        return calidad

class ActuadorRiego(DispositivoIoT):
    def __init__(self, nombre):
        super().__init__(nombre)

# Simulación de control de actuador de riego
    def controlar(self, estado):
        if estado:
            print(f"{self.nombre}: Riego activado")
        else:
            print(f"{self.nombre}: Riego desactivado")

class SistemaRiego:
    def __init__(self, sensor_humedad, sensor_temperatura, sensor_calidad_agua, actuador, umbral_humedad, tiempo_riego):
        self.sensor_humedad = sensor_humedad
        self.sensor_temperatura = sensor_temperatura
        self.sensor_calidad_agua = sensor_calidad_agua
        self.actuador = actuador
        self.umbral_humedad = umbral_humedad
        self.tiempo_riego = tiempo_riego

        self.root = tk.Tk()
        self.root.title("Sistema de Riego Automatizado")
        self.root.geometry("400x200")

        self.root.configure(bg="white")
        
        self.label_humedad = tk.Label(self.root, text="Humedad del suelo: ", bg="white")
        self.label_humedad.pack()

        self.label_temperatura = tk.Label(self.root, text="Temperatura ambiente: ", bg="white")
        self.label_temperatura.pack()

        self.label_calidad_agua = tk.Label(self.root, text="Calidad del agua: ", bg="white")
        self.label_calidad_agua.pack()

        self.label_proximo_riego = tk.Label(self.root, text="Próximo riego automático a las: ", bg="white")
        self.label_proximo_riego.pack()

        # Variables para almacenar los datos anteriores
        self.humedad_anterior = None
        self.temperatura_anterior = None
        self.calidad_agua_anterior = None

    def monitorear_humedad(self):
        humedad = self.sensor_humedad.leer_datos()
        self.label_humedad.config(text=f"Humedad del suelo: {humedad}")
        self.humedad_anterior = humedad
        return humedad

    def monitorear_temperatura(self):
        temperatura = self.sensor_temperatura.leer_datos()
        self.label_temperatura.config(text=f"Temperatura ambiente: {temperatura}°C")
        self.temperatura_anterior = temperatura
        return temperatura

    def monitorear_calidad_agua(self):
        calidad_agua = self.sensor_calidad_agua.leer_datos()
        self.label_calidad_agua.config(text=f"Calidad del agua: {calidad_agua}")
        self.calidad_agua_anterior = calidad_agua
        return calidad_agua

    def calcular_hora_riego(self, humedad_actual):

        # Calcula el tiempo en minutos hasta el próximo riego basado en la humedad actual
        tiempo_riego = (100 - humedad_actual) * 2  # Por ejemplo, más seco, más rápido el riego
        return time.strftime("%H:%M", time.localtime(time.time() + tiempo_riego * 20))

    def activar_riego(self):
        print("Iniciando riego...")
        self.actuador.controlar(True)
        print("Riego activado")
        time.sleep(self.tiempo_riego)
        self.actuador.controlar(False)
        print("Riego desactivado")
        print("Riego finalizado.")

    def ejecutar_sistema(self):
        humedad_actual = self.monitorear_humedad()
        temperatura_actual = self.monitorear_temperatura()
        calidad_agua_actual = self.monitorear_calidad_agua()
        hora_riego = self.calcular_hora_riego(humedad_actual)
        self.label_proximo_riego.config(text=f"Próximo riego automático a las: {hora_riego} debido a la humedad del suelo.")
        if humedad_actual < self.umbral_humedad:
            self.activar_riego()
        
        # Función para actualizar los datos cada 20 segundos
        self.root.after(20000, self.ejecutar_sistema)

# Crea instancias de los dispositivos
sensor_humedad = SensorHumedad("Sensor de Humedad")
sensor_temperatura = SensorTemperatura("Sensor de Temperatura")
sensor_calidad_agua = SensorCalidadAgua("Sensor de Calidad del Agua")
actuador = ActuadorRiego("Actuador de Riego")

# Crea instancia del sistema de riego
sistema_riego = SistemaRiego(sensor_humedad, sensor_temperatura, sensor_calidad_agua, actuador, umbral_humedad=40, tiempo_riego=10)

# Ejecuta el sistema de riego
sistema_riego.ejecutar_sistema()

# Inicia el bucle de la interfaz de usuario
sistema_riego.root.mainloop()
