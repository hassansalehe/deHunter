class Composer:
    def __init__(self):
        pass

    def compose(self, data):
        print ('Composer: composing messages')
        new_houses = 'New houses: '
        for d in data:
            new_houses += d + '\n'

        return new_houses
        #results = data.getResults()
        #for result in results:
        #print (result)
