class Solution:
    def validIPAddress(self, IP: str) -> str:
        if IP.count('.') == 3:
            return self.validate_IPv4(IP)
        elif IP.count(':') == 7:
            return self.validate_IPv6(IP)
        else:
            return 'Neither'

    def validate_IPv4(self, IP: str) -> str:
        nums = IP.split('.')

        for num in nums:
            # Each number in IPv4 needs to be length 1, 2 or 3
            if len(num) == 0 or len(num) > 3:
                return 'Neither'

            # Leading 0 is not allowed
            # Non digits are not allowed
            # digit bigger than 255 is not allowed
            if (num[0] == '0' and len(num) != 1) or not num.isdigit() or int(num) > 255:
                return 'Neither'

        return 'IPv4'

    def validate_IPv6(self, IP: str) -> str:
        nums = IP.split(':')
        hexdigits = '0123456789abcdefABCDEF'
        for num in nums:

            # Empty is not allowed
            # num longer than 4 is not allowed
            # If num contains characters other than the above hexdigits, not allowed
            if len(num) == 0 or len(num) > 4 or not all(c in hexdigits for c in num):
                return 'Neither'

        return 'IPv6'


IP = "172.16.254.1"  # IPv4
IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"  # IPv6
IP = "256.256.256.256"  # Neither
IP = "2001:0db8:85a3:0:0:8A2E:0370:7334:"  # Neither
IP = "1e1.4.5.6"  # Neither
print(Solution().validIPAddress(IP))

