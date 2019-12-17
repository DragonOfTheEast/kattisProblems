#include <iostream>
#include <vector>
#include <climits>
using namespace std;


bool my_sum(vector<int> arr, int cut, int max, int min){
    if (arr[cut] == 0){
        long int sum1 = 0;
        long int sum2 = 0;

        for (int i =min; i < cut; i++){
            sum1 += arr[i] * i;
        }
        for (int i = cut+1; i < max + 1; i++){
            sum2 += arr[i] * i;
        }

        return sum1 == sum2;
    }
    else if ( arr[cut] % 2 == 1){
        long int sum1 = ((arr[cut] - 1) /2) * cut;
        long int sum2 = sum1;

        for (int i =min; i < cut; i++){
            sum1 += arr[i] * i;
        }
        for (int i = cut+1; i < max + 1; i++){
            sum2 += arr[i] * i;
        }

        return sum1 == sum2;
    }
    else{
        long int sum1 = ((arr[cut] ) /2) * cut;
        long int sum2 = sum1;

        for (int i =min; i < cut; i++){
            sum1 += arr[i] * i;
        }
        for (int i = cut+1; i < max + 1; i++){
            sum2 += arr[i] * i;
        }

        return sum1 == sum2;
    }
}
int main(){

    vector<int> vector1(20001, 0);
    int num ;
    cin >> num;
    int max = INT_MIN;
    int min = INT_MAX;
    int temp ;
    for (size_t i = 0 ; i < num; i++){
        cin >> temp;

        vector1[temp] += 1;
        if (temp > max){
            max = temp ;
        }
        if (temp < min){
            min = temp;
        }
    }

    for (int i = min; i < max+1; i++){
        if (my_sum(vector1, i, max, min)) {
            cout << "ans :" << i;
            break;
        }
    }
    return 0;
}
