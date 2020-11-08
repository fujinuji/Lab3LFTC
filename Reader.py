class Reader:
    def read(self, fileName):
        file = open(fileName, 'r')
        text = file.readline()

        buffer = []
        count = 1

        while text != "":
            buffer.append(text)
            text = file.readline()
            count += 1

            if count == 10 or text == "":
                yield_buffer = ''.join(buffer)
                count = 1
                yield yield_buffer

                buffer = []

        file.close()