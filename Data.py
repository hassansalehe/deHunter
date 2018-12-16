class Data:
    def __init__(self):
        self.results = []

    def reset(self):
        self.results = []

    def append(self, search_data):
        self.results.append( search_data )

    def getResults(self):
        return self.results
