# # Método de clase

```python
class Persona:
    especie = "Humano"

    @classmethod
    def mostrar_especie(cls):
        print(cls.especie)

    # cls → clase actual
```

```python
Persona.mostrar_especie()
```
