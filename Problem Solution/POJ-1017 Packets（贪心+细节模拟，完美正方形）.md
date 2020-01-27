> # POJ-1017 Packets（贪心+细节模拟，完美正方形）

# Description

A factory produces products packed in square packets of the same height h and of the sizes `1*1, 2*2, 3*3, 4*4, 5*5, 6*6`. These products are always delivered to customers in the square parcels of the same height h as the products have and of the size 6*6. Because of the expenses it is the interest of the factory as well as of the customer to minimize the number of parcels necessary to deliver the ordered products from the factory to the customer. A good program solving the problem of finding the minimal number of parcels necessary to deliver the given products according to an order would save a lot of money. You are asked to make such a program.

# Input

The input file consists of several lines specifying orders. Each line specifies one order. Orders are described by six integers separated by one space representing successively the number of packets of individual size from the smallest size 1*1 to the biggest size 6*6. The end of the input file is indicated by the line containing six zeros.

# Output

The output file contains one line for each line in the input file. This line contains the minimal number of parcels into which the order from the corresponding line of the input file can be packed. There is no line in the output file corresponding to the last ``null'' line of the input file.

# Sample Input

```
0 0 4 0 0 1 
7 5 1 0 0 0 
0 0 0 0 0 0 
```

# Sample Output

```
2
1
```

----

```c++
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff;

vector<int> sequence(6, 0);

int packet()
{
	int cnt = 0;

	cnt += sequence[5]; //6x6的每个单独分配一个包裹
	sequence[5] = 0;

	while (sequence[4]) {
		++cnt; //5x5的必须需要一个包裹，配合11个1x1的
		--sequence[4];
		if (sequence[0] >= 11) sequence[0] -= 11;
		else {
			sequence[0] = 0;
			break;
		}
	}
	cnt += sequence[4];

	while (sequence[3]) {
		int space = 20;
		++cnt;
		--sequence[3]; //4x4也必须单独分配一个，配合5个2x2的
		while (space > 0) {
			if (sequence[1]) {//先用2x2的去填充
				space -= 4;
				--sequence[1];
			}
			else { //意味着2x2的没有了
				if (sequence[0]) { //余下的用1x1的填充
					space -= 1;
					--sequence[0];
				}
				else break;
			}
		}
	}

	cnt += sequence[2] / 4; //3x3的先自己4个填充
	sequence[2] = sequence[2] % 4;
	if (sequence[2]) {
		int space = 36;
		space -= sequence[2] * 9;
		if (sequence[2] == 1) { //1个3x3 配5个2x2 和7个1x1
			if (sequence[1] >= 5) { //可以凑出5个2x2
				sequence[1] -= 5;
				space -= 20;
				while (space > 0 && sequence[0]) {
					--sequence[0];
					--space;
				}
			}
			else {
				space -= sequence[1] * 4; //不够5个就全都用上
				sequence[1] = 0;
				while (space > 0 && sequence[0]) {
					--sequence[0];
					--space;
				}
			}
		}
		else if (sequence[2] == 2) { //2个3x3 配3个2x2 和6个1x1
			if (sequence[1] >= 3) { //可以凑出3个2x2
				sequence[1] -= 3;
				space -= 12;
				while (space > 0 && sequence[0]) {
					--sequence[0];
					--space;
				}
			}
			else {
				space -= sequence[1] * 4; //不够3个就全都用上
				sequence[1] = 0;
				while (space > 0 && sequence[0]) {
					--sequence[0];
					--space;
				}
			}
		}
		else if (sequence[2] == 3) { //3个3x3 配1个2x2 和5个1x1
			if (sequence[1] >= 1) { //可以凑出3个2x2
				sequence[1] -= 1;
				space -= 4;
				while (space > 0 && sequence[0]) {
					--sequence[0];
					--space;
				}
			}
			else {
				space -= sequence[1] * 4; //不够1个就全都用上
				sequence[1] = 0;
				while (space > 0 && sequence[0]) {
					--sequence[0];
					--space;
				}
			}
		}
		++cnt;
		sequence[2] = 0;
	}

	while (sequence[1] || sequence[0]) {
		int space = 36;
		if (sequence[1] >= 9) { //9个2x2的位置
			sequence[1] -= 9;
			space -= 36;
		}
		else {
			space -= sequence[1] * 4;
			sequence[1] = 0;
			while (space > 0 && sequence[0]) {
				--sequence[0];
				--space;
			}
		}
		++cnt;
	}

	return cnt;
}

inline bool getInput()
{
	for (int i = 0; i < 6; ++i) cin >> sequence[i];
	bool flag = false;
	for (int i = 0; i < 6; ++i) flag = (flag || sequence[i]);

	return flag;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	while (getInput()) cout << packet() << endl;

    return 0;
}
```

