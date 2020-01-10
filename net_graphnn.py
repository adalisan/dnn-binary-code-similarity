import os
import sys
import numpy as np
import networkx as nx
from networkx import DiGraph
from networkx.generators.community import stochastic_block_model as sbm

from numpy.random import poisson as ps
from networkx import adjacency_matrix as adjmat

class graph(object):
    def __init__(self, node_num=0, label=None, name=None):
        self.node_num = node_num
        self.label = label
        self.name = name
        self.features = []
        self.succs = []
        self.preds = []
        if (node_num > 0):
            for i in range(node_num):
                self.features.append([])
                self.succs.append([])
                self.preds.append([])

    def add_node(self, feature=[]):
        self.node_num += 1
        self.features.append(feature)
        self.succs.append([])
        self.preds.append([])

    def add_edge(self, u, v):
        self.succs[u].append(v)
        self.preds[v].append(u)

    def toString(self):
        ret = '{} {}\n'.format(self.node_num, self.label)
        for u in range(self.node_num):
            for fea in self.features[u]:
                ret += '{} '.format(fea)
            ret += str(len(self.succs[u]))
            for succ in self.succs[u]:
                ret += ' {}'.format(succ)
            ret += '\n'
        return ret

#isgraph
class graph_networkx(DiGraph):
    def __init__(self, node_num=0, label=None, name="", incoming_graph_data=None, node_feats=[],  **attr):
        self.nxgraph = None
        super(graph_networkx, self).__init__(
            incoming_graph_data=incoming_graph_data, name=name, label=label)
        if incoming_graph_data is not None:

            self.node_num = self.number_of_nodes
            self.label = label
            self.name = name
            self.features = node_feats
            self.succs = []
            self.preds = []

        else:
            self.node_num = node_num
            self.label = label
            self.name = name
            self.features = []
            self.succs = []
            self.preds = []
            if (node_num > 0):
                for i in range(node_num):
                    node_feat=[]
                    if len(node_feats)>0 and i<len(len(node_feats)):
                        node_feat= node_feats[i]
                    self.add_node(i,feature=node_feat)
                    self.features.append([])
                    self.succs.append([])
                    self.preds.append([])
                    self.preds.append([])

    def add_node_compat(self, feature = []):
        self.node_num += 1
        self.features.append(feature)
        self.succs.append([])
        self.preds.append([])
        self.add_node(self.node_num-1, feature=feature)

    def add_edge_compat(self, u, v):
        self.succs[u].append(v)
        self.preds[v].append(u)


    def toString(self):
        ret = '{} {}\n'.format(self.node_num, self.label)
        for u in range(self.node_num):
            for fea in self.features[u]:
                ret += '{} '.format(fea)
            ret += str(len(self.succs[u]))
            for succ in self.succs[u]:
                ret += ' {}'.format(succ)
            ret += '\n'
        return ret


def convert_to_list_of_list (SBM_prob_mat):
    nrow  = SBM_prob_mat.shape[0]
    ncol = SBM_prob_mat.shape[1]
    return [[ SBM_prob_mat[i,j] for i in range(nrow)] for j in range(ncol) ]

class sbm_graph_generator:
    def __init__(self,sizes,seed,graph_Bp,graph_Bmu):
        self.sizes = sizes
        self.seed = seed

        self.n_nodes = sum(sizes)
        self.n_blocks = len(sizes)
        self.probs = convert_to_list_of_list(graph_Bp)
        self.graph_Bp = graph_Bp
        self.graph_Bmu = graph_Bmu
        self.tau = [k for k in range(self.n_blocks) for j in range(k)]

    def __iter__(self):
        g = nx.stochastic_block_model(self.sizes,self.probs,seed=self.seed,directed=True)

        W = np.zeros((self.n_nodes, self.n_nodes))
        for node_in_sbm_i in self.tau:
            for node_in_sbm_j in self.tau:
              W[node_in_sbm_i, node_in_sbm_j] = ps(
                  self.graph_Bp[node_in_sbm_i, node_in_sbm_j], size=1)
        A = adjmat(g).to_numpy_matrix()
        A_W = np.multiply(A,W)
        weighted_g = nx.DiGraph()
        nonzero_indices = np.argwhere(A_W)
        weighted_g.add_weighted_edges_from(
            [ [ (index_pair[0],  index_pair[1], A_W[index_pair]) for index_pair in nonzero_indices ] ] )
        yield weighted_g


