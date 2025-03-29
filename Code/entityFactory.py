import pygame

from Code.constants import windowHeight, entitySpeed
from Code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position = (0,0)):
        match entity_name:
            case "Player":
                #return Player(f"player{i}", (10, windowHeight / 2))

            #case "Run":

                list_run=[]
                for i in range(9):
                    list_run.append(Player(f"Player{i}", (10, windowHeight / 2)))

                return list_run