from fastapi import APIRouter
from typing import Optional
import utils
from models.responseTsp import InitTsp, ResponseTsp

router = APIRouter(prefix='/tsp', tags=['tsp'])


def _make_response(tsp: ResponseTsp) -> ResponseTsp:
    return ResponseTsp(
       progress=tsp.progress,
        list_best_route=tsp.list_best_route
    )

@router.post("/")
def init_tsp(info: InitTsp):
    response_tsp = utils.init_ag(list_district=info.list_district,pop_size=info.pop_size,elite_size=info.elite_size,
            mutation_rate=info.mutation_rate,n_generations=info.n_generations)
    return _make_response(response_tsp)


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}