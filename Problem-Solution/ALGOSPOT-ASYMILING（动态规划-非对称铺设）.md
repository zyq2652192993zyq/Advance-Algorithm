> # ALGOSPOT-ASYMILING（动态规划-非对称铺设）

#### 问题问题

![13.png](http://algospot.com/media/judge-attachments/99b44b86e82ea246a21867a6970aedfb/13.png)![12.png](http://algospot.com/media/judge-attachments/eabd9fdeb757541289354b1dde1357f0/12.png)![11.png](http://algospot.com/media/judge-attachments/56f26d8f5217e108489083aa594fca16/11.png)

![10.png](http://algospot.com/media/judge-attachments/b60ba1f71aaa61dde733d5088c75b82b/10.png)![09.png](http://algospot.com/media/judge-attachments/03beebe7a6a34a588d0742a71e6d63e4/09.png)![07.png](http://algospot.com/media/judge-attachments/71701ba4f30e767b1894c86b216a5daa/07.png)

我想用2 * 1大小的图块填充2 * n矩形，如图所示。磁贴不应相互重叠，但可以旋转90度。但是，这种平铺方法不应对称。上图显示了六种不对称的平铺方法来填充2 * 5矩形。由于以下两个是对称的，因此不计算在内。

![14.png](http://algospot.com/media/judge-attachments/25c64a7a37ecfc8c5b2691d24c237510/14.png)![08.png](http://algospot.com/media/judge-attachments/c9dec0372bcc0b198a30305af57364fa/08.png)

编写一个程序，计算给定n可能的非对称平铺方法的数量。方法的数量可能非常多，因此我们将余数除以1,000,000,007。

#### 输入值

输入的第一行给出了测试用例C的数量（1 <= C <= 50）。然后，每行的矩形宽度为n（1 <= n <= 100）。

#### 输出量

对于每个测试用例，请打印出不对称平铺方法的其余部分除以每行1,000,000,007。

#### 输入示例

```
3
2
4
92
```

#### 输出示例

```
0
2
913227494
```

#### 注意事项

这道题目是简单铺设的扩展，即不允许对称铺设。那么其实起作用的是中间的那块砖，需要分奇数和偶数来讨论。

任然是先计算出所有可能的情况，然后减去多余对称的情况。

奇数的情况：只有中间的砖是竖放的情况才会出现对称，也就是计算(n-1)/2的铺设情。

偶数的情况：中间竖放和横放都会产生重复的情况，所以需要剪掉两个部分。

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <cstdio>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>

using namespace std;

const long long MODE = 1000000007;

vector<long long> d = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,
 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 
 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 
 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 
 701408733, 134903163, 836311896, 971215059, 807526948, 778742000,
  586268941, 365010934, 951279875, 316290802, 267570670, 583861472, 
  851432142, 435293607, 286725742, 722019349, 8745084, 730764433, 
  739509517, 470273943, 209783453, 680057396, 889840849, 569898238, 
  459739080, 29637311, 489376391, 519013702, 8390086, 527403788, 
  535793874, 63197655, 598991529, 662189184, 261180706, 923369890, 
  184550589, 107920472, 292471061, 400391533, 692862594, 93254120, 
  786116714, 879370834, 665487541, 544858368, 210345902, 755204270, 
  965550172, 720754435, 686304600, 407059028, 93363621, 500422649, 
  593786270, 94208912, 687995182, 782204094};

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
   	int caseNum; cin >> caseNum;
   	while (caseNum--) {
   		int n; cin >> n;
   		if (n & 1) {
   			cout << (d[n] - d[(n - 1) >> 1] + MODE) % MODE << endl;
   		}
   		else {
   			cout << (d[n] - d[n >> 1] - d[(n -2 ) >> 1] + 2 * MODE) % MODE << endl;
   		}
   	}

    return 0;
}
```

注意因为取模可能导致相减出现负数的情况，所以需要针对不同的情况增加MODE