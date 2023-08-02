#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    time_t start, end;
    time(&start);
    ios_base::sync_with_stdio(false);

    vector<string> msg{"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};

    for (const string &word : msg)
    {
        cout << word << " ";
    }
    cout << endl;

    ofstream myfileRead("example.txt");
    if (myfileRead.is_open())
    {
        myfileRead << "This is a line.\n";
        myfileRead << "This is another line.\n";
        myfileRead.close();
    }
    else
        cout << "Unable to open file";

    string line;
    ifstream myfile("../Data/100_data.txt");
    if (myfile.is_open())
    {
        while (getline(myfile, line))
        {
            cout << line << '\n';
        }
        myfile.close();
    }

    else
        cout << "Unable to open file";

    for (int i=0; i<1000; i++)
    {
        cout << i;
    }
    
    time(&end);
 
    // Calculating total time taken by the program.
    double time_taken = double(end - start);
    cout << "Time taken by program is : " << fixed
        << time_taken << setprecision(5);
    cout << " sec " << endl;

    return 0;
}