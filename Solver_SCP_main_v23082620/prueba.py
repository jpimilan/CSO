class IncrementalCSO:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        
        self.prev_error = 0
        self.prev_integral = 0
        self.prev_derivative = 0
        
    def update(self, setpoint, actual_value):
        error = setpoint - actual_value
        derivative = error - self.prev_error
        integral = self.prev_integral + error
        
        output = self.kp * error + self.ki * integral + self.kd * derivative
        
        self.prev_error = error
        self.prev_integral = integral
        self.prev_derivative = derivative
        
        return output

# Parámetros del control CSO
kp = 1.0
ki = 0.1
kd = 0.01

# Crear el controlador CSO incremental
CSO = IncrementalCSO(kp, ki, kd)

# Valores iniciales
setpoint = 50
actual_value = 0

# Simulación de control
for _ in range(50):
    control_output = CSO.update(setpoint, actual_value)
    actual_value += control_output
    
    print("Setpoint:", setpoint, "Actual:", actual_value, "Control:", control_output)