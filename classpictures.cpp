#include <iostream> 
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
using namespace std;


int main(){
	int n;
	while(cin >> n){
	//cout << n << endl;
	vector<string>names(n);
	for(int i = 0; i < n; i++)
		cin >> names[i];
	sort(names.begin(), names.end());
	
	unordered_map<string, int> people;
	
	for (int i = 0; i < n; i++)
		people[names[i]] = i;
	string a, b;
	vector<vector<bool> > haters(n, vector<bool>(n, false));
	cin >> n; 
	for(int i = 0; i < n; i++){
	     cin >> a >> b; 
	     haters[people[a]][people[b]] = true;
	     haters[people[b]][people[a]] = true;
	}
	bool flag2 = false;
	vector<int> temp(names.size());
	for (int num = 0; num < names.size(); num++){
		temp[num] = num;
	}
	do{	
		bool flag = false; 
      		for (int i = 0; i < temp.size()-1; i++){
			if (haters[temp[i]][temp[i+1]]){
				flag = true;	
				break;
			}
		}
		
		if (!flag){	
			for (auto i: temp){
				cout << names[i] << " ";
			}
			cout << '\n';
			flag2 = true;
			break;
		}
	}while( next_permutation(temp.begin(), temp.end()));
    	if(!flag2) cout << "You all need therapy.\n"; 
}	
  return 0;
}
