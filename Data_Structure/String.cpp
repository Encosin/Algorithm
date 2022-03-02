// 이 내용은 흔히 말하는 종만북을 공부하면서 얻은 지식을 정리하기 위함이다.
// Python에서는 문자열에 관한 처리가 쉬웠던것 같은데 C++에서는 아닌 것 같다.
#include <iostream>
#include <string>
#include <vector>
using namespace std;
/*
문자열 검색 Algorithm 
: 주어진 긴 '짚더미(haystack)' 문자열 H가 '바늘(needle)' 문자열 N을 부분 문자열로 포함하는지 확인하고, 
  포함한다면 N과 일치하는 부분 문자열의 시작 위치를 찾는 문제를 문자열 검색 문제라고 한다.
  H = "hogwarts", N = "gwart" 이라고 하면 H [2:6] = N이므로 H는 N을 포함하며, N의 시작위치는 2가 됩니다. 
  만약 N이 두 번 이상 출현한다면 문자열 검색 알고리즘은 N이 출현하는 모든 위치를 반환해야 합니다. 
  예를 들어, H = "avava"는 N = "ava"를 두 번 포함하며, 각각의 시작 위치는 0, 2 입니다.
   이 문제를 푸는 간단한 방법은 N의 가능한 모든 시작위치를 다 시도해보는 것입니다.
  처음에는 0번 글자에서 시작하는 부분 문자열이 N과 같은지 확인하기 위해 H와 N의 글자를 하나하나 맞춰갑니다.
  만약 모든 글자가 서로 일치한다면 이 위치를 답에 추가하고, 중간에 실패하거나 답을 하나 찾으면 시작 위치를 오른쪽으로 한칸 옮겨 계속합니다.

*/
// 코드 20.1 단순한 문자열 검색 알고리즘의 구현
// '짚더미' H의 부분 문자열로 '바늘' N이 출현하는 시작 위치들을 모두 반환한다.
vector <int> naiveSearch (const string& H, const string& N) {
    vector <int> ret;
    // 모든 시작 위치를 다 시도해 본다. 
    for (int begin = 0; begin + N.size() <= H.size(); ++begin) {
        bool matched = true;
        for (int i = 0; i < N.size(); ++i) {
            if (H[begin + i] != N[i]) {
                matched = false; 
                break;
            }
        }
        if (matched) ret.push_back(begin);
    }
    return ret;
} 
