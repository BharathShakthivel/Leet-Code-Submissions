class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Brute Force - O(nlogn)
        # points.sort(key = lambda p: p[0]**2 + p[1]**2)
        # return points[:k]

        # Min heap - Time - O(n + klogn) ; Space - O(N)
        """
        Layman Idea
        Put all points into a priority bucket ordered by distance
        The closest point is always on top
        Pop the top k times
        Done

        Think of it like:

        You dump all distances into a pile
        The smallest always floats to the top
        You take the closest k
        """
        # min_heap = []
        # for x,y in points:
        #     dist = x**2 + y **2
        #     min_heap.append([dist,x,y])
        # heapq.heapify(min_heap)

        # res = []
        # while k>0:
        #     dist,x,y = heapq.heappop(min_heap)
        #     res.append([x,y])
        #     k-=1
        # return res

        # Max Heap - Time - O (n logk)
        """
        Layman Idea

        Instead of keeping all points, we:

        Keep only k closest so far
        If heap grows bigger than k → remove the farthest

        So heap never grows beyond k

        This is the trick.
        """
        max_heap = []
        for x,y in points:
            dist = -(x**2 + y**2)
            heapq.heappush(max_heap,[dist,x,y])
            if len(max_heap)>k:
                heapq.heappop(max_heap)
        res = []
        while max_heap:
            dist,x,y = heapq.heappop(max_heap)
            res.append([x,y])
        return res


        '''
        You already understand the **sort (brute force)** version. Now let’s explain the **Min Heap** and **Max Heap** versions in simple, intuitive terms.

---

# 1. Min Heap Approach (Keep everything, take k smallest)

```python
min_heap = []
for x,y in points:
    dist = x**2 + y**2
    min_heap.append([dist,x,y])

heapq.heapify(min_heap)

res = []
while k>0:
    dist,x,y = heapq.heappop(min_heap)
    res.append([x,y])
    k-=1
return res
```

## Layman Idea

1. Put **all points into a priority bucket** ordered by distance
2. The **closest point is always on top**
3. Pop the top **k times**
4. Done

Think of it like:

* You dump **all distances into a pile**
* The smallest always floats to the top
* You take the closest k

---

## Example

```
points = [[1,3], [-2,2], [5,8]]
k = 2
```

Step 1 — compute distances:

```
[10, 1, 3]
[8, -2, 2]
[89, 5, 8]
```

Heap becomes (smallest on top):

```
[8, -2, 2]
[10, 1, 3]
[89, 5, 8]
```

Pop k=2 times:

Pop 1:

```
[-2,2]
```

Pop 2:

```
[1,3]
```

Return:

```
[[-2,2], [1,3]]
```

---

## Time Complexity (Layman)

You:

* build heap from **n items** → O(n)
* remove **k items** → each pop costs log n

So total:

```
O(n + k log n)
```

### Simple words

* Put everything in → linear time
* Take k smallest → slightly expensive each time

---

## Space Complexity

You store **all points in heap**

```
O(n)
```

---

# 2. Max Heap Approach (Keep only k best)

This is the **smartest one**.

```python
max_heap = []
for x,y in points:
    dist = -(x**2 + y**2)
    heapq.heappush(max_heap,[dist,x,y])
    if len(max_heap)>k:
        heapq.heappop(max_heap)
```

## Layman Idea

Instead of keeping **all points**, we:

* Keep only **k closest so far**
* If heap grows bigger than k → remove the farthest

So heap **never grows beyond k**

This is the trick.

---

## Why negative distance?

Python only has **min heap**

We want **max heap** (remove farthest)

So we store:

```
-dist
```

Largest distance becomes **smallest negative number**

Example:

```
dist = 10  -> -10
dist = 5   -> -5
```

Heap pops **-10 first** → which means distance 10 → farthest removed

---

## Step-by-step Example

```
points = [[1,3], [-2,2], [5,8]]
k = 2
```

### Insert [1,3]

dist = 10 → store -10

heap:

```
[-10,1,3]
```

---

### Insert [-2,2]

dist = 8 → store -8

heap:

```
[-10,1,3]
[-8,-2,2]
```

size = 2 (OK)

---

### Insert [5,8]

dist = 89 → store -89

heap:

```
[-89,5,8]
[-8,-2,2]
[-10,1,3]
```

size = 3 > k → pop

pop removes **-89** (farthest)

heap now:

```
[-10,1,3]
[-8,-2,2]
```

We kept only **2 closest**

---

Return heap:

```
[[1,3], [-2,2]]
```

---

# Time Complexity (Layman)

Loop runs **n times**

Each push/pop costs:

```
log k
```

Because heap size never > k

Total:

```
O(n log k)
```

### Why is this better?

Because:

```
k << n
```

Example:

```
n = 100000
k = 10
```

Sort → log n
Heap → log k (tiny)

Much faster.

---

# Space Complexity

Heap size is **only k**

```
O(k)
```

This is best possible.

---

# Visual Comparison

| Method   | Idea             | Time           | Space    |
| -------- | ---------------- | -------------- | -------- |
| Sort     | sort everything  | O(n log n)     | O(1)     |
| Min Heap | store all, pop k | O(n + k log n) | O(n)     |
| Max Heap | keep only k      | **O(n log k)** | **O(k)** |

---

# When to use each

Use **sort** when:

* small input
* want simple code

Use **min heap** when:

* want k smallest
* don't care about memory

Use **max heap** when:

* **best performance**
* large dataset
* interview preferred answer

---

# One-line intuition

Min heap:

> Put everything in, take k

Max heap:

> Keep only the best k, throw away the rest

        '''
