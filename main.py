class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        arrive.sort()
        depart.sort()

        n = len(arrive)
        events = [(item, 1) for item in arrive] + [(item, 0) for item in depart]
        events.sort()

        count = 0
        for event in events:
            if event[1] == 1:
                count += 1
            else:
                count -= 1
            if count > k:
                return false

        return true