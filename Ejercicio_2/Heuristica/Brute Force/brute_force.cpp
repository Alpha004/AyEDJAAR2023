
#include <bits/stdc++.h>
#include <fstream>
#include <vector>
#include <string>
#include <iostream>
#include <ctime>

using namespace std;

class Tour
{
    public:
        Tour();

        Tour(int n, float x, float y): n{n},x{x},y{y}{}
        friend std::ostream &operator<<(std::ostream& os, const Tour& c);   
        int n;
        float x,y;  
};

class brute_force
{
public:
    int shortest_path_sum(int **edges_list, int num_nodes)
    {
        int source = 0;
        vector<int> nodes;
        for (int i = 0; i < num_nodes; i++)
        {
            if (i != source)
            {
                nodes.push_back(i);
            }
        }
        int n = nodes.size();
        std::cout << "Working size " << n +1 << std::endl;
        int shortest_path = INT_MAX;
        while (next_permutation(nodes.begin(), nodes.end()))
        {
            int path_weight = 0;

            int j = source;
            for (int i = 0; i < n; i++)
            {
                path_weight += edges_list[j][nodes[i]];
                j = nodes[i];
            }
            path_weight += edges_list[j][source];

            shortest_path = min(shortest_path, path_weight);
            //std::cout << "Shortest path at now: " << shortest_path << std::endl;
        }
        return shortest_path;
    }
};


double distance (Tour cityi, Tour cityj) {
    cout << "DIstancia entra: " << cityj.x << " y " << cityi.x << std::endl;
    cout << "DIstancia entra: " << cityj.y << " y " << cityi.y << std::endl;
	return (double) 
		sqrt (pow (cityi.x - cityj.x, 2) + 
 			  pow (cityi.y - cityj.y, 2));
}

void connectCITIES (int **arr,int cityi, int cityj) {
	arr[cityi][cityj] = 1;
	arr[cityj][cityi] = 1;
}

int main(int argc, char *argv[])
{
    /// Getting the number of nodes and number of edges as input
    printf("Lista de Adjacencias: %s \n", argv[1]);
	printf("Posicion Nodos: %s \n", argv[2]);
    std::ifstream myedges(argv[1]);
	std::ifstream mytour(argv[2]);

    int num_nodes = std::stoi(argv[3]);    

    std::vector<Tour> tours;
	vector<std::pair<int,int> > edges;
	string line;
	/* 
	PROCESSING THE EDGES_TXT
	*/	
	if(myedges.is_open())
    {
        while(getline(myedges,line) )
        {
			std::istringstream iss(line);
			std::string token;
			int city[2];
			int k = 0;
			// Read each space-separated token and store it in the vector
			while (std::getline(iss, token, ' ')) {				
				city[k] = std::stoi(token);
				k++;
			}
			edges.push_back(pair<int,int>(city[0],city[1]));
		}
		myedges.close();
	}

	if(mytour.is_open())
    {
        while(getline(mytour,line) )
        {
			std::istringstream iss(line);			
			std::string token;
			int tour[3];
			int k = 0;
			// Read each space-separated token and store it in the vector
			while (std::getline(iss, token, ' ')) {
				tour[k] = std::stoi(token);
				k++;
			}
			tours.push_back(Tour(tour[0],tour[1],tour[2]));			
		}
		mytour.close();
	}

    for(auto o:tours) {
		std::cout << "N: " << o.n << ", X: " << o.x << ", Y: " << o.y << std::endl;		
	}
    /// creating a multi-dimensional array
    int **edges_list = new int *[num_nodes];
    int **weight_list = new int *[num_nodes];
    for(int i=0;i<num_nodes;i++)
    {
        edges_list[i] = new int[num_nodes];
        weight_list[i] = new int[num_nodes];
        for(int j=0;j<num_nodes;j++)
        {            
            edges_list[i][j] = 0;
            weight_list[i][j] = 0;
        }
    }
    for (const auto& pair : edges) {
		std::cout << "First: " << pair.first << ", Second: " << pair.second << std::endl;    
		connectCITIES(edges_list, pair.first, pair.second);
	}
    for (int i = 0; i < num_nodes; i++)
    {        
        for (int j = 0; j < num_nodes; j++)
        {
            if(edges_list[i][j] == 1){                
                weight_list[i][j] = distance(tours[i],tours[j]);
                std::cout << "Peso entre " << i << " y  " << j << " es: " << weight_list[i][j] << std::endl;
            }            
        }
    }
    cout << "MATRIZ DE ADYACENCIA " << endl;
    for (int i = 0; i < num_nodes; i++)
    {
        for (int j = 0; j < num_nodes; j++)
        {
            cout << edges_list[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl
         << endl;
    
    cout << "PESOS DEL GRAFO" << endl;
    for (int i = 0; i < num_nodes; i++)
    {
        for (int j = 0; j < num_nodes; j++)
        {
            cout << weight_list[i][j] << " ";
        }
        cout << endl;
    }

    brute_force approach1;
    clock_t start; 
    start = clock();

    cout << approach1.shortest_path_sum(weight_list, num_nodes) << endl;

    clock_t endTime = clock() - start; 
    double timeBF = ((double)endTime)/CLOCKS_PER_SEC; // in seconds       
    std::cout<<"Time Brute Force version: "<<timeBF<<std::endl; 
    return 0;
}
