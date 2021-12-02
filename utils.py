
from graph.graph_tsp import graph_fit_vs_gen,graph_final_rute
from models.district import District
import  tsp

def init_ag(list_district,pop_size,elite_size,mutation_rate,n_generations):
    district_list = []

    for i in range(0, len(list_district)):
        district_list.append(District(name=list_district[i].name, x=list_district[i].x, y=list_district[i].y))

    response_tsp = tsp.genetic_algorithm(district_list=district_list, popSize=pop_size, eliteSize=elite_size,
                                         mutationRate=mutation_rate, generations=n_generations)
    ##print(response_tsp.best_route)
    ##print(response_tsp.progress)
    graph_fit_vs_gen(response_tsp.progress)
    graph_final_rute(response_tsp.list_best_route[0],district_list)

    return response_tsp