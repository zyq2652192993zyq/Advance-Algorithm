> # HDU-1257 最少拦截系统（二分查找）

某国为了防御敌国的导弹袭击,发展出一种导弹拦截系统.但是这种导弹拦截系统有一个缺陷:虽然它的第一发炮弹能够到达任意的高度,但是以后每一发炮弹都不能超过前一发的高度.某天,雷达捕捉到敌国的导弹来袭.由于该系统还在试用阶段,所以只有一套系统,因此有可能不能拦截所有的导弹.
怎么办呢?多搞几套系统呗!你说说倒蛮容易,成本呢?成本是个大问题啊.所以俺就到这里来求救了,请帮助计算一下最少需要多少套拦截系统.

# Input

输入若干组数据.每组数据包括:导弹总个数(正整数),导弹依此飞来的高度(雷达给出的高度数据是不大于30000的正整数,用空格分隔)

# Output

对应每组数据输出拦截所有导弹最少要配备多少套这种导弹拦截系统.

# Sample Input

```
8 389 207 155 300 299 170 158 65
```

# Sample Output

```
2
```

-----

```c++
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff; 

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    while (cin >> n) {
    	vector<int> sequence;
    	while (n--) {
    		int bomb;
    		cin >> bomb;
			//手写一个标准库算法lower_bound
    		int left = 0, right = sequence.size();
    		while (left < right) {
    			int mid = left + ((right - left) >> 1);
    			if (sequence[mid] < bomb) left = mid + 1;
    			else right = mid;
    		}
    		if (left == static_cast<int>(sequence.size())) sequence.push_back(bomb);
    		else sequence[left] = bomb;
    	}
    	cout << sequence.size() << endl;
    }
    
    return 0;
}
```

这道题目初看不难，但是自己第一遍写的时候犯了一个错误，写成了下面的代码：

```c++
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff; 

set<int> ms;

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    while (cin >> n) {
    	int cnt = 0;
    	while (n--) {
    		int bomb;
    		cin >> bomb;
    		auto pos = lower_bound(ms.begin(), ms.end(), bomb);
    		if (pos == ms.end()) {
    			++cnt;
    			ms.emplace(bomb);
    		}
    		else *pos = bomb;
    	}
    	cout << cnt << endl;
    	ms.clear();
    }
    
    return 0;
}
```

这个程序错在这两句：

```c++
auto pos = lower_bound(ms.begin(), ms.end(), bomb);
 ....   		
else *pos = bomb;
```

这里`lower_bound`返回的迭代器是`const`类型的，也就是对应的值是不被允许修改的，那么就陷入了难题，如何修改。起始仔细分析这道题目，发现并不需要用到`set`。

题意是当一个导弹来袭，所有的拦截系统没有高度可以超过来袭导弹高度的，那么就增加一台，如果有高度大于等于来袭高度的，就选择与来袭高度最接近的去拦截。

思路确定后来增加拦截系统和修改拦截高度产生的影响。需要增加拦截系统一定是目前所有的拦截高度都小于导弹来袭的高度，那么增加的拦截系统可以拦截的高度一定比原来所有的拦截系统的拦截高度要高，所以假如到序列的最后，序列仍然是升序排列的。

如果存在一个拦截系统可以拦截来袭的导弹，那么选择最接近来袭导弹高度的，显然是利用`lower_bound`，这里我选择了手写一个算法来寻找其位置，然后进行修改。修改后不会改变整个序列的有序性，因为要修改一定是修改的点对应的高度大于等于来袭导弹的高度，如果修改后导致其数值小于了序列前面的某个数值，那么完全可以用前面的数值对应的点来修改，所以产生了矛盾。

通过上述分析，发现核心部分仍然是写出`lower_bound`的代码，另外还需要去分析修改与增加对序列有序性产生的影响。