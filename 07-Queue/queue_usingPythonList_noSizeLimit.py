# queue_usingPythonList_noSizeLimit

class Queue:
    def __init__(self):
        self.items = list()

    def __str__(self):
        values = [str(v) for v in self.items]
        return ' '.join(values)

    def isEmpty(self):
        return True if len(self.items) == 0 else False 

    