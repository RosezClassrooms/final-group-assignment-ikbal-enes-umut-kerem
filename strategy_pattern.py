import random
from abc import ABC, abstractmethod


class Runner():
    '''
    The Runner defines the interface of interest to clients.
    '''

    def __init__(self, name=None, strat=None):
        '''
        The Runner accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        '''
        self.name = name
        self.energy = 100
        self.pace = 5
        self.run_dist = 0
        self.strategy = strat

    def __str__(self):
        return f"\n{self.name} has {self.energy} energy, and his current pace is {self.pace}. \
            \nHe covered {self.run_dist} meters by now.\
            \nHis current strategy: {str(self.strategy.__class__.__name__)}."


    @property
    def strategy(self):
        '''
        The Runner maintains a reference to one of the Strategy objects. The
        Runner does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        '''

        return self._strategy

    @strategy.setter
    def strategy(self, strat=None):
        '''
        The Runner allows replacing a Strategy object at runtime.
        '''

        self._strategy = strat

    def delegate(self):
        '''
        The Runner delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        '''

        self._strategy.status(self)


class Strategy(ABC):
    '''
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Runner uses this interface to call the algorithm defined by Concrete
    Strategies.
    '''

    @abstractmethod
    def status(self, runner:Runner):
        pass


'''
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Runner.
'''

class Sprint(Strategy):
    def status(self, runner:Runner):
        runner.energy -= 40
        runner.pace = 8
        runner.run_dist += 40
        return runner.energy, runner.pace, runner.run_dist

class NormalPace(Strategy):
    def status(self, runner:Runner):
        runner.energy -= 20
        runner.pace = 5
        runner.run_dist += 28
        return runner.energy, runner.pace, runner.run_dist

class SaveEnergy(Strategy):
    def status(self, runner:Runner):
        runner.energy -= 4
        runner.pace = 2
        runner.run_dist += 12
        return runner.energy, runner.pace, runner.run_dist


def main():

    print("----------WELCOME TO THE 100M SPRINT RACE AT OLYMPICS!----------")

    strategies = [Sprint(), NormalPace(), SaveEnergy()]

    bolt = Runner(name='Usain Bolt', strat=NormalPace())
    guliyev = Runner(name='Mo Farah', strat=NormalPace())

    winner = ""

    while((bolt.energy > 0 and guliyev.energy > 0) and\
        (bolt.run_dist < 100 and guliyev.run_dist < 100)):

        # refer to Runner.delegate()
        bolt.delegate()
        guliyev.delegate()

        # choosing random strategies
        bolt.strategy = random.choice(strategies)
        guliyev.strategy = random.choice(strategies)

        # printing the statuses
        print(bolt)
        print(guliyev)

        # deciding the race winner
        if((bolt.run_dist > 88) and (bolt.run_dist > guliyev.run_dist)):
            winner = "\nBOLT WON THE RACE!"
        if((guliyev.run_dist > 88) and (guliyev.run_dist > bolt.run_dist)):
            winner = "\nGULIYEV WON THE RACE!"

    # printing the winner
    if(winner):
        print(winner)
    else:
        print("IT IS A DRAW!")
        

if __name__ == "__main__":
    main()
