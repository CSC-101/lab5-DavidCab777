import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def time_add(tim1, tim2):
    sum_seconds = tim1.second + tim2.second
    minutes_from_seconds = sum_seconds // 60
    seconds = sum_seconds % 60

    sum_minutes = tim1.minute + tim2.minute + minutes_from_seconds
    hours_from_minutes = sum_minutes // 60
    remaining_minutes = sum_minutes % 60
    sum_hours = tim1.hour + tim2.hour + hours_from_minutes
    return f'{sum_hours}, {remaining_minutes}, {seconds}'

# Part 4
def is_descending(lst: list[float]):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] < lst[j + 1]:
                new = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = new

        return lst

# Part 5
def largest_between(lst:list[int], lower:int, upper:int):
    if lower > upper:
        return None
    if lower > upper:
        return None
    lower = max(0, lower)
    upper = min(len(lst) - 1, upper)
    idx = lower
    for i in range(lower, upper + 1):
        if lst[i] > lst[idx]:
            idx = i
    return idx
# Part 6
def furthest_from_origin(lst:list):
    if not data.Point:
        return None
    idx = 0
    for i in range(0, 1):
        if lst[i] > lst[idx]:
            idx = i
        for i in range(1, len(lst)):
            if lst[i] > lst[idx]:
                idx = i
        return idx
