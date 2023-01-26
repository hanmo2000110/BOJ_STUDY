#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
 
const int MAX = 1000;
 
string cache[MAX] = { "0", "1" };
 
string bigNumAdd(string num1, string num2)
{
        long long sum = 0;
        string result;
 
        //1의 자리부터 더하기 시작한다
        while (!num1.empty() || !num2.empty() || sum)
        {
                 if (!num1.empty())
                 {
                         sum += num1.back() - '0';
                         num1.pop_back();
                 }
                 if (!num2.empty())
                 {
                         sum += num2.back() - '0';
                         num2.pop_back();
                 }
                 //다시 string 형태로 만들어 push_back
                 result.push_back((sum % 10) + '0');
                 sum /= 10;
        }
        //1의 자리부터 result에 넣었으므로 뒤집어줘야한다
        reverse(result.begin(), result.end());
        return result;
}
 
//string 연산자 <= 오버로딩
bool operator<=(const string &a, const string &b)
{
        if (a.size() == b.size())
        {
                 for (int i = 0; i < a.size(); i++)
                 {
                         if (a[i] > b[i])
                                 return false;
                         else if (a[i] < b[i])
                                 return true;
                 }
                 return true;
        }
        if (a.size() < b.size())
                 return true;
        else
                 return false;
}
 
void preCalculate(void)
{
        for (int i = 2; i < MAX; i++)
                 cache[i] = bigNumAdd(cache[i - 1], cache[i - 2]);
}
 
int main(void)
{
        preCalculate();
 
        while (1)
        {
                 string a, b;
                 cin >> a >> b;
 
                 if (a == "0" && b == "0")
                         break;
 
                 int cnt = 0;
                 for (int i = 2; i < MAX; i++)
                         if (a <= cache[i] && cache[i] <= b)
                                 cnt++;
                 cout << cnt << "\n";
        }
        return 0;
}
