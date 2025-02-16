def is_leap(year):
    if 1900<=year or year<10^5:
        if year%4==0 and (year%100!=0 or year%400==0):
            return True
        else:
            return False
    else:
        return False

year = int(input())
print(is_leap(year))