#include <iostream>
#include <string>
#include <vector>
#include <regex>
#include <fstream>
#include <map>
#include <limits>
#include <queue>

#include "TD2-bibliotheque.cpp"

using namespace std;

class Graph
{
private:
    int vertices;
    vector<vector<int>> adjacencyMatrix;

public:
    Graph(int vertices) : vertices(vertices), adjacencyMatrix(vertices, vector<int>(vertices, 0)) {}

    int GetKey(string Node)
    {
        regex pattern("Node(\\d+)");
        smatch matches;

        if (regex_search(Node, matches, pattern))
        {
            return stoi(matches[1]);
        }
        else
        {
            cerr << "ERREUR, node invalide" << endl;
            return -1;
        }
    }

    void addEdge(string Node1, string Node2)
    {
        int u = GetKey(Node1);
        int v = GetKey(Node2);

        if (u != v && u >= 0 && v >= 0 && u < vertices && v < vertices)
        {
            this->adjacencyMatrix[u][v] = 1;
            this->adjacencyMatrix[v][u] = 1;
        }
    }

    void afficher()
    {
        for (int i = 0; i < vertices; i++)
        {
            cout << "|  ";
            for (int j = 0; j < vertices; j++)
            {
                cout << adjacencyMatrix[i][j] << "  ";
            }
            cout << "|\n";
        }
        cout << endl;
    }

    vector<int> dijkstra(int startNode, int endNode, vector<vector<int>> &previousNodes)
{
    vector<int> distance(vertices, numeric_limits<int>::max());
    vector<bool> visited(vertices, false);

    distance[startNode] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, startNode});

    while (!pq.empty())
    {
        int u = pq.top().second;
        pq.pop();

        if (u == endNode)
            break;

        if (visited[u])
            continue;

        visited[u] = true;

        for (int v = 0; v < vertices; v++)
        {
            if (!visited[v] && adjacencyMatrix[u][v] && distance[u] != numeric_limits<int>::max() && distance[u] + adjacencyMatrix[u][v] < distance[v])
            {
                distance[v] = distance[u] + adjacencyMatrix[u][v];
                previousNodes[v].clear();
                previousNodes[v].push_back(u);
                pq.push({distance[v], v});
            }
            else if (!visited[v] && adjacencyMatrix[u][v] && distance[u] + adjacencyMatrix[u][v] == distance[v])
            {
                previousNodes[v].push_back(u);
            }
        }
    }

    return distance;
}


    void printShortestPaths(int startNode, const vector<int> &distance, const vector<vector<int>> &previousNodes)
    {
        cout << "Shortest paths from Node" << startNode + 1 << ":\n";
        for (int i = 0; i < vertices; i++)
        {
            if (i != startNode)
            {
                cout << "Node" << startNode + 1 << " to Node" << i + 1 << ": " << distance[i] << ", Path: ";
                printPath(startNode, i, previousNodes);
                cout << endl;
            }
        }
    }

    void printPath(int startNode, int currentNode, const vector<vector<int>> &previousNodes)
    {
        if (currentNode == startNode)
        {
            cout << "Node" << startNode + 1;
            return;
        }

        printPath(startNode, previousNodes[currentNode][0], previousNodes);

        cout << " -> Node" << currentNode + 1;
    }

    int getVerticies() const
    {
        return vertices;
    }
};

Graph AdjancyMatrixFromFile(const string &PATH, ifstream &in_file)
{
    map<string, pair<int, int>> dico = Plot(PATH, in_file);
    int dimension = dico.size();

    Graph graph(dimension);

    in_file.open(PATH);
    if (!in_file.is_open())
    {
        cerr << "ERROR, le path du fichier est mauvais" << endl;
        return graph;
    }
    while (!in_file.eof())
    {
        string ligne;
        getline(in_file, ligne);
        int type = getCode(ligne);
        if (type == 4)
        {
            vector<string> result = ExtractType4(ligne);
            graph.addEdge(result[0], result[1]);
        }
    }
    in_file.close();
    return graph;
}

int main()
{
    string PATH = "Examples/test-PMR_simple.csv";
    ifstream in_file;

    Graph graph = AdjancyMatrixFromFile(PATH, in_file);

    graph.afficher();

    int startNode = 0;
    int endNode = 2;  // Modifiez endNode selon le nœud souhaité
    vector<vector<int>> previousNodes(graph.getVerticies());
    vector<int> distance = graph.dijkstra(startNode, endNode, previousNodes);

    graph.printShortestPaths(startNode, distance, previousNodes);

    return 0;
}