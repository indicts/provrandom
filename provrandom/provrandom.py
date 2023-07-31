class Random:
    def __init__(self, random_information=None):
        self.random_information = random_information or self._generate_random_information()

    def _generate_random_information(self):
        return self._generate_random_string(32)  # Generate a random string of length 32

    def _generate_random_string(self, length):
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        return ''.join(self._generate_random_char(characters) for _ in range(length))

    def _generate_random_char(self, characters):
        seed = self._generate_seed()
        index = seed % len(characters)
        return characters[index]

    def _generate_seed(self):
        # A simple custom pseudo-random number generator
        # You can replace this with any custom algorithm of your choice
        seed = (1103515245 * self._generate_seed()) + 12345
        return seed & 0xFFFFFFFF  # Limit to 32 bits

    def number(self, min_value, max_value):
        seed = self._generate_seed()
        return min_value + (seed % (max_value - min_value + 1))

    def _float(self, min_value, max_value):
        seed = self._generate_seed()
        normalized = seed / 0xFFFFFFFF  # Scale to [0, 1)
        return min_value + normalized * (max_value - min_value)

    def string(self, length):
        return self._generate_random_string(length)

    def _random_container(self, length, min_value, max_value):
        return [self.number(min_value, max_value) for _ in range(length)]

    def _hash(self):
        h = 0x811c9dc5
        for char in self.random_information.encode():
            h ^= char
            h *= 0x1000193
            h &= 0xFFFFFFFF
        return format(h, '08x')  # Return the hash in hexadecimal format with leading zeros