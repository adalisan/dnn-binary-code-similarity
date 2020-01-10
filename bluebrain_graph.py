import networkx as nx
import numpy as np
import pandas as pd
from utils import graph_networkx
from net_graphnn import sbm_graph_generator as sbm_gen

def main():
    bb_graph1= nx.read_graphml("/nfs/raid89/u21/projects/GraphMatchApps/data/BlueBrain/BBrain_graph_1.graphml")
    bb_graph2 = nx.read_graphml(
        "/nfs/raid89/u21/projects/GraphMatchApps/data/BlueBrain/BBrain_graph_2.graphml")
    bb_graph1_feats = pd.read_csv(
        "/nfs/raid89/u21/projects/GraphMatchApps/data/BlueBrain/BBrain_graph_1.csv")
    bb_graph_a = graph_networkx(incoming_graph_data=bb_graph1)
    bb_graph_b = graph_networkx(incoming_graph_data=bb_graph2)
    #B_probs = nx.adjacency_matrix(bb_graph_b)
    graph_Bmu = np.loadtxt(
        "/nfs/raid89/u21/projects/GraphMatchApps/Bluebrain/reports/graphBmu.Rmat",usecols=range(1,56))


    B_probs = np.loadtxt(
    "/nfs/raid89/u21/projects/GraphMatchApps/Bluebrain/reports/graphBp.Rmat", usecols=range(1, 56))
    print(B_probs)
    #print(graph_Bmu[0:2] )
    block_sizes = np.loadtxt(
        "/nfs/raid89/u21/projects/GraphMatchApps/Bluebrain/reports/rho.Rmat",usecols=[1])
    sbm_g = sbm_gen(sizes = block_sizes, seed=200, graph_Bp=B_probs, graph_Bmu=graph_Bmu)
    for new_G in sbm_g:
        print(sbm_g)

if __name__== "__main__":
    main()
