#include <vector>
#include <iostream>
using namespace std;


int solution(int n, int m, vector<vector<int>> timetable) {
    int answer = 0;
    return answer;
}


int main(){

    vector<vector<int>> vec;
    vector<int> v1,v2;
    v1.push_back(1170);
    v1.push_back(1210);
    v2.push_back(1200);
    v2.push_back(1260);
    vec.push_back(v1);
    vec.push_back(v2);
    cout << vec[0][1] <<"\n";
    cout << solution(3, 2, vec);

    return 0;
}