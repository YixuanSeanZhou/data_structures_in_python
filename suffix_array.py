class SuffixArray:
    def __init__(self, string: str):
        self.array = []
        self.add_string(s=string)

    def add_string(self, s: str):
        """
        s --> the long-string of the database
        """
        self.array = [0]
        for i in range(1, len(s)):
            start_idx = 0
            end_idx = len(self.array) - 1
            attemp_idx = 0
            s_to_insert = s[i:]
            while start_idx != end_idx:
                attemp_idx = (start_idx + end_idx) // 2
                if s_to_insert < s[self.array[attemp_idx]:]:
                    # insert at the front
                    end_idx = attemp_idx
                elif s_to_insert > s[self.array[attemp_idx]:]:
                    start_idx = attemp_idx + 1
                else:
                    break
            if s_to_insert < s[self.array[start_idx]:]:
                self.array.insert(start_idx, i)
            else:
                self.array.insert(start_idx + 1, i)


if __name__ == '__main__':
    suffix_array = SuffixArray('CACAGATTACACACA')
    print(suffix_array.array)