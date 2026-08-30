# Método estático

```python
class Calculadora:

    @staticmethod
    def sumar(a, b):
        return a + b

    # no self, no cls
```

```python
Calculadora.sumar(3, 5)
```
