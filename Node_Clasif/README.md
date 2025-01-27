# GNN for Node Clasification task

Here we'll try to code a GNN for a node classification task on the citation network 'Cora'. This citation network introduced  by [Yang t al. (2016)](https://arxiv.org/abs/1603.08861); and we'll use PyTorch Geometric to charge it.

In this network we have 7 pssible classifications for the nodes. We recomend do some exploration of the dataset we are working for a deep 
understanding. Thus we have an AE.py where we analyze some features of the graph.

Once we know how with what we are going to work, an essential step is define our objective and with what model are we going to achive it. So in this case, we want to define a model wich classifys in the 7 possible: (INTRODUIR POSSIBLES CLASSIFICADORS). So our first try will be a GNN for a node-level task and a MLP (Multilayer Percepton). Then we'll compare our  results.

## Our Model: GNN for node-level task
