class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window + HashSet
        l = 0                  # Left pointer of window
        res = 0                # Stores maximum length found
        window = set()         # Set to track unique characters in current window
        for r in range(len(s)):   # Expand window using right pointer        
            # If duplicate found, shrink window from left
            # Keep removing characters until duplicate is removed
            while s[r] in window:
                window.remove(s[l])   # Remove left character
                l += 1                # Move left pointer forward
            # Add current character to window (now it's unique)
            window.add(s[r])
            # Update max length of valid window
            # Window size = r - l + 1
            res = max(res, r - l + 1)
        return res


