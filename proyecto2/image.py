class Image:
    def __init__(self, name, pixels):
        name_divided = name.split('.')

        self.name = name_divided[0]
        self.extension = name_divided[1]
        self.pixels = pixels

