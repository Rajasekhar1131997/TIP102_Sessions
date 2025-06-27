"""
Problem 1: Manage Performance Stage Changes
At a cultural festival, multiple performances are scheduled on a single stage. However, due to last-minute changes, 
some performances need to be rescheduled or canceled. The festival organizers use a stack to manage these changes efficiently.
You are given a list changes of strings where each string represents a change action. The actions can be:
"Schedule X": Schedule a performance with ID X on the stage.
"Cancel": Cancel the most recently scheduled performance that hasn't been canceled yet.
"Reschedule": Reschedule the most recently canceled performance to be the next on stage.
Return a list of performance IDs that remain scheduled on the stage after all changes have been applied.
"""
def manage_stage_changes(changes):
    stack = []
    empty = []
    for change in changes:
        if change.startswith("Schedule"):
            stack.append(change.split(" ")[1])
        elif stack and change == "Cancel":
            empty.append(stack.pop())
        elif stack and change == "Reschedule":
            stack.append(empty.pop())
    return stack

print("--------Problem 1---------")
print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 


"""
Problem 2: Queue of Performance Requests
You are organizing a festival and want to manage the queue of requests to perform. Each request has a priority. 
Use a queue to process the performance requests in the order they arrive but ensure that requests 
with higher priorities are processed before those with lower priorities. Return the order in which performances are processed.
"""
# solving this problem without queue, with the help of list and lambda function
def process_performance_requests(requests):
    requests.sort(key=lambda x:x[0], reverse = True)
    result = []
    for priority, performance in requests:
        result.append(performance)
    return result

print("--------Problem 2 (without queues)---------")
print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))

# solving this problem with the help of queue
from collections import deque
def process_performance_requests(requests):
    q = deque(requests)
    prorities = sorted((p for p, _ in requests), reverse = True)
    result = []
    while q:
        priority, performance = q.popleft()
        if priority == prorities[0]:
            result.append(performance)
            prorities.pop(0)
        else:
            q.append((priority,performance))
    return result

print("--------Problem 2---------")
print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))

"""
Problem 3: Collecting Points at Festival Booths
At the festival, there are various booths where visitors can collect points. Each booth has a specific number of points available. 
Use a stack to simulate the process of collecting points and return the total points collected after visiting all booths.
"""
def collect_festival_points(points):
    if not points:
        return 0
    if len(points) == 1:
        return points
    stack = list(points)
    total = 0
    while(stack):
        total += stack.pop()
    return total

print("--------Problem 3---------")
print(collect_festival_points([5, 8, 3, 10])) 
print(collect_festival_points([2, 7, 4, 6])) 
print(collect_festival_points([1, 5, 9, 2, 8])) 

"""
Problem 4: Festival Booth Navigation
At the cultural festival, you are managing a treasure hunt where participants need to visit booths in a specific order. 
The order in which they should visit the booths is defined by a series of clues. 
However, some clues lead to dead ends, and participants must backtrack to previous booths to continue their journey.
You are given a list of clues, where each clue is either a booth number (an integer) to visit or the word "back" indicating 
that the participant should backtrack to the previous booth.
Write a function to simulate the participant's journey and return the final sequence of booths visited, in the order they were visited.
"""
def booth_navigation(clues):
    stack = []
    for clue in clues:
        if stack and (clue == "back"):
            stack.pop()
        elif not stack and clue == "back":
            continue
        else:
            stack.append(clue)
    return stack

print("--------Problem 4---------")
clues = [1, 2, "back", 3, 4]
print(booth_navigation(clues)) 

clues = [5, 3, 2, "back", "back", 7]
print(booth_navigation(clues)) 

clues = [1, "back", 2, "back", "back", 3]
print(booth_navigation(clues)) 

"""
Problem 5: Merge Performance Schedules
You are organizing a cultural festival and have two performance schedules, schedule1 and schedule2, 
each represented by a string where each character corresponds to a performance slot. 
Merge the schedules by adding performances in alternating order, starting with schedule1. 
If one schedule is longer than the other, append the additional performances onto the end of the merged schedule.
Return the merged performance schedule.
"""
def merge_schedules(schedule1, schedule2):
    merged = []
    i,j = 0, 0
    turn = 0
    while i < len(schedule1) and j < len(schedule2):
        if turn == 0:
            merged.append(schedule1[i])
            i+=1
        else:
            merged.append(schedule2[j])
            j+=1
        turn ^= 1
    if i < len(schedule1):
        merged.extend(schedule1[i:])
    if j < len(schedule2):
        merged.extend(schedule2[j:])
    return ''.join(merged)
    

print("--------Problem 5---------")
print(merge_schedules("abc", "pqr")) 
print(merge_schedules("ab", "pqrs")) 
print(merge_schedules("abcd", "pq"))

"""
Problem 6: Next Greater Event
At a cultural festival, you have a schedule of events where each event has a unique popularity score. 
The schedule is represented by two distinct 0-indexed integer arrays schedule1 and schedule2, where schedule1 is a subset of schedule2.
For each event in schedule1, find its position in schedule2 and determine the next event in schedule2 with a higher popularity score. 
If there is no such event, then the answer for that event is -1.
Return an array ans of length schedule1.length such that ans[i] is the next greater event's popularity score as described above.
"""
def next_greater_event(schedule1, schedule2):
    schedule2_pos = {}
    for key, value in enumerate(schedule2):
        schedule2_pos[value] = key
    print(schedule2_pos)
    answer = []
    n = len(schedule2)
    for i in schedule1:
        j = schedule2_pos[i]
        found = -1
        
        for k in range(j+1, n):
            if schedule2[k] > i:
                found = schedule2[k]
                break
        answer.append(found)
    return answer


print("--------Problem 6---------")
print(next_greater_event([4, 1, 2], [1, 3, 4, 2])) 
print(next_greater_event([2, 4], [1, 2, 3, 4]))


"""
Problem 7: Sort Performances by Type
You are organizing a cultural festival and have a list of performances represented by an integer array performances. 
Each performance is classified as either an even type (e.g., dance, music) or an odd type (e.g., drama, poetry).
Your task is to rearrange the performances so that all the even-type performances appear at the beginning of the array, 
followed by all the odd-type performances.
Return any array that satisfies this condition.
"""
def sort_performances_by_type(performances):
    if not performances:
        return []
    if len(performances) == 1:
        return performances
    left = 0
    right = len(performances) - 1
    while left < right:
        if performances[left] % 2 == 0:
            left += 1
        elif performances[right] % 2 == 1:
            right -= 1
        else:
            performances[left], performances[right] = performances[right], performances[left]
            left += 1
            right -= 1
    return performances

print("--------Problem 7---------")
print(sort_performances_by_type([3, 1, 2, 4]))
print(sort_performances_by_type([3, 2, 1, 0, 5, 6, 8]))
print(sort_performances_by_type([0]))