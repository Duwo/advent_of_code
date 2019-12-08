import os


def read_image():
    file = os.path.dirname(os.path.abspath(__file__)) + '/data/input'
    with open(file) as fh:
        image_code = fh.read()
    return image_code


def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

class Image():
    def __init__(self, width, height, code):
        self.width = width
        self.height = height
        self.code = code
        self.layer_size = width * height
        self.layers = []


    def create_layers(self):
        chunks = divide_chunks(self.code, self.layer_size)
        for chunk in chunks:
            layer = Layer(chunk, self.width, self.height)
            self.layers.append(layer)

        # print(self.layers[-2].code)

    def decode(self):
        # print(len(self.layers))
        pixels = ''
        for i in range(self.layer_size):
            print(i)
            for pixel_i in range(i, len(self.code), self.layer_size):
                print(pixel_i)
                pixel = self.code[pixel_i]
                if pixel in ['0','1']:
                    pixels += pixel
                    break

        return pixels



    def layer_with_min(self, number):
        number_count = []
        for i, layer in enumerate(self.layers):
            number_count.append(self.count_number(layer, number))

        index = number_count.index(min(number_count))

        return self.layers[index]

    def count_number(self, layer, number):
        return layer.code.count(number)

class Layer():
    def __init__(self, code, width, height):
        self.code = code
        self.width = width
        self.height = height
        self.rows = self.create_rows()

    def create_rows(self):
        row_chunks = divide_chunks(self.code, self.width)
        rows = []
        for row_chunk in row_chunks:
            rows.append(row_chunk)
        return rows


def main():
    # width, height = [3, 2]
    # image_code = str(123456789012)
    width, height = [25, 6]
    image_code = read_image()
    image = Image(width, height, image_code.strip())
    pixels = image.decode()
    layer = Layer(pixels, width, height)
    for row in layer.rows:
        print(row)
    # image.create_layers()
    # print(len(image.layers[0].code))
    # layer = image.layer_with_min('0')
    # one_count = image.count_number(layer, '1')
    # two_count = image.count_number(layer, '2')

    # print(one_count * two_count)

if __name__ == "__main__":
    main()
