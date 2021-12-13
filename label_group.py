class LabelGroup(object):

    def __init__(self, label, count):
        self.label = label
        self.count = count

    def __lt__(self, other):
        """
        重写 __lt__ 对比大小
        :param other:
        :return:
        """
        return self.count < other.count
