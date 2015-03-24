

# Problem 19: Counting Sundays
# https://projecteuler.net/problem=19

def is_leapyear(year):
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        return 1
    else:
        return 0
        
month = [31, 28, 31, 30, 31, 30,
         31, 31, 30, 31, 30, 31]
         
def days_of_month(m, y):
    return month[m-1] + (is_leapyear(y) if m == 2 else 0)
    
def days_of_year(y):
    return sum(month) + is_leapyear(y)

# date 1 Jan 1900 represented as (1, 1, 1900) 
# 1 Jan 1900 was Monday, days is 1
# 7 Jan 1900 was Sunday, days is 7
def date_to_days(date):
    dy, mn, yr = date
    days = dy
    for y in range(1900, yr):
        days += days_of_year(y)
    for m in range(1, mn):
        days += days_of_month(m, yr)
    return days

def is_sunday(days):
    return days % 7 == 0
    
def cs():
    count = 0
    for y in range(1901, 2000+1):
        for m in range(1, 12+1):
            days = date_to_days((1, m, y))
            if is_sunday(days):
                count += 1
    return count

#
def test():
    return 'No test'
    
def main():
    return cs()
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

