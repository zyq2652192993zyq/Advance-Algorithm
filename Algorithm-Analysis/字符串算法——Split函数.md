> # 字符串算法——Split函数

在C++里面标准库没有提`Split`函数（一种说法是存储的方式无法统一，究竟是存储在`vector`，还是内置数组`[]`里，还是`list`），但是却经常会遇到需要使用`Split`函数的地方，比如验证IP地址，或者将通过空格分隔的字符串切分成一个个的单词，都需要用到。

## 使用`istringstream`和`getline`

比如LeetCode 468. 验证IP地址

```c++
class Solution {
public:
    string validIPAddress(string IP) {
    	std::ios_base::sync_with_stdio(false);
		cin.tie(NULL);
		cout.tie(NULL);

		return dotFind(IP) ? IPv4Check(IP) : IPv6Check(IP);
    }

    bool dotFind(const string s)
    {
    	for (const auto & e : s) {
    		if (e == '.') return true;
    	}

    	return false;
    }

    string IPv4Check(const string & s)
    {
    	istringstream is(s);
    	string tmp;
    	int cnt = 0;
    	while (getline(is, tmp, '.')) {
    		++cnt;
    		if (tmp.size() == 0 || tmp.size() > 3) return "Neither";
    		if (tmp.size() > 1 && tmp[0] == '0') return "Neither";
    		for (const auto & e : tmp) if (!isdigit(e)) return "Neither";
    		if (stoi(tmp) > 255) return "Neither";
    		if (cnt > 4) return "Neither";
    	}

    	return (cnt == 4 && s.back() != '.') ? "IPv4" : "Neither";
    }

    string IPv6Check(const string & s)
    {
    	istringstream is(s);
    	string tmp;
    	int cnt = 0;
    	while (getline(is, tmp, ':')) {
    		++cnt;
    		if (tmp.size() == 0 || tmp.size() > 4) return "Neither";
    		for (const auto & e : tmp) 
    			if (!(('0' <= e && e <= '9') || ('a' <= e && e <= 'f') || ('A' <= e && e <= 'F'))) return "Neither";
    		if (cnt > 8) return "Neither";
    	}
 
		return (cnt == 8 && s.back() != ':') ? "IPv6" : "Neither";
    }
};
```

## 使用字符串自带的`find`函数

比如HDU-1062 Text Reverse

```c++
#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
using namespace std;
int main(void)
{
    int t,loc;
    cin>>t;
    getchar();
    string s1;    
    while (t--)
    {
        getline(cin,s1);
        loc=0;
        while (s1.find(" ",loc)!=string::npos)//反转前n-1个单词
        {
            reverse( s1.begin()+loc , s1.begin()+s1.find(" ",loc) );
            loc=s1.find(" ",loc)+1;//更新每次反转的begin位置
        }
        reverse( s1.begin()+s1.find_last_of(" ")+1 , s1.end() );//反转最后一个单词
        cout<<s1<<endl;
    }
    return 0;
}
```

相对来讲，使用`istringstream`更加优雅一些。

## 使用`stringstream`

使用`stringstream`有个特殊的条件，就是字符串之间是用空格进行分割的。

- [x] LeetCode 1570.Reformat Date

```c++
class Solution {
public:
    string reformatDate(string date) {
        unordered_map<string, string>mp = {{"Jan", "01"}, {"Feb", "02"}, {"Mar", "03"}, {"Apr", "04"}, 
                                           {"May", "05"}, {"Jun", "06"}, {"Jul", "07"}, {"Aug", "08"}, 
                                           {"Sep", "09"}, {"Oct", "10"}, {"Nov", "11"}, {"Dec", "12"}};
        string out = "", temp;
        stringstream ss(date);
        ss >> temp;
        if(temp.length()==3)
            out+="0";
        out += temp.substr(0, temp.length()-2);
            
        ss >> temp;
        out = mp[temp] + "-" + out;
        
        ss >> temp;
        out = temp + "-" + out;
        return out;       
    }
};
```



