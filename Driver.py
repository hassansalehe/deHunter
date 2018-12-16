import time

from Searcher import Searcher
from Composer import Composer
from Mailer   import Mailer
class Driver:
    def __init__(self):
        self.timestep_secs = 10
        self.searcher = Searcher()
        self.composer = Composer()
        self.mailer = Mailer()

    def sleep(self):
        print('==================')
        print('Going to sleep')
        time.sleep( self.timestep_secs )
        print('Have woken up')

    def loop(self):
        while (True):
            self.sleep()

            data = self.searcher.search()
            data = self.composer.compose( data )
            self.mailer.send( data )
