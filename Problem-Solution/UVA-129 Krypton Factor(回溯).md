> # UVA-129 Krypton Factor(回溯)

## Description

You have been employed by the organisers of a Super Krypton Factor Contest in which contestants have very high mental and physical abilities. In one section of the contest the contestants are tested on their ability to recall a sequenace of characters which has been read to them by the Quiz Master. Many of the contestants are very good at recognising patterns. Therefore, in order to add some difficulty to this test, the organisers have decided that sequences containing certain types of repeated subsequences should not be used. However, they do not wish to remove all subsequences that are repeated, since in that case no single character could be repeated. This in itself would make the problem too easy for the contestants. Instead it is decided to eliminate all sequences containing an occurrence of two adjoining identical subsequences. Sequences containing such an occurrence will be called “easy”. Other sequences will be called “hard”. For example, the sequence ABACBCBAD is easy, since it contains an adjoining repetition of the subsequence CB. Other examples of easy sequences are: 
• BB 
• ABCDACABCAB 
• ABCDABCD 
Some examples of hard sequences are: 
• D 
• DC
• ABDAB 
• CBABCBA 
In order to provide the Quiz Master with a potentially unlimited source of questions you are asked to write a program that will read input lines from standard input and will write to standard output.

## Input

Each input line contains integers n and L (in that order), where n > 0 and L is in the range 1 ≤ L ≤ 26. Input is terminated by a line containing two zeroes.

## Output

For each input line prints out the n-th hard sequence (composed of letters drawn from the first L letters in the alphabet), in increasing alphabetical order (Alphabetical ordering here corresponds to the normal ordering encountered in a dictionary), followed (on the next line) by the length of that sequence. The first sequence in this ordering is ‘A’. You may assume that for given n and L there do exist at least n hard sequences. 

As such a sequence is potentially very long, split it into groups of four (4) characters separated by a space. If there are more than 16 such groups, please start a new line for the 17th group. Your program may assume a maximum sequence length of 80.

For example, with L = 3, the first 7 hard sequences are:

```
A
AB
ABA
ABAC
ABACA
ABACAB
ABACABA
```

## Sample Input

```
7 3
30 3
0 0
```

## Sample Outptu

```
ABAC ABA
7
ABAC ABCA CBAB CABA CABC ACBA CABA
28
```

-----

用step代表目前找到的合法数字的个数，因为只有合法的数字才能除法step增加。

用`pos`代表当前探寻的位置，对于每个位置都去尝试是否可行，有个trick就是每次只需要检查后缀中长度为偶数的子串是否合法即可。

另外就是对输出有格式的要求，注意4个一组和换行同时出现的情况。

```c++
#include <bits/stdc++.h>

using namespace std;


int n, l, step;
vector<int> seq(85);



bool DFS(int pos) {
    if (step++ == n) {
        int cnt = 0;
        for (int i = 0; i < pos; ++i) {
            cout << (char)('A' + seq[i]);
            if (i != pos - 1 && (i + 1) % 4 == 0) {
                ++cnt;
                if (cnt == 16) cout << endl;
                if (cnt != 16) cout << " ";
            }
        }
        cout << endl;
        cout << pos << endl;
        return true;
    }

    for (int i = 0; i < l; ++i) {
        seq[pos] = i;
        bool isValid = true;
        for (int j = 1; j * 2 <= pos + 1; ++j) {
            bool tmpPass = false;
            for (int k = 0; k < j; ++k) {
                if (seq[pos - k] != seq[pos - k - j]) {
                    tmpPass = true;
                    break;
                }
            }
            if (! tmpPass) {
                isValid = false;
                break;
            }
        }

        if (isValid) {
            if (DFS(pos + 1)) {
                return true;
            }
        }
    }

    return false;
} 



int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    while (cin >> n >> l) {
        if (n == 0 && l == 0) break;
        step = 0;
        DFS(0);
    }

    return 0;
}
```

