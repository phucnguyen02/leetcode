class Solution:
    def hund_to_word(self, num):
        if len(num) == 1:
            return self.small[num[0]]
        second_third = ""
        if num[-2:] in self.tens:
            second_third = self.tens[num[-2:]]
        elif num[-2:] in self.tens_2:
            second_third = self.tens_2[num[-2:]]
        else:
            if num[-2] != "0":
                second_third += self.tens_2[num[-2] + "0"] + " "
            second_third += self.small[num[-1]]
        
        if len(num) == 2 or num[0] == "0":
            return second_third

        return self.small[num[0]] + " Hundred " + second_third if second_third else self.small[num[0]] + " Hundred"

    def numberToWords(self, num: int) -> str:
        if num == 0: return "Zero"
        self.tens = {"10": "Ten", "11": "Eleven", "12": "Twelve", "13": "Thirteen", "14": "Fourteen", "15": "Fifteen", \
        "16": "Sixteen", "17": "Seventeen", "18": "Eighteen", "19": "Nineteen"}
        self.tens_2 = {"20": "Twenty", "30": "Thirty", "40": "Forty", "50": "Fifty", "60": "Sixty", \
        "70": "Seventy", "80": "Eighty", "90": "Ninety"}
        self.small = {"0": "", "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five",\
        "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine"}
        suffixes = {0: "", 1: "Thousand", 2: "Million", 3: "Billion", 4: "Trillion"}
        num = str(num)
        if len(num) % 3 != 0:
            num = "0"*(3 - len(num) % 3) + num
        count = 0
        res = ""
        for i in range(len(num) - 1, -1, -3):
            hund_word = self.hund_to_word(num[i-2:i+1])
            if hund_word:
                if suffixes[count]:
                    hund_word += " " + suffixes[count]
                if res:
                    res = hund_word + " " + res
                else:
                    res = hund_word
            count += 1
        return res


