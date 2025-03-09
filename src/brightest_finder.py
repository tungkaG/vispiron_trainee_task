from src.color import Color

class BrightestColorFinder:
    @staticmethod
    def find_brightest(colors):
        color_objects = [Color(hex_value) for hex_value in colors]
        
        if not color_objects:
            return None
        
        brightest_color = color_objects[0]
        for color in color_objects:
            if color.get_brightness() > brightest_color.get_brightness():
                brightest_color = color
        
        return brightest_color
