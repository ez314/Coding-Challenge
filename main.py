import math

tolerance = 0.5

# modified union find that does clustering
class graph:
    coordinates = [] # list of tuples
    parents = []     # list of ints
    sizes = []       # list of ints

    clusters = {}    # int → list of tuples

    # init based on size of the graph
    def __init__(self, coordinates):
        self.coordinates = coordinates
        size = len(coordinates)
        for i in range(size):
            self.parents.append(i)
        self.sizes = [1]*size

    # union-find root, with path compression
    def root(self, a):
        while self.parents[a] != a:
            self.parents[a] = self.parents[self.parents[a]]
            a = self.parents[a]

        return a

    # union-find join
    def join(self, a, b):
        a = self.root(a)
        b = self.root(b)

        if a != b:
            if self.sizes[a] > self.sizes[b]:
                self.parents[b] = a
                self.sizes[a] += self.sizes[b]
            else:
                self.parents[a] = b
                self.sizes[b] += self.sizes[a]

    # simple pythag
    def distance(self, a, b):
        return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    # joins points and generates clusters
    def form_clusters(self, maxDist):
        # join points close together
        for i, iCoord in enumerate(self.coordinates):
            for j, jCoord in enumerate(self.coordinates):
                if self.distance(iCoord, jCoord) < maxDist:
                    self.join(i, j)

        # determine clusters using root ID
        self.clusters = {}
        for i, coord in enumerate(self.coordinates):
            if not self.root(i) in self.clusters:
                self.clusters[self.root(i)] = []
            self.clusters[self.root(i)].append(coord)


verticies = []

# read data from CSV
csv = open('ClusterPlot.csv', 'r')
for line in csv:
    if line[0] == ',': continue

    _, v1, v2 = [float(x) for x in line.split(',')]
    verticies.append((v1, v2))
csv.close()

g = graph(verticies)
g.form_clusters(tolerance)

# uncomment to print clusters
# for c in g.clusters: print(c, len(g.clusters[c]), g.clusters[c][:5])

print(
    'Number of significant clusters: {}'.format(
        sum([(1 if len(c) > len(verticies)*0.05 else 0) for c in g.clusters.values()])
    ))
