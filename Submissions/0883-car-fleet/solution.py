class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # cars = sorted(zip(position, speed), reverse=True)
        # stack = []
        # for p,s in cars:
        #     time = (target - p)/s
        #     if not stack or time > stack[-1]:
        #         stack.append(time)
        # return len(stack)

        # Without using stack
        cars = sorted(zip(position, speed), reverse=True)
        count = 1
        pre_time = (target - cars[0][0])/cars[0][1]
        for p,s in cars:
            time = (target - p)/s
            if time > pre_time:
                count+=1
                pre_time = time
            else:
                continue
        return count

    # 🔹 Pattern Logic (Memorize This)
    #  "Monotonic Increasing Arrival Time Stack"
    #     1. Sort cars by position descending.
    #     2. For each car:
    #         compute arrival time.
    #         if stack empty OR time > last_time:
    #             push time (new fleet)
    #         else:
    #             merge (do nothing)
    #     3. Answer = number of fleet times stored.


    '''
    🚗 Car Fleet — Core Pattern Summary
🔹 Problem Type

Sort + Monotonic Stack (Greedy)

🔹 Core Insight

A car can only merge with cars in front of it, never behind.

So we must process cars from:

Closest to target → Farthest from target

That means:

Sort cars by position in descending order.

🔹 Key Observation

Instead of simulating movement:

Compute:

time_to_target = (target - position) / speed


Now the problem becomes:

Count how many times the arrival time increases as we move backward.

🔹 Fleet Formation Rule

When scanning cars (front → back):

If current time > last fleet time
→ ❗ Cannot catch up
→ ✅ New fleet

If current time ≤ last fleet time
→ 🚗 Catches up
→ ❌ Merges (ignore it)


🔹 Why It Works

A slower car ahead creates a "blocking fleet".

Any faster car behind with smaller/equal time will catch up before target.

Arrival times must form a monotonic increasing sequence to create new fleets.

🔹 Pattern Name to Remember

"Monotonic Increasing Arrival Time Stack"

Whenever you see:

Cars moving in one direction

No overtaking

Catch-up behavior

Count groups

Think:

Sort by position → Compare arrival times → Monotonic stack

🔹 Interview One-Liner Explanation

If interviewer asks for intuition:

"I sort cars by position descending and compute arrival times.
While scanning from front to back, I only form a new fleet when a car's arrival time is greater than the fleet ahead. Otherwise, it merges."

Clean. Simple. Confident.

🔹 Space Optimization Insight

You don’t actually need a stack.
You only need:

last_time

fleet_count

Because you only compare with the previous fleet.

🧠 Memory Hook

Think:

“New fleet only if slower than the fleet ahead.”

Or even shorter:

“Arrival time increases → fleet increases.”
    '''
