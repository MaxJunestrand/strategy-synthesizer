from .vertex import Vertex
import re

class Graph():
    def __init__(self, filename):
        """
        :param filename: the name of the .dot file.
        """
        self.vert_dict = {}
        self.locdict = {}
        self.filename = filename

    def add_vert(self, vert):
        """
        :param vert: label of node.
        :return: adds a new Vertex object to the game graphs vert_dict with the node label as key.
        """
        new_vert = Vertex(vert)
        self.vert_dict[vert] = new_vert

    def add_edge(self, current_vert, next_vert, action):
        """
        Creates an action-labeled transition between two nodes.

        :param current_vert: current node
        :param next_vert: node to connect to
        :param action: action that transitions to connected node
        :return:
        """

        self.vert_dict[current_vert].add_adjacent_vert(self.vert_dict[next_vert], self.vert_dict, action)

    def get_graph(self):
        """
        :return: the game graph as a dictionary.
        """
        return self.vert_dict


class Agent_graph(Graph):
    def __init__(self, filename):
        """
        :param filename: the name of the .dot file.
        """
        super().__init__(filename)

    def locDic(self):
        """
        Parses the locations in the .dot file from numbers to their pre-set labels.

        :return: returns a dictionary with the locations and their relevant number in the .dot file.
        """
        i = 5

        with open("pictures/" + self.filename + ".dot", "r") as strfile:
            for _ in range(5): # skips the first 5 lines in the .dot file.
                next(strfile)

            for line in strfile:

                try:
                    x = [re.search(r'[a-zA-Z\d]+', line).group(0), re.findall(r'({[a-zA-Z\d,\s-]+})+', line)]

                    if x[0] != "hidden":
                        x[1] = x[1][0]
                        self.locdict[x[0]] = x[1]
                        self.add_vert(x[1])

                    else:
                        pass

                except:
                    break

                i += 1

        return i

    def deltaDic(self):
        """
        Uses the location dictionary to parse the .dot file into the action-labeled transitions for the Agent's game

        :return: Returns the action-labeled transitions as a dictionary
        """
        i = self.locDic()

        with open("pictures/" + self.filename + ".dot", "r") as strfile:

            for _ in range(i):
                next(strfile)

            for line in strfile:

                try:
                    search = re.search('arrowhead', line) or \
                             re.search('dir=back', line) or \
                             re.search('hidden', line) or \
                             re.search('}', line)

                    if search is None:
                        nodes = re.findall('[\d]+', line)

                        try:
                            rawAction = re.search('label=(.*)', line).group(1)
                            rawAction = rawAction[:-2]
                            actions = re.split('\), \(', rawAction)[0]

                            if '"(-)"' in rawAction:
                                actions = '(-)'

                        except:
                            actions = re.search('label=\"\((\-)', line).group(1)[0]
                        self.add_edge(self.locdict[nodes[0]], self.locdict[nodes[1]], actions)

                except:
                    print("Error")


class Coalition_graph(Graph):
    def __init__(self, filename):
        """
        :param filename: the name of the .dot file.
        """
        super().__init__(filename)

    def locDic(self):
        """
        Parses the locations in the .dot file from numbers to their pre-set labels.

        :return: returns a dictionary with the locations and their relevant number in the .dot file.
        """
        i = 5
        with open("pictures/" + self.filename + ".dot", "r") as strfile:

            for _ in range(5):
                next(strfile)

            for line in strfile:

                try:
                    x = [re.search(r'[a-zA-Z\d]+', line).group(0), re.findall(r'({[a-zA-Z\d,\s-]+})+', line)]

                    if x[0] != "hidden":
                        x[1] = ', '.join(x[1])
                        self.locdict[x[0]] = x[1]
                        self.add_vert(x[1])

                    else:
                        break

                except:
                    break

        return i

    def deltaDic(self):
        """
        Uses the location dictionary to parse the .dot file into the action-labeled transitions for the coalition game

        :return: Returns the action-labeled transitions as a dictionary
        """
        i = self.locDic()

        with open("pictures/" + self.filename + ".dot", "r") as strfile:

            for _ in range(i):
                next(strfile)

            for line in strfile:

                try:
                    search = re.search('arrowhead', line) or \
                             re.search('dir=back', line) or \
                             re.search('hidden', line) or \
                             re.search('}', line)

                    if search is None:
                        nodes = re.findall('[\d]+', line)

                        try:
                            rawAction = re.findall('label=(.*)', line)

                            if len(rawAction[0]) > 3:
                                rawAction = rawAction[0][2:-4]

                            else:
                                rawAction = rawAction[0][:-2]

                            actions = re.split('\), \(', rawAction)

                        except:
                            actions = re.search('label=\"\((\-)', line).group(1)[0]
                        self.add_edge(self.locdict[nodes[0]], self.locdict[nodes[1]], actions)

                except:
                    pass