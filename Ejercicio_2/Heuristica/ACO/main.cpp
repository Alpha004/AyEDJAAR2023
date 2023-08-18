/*
@author:	Diogo A. B. Fernandes
@contact:	diogoabfernandes@gmail.com
@license:	see LICENSE
*/
#include <bits/stdc++.h>
#include <fstream>
#include <vector>
#include <string>
#include <iostream>
#include <cstdlib>


#include <cmath>
#include <limits>
#include <climits>
#include <ctime>

#include "ACO.h"

// #define ITERATIONS		(int) 5

// #define NUMBEROFANTS	(int) 5
//#define NUMBEROFCITIES	(int) 51

// if (ALPHA == 0) { stochastic search & sub-optimal route }
#define ALPHA			(double) 0.5
// if (BETA  == 0) { sub-optimal route }
#define BETA			(double) 0.8
// Estimation of the suspected best route.
#define Q				(double) 100
// Pheromones evaporation. 
#define RO				(double) 0.2
// Maximum pheromone random number.
#define TAUMAX			(int) 2

#define INITIALCITY		(int) 1

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

int main(int argc, char *argv[]) {
	printf("Lista de Adjacencias: %s \n", argv[1]);
	printf("Posicion Nodos: %s \n", argv[2]);	
	int NUMBEROFCITIES = std::stoi(argv[3]);
	std::cout << "Hola! ACO ejecutandose..." << "\n" << "Por favor ingrese su nro de hormigas:" << "\n";
	int NUMBEROFANTS = 5;
	std::cin >> NUMBEROFANTS;
	std::cout << "Ingrese el numero de iteraciones: " << "\n";
	int ITERATIONS = 5;
	std::cin >> ITERATIONS;

	std::ifstream myedges(argv[1]);
	std::ifstream mytour(argv[2]);
	ACO *ANTS = new ACO (NUMBEROFANTS, NUMBEROFCITIES, 
			 			ALPHA, BETA, Q, RO, TAUMAX,
			 			INITIALCITY);

	ANTS -> init();
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

	for (const auto& pair : edges) {
		std::cout << "First: " << pair.first << ", Second: " << pair.second << std::endl;    
		ANTS -> connectCITIES (pair.first, pair.second);
	}

	// ANTS -> connectCITIES (0, 1);
	// ANTS -> connectCITIES (0, 2);
	// ANTS -> connectCITIES (0, 3);
	// ANTS -> connectCITIES (0, 7);
	// ANTS -> connectCITIES (1, 3);
	// ANTS -> connectCITIES (1, 5);
	// ANTS -> connectCITIES (1, 7);
	// ANTS -> connectCITIES (2, 4);
	// ANTS -> connectCITIES (2, 5);
	// ANTS -> connectCITIES (2, 6);
	// ANTS -> connectCITIES (4, 3);
	// ANTS -> connectCITIES (4, 5);
	// ANTS -> connectCITIES (4, 7);
	// ANTS -> connectCITIES (6, 7);
	/* ANTS -> connectCITIES(8, 2);
	ANTS -> connectCITIES(8, 6);
	ANTS -> connectCITIES(8, 7); */

	// for(int i = 0; i < n_vertices_; ++i)

	for(auto o:tours) {
		std::cout << "N: " << o.n << ", X: " << o.x << ", Y: " << o.y << std::endl;
		ANTS -> setCITYPOSITION (o.n, o.x, o.y);
	}
	// ANTS -> setCITYPOSITION (0,  1,  1);
	// ANTS -> setCITYPOSITION (1, 10, 10);
	// ANTS -> setCITYPOSITION (2, 20, 10);
	// ANTS -> setCITYPOSITION (3, 10, 30);
	// ANTS -> setCITYPOSITION (4, 15,  5);
	// ANTS -> setCITYPOSITION (5, 10,  1);
	// ANTS -> setCITYPOSITION (6, 20, 20);
	// ANTS -> setCITYPOSITION (7, 20, 30);

	// ANTS -> setCITYPOSITION(8, 26, 20);

	ANTS -> printGRAPH ();

	ANTS -> printPHEROMONES ();

	clock_t start; 
    start = clock();

	ANTS -> optimize (ITERATIONS);

	clock_t endTime = clock() - start; 
    double timeACO = ((double)endTime)/CLOCKS_PER_SEC; // in seconds            

	ANTS -> printRESULTS ();

	std::cout<<"Time ACO version: "<<timeACO<<std::endl; 

	return 0;
}
