import networkx as nx
import pandas as pd
from utils import graph_networkx
def main():
    bb_graph1= nx.read_graphml("/nfs/raid89/u21/projects/GraphMatchApps/data/BlueBrain/BBrain_graph_1.graphml")
    bb_graph2 = nx.read_graphml(
        "/nfs/raid89/u21/projects/GraphMatchApps/data/BlueBrain/BBrain_graph_2.graphml")
    bb_graph1_feats = pd.read_csv(
        "/nfs/raid89/u21/projects/GraphMatchApps/data/BlueBrain/BBrain_graph_1.csv")
    bb_graph_a = graph_networkx(incoming_graph_data=bb_graph1)
    bb_graph_b = graph_networkx(incoming_graph_data=bb_graph2)




if __name__=="__main__":
    main()
