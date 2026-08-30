# Abstracción

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def hablar(self):
        pass
```

```python
class Perro(Animal):
    def hablar(self):
        print("Guau")
```
