#!/usr/bin/env python3

def parse_ranges(s):
    s = s.strip()
    if not s:
        return []
    parts = [p.strip() for p in s.split(',') if p.strip()]
    ranges = []
    for p in parts:
        if '-' not in p:
            continue
        a, b = p.split('-', 1)
        ranges.append((int(a), int(b)))
    return ranges

def sum_double_ids_in_ranges(ranges):
    found = set()
    if not ranges:
        return 0
    max_b = max(b for (_, b) in ranges)
    max_digits = len(str(max_b))
    for a, b in ranges:
        if a > b:
            continue
        max_k = max_digits // 2
        for k in range(1, max_k + 1):
            pow10k = 10 ** k
            multiplier = pow10k + 1
            s_min_digits = 10**(k-1)
            s_max_digits = 10**k - 1
            s_low = max(s_min_digits, (a + multiplier - 1) // multiplier)
            s_high = min(s_max_digits, b // multiplier)
            if s_low <= s_high:
                for s in range(s_low, s_high + 1):
                    n = s * multiplier
                    if a <= n <= b:
                        found.add(n)
    return sum(found)

def main():
    ranges_text = "8123221734-8123333968,2665-4538,189952-274622,4975-9031,24163352-24202932,1233-1772,9898889349-9899037441,2-15,2147801-2281579,296141-327417,8989846734-8989940664,31172-42921,593312-632035,862987-983007,613600462-613621897,81807088-81833878,13258610-13489867,643517-782886,986483-1022745,113493-167913,10677-16867,372-518,3489007333-3489264175,1858-2534,18547-26982,16-29,247-366,55547-103861,57-74,30-56,1670594-1765773,76-129,134085905-134182567,441436-566415,7539123416-7539252430,668-1146,581563513-581619699"
    ranges = parse_ranges(ranges_text)
    result = sum_double_ids_in_ranges(ranges)
    print(result)

if __name__ == "__main__":
    main()
