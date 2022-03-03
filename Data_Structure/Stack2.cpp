#include <iostream>
#include <string>
#include <vector>
using namespace std;
// Page 628 스택을 이용한 울타리 자르기 문제의 해법 중

// 스위핑 Algorithm
//-----------------------------------------------------------
// 각 판자의 높이를 저장하는 배열 
/*
vector <int> h;
// 스택을 사용한 O(n) 해법
int solveStack() {
    // 남아 있는 판자들의 위치들을 저장한다.
    stack<int> remaining;
    h.push_back(0);
    int ret = 0;
    for(int i = 0; i < h.size(); ++i) {
        // 남아있는 판자들 중 오른쪽 끝 판자가 h[i] 보다 높다면
        // 이 판자의 최대 사각형은 i에서 끝난다.
        while (!remaining.empty() && h[remaining.top()] >= h[i]) {
            int j = remaining.top();
            remaining.pop();
            int width = -1;
            // i번째 판자 왼쪽에 판자가 하나도 안 남아있는 경우 left[i] - 1
            // 아닌 경우 left[i] = 남아있는 판자 중 가장 오른쪽에 있는 판자의 번호가 된다.
            if (remaining.empty())
                width = i;
            else 
                width = (i - remaining.top() - 1);
            ret = max(ret, h[j] * width);
        }
        remaining.push(i);
    }
    return ret;
}
*/
/* page 635
19.4 괄호쌍 맞춰주는 문제
: 스택을 이용해 짝이 맞지 않는 괄호문제를 해결하는 알고리즘의 구현
#include<iostream>

bool wellMatched(const string& formula) {
    // 여는 괄호 문자들과 닫는 괄호 문자들
    const string opening ("({["), closing (")}]");
    // 이미 열린 괄호들을 순서대로 닫는 스택
    stack <char> openStack;
    for(int i = 0; i < formula.size(); ++i) {
        // 여는 괄호인지 닫는 괄호인지 확인한다.
        if (opening.find(formula[i]) != -1)
            // 여는 괄호라면 무조건 스택에 집어넣는다.
            openStack.push(formula[i]);
        else {
            // 이 외의 경우 스택 맨 위의 문자와 맞춰보자.
            // 스택이 비어있는 경우 실패 
            if( openStack.empty() ) return false;
            // 서로 짝이 맞지 않아도 실패
            if(opening.find(openStack.top()) != closing.find(formula[i]))
                return false;
            // 짝을 맞춘 괄호는 스택에서 뺀다.
            openStack.pop();
        }
    }
    // 닫히지 않은 괄호가 없어야 성공
    return openStack.empty();
}
*/ 

/* page 638 오프라인 알고리즘
code 19.3 외계 신호 분석 문제를 해결하는 가장 단순한 알고리즘
int simple(const vector<int>& signals, int k) {
    int ret = 0;
    for(int head=0; head < signals.size(); ++head) {
        int sum = 0;
        for(int tail=head; tail < signals.size(); ++tail) {
            // sum은 [head, tail] 구간의 합이다
            sum += signals[tail];
            if(sum == k) ret++;
            if(sum >= k) break;
        }
    }
    return ret;
}
*/

/* page 640 
code19.4 외계신호 분석 문제를 해결하는 최적화된 알고리즘
int optimized(const vector<int>& signals, int k) {
    int ret = 0; tail = 0; rangeSum = signals[0];
    for(int head=0; head < signals.size(); ++head) {
        // rangeSum이 k 이상인 최초의 구간을 만날 때까지 tail을 옮긴다.
        while(rangeSum < k && tail + 1 <signals.size())
            rangeSum += signals[++tail];

        if(rangeSum == k) ret++;

        // signals[head]는 이제 구간에서 빠진다.
        rangeSum -= signals[head];
    }
    return ret;
}
*/
/* page 641 
code 19.5 외계 신호 분석 문제를 해결하는 온라인 알고리즘
int countRanges(int k, int n) {
    RNG rng; // 신호값을 생성하는 난수 생성기
    queue<int> range; // 현재 구간에 들어있는 숫자들을 저장하는 큐
    int ret = 0; rangeSum = 0;
    for(int i = 0; i < n; i++) {
        // 구간에 숫자를 추가한다
        int newSignal = rng.next();
        rangeSum += newSignal;
        range.push(newSignal);
        
        // 구간의 합이 k를 초과하는 동안 구간에서 숫자를 뺀다.
        while(rangeSum > k) {
            rangeSum -= range.front();
            range.pop();
        }

        if(rangeSum == k) ret++;
    }
    return ret;
}
*/

/* page 642
code 19.6 외계신호 분석 문제에서 사용하는 선형합동 난수 생성기의 구현
struct RNG {
    unsigned seed;
    RNG() : seed(1983) {}
    unsigned next() {
        unsigned ret = seed;
        seed = ((seed * 214013u) + 2531011u);
        return ret % 10000 + 1;
    }
};

*/




