# Composición

```python
class Motor:
    def encender(self):
        print("Motor encendido")


class Auto:
    def __init__(self):
        self.motor = Motor()

    def arrancar(self):
        self.motor.encender()
```
