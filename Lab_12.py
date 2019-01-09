class Vertex:

    def __init__(self, key):
        self.mKey = key
        self.mData = None
        self.mNeighbors = {}
        self.mFather = None


    def key(self):
        return self.mKey


    def setData(self, data):
        self.mData = data


    def data(self):
        return self.mData


    def addNeighbor(self, vertex, weight=1):
        if not isinstance(vertex, Vertex):
            vertex = Vertex(vertex)
        self.mNeighbors[vertex.key()] = weight
        vertex.mFather = self.key()

    def getFather(self):
        return self.mFather

    def neighbors(self):
        return self.mNeighbors.keys()


    def weight(self, neighbor):
        if isinstance(neighbor, Vertex):
            return self.mNeighbors[neighbor.key()]
        else:
            return self.mNeighbors[neighbor]


class Graph:

    def __init__(self):
        self.mVertexNumber = 0
        self.mVertices = {}


    def addVertex(self, vertex):
        if vertex in self:
            return False

        new_vertex = Vertex(vertex)
        self.mVertices[vertex] = new_vertex
        self.mVertexNumber += 1
        return True


    def addEdge(self, source, destination, weight=1):
        if source not in self.mVertices:
            self.addVertex(source)
        if destination not in self.mVertices:
            self.addVertex(destination)

        self.mVertices[source].addNeighbor(destination, weight)



    def __contains__(self, vertex):
        if isinstance(vertex, Vertex):
            return vertex.key() in self.mVertices
        else:
            return vertex in self.mVertices

    def __iter__(self):
        return iter(self.mVertices.values())

    def __len__(self):
        return self.mVertexNumber

    def __str__(self):
        s = ""
        for vertex in self:
            s = s + str(vertex) + "\n"
        return s



res = []
def DFS(graph, start):
    visited = set()
    __dfs_helper(graph, visited, start)


def __dfs_helper(graph, visited, start, current = False):
    visited.add(start)

    for neighbour in graph.mVertices[start].neighbors():
        if neighbour not in visited:
            __dfs_helper(graph, visited, neighbour,start)

    global res
    res.append((start, current))


def eolymp():
    n = int(input().split()[1])
    g = Graph()
    for i in range(n):
        tmp = input().split()
        g.addEdge(tmp[0],tmp[1])
        if i == 0:
            start = tmp[0]
    DFS(g,start)
    for i in res:
        if all(i):
            print(i[0],i[1])



if __name__ == "__main__":
    try :
        eolymp()
    except Exception:
        print()