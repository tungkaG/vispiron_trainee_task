import math
import re

class Color:
    HEX_BASE = 16  # Basis für die Umwandlung von Hex in Dezimal

    def __init__(self, hex_value):
        self._validate_hex(hex_value)
        self.hex_value = hex_value.upper() 
        self.r, self.g, self.b = self._hex_to_rgb(hex_value)
        self.brightness = self._calculate_brightness()

    def _validate_hex(self, hex_value):
        if not isinstance(hex_value, str) or not re.fullmatch(r"#[0-9A-Fa-f]{6}", hex_value):
            raise ValueError(f"Ungültiger Hex-Farbwert: {hex_value}")

    def _hex_to_rgb(self, hex_value):
        return (
            int(hex_value[1:3], self.HEX_BASE),
            int(hex_value[3:5], self.HEX_BASE),
            int(hex_value[5:7], self.HEX_BASE),
        )

    def _calculate_brightness(self):
        r2, g2, b2 = self.r**2, self.g**2, self.b**2  # Vermeidung doppelter Berechnungen
        return math.sqrt(0.241 * r2 + 0.691 * g2 + 0.068 * b2)

    def get_brightness(self):
        return self.brightness

    def get_rgb(self):
        return self.r, self.g, self.b