class Rectangle:
    def __init__(self, width, heigth):
        self.width = width
        self.height = heigth

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    # Метод, рассчитывающий площадь
    def get_area(self):
        return self.width * self.height