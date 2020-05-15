> # Codeforces 510C Fox and Names（拓扑排序）

Tags: `DFS and similar` `graphs` `greedy` `sorting` `1600`

Links: http://codeforces.com/contest/512/problem/A

-----

# Description

Fox Ciel is going to publish a paper on FOCS (Foxes Operated Computer Systems, pronounce: "Fox"). She heard a rumor: the authors list on the paper is always sorted in the lexicographical order.

After checking some examples, she found out that sometimes it wasn't true. On some papers authors' names weren't sorted in lexicographical order in normal sense. But it was always true that after some modification of the order of letters in alphabet, the order of authors becomes lexicographical!

She wants to know, if there exists an order of letters in Latin alphabet such that the names on the paper she is submitting are following in the lexicographical order. If so, you should find out any such order.

Lexicographical order is defined in following way. When we compare *s* and *t*, first we find the leftmost position with differing characters: $s_i ≠ t_i$. If there is no such position (i. e. *s* is a prefix of *t* or vice versa) the shortest string is less. Otherwise, we compare characters $s_i$and $t_i$ according to their order in alphabet.

# Input

The first line contains an integer *n* (1 ≤ *n* ≤ 100): number of names.

Each of the following *n* lines contain one string *name**i* (1 ≤ |*name**i*| ≤ 100), the *i*-th name. Each name contains only lowercase Latin letters. All names are different.

# Output

If there exists such order of letters that the given names are sorted lexicographically, output any such order as a permutation of characters 'a'–'z' (i. e. first output the first letter of the modified alphabet, then the second, and so on).

Otherwise output a single word "Impossible" (without quotes).

# Example

## Input

```
3
rivest
shamir
adleman
```

## Output

```
bcdefghijklmnopqrsatuvwxyz
```

## Input

```
10
tourist
petr
wjmzbmr
yeputons
vepifanov
scottwu
oooooooooooooooo
subscriber
rowdark
tankengineer
```

## Output

```
Impossible
```

## Input

```
10
petr
egor
endagorion
feferivan
ilovetanyaromanova
kostka
dmitriyh
maratsnowbear
bredorjaguarturnik
cgyforever
```

## Output

```
aghjlnopefikdmbcqrstuvwxyz
```

## Input

```
7
car
care
careful
carefully
becarefuldontforgetsomething
otherwiseyouwillbehacked
goodluck
```

## Output

```
acbdefhijklmnogpqrstuvwxyz
```

---

```c++
#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>

using namespace std;

vector<vector<int>> adj(26, vector<int>(26, 0));
vector<int> result, inDegree(26, 0);
queue<int> q;

ostream & operator<<(ostream & os, const vector<int> & v)
{
    string s;
    for (size_t i = 0; i < v.size(); ++i){
        s.push_back(char('a' + v[i]));
    }
    os << s;
    return os;
}

ostream & operator<<(ostream & os, const vector<vector<int>> & v)
{
    for (size_t i = 0; i < 26; ++i){
        for (size_t j = 0; j < 26; ++j){
            os << v[i][j] << " ";
        }
        os << endl;
    }
    return os;
}

void topologicalSort()
{
    for (int i = 0; i < 26; ++i){
        if (inDegree[i] == 0)
            q.push(i);
    }

    while (!q.empty()) {
        int tmp = q.front();
        q.pop();
        result.push_back(tmp);
        for (int i = 0; i < 26; ++i){
            if (adj[tmp][i] && (--inDegree[i]) == 0)
                q.push(i);
        }
    }
    if (result.size() < 26) cout << "Impossible" << endl;
    else cout << result << endl;
}


int main()
{
    int stringNum;
    cin >> stringNum;
    vector<string> word;
    for (int i = 0; i < stringNum; ++i){
        string tmp;
        cin >> tmp;
        word.push_back(tmp);
    }

    bool flag = false;
    for (size_t i = 0; i < word.size() - 1; ++i){
        auto length = min(word[i].size(), word[i+1].size());
        size_t k = 0;
        while (word[i][k] == word[i+1][k] && k < length) {
            ++k;
        }
        if (k >= length && word[i].size() > word[i+1].size()){
            cout << "Impossible" << endl;
            flag = true;
            break;
        } 
        int pos1 = word[i][k] - 'a', pos2 = word[i+1][k] - 'a';
        if (!adj[pos1][pos2]){
            adj[pos1][pos2] = 1;
            ++inDegree[pos2];
        }
    }
    if (!flag) topologicalSort();

    return 0;
}
```

