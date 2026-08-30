# Generadores infinitos

```python
def contador():
    numero = 0

    while True:
        yield numero
        numero += 1
```
