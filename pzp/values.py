#Temperature definitions
class FloatValue:
    def __init__(self, name: str, value: float):
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f"{self.name}={self.value}"

class BoolValue:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f"{self.name}={self.value}"
