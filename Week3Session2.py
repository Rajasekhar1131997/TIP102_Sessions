'''
Problem 1

Understand
1. input/output
    input: list(stack)
    output: list
2. edge cases
    empty list, empty string
3. run time/space constraints
    large list
4. restrictions
    n/a
5. happy cases
    given 

Plan
1. create empty list (for output)
2. create empty list, tracking cancelled schedules (stack)
3. iterate through the input list
    check if starts with "schedule"
        if yes append letter to first empty list
    else if string = cancel
        pop most recently scheduled
        append to cancelled list
    else if string = reschedule
        pop recently cancelled schedule
        append to first list
4. return first list


Implement
def manage_stage_changes(changes):
    output = []
    empty = []
    for schedule in changes:
        if schedule.startswith("Schedule"):
            output.append(schedule.split(" ")[1])
        elif schedule == "Cancel":
            empty.append(output.pop())
        elif schedule == "Reschedule":
            output.append(empty.pop())
    return output

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 
'''


'''
Problem 2

Understand
1. input/output
    input: list 
    output: list of strings based on order 
2. edge cases
    0 as priority number, two strings have the same number 
3. run time/space constraints
    number of elements given in list 
4. restrictions
    n/a 
5. happy cases  
    given 

Plan 
1. create a new queue 
2. sort the numbers in the queue and then reverse the numbers of the sorted queue
3. after sorting, we can return the string element associated with priority queue numbers 

Implement
def process_performance_requests(requests): 
    requests.sort(key = lambda x:x[0])
    requests.sort(reverse = True)

    proccessed_in_order = [] 
    for priority, performance in requests: 
        proccessed_in_order.append(performance)
    return proccessed_in_order
    

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))
'''

'''
Problem 3

Understand
1. input/output
 input: list
 output: integer
2. edge cases: empty list
3. runtime/space constraints: based on the elements from the list
4. restrictions : use stack
5. happy cases :given in the question

Plan:
1. initialize a stack
2. let our sum be 0
3. while loop:
    sum = sum + recently popped element from the stack
4. return sum

Implement
'''


def collect_festival_points(points):
    stack = list(points)
    total_sum = 0

    while(stack):
        popped_element = stack.pop()
        total_sum += popped_element
    return total_sum

print(collect_festival_points([5, 8, 3, 10])) 
print(collect_festival_points([2, 7, 4, 6])) 
print(collect_festival_points([1, 5, 9, 2, 8])) 