from pydantic import BaseModel
from typing import Union

class ResponseTsp(BaseModel):
        progress: list[float]
        list_best_route: list[Union[list,list[list]]]

class DistrictDTO(BaseModel):
        name: int
        x: int
        y: int

class InitTsp(BaseModel):
    list_district: list[DistrictDTO]
    pop_size: int
    elite_size: int
    mutation_rate: float
    n_generations: int


