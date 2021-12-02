import utils
from fastapi import FastAPI
import  random

from models.district import District
from routers.tsp_router import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    # Add other origins here
    # You can add "*" for allow all origins
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(router)

if __name__ == '__main__':
    district_list = []

    for i in range(0, 15):
        district_list.append(District(name=i, x=int(random.random() * 200), y=int(random.random() * 200)))
    utils.init_ag(list_district = district_list,pop_size=30,elite_size=10,mutation_rate=0.01,n_generations=50)








