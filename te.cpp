
#include <iostream>
#include <array>
#include <vector>
#include <cstdio>
const int maxn = 100;
using namespace std;
int n;
int x[maxn];
int a[maxn];
int main()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d%d", &x[n], &a[n]);
	}
	bool right = 0;
	int total = 10;
	while (n >= 1 && n <= maxn) {
		for (int i = 0; i < n; i++)
		{
			total += a[i];
		}
		return total;
	}
	return total;
}
