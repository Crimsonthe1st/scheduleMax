import math
import networkx as nx
import matplotlib.pyplot as plt

csc = nx.DiGraph()

csc.add_edges_from([("CSC130","CSC230"),("CSC130","CSC250"),("CSC130","CSC261"),("CSC230","CSC330"),("CSC250","CSC330"),("CSC330","CSC339"),
                    ("CSC330","CSC340"),("CSC250","CSC350"),("CSC230","CSC362"),("CSC261","CSC362"),("CSC350","CSC452"),("CSC340","CSC462"),
                    ("CSC362","CSC462"),("CSC330","CSC471"),("MAT196","CSC130"),("MAT196","MAT296"),("MAT196","STA271orSTA290"),("PHI222","PHI222"),
                    ("SCI1","SCI2"),("LANG101","LANG102"),("LANG102","LANG203"),("LANG203","LANG204"),("MACF","MACF"),("MACWC","MACWC"),
                    ("MACOC","MACOC"),("MACHW","MACHW"),("MACHFA","MACHFA"),("MACSBS","MACSBS"),("MACNS","MACNS"),("MACGC","MACGC"),("MACDE","MACDE"),
                    ("CSC462","CSC462"),("STA271orSTA290","STA271orSTA290"),("CSC471","CSC471"),("CSC339","CSC339"),("LANG204","LANG204"),("MAT296","MAT296"),
                    ("SCI2","SCI2"),("CSC452","CSC452")])
# nx.draw_networkx(csc,arrows=True)
# plt.draw()
# plt.show()

credits={"CSC130":3,"CSC230":3,"CSC250":3,"CSC261":3,"CSC330":3,"CSC339":3,"CSC340":3,"CSC350":3,"CSC362":3,"CSC452":3,"CSC462":3,"CSC471":3,"CSC490":3,
         "MAT196":4,"MAT296":4,"STA271orSTA290":3,"PHI222":3,"SCI1":4,"SCI2":4,"LANG101":3,"LANG102":3,"LANG203":3,"LANG204":3,"MACF":3,"MACWC":3,"MACOC":3,
         "MACHW":3,"MACHFA":3,"MACSBS":3,"MACNS":3,"MACGC":3,"MACDE":3}

schedule=[]

def knapsack_all_solutions_last_column(capacity, weights, values):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    trace = [[[] for _ in range(capacity + 1)] for _ in range(n + 1)]


    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                without_item = dp[i - 1][w]
                with_item = dp[i - 1][w - weights[i - 1]] + values[i - 1]

                if with_item > without_item:
                    dp[i][w] = with_item
                    trace[i][w] = [comb + [i - 1] for comb in trace[i - 1][w - weights[i - 1]]]
                    if not trace[i][w]:  
                        trace[i][w] = [[i - 1]]
                elif with_item == without_item:
                    dp[i][w] = with_item
                    trace[i][w] = trace[i - 1][w] + [
                        comb + [i - 1] for comb in trace[i - 1][w - weights[i - 1]]
                    ]
                else:
                    dp[i][w] = without_item
                    trace[i][w] = trace[i - 1][w]
            else:
                dp[i][w] = dp[i - 1][w]
                trace[i][w] = trace[i - 1][w]

    
    last_column_all_solutions = [trace[i][capacity] for i in range(n + 1)]

    return last_column_all_solutions



##### Important Values #####

def find_longest_path(G, start_node):
    longest_paths = {node: [] for node in G.nodes}
    
    def dfs(node, path):
        
        if len(path) > len(longest_paths[node]):
            longest_paths[node] = path
        
        for neighbor in G.successors(node):
            if neighbor not in path:  
                dfs(neighbor, path + [neighbor])
    
    dfs(start_node, [start_node])
    
    return longest_paths




def find_longest_length_with_index(lst):
    if not lst:
        return None, None 

    max_length = len(lst[0])
    max_index = 0

    for i in range(1, len(lst)):
        current_length = len(lst[i])
        if current_length > max_length:
            max_length = current_length
            max_index = i

    return lst[max_index]






def algorithm(graph):
    all_longest_paths = {node: find_longest_path(graph, node) for node in graph.nodes}

    longest_path_dict={}

    for node, paths in all_longest_paths.items():
        longest_path_dict[node]= len(find_longest_length_with_index(list(paths.values())))

    sources=set()
    targets=set()

    for e in csc.edges():
        source,target = e
        if target != source:
            sources.add(source)
            targets.add(target)

    realtargets = targets-sources
    realsources=sources-targets

    for e in csc.edges():
        source,target = e
        if source==target and csc.in_degree(source)==1 and csc.out_degree(source)==1:
            realsources.add(source)


    startcourse= list(realsources)

    print(startcourse)

    courseweight=[credits[x] for x in startcourse]
    coursevalue=[longest_path_dict[x] for x in startcourse]

    last_column_solutions = knapsack_all_solutions_last_column(16,courseweight,coursevalue)

    print(last_column_solutions[-1])
    print(len(last_column_solutions[-1]))
    
    if len(last_column_solutions[-1]) == 0:
        print("done")
        return True

    chose=int(input())
    chosed=last_column_solutions[-1][chose]

    semester=[startcourse[x] for x in chosed]
    for x in semester:
        csc.remove_node(x)
    schedule.append(semester)
    print(schedule)

    nx.draw_networkx(csc,arrows=True)
    plt.draw()
    plt.show()

    algorithm(csc)

    
nx.draw_networkx(csc,arrows=True)
plt.draw()
plt.show()

algorithm(csc)
