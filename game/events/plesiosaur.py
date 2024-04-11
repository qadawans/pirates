from game import event
from game.player import Player
from game.context import Context
import game.config as config
import random

class Plesiosaur (Context, event.Event):
    '''Encounter with a plesiosaur! Uses the parser to decide what to do about it.'''
    def __init__ (self):
        super().__init__()
        self.name = "plesiosaur"
        self.plesiosaur = 1
        self.verbs['kill'] = self
        self.verbs['feed'] = self
        self.verbs['shoo'] = self
        self.result = {}
        self.go = False

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "kill"):
            self.go = True
            r = random.randint(1,10)
            if (r < 7):
                self.result["message"] = "the plesiosaur is dead."
                if (self.plesiosaur > 1):
                    self.plesiosaur = self.plesiosaur - 1
            else:
                c = random.choice(config.the_player.get_pirates())
                if (c.isLucky() == True):
                    self.result["message"] = "luckily, the plesiosaur is killed."
                else:
                    self.result["message"] = c.get_name() + " is attacked by the plesiosaur."
                    if (c.inflict_damage (self.plesiosaur, "chomped in half by the plesiosaur.")):
                        self.result["message"] = ".. " + c.get_name() + " is bitten in half by the plesiosaur!"

