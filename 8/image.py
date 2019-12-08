import os


def read_image():
    file = os.path.dirname(os.path.abspath(__file__)) + '/data/input'
    with open(file) as fh:
        image_code = fh.read()
    return image_code


class Image():
    def __init__(self, width, height, code):
        self.width = width
        self.height = height
        self.code = code
        self.layer_size = width * height
        self.layers = []

    def divide_chunks(self,l, n):
        for i in range(0, len(l), n):
            self.layers.append(l[i:i + n])

    def create_layers(self):
        self.divide_chunks(self.code, self.layer_size)
        self.layers = self.layers[:-2]

    def layer_with_min(self, number):
        number_count = []
        for i, layer in enumerate(self.layers):
            number_count.append(self.count_number(layer, number))
        index = number_count.index(min(number_count))

        return self.layers[index]

    def count_number(self, layer, number):
        return layer.count(number)

def main():
    # width, height = [3, 2]
    # image_code = str(123456789012)
    width, height = [25, 6]
    image_code = read_image()
    image = Image(width, height, image_code)
    image.create_layers()
    layer = image.layer_with_min('0')
    one_count = image.count_number(layer, '1')
    two_count = image.count_number(layer, '2')

    print(one_count * two_count)




if __name__ == "__main__":
    main()
