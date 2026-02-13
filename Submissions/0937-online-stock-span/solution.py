class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0]<=price:
            span+= self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price,span))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


# LOGIC

# PATTERN: Monotonic Decreasing Stack (Price, Span)
#
# Goal:
# For each price, calculate how many consecutive previous days
# had prices <= today's price.
#
# Core Idea:
# Maintain a stack of (price, span) where:
# - Stack is strictly decreasing by price.
# - Each element stores how many days it already covers (its span).
#
# Why it works:
# If today's price >= stack top price,
# then today's price also dominates all days covered by that top element.
# So we:
#   1. Pop the top
#   2. Add its span to today's span
#   3. Repeat while top price <= current price
#
# Then push (current_price, total_span)
#
# This ensures:
# - Each price is pushed once and popped once
# - Time complexity = O(n) overall
#
# Mental Model:
# "Collapse all smaller/equal prices behind me
#  and absorb their spans."
#
# When to recognize this pattern:
# - Need consecutive counts
# - Comparing current element with previous ones
# - Elements become useless once a bigger one appears
# - Classic Monotonic Stack problem

