from flarmnet.record import Record

class Reader:
    def __init__(self, file):
        self.file = file

    def read(self):
        for line in self.file:
            # Valid records have at least 172 characters
            if len(line) < 172:
                continue

            yield Record(line)
