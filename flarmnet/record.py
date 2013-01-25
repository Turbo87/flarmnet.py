from flarmnet.encryption import decrypt

class Record:
    def __init__(self, line):
        self._line = line.strip()
        self._cache = {}

    def get_or_cache(self, attribute, start, end):
        if attribute not in self._cache:
            self._cache[attribute] = decrypt(self._line[start:end])

        return self._cache[attribute]

    @property
    def line(self):
        return self._line

    @property
    def id(self):
        return self.get_or_cache('id', 0, 12)

    @property
    def pilot(self):
        return self.get_or_cache('pilot', 12, 54)

    @property
    def airfield(self):
        return self.get_or_cache('airfield', 54, 96)

    @property
    def plane_type(self):
        return self.get_or_cache('plane_type', 96, 138)

    @property
    def registration(self):
        return self.get_or_cache('registration', 138, 152)

    @property
    def competition_id(self):
        return self.get_or_cache('competition_id', 152, 158)

    @property
    def radio_frequency(self):
        return self.get_or_cache('radio_frequency', 158, 172)
