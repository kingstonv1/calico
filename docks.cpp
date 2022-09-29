//Not Working (U.D.)
//This is a shortest path problem, but modified.
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <list>

void addRoad(std::vector<int> adj[], int start, int destination)
{
    adj[start].push_back(destination);
    adj[destination].push_back(start);
}

//A modified Breadth First Search from GeeksForGeeks.org
bool BFS (std::vector<int> adj[], int start, int destination, int v, int pred[], int dist[]) 
{
    std::list<int> queue;
    bool visited[v];

    //Setting defaults for a few values
    for (int i = 0; i < v; i++)
    {
        visited[i] = false;
        dist[i] = 1000;
        pred[i] = -1;
    }

    visited[start] = true;
    dist[start] = 0;
    queue.push_back(start);

    while (!queue.empty())
    {
        int x = queue.front();
        queue.pop_front();
        for (int i = 0; i < adj[x].size(); i++) 
        {
            if (!visited[adj[x][i]]) 
            {
                visited[adj[x][i]] = true;
                dist[adj[x][i]] = dist[x] + 1;
                pred[adj[x][i]] = x;
                queue.push_back(adj[x][i]);

                if (adj[x][i] == destination)
                    { return true; }
            }
        }
    }

    return false;
}

std::vector<int> printShortest(std::vector<int> adj[], int s, int destination, int v) 
{
    int pred[v], dist[v];
    std::vector<int> vec;

    if (BFS(adj, s, destination, v, pred, dist) == false) 
    {
        vec.push_back(-1);
        return vec;
    }

    std::vector<int> path;
    int crawl = destination;
    path.push_back(crawl);
    while (pred[crawl] != -1) 
    {
        path.push_back(pred[crawl]);
        crawl = pred[crawl];
    }

    //Total distance
    vec.push_back(dist[destination]);
    
}

int main()
{
    int t;
    std::cin >> t;
    std::cin.ignore(1, '\n');

    for (int i = 0; i < t; i++)
    {
        
    }
    

    return 0;
}