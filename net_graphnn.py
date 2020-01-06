import networkx
from networkx import DiGraph


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
    def __init__(self, incoming_graph_data=None, node_num=0,label=None, name="",node_feats=[],  **attr):
        self.nxgraph = None
        if incoming_graph_data is not None:
            super.__init__(incoming_graph_data,name=name,label=label)
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
                    self.features.append([])
                    self.succs.append([])
                    self.preds.append([])
                    self.preds.append([])

    def add_node_compat(self, feature = []):
        self.node_num += 1
        self.features.append(feature)
        self.succs.append([])
        self.preds.append([])
        self.add_node(feature=feature)

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
