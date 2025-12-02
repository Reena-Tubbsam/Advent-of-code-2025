#!/usr/bin/env python3

def parse_ranges(s):
    parts = [p.strip() for p in s.split(',') if p.strip()]
    out = []
    for p in parts:
        if '-' in p:
            a, b = p.split('-', 1)
            out.append((int(a), int(b)))
    return out

def sum_invalid(ranges):
    found = set()
    if not ranges:
        return 0
    max_b = max(b for _, b in ranges)
    max_digits = len(str(max_b))

    for a, b in ranges:
        for digits in range(1, max_digits):
            s_min = 10**(digits - 1)
            s_max = 10**digits - 1

            for reps in range(2, max_digits // digits + 1):
                mult = sum(10**(digits * i) for i in range(reps))
                low = max(s_min, (a + mult - 1) // mult)
                high = min(s_max, b // mult)

                if low <= high:
                    for s in range(low, high + 1):
                        n = s * mult
                        if a <= n <= b:
                            found.add(n)

    return sum(found)

def main():
    s = "8123221734-8123333968,2665-4538,189952-274622,4975-9031,24163352-24202932,1233-1772,9898889349-9899037441,2-15,2147801-2281579,296141-327417,8989846734-8989940664,31172-42921,593312-632035,862987-983007,613600462-613621897,81807088-81833878,13258610-13489867,643517-782886,986483-1022745,113493-167913,10677-16867,372-518,3489007333-3489264175,1858-2534,18547-26982,16-29,247-366,55547-103861,57-74,30-56,1670594-1765773,76-129,134085905-134182567,441436-566415,7539123416-7539252430,668-1146,581563513-581619699"
    ranges = parse_ranges(s)
    print(sum_invalid(ranges))

if __name__ == "__main__":
    main()
