class Solution:
    def validate_ipv4(self, tokens):
        for token in tokens:
            if not token or len(token) > 3: return False
            if len(token) > 1 and token[0] == "0": return False
            num = 0
            for i in range(len(token)):
                if not token[i].isdigit():
                    return False

                num = num * 10 + int(token[i])
            if num > 255: return False

        return True

    def validate_ipv6(self, tokens):
        for token in tokens:
            if not token or len(token) > 4: return False
            for i in range(len(token)):
                if token[i].isalpha() and not ("a" <= token[i].lower() <= "f"):
                    return False
        return True

    def validIPAddress(self, queryIP: str) -> str:
        dot_tokens = queryIP.split(".")
        if len(dot_tokens) == 4:
            return "IPv4" if self.validate_ipv4(dot_tokens) else "Neither"
        else:
            colon_tokens = queryIP.split(":")
            if len(colon_tokens) == 8:
                return "IPv6" if self.validate_ipv6(colon_tokens) else "Neither"
        return "Neither"