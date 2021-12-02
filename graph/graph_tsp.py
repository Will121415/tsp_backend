import matplotlib.pyplot as plt

def graph_fit_vs_gen(progress):
    plt.plot(progress)
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.title('Best Fitness vs Generation')
    plt.tight_layout()
    plt.show()

def graph_final_rute(best_route,cityList):

    x = []
    y = []
    for i in best_route:
        x.append(i.x)
        y.append(i.y)

    ##print(x)
    ##print(y)
    x.append(best_route[0].x)
    y.append(best_route[0].y)
    print(x)
    print(y)
    print(cityList[0].x)
    plt.plot(x, y, '--o')
    plt.xlabel('X')
    plt.ylabel('Y')
    ax = plt.gca()
    plt.title('Final Route Layout')
    bbox_props = dict(boxstyle="circle,pad=0.3", fc='C0', ec="black", lw=0.5)
    for i in range(1, len(cityList) + 1):
        ax.text(cityList[i - 1].x, cityList[i - 1].y, str(i), ha="center", va="center",
                size=8,
                bbox=bbox_props)
    plt.tight_layout()
    plt.show()
