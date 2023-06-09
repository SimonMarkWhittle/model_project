
class Numberstreamator:

    def __init__(self, streamcount, modnum=7, startnum=-100):
        self.streamcount = streamcount
        self.modnum = modnum
        self.nextnum = startnum

    def stream_numbers(self):
        retlist = [ n % self.modnum for n in range(self.nextnum, self.nextnum + self.streamcount) ]
        self.nextnum += self.streamcount
        return retlist
