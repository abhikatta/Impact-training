#include <vector>
#include <bits/stdc++.h>
using namespace std;
int dfs(int node, vector<int> &vis, vector<int> &path, vector<int> adj[], int sum)
{
    vis[node] = 1;
    path[node] = sum;
    int tsum = INT_MIN;
    for (auto it : adj[node])
    {
        if (!vis[it])
        {
            int x = dfs(it, vis, path, adj, sum + it);
            tsum = max(tsum, x);
        }
        else if (path[it] != -1)
        {
            int x = path[node] - path[it] + it;
            tsum = max(tsum, x);
        }
    }
    path[node] = -1;
    return tsum;
}

int main()
{
    int n;
    cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
    }
    vector<int> adj[n];
    for (int i = 0; i < n; i++)
        if (v[i] != -1)
            adj[i].push_back(v[i]);
    vector<int> vis(n, 0);
    vector<int> path(n, -1);
    int ans = 0;
    for (int i = 0; i < n; i++)
    {
        if (!vis[i])
        {
            int x = dfs(i, vis, path, adj, i);
            ans = max(ans, x);
        }
    }
    cout << ans;
}
