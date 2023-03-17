> # CodeWars-Multiples of 3 or 5

Link: https://www.codewars.com/kata/514b92a657cdc65150000006

level: `6kyu`

----

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 **below** the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

**Note:** If the number is a multiple of **both** 3 and 5, only count it *once*.

----

my solution:

```scala
object MultiplesOf3Or5 {   
    def solution(number: Int): Long = 
  if (number < 0) 0
    else {
      val arr = (0 until number).filter(e => e % 3 == 0 || e % 5 == 0).toList
      arr match {
        case Nil => 0
        case _ => arr.foldLeft(0L)((s, e) => s + e)
      }
    }
}
```

an efficient and elegant way:

```scala
object MultiplesOf3Or5 {   
    def solution(number: Int): Long =
    (1 until number).view.filter(x => x % 3 == 0 || x % 5 == 0).foldLeft(0L)(_ + _)
}
```

Through this problem, i learn how the `view` method. In scala collections, the default mode is strict. Using `view`, we can transform a strict collection into lazily collection. It has same effect about loop. Using `force`, it can turn from lazily to strict.

referemce:

* [scala collections view](https://docs.scala-lang.org/overviews/collections/views.html)

