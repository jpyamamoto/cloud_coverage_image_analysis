class Image:
    def __init__(self, name, pixels):
        name_divided = name.split('.')

        self.name = ".".join(name_divided[0:-1])
        self.extension = name_divided[-1]
        self.pixels = pixels