这是我最开始写的AC代码，可以看出，虽然整个过程都想明白了，但是代码过于冗长，可以有很多精简的地方。

整体思路：

* 6x6的只能分配单独的一个包裹
* 5x5的也必须每个分配一个单独的包裹，每个包裹剩余的部分可以用11个1x1的来填充，直到两者中有一个耗尽
* 4x4的每个也必须分配一个单独的包裹，每个包裹剩余的部分可以用5个2x2的填充，如果2x2的耗尽，那么用1x1的填充，直到4x4或1x1的消耗完
* 3x3的分配方案较多，首先应该自己4个配一个包裹，余下的数量只可能是3，2，1
  * 余下数量是3，配1个2x2和5个1x1
  * 余下数量是2， 配3个2x2和6个1x1
  * 余下数量是1，配5个2x2和7个1x1
* 2x2和1x1的分配就是先用2x2的填充，2x2的耗尽了再用1x1的填充

整体思路不难，但是到3x3的部分时候需要格外小心，很容易写错。

自己第一遍写的时候就出错了，好在可以再virtual judge上找到UVA live的同样题目，就可以用`Udebug`来辅助debug。

下面对代码进行精简，自己第一次AC的代码也是贪心的方法，但是因为每种分配里掺杂2x2和1x1的分配会导致代码看起来很混乱，极其容易写错。所以可以换一种思路，先不考虑把每个箱子填满，比如5x5的，就每一个分配一个箱子，空着的部分先不做处理，4x4的也是，等到处理2x2的时候，先用2x2去逐个填充，也就是去填充4x4的，然后是3x3的。那么1x1的同理。这样代码就会精简很懂。

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff;

vector<int> sequence(6, 0);
int other[4] = {0, 5, 3, 1}; //因为POJ不支持vector列表初始化，所以采用数组

int packet()
{
	int cnt = 0;
	//3x3的四个拼一组，4x4,5x5,6x6每个都必须分配一个单独的
	cnt += ceil(double(sequence[2]) / 4) + sequence[3] + sequence[4] + sequence[5];
	//two代表需要多少个2x2去填充4x4和3x3空下来的部分
	int two = sequence[3] * 5 + other[sequence[2] % 4];
	//如果用2x2的填充完了还有空余
	if (two <= sequence[1]) cnt += ceil(double(sequence[1] - two) / 9);
	//one代表用1x1去填充其他箱子留下来的空余
	int one = cnt * 36 - sequence[5] * 36 - sequence[4] * 25 - sequence[3] * 16 - sequence[2] * 9 - sequence[1] * 4;
	//如果1x1填满了空余还有剩余
	if (one <= sequence[0]) cnt += ceil(double(sequence[0] - one) / 36);

	return cnt;
}

inline bool getInput()
{
	for (int i = 0; i < 6; ++i) cin >> sequence[i];
	bool flag = false;
	for (int i = 0; i < 6; ++i) flag = (flag || sequence[i]);

	return flag;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	while (getInput()) cout << packet() << endl;

    return 0;
}
```

代码瞬间少了很多，从整体上看，

* 对于6x6的，肯定不需要额外的来填充
* 对于5x5的，只需要1x1来填充，但是实际需要包裹数没有增加
* 对于4x4的，先利用2x2的填充，再1x1的，包裹数也是不增加的

所以可以最开始根据6x6, 5x5, 4x4和3x3的来确定这些部分需要多少个包裹，这里我们利用了`ceil`函数来针对`3x`这种特殊情况，用`cnt`来记录到此时需要的包裹数量。

然后考虑2x2的，先考虑去填充前面没有放满的箱子，我们用变量`two`来记录把前面空出来的部分填满至少需要多少个2x2的，比较特殊的就是3x3的部分，因为3x3先4个一组，剩余下来的可能是0，1，2，3个，需要的2x2的数量也是不规则的，所以用了一个数组`other`来解决这种特殊情形。

如果2x2的填满了前面空余的部分还有剩余，那么就9个一组的放置。

下面考虑1x1的数量，优先把1x1去放置在前面箱子空出来的部分，也就是5x5的，4x4可能也需要，3x3的，这时候有一个比较奇妙的办法就是利用“面积”来考虑，不妨忽略高度想象成平面图形，因为只要是空出来的部分，一定可以用1x1的来填满。此时`cnt`记录的是到目前为止，6x6,5x5, 4x4, 3x3, 2x2所需要的包裹数目，每个的“面积”都是6x6也就是36，然后去除这些包裹占据的“面积”，那么余下来的就是需要1x1填充的，由此计算出`one`。

如果填充完前面空余的部分还有剩余的1x1，那么就自己单独36个一组放置。

这种其实是以完美正方形为背景的。

















