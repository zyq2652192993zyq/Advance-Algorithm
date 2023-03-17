> # CodeWars-Unique In Order

Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

```scala
uniqueInOrder("AAAABBBCCDAABBB")   == List('A', 'B', 'C', 'D', 'A', 'B')
uniqueInOrder("ABBCcAD")           == List('A', 'B', 'C', 'c', 'A', 'D')
uniqueInOrder(List(1, 2, 2, 3, 3)) == List(1, 2, 3)
```

---

本质上就是LeetCode去除重复数字，可以用一行代码来实现。

my solution:

```scala
  def uniqueInOrder[T](xs: Iterable[T]): Seq[T] = {
    def loop(pre: T, seq: Seq[T], acc: Seq[T], isFirst: Boolean): Seq[T] = {
      seq match {
        case s if s.isEmpty => acc.reverse
        case s =>
          if (!isFirst && s.head == pre) loop(s.head, s.tail, acc, false)
          else loop(s.head, s.tail, s.head +: acc, false)
      }
    }

    loop(null.asInstanceOf[T], xs.toSeq, Seq[T](), true)
  }
```

elegant way:

```scala
object Kata {

    def uniqueInOrder[T](xs: Iterable[T]): Seq[T] =
    	if (xs.isEmpty) Nil else xs.head +: uniqueInOrder(xs.dropWhile(_ == xs.head))
}
```

