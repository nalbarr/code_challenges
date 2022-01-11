class HelloRepository(object):
    def __init__(self, part1):
        self.part1 = part1

    def get_greeting(self, part2):
        message = "{0} {1}".format(self.part1, part2)
        return message
