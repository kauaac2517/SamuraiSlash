from Code.constants import windowHeight
from Code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position = (0,0)):
        match entity_name:
            case "Player":
                return Player("Player", (10, windowHeight / 2))
                #list_bg=[]
                #for i in range(1):
                    #list_bg.append(Background(f"bgInGame{i}", (0, 0)))
                #return list_bg
