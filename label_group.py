class LabelGroup(object):

    def __init__(self, label, count):
        self.label = label
        self.count = count

    def __lt__(self, other):
        return self.count < other.count
