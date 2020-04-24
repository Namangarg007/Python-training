class vertex:

    def __init__(self, value):
        self.value = value
        self.neighbour = []

    def __repr__(self):
        return str(self.value)


class Graph:

    def __init__(self):
        self.vertices = []

    def find(self, value):
        for vertex in self.vertices:
            if vertex.value == value:
                return vertex
        return None

    def add_vertex(self, value):

        if not self.find(value):
            self.vertices.append(vertex(value))
        else:
            print(value, "already Exist's")

    def add_edge(self, source, target):
        source_v = self.find(source)
        target_v = self.find(target)
        if source_v and target_v:
            source_v.neighbour.append(target_v)
            target_v.neighbour.append(source_v)
        else:
            print(source, "or", target, "doesn't exist")

    def display(self):

        for vertex in self.vertices:
            print(vertex, end=" : ")

            # way 1
            print(", ".join([str(neighbour) for neighbour in vertex.neighbour]))

            # way 2
            # for neighbour in vertex.neighbour:
            #    print(neighbour, end=", ")
            # print()
    def depth_first_trev(self, source=None):
        if not source:
            vertex = self.vertices[0]
        else:
            vertex = self.find(source)

        stack = list()
        visited = set()

        stack.append(vertex)
        visited.add(vertex)

        while len(stack) > 0:
            vertex = stack.pop()
            print(vertex)

            for neighbour in vertex.neighbour:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)

    def breadth_first_trev(self, source=None):
        if not source:
            vertex = self.vertices[0]
        else:
            vertex = self.find(source)

        queue = list()
        visited = set()

        queue.append(vertex)
        visited.add(vertex)

        while len(queue) > 0:
            vertex = queue.pop(0)
            print(vertex)

            for neighbour in vertex.neighbour:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

    def depth_first_search(self, source, target):

        vertex = self.find(source)

        stack = list()
        visited = set()

        stack.append(vertex)
        visited.add(vertex)

        while len(stack) > 0:
            vertex = stack.pop()
            print(vertex)

            if vertex.value == target:

                return True

            for neighbour in vertex.neighbour:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)
        return False

    def breadth_first_search(self, source, target):

        vertex = self.find(source)

        queue = list()
        visited = set()

        queue.append(vertex)
        visited.add(vertex)

        while len(queue) > 0:
            vertex = queue.pop(0)
            print(vertex)

            if vertex.value == target:
                return True

            for neighbour in vertex.neighbour:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return False

g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(4, 5)
g.depth_first_trev()
print()
g.depth_first_search(3, 5)
print()
g.breadth_first_trev()
print()
g.breadth_first_search(3, 5)
