from Candle import Candle
from OrderType import OrderType
from TimeFrame import TimeFrame


class Algorithm:

    def __init__(self, engine):
        self.engine = engine
        self.countsignal = 0
        self.initialize()

    def initialize(self):
        print(f'Im an Algo!')

        self.engine.setcomputingdates('2019/08/02', '2020/01/02')
        self.engine.addconsolidator('EURUSD', TimeFrame.M15, self.onconsolidate)

    def onconsolidate(self, candle: Candle):
        print(f'Event On Consolidate - {candle.tostring()}')

        self.countsignal += 1
        if self.countsignal >= 50:
            self.countsignal = 0
            self.engine.signal(OrderType.Buy, candle.pair, candle.close)
