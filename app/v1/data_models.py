from dataclasses import dataclass,field,asdict
from typing import List

@dataclass
class Food:
    id:int=field(default_factory=int)
    recipe:str=field(default_factory=str)
    ingredients:str=field(default_factory=str)
    cuisine:str=field(default_factory=str)
    course:str=field(default_factory=str)
    diet:str=field(default_factory=str)
    instructions:str=field(default_factory=str)

@dataclass
class FoodResponse:
    foods:List[Food]=field(default_factory=list)

    def __post_init__(self):
        self.foods=[Food(*i) for i in self.foods]

    def toJson(self):
        return asdict(self)