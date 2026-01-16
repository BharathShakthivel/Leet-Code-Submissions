class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p_1 = 0
        p_2 = 0
        result = ""
        while p_1 <= len(word1)-1 and p_2 <= len(word2)-1 : 
            result+= word1[p_1] + word2[p_2]    
            p_1+=1
            p_2+=1
        if p_1 == len(word1):
            result+= word2[p_2::]
            return result
        elif p_2 == len(word2):
            result+= word1[p_1::]
            return result
        return result

'''
1. Your loop condition is now correct

You changed the loop to run only while both pointers are valid.

That’s the key insight:

Alternating requires both strings to still have characters

Because of this:

Every indexing inside the loop is guaranteed safe

No more “one pointer valid, the other not” situations

This alone eliminates the index-out-of-range error.

2. You separated the phases cleanly

Your logic now has two clear phases:

Phase 1:

Alternate characters while both strings have characters

Phase 2:

One string is exhausted

Append the remainder of the other string

This separation is exactly what your earlier attempts were missing.

3. Pointer exhaustion is detected correctly

You now check:

p_1 == len(word1) → word1 fully consumed

p_2 == len(word2) → word2 fully consumed

That’s the correct exhaustion condition — not len(word) - 1.

This shows you’ve internalized the difference between:

Last valid index

First invalid index (termination condition)

That’s a big step forward.

4. No unsafe access ordering

Crucially:

All indexing happens only when safety is guaranteed

All remainder appending happens after the loop

There’s no longer any “check after indexing” risk.

Final takeaway

Compared to your first version, you’ve fixed all three root causes:

✔ Correct loop condition
✔ Correct exhaustion detection
✔ Correct responsibility separation

This is solid logic now — not just “working by luck”.

Nice progress
'''
