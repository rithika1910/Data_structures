class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.front = []
        self.back = []
        self.depfs = []

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):  # f is from node, t is to node
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def printdfs(self):
        for node in self.depfs:
            print(node.id, end=' ')
        print()

    def __iter__(self):
        return iter(self.vertList.values())

    def createAdjMatrix(self):
        # Initializing the matrix with 0's
        AdjMat = [[0 for _ in range(self.numVertices)]
                  for _ in range(self.numVertices)]

        for i in self.vertList:
            v = self.getVertex(i).getConnections()
            list = []
            for l in v:
                list.append(l.getId())
            for j in self.vertList:
                if j in list:
                    AdjMat[i][j] = self.getVertex(
                        i).getWeight(self.getVertex(j))
        return AdjMat

    """
    Write a method to traverse the graph using dfs from start node. 
    The function must print the nodes and edges in the order in which 
    they are visited, and mention if it is a forward or backward edge.
    """

    def get_node_id(node, k):
        return node.id

    def dfs(self, stnode):
        # First starting node comes in depfs
        self.depfs.append(stnode)

        # Keep visiting neighbours one level deeper, in ascending order of weights
        neighbours = list(stnode.getConnections())
        sortedNeighbours = [node.id for node in neighbours]

        # sortedNeighbours contains sorted values of keys of neighbour vertices
        sortedNeighbours.sort()

        for node in sortedNeighbours:
            # Converting the node id value to vertex
            node = self.getVertex(node)
            if node in self.depfs:
                # Node is already visited, so backedge
                self.back.append(stnode.getWeight(node))
            else:
                # New node is discovered, add to depfs
                self.front.append(stnode.getWeight(node))

                # Further explore its neighbours one level deeper
                self.dfs(node)

    """
    Write a method to traverse the graph using bfs from start node.  The function must print the nodes and edges in the order in which 
    they are visited, and mention if it is a forward or cross edge.
    """

    def bfs(self, stnode):
        # To keep track of the nature of visited edges
        forwardEdges = []
        backwardEdges = []

        # Stores the elements in bfs order
        bfs_order = []

        # Starting from the first node
        bfs_order.append(stnode)

        # Visiting the nodes in the bfs order and eploring them
        for node in bfs_order:
            # Exploring the vertex
            for neighbour in node.getConnections():
                if neighbour in bfs_order:
                    # Its already visited, so back edge
                    backwardEdges.append(node.getWeight(neighbour))
                else:
                    # Its not visited
                    bfs_order.append(neighbour)
                    forwardEdges.append(node.getWeight(neighbour))

        # Printing the BFS
        for node in bfs_order:
            print(node.getId(), end=' ')
        print()

    """
    Write a method to generate the minimum spanning tree of the graph using Kruskal algorithm
    """

    def parent(self, node, parents):
        # If parent index and content are same, then it is the topmost parent
        if parents[node] == node:
            return node
        
        # Recursively find the topmost parent of the node
        return self.parent(parents[node], parents)

    def mstKruskal(self):
        # Constructing edge list for the graph
        edgeList = []
        for src in self.vertList:
            for dest in self.getVertex(src).getConnections():
                edgeList.append([self.getVertex(src).id, dest.id,
                                self.getVertex(src).getWeight(dest)])

        # Sort the edge list in increasing order of weights
        # 3rd element in sublist => weight (src, dest, weight)
        sortedEdgeList = sorted(edgeList, key=lambda x: x[2])

        minimumSpanningTree = []

        # To keep track of the parents of the nodes in the MST
        parents = []
        for i in range(self.numVertices):
            parents.append(i)

        print('Parents', parents)
        count = 0
        i = 0
        while count != self.numVertices - 1:
            currEdge = sortedEdgeList[i]

            # Finding the topmost parent of the vertices connected by the edge
            srcParent = self.parent(currEdge[0], parents)
            destParent = self.parent(currEdge[1], parents)

            # If srcParent != destParent, then those both the vertices are
            # not already present, only one of them is present in the MST
            if srcParent != destParent:
                minimumSpanningTree.append(currEdge)
                # Setting one edge as parent of another
                parents[destParent] = srcParent
                count += 1
            i += 1

        for edge in minimumSpanningTree:
            print(edge)

        return
