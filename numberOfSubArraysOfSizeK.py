class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        window = deque(maxlen=k)
        window_sum = 0

        for num in arr:
            if len(window) == k:
                window_sum -= window[0]

            window.append(num)
            window_sum += num

            if len(window) == k and window_sum / k >= threshold:
                count += 1

        return count