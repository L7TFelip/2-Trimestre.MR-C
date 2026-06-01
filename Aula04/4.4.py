class Sensor: 
    def __init__(self, temperatura): 
        self.set_temperatura(temperatura)

    def set_temperatura(self, temperatura): 
        if -50 <= temperatura <= 150: 
            self.__temperatura = temperatura 
        else: 
            print(f"Valor inválido: {temperatura}. Fora do limite de -50 a 150.")
            self.__temperatura = None

    def status(self): 
        if self.__temperatura is None:
            return "Indefinido"
            
        if -50 <= self.__temperatura <= 80: 
            return "Normal" 
        elif 81 <= self.__temperatura <= 120: 
            return "Alerta" 
        else: 
            return "Crítico"

temp1 = Sensor(65) 
temp2 = Sensor(90) 
temp3 = Sensor(-45) 
temp4 = Sensor(145) 

print(f"Status temp1: {temp1.status()}")
print(f"Status temp2: {temp2.status()}")
print(f"Status temp3: {temp3.status()}")
print(f"Status temp4: {temp4.status()}")
