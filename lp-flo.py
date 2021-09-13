from pulp import *
from sklearn.metrics.pairwise import euclidean_distances
from helper import *


def FLO_M_LP(Facilities, Clients, Distances, z, m):
    # Setting the Problem
    Facilities = ['STATION {}'.format(x) for x in Facilities]
    prob = LpProblem("Facility Location Problem with m outliers", LpMinimize)
    # Defining our Desicion Variables
    # is facility f open
    use_facility = LpVariable.dicts("Use Facility", Facilities, 0, 1, LpBinary)
    #is client v served by facility f
    ser_customer = LpVariable.dicts("Service", [(v,f) for v in Clients for f in Facilities], 0, 1, LpBinary)
    #is point v outlier
    outlier_customer = LpVariable.dicts("Outlier", Clients, 0, 1, LpBinary)
    # Setting the Objective Function
    #min \sum d_vf*x_vf + z*\sum y_f
    prob +=  lpSum(Distances[v][int(f.split(' ')[1])]*ser_customer[(v,f)] for f in Facilities for v in Clients)\
        + z*lpSum(use_facility[f] for f in Facilities)


    # Costraints
    # for all v,f : y_f-x_vf >=0
    for v in Clients:
        for f in Facilities:
            prob += use_facility[f] - ser_customer[(v,f)] >=0


    # for all v: \sum f x_vf + o_v >=1
    for v in Clients:
        prob += lpSum(ser_customer[(v,f)] for f in Facilities) + outlier_customer[v] >=1

    # -\sum o_v >= -m
    prob+= -lpSum(outlier_customer[v] for v in Clients) >= -m

    # forall v,f: x_vf, y_f, o_v >=0
    for v in Clients:
        prob += outlier_customer[   v] >= 0 #o_v
        for f in Facilities:
            prob += use_facility[f] >=0 # y_f
            prob += ser_customer[(v,f)] >=0 #x_vf

    # SOLUTION
    prob.solve()
    print("Status: ", LpStatus[prob.status])
    open_facilities, final_clients, outliers = [], [], []
    # PRINT DECISION VARIABLES
    TOL = .0001  # tolerance for identifying which locations the algorithm has chosen
    for f in Facilities:
        if use_facility[f].varValue > TOL:
            current_f = int(f.split(' ')[1])
            open_facilities.append(current_f)
            print("Establish facility at site: ", current_f)

    for v in Clients:
        for f in Facilities:
            if ser_customer[(v,f)].varValue > TOL:
                current_f = int(f.split(' ')[1])
                if v not in final_clients:
                    final_clients.append(v)
                print("client:", v, ' is served by facility:' , current_f)

    for o in Clients:
        if outlier_customer[o].varValue > TOL:
            outliers.append(o)
            print("Establish outlier of index: ", o)


    # PRINT OPTIMAL SOLUTION
    cost = value(prob.objective)
    print("The total cost of installing and operating facilities = ", cost)

    return open_facilities, final_clients, outliers, cost


if __name__ == '__main__':
    num_args = len(sys.argv)
    if num_args == 0:
        #generate data with default values
        types = ['Boston', 'Simple']
        P = generate_date(type='Boston')
        z, m = 20, 6
    #insert data from txt file (no header)
    elif num_args == 3:
        file_name = sys.argv[1]
        z = int(sys.argv[2])
        m = int(sys.argv[3])
        P = np.loadtxt(file_name)

    D = euclidean_distances(P.T, P.T)
    Clients, Facilities = list(range(P.shape[1])), list(range(P.shape[1]))
    open_facilities, final_clients, outliers, cost = FLO_M_LP(Facilities, Clients, D, z, m)
    plot_points(open_facilities, final_clients, outliers, cost, m , z, P)