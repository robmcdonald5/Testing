class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        unjustified_list = [[]]
        justified_list = []
        unjustified_list[0].append(words[0])
        current_len = len(unjustified_list[0][0])

        if len(words) <= 1:
            return words
        
        i = 0
        for word in words[1:]:
            if current_len + len(word) <= maxWidth:
                unjustified_list[i].append(word)
            else:
                i += 1
                

        for i in range(len(unjustified_list)):
            white_space = maxWidth - sum(len(word) for word in unjustified_list[0])
            gcd_current = reduce(math.gcd, white_space)
            if white_space > 0 and sum(len(word) for word in range unjustified_list)

        return justified_list