"""
Problem 1: Planning Your Daily Work Schedule
Your day consists of various tasks, each requiring a certain amount of time. To optimize your workday, 
you want to find a pair of tasks that fits exactly into a specific time slot you have available. 
You need to identify if there is a pair of tasks whose combined time matches the available slot.
Given a list of integers representing the time required for each task and an integer representing the available time slot, 
write a function that returns True if there exists a pair of tasks that exactly matches the available time slot, and False otherwise.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def find_task_pair(task_times, available_time):
    if not task_times:
        return False
    left , right = 0, len(task_times) - 1
    while left < right:
        sum = task_times[left] + task_times[right]
        if sum == available_time:
            return True
        elif sum < available_time:
            left += 1
        else:
            right -= 1
    return False

# Time Complexity is O(n) and Space Complexity is O(n)
def find_task_pair(task_times, available_time):
    if not task_times:
        return False
    seen = set()
    for time in task_times:
        if available_time - time in seen:
            return True
        seen.add(time)
    return False

print("--------Problem 1 (Two Pointer Approach)---------")
task_times = [30, 45, 60, 90, 120]
available_time = 105
print(find_task_pair(task_times, available_time))

task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
print(find_task_pair(task_times_2, available_time))

task_times_3 = [20, 30, 50, 70]
available_time = 60
print(find_task_pair(task_times_3, available_time))
print("Time Complexity: O(n logn)")
print("Space Complexity: O(1)")

"""
Problem 2: Minimizing Workload Gaps
You work with clients across different time zones and often have gaps between your work sessions. 
You want to minimize these gaps to make your workday more efficient. You have a list of work sessions, each with a start time and an end time. 
Your task is to find the smallest gap between any two consecutive work sessions.
Given a list of tuples where each tuple represents a work session with a start and end time 
(both in 24-hour format as integers, e.g., 1300 for 1:00 PM), write a function to find the smallest gap between any two consecutive work sessions. The gap is measured in minutes.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def find_smallest_gap(work_sessions):
    if not work_sessions:
        return 0
    work_sessions.sort(key=lambda x:to_minutes(x[0]))
    min_gap = float('inf')
    previous_end = to_minutes(work_sessions[0][1])
    for start, end in work_sessions[1:]:
        current_start = to_minutes(start)
        gap = current_start - previous_end
        if gap < min_gap:
            min_gap = gap
        previous_end = max(previous_end, to_minutes(end))
    return max(0, min_gap)

def to_minutes(hhmm):
    h = hhmm//100
    m = hhmm % 100
    return h * 60 + m

print("--------Problem 2---------")
work_sessions1 = [(900, 1100), (1300, 1500), (1600, 1800)]
print(find_smallest_gap(work_sessions1))

work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
print(find_smallest_gap(work_sessions_2))

work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
print(find_smallest_gap(work_sessions_3))
print("Time Complexity: O(n logn)")
print("Space Complexity: O(1)")

"""
Problem 3: Expense Tacking and Categorization
You travel frequently and need to keep track of your expenses. You categorize your expenses into different categories such as 
"Food," "Transport," "Accommodation," etc. At the end of each month, you want to calculate the total expenses for each category 
to better understand where your money is going.
Given a list of tuples where each tuple contains an expense category (string) and an expense amount (float), 
write a function that returns the expense categories and the total expenses for each category. 
Additionally, the function should return the category with the highest total expense.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def calculate_expenses(expenses):
    if not expenses:
        return ()
    dictionary = {}
    for expense, amount in expenses:
        dictionary[expense] = dictionary.get(expense, 0) + amount
    max_expense = max(dictionary, key=dictionary.get)
    return (dictionary, max_expense)

print("--------Problem 3---------")
expenses = [("Food", 12.5), ("Transport", 15.0), ("Accommodation", 50.0),
            ("Food", 7.5), ("Transport", 10.0), ("Food", 10.0)]
print(calculate_expenses(expenses))

expenses_2 = [("Entertainment", 20.0), ("Food", 15.0), ("Transport", 10.0),
              ("Entertainment", 5.0), ("Food", 25.0), ("Accommodation", 40.0)]
print(calculate_expenses(expenses_2))

expenses_3 = [("Utilities", 100.0), ("Food", 50.0), ("Transport", 75.0),
              ("Utilities", 50.0), ("Food", 25.0)]
print(calculate_expenses(expenses_3))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")

"""
Problem 4: Analyzing Word Frequency
As a digital nomad who writes blogs, articles, and reports regularly, it's important to analyze the text you produce to 
ensure clarity and avoid overusing certain words. You want to create a tool that analyzes the frequency of 
each word in a given text and identifies the most frequent word(s).
Given a string of text, write a function that returns the unique words and the number of times each word appears in the text. 
Additionally, return a list of the word(s) that appear most frequently.
Assumptions:
The text is case-insensitive, so "Word" and "word" should be treated as the same word.
Punctuation should be ignored.
In case of a tie, return all words that have the highest frequency.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
import string
def word_frequency_analysis(text):
    if not text:
        return ()
    translator = str.maketrans('','',string.punctuation)
    text = text.translate(translator)
    text = text.lower()
    text = text.split(" ")
    dictionary = {}
    for word in text:
        dictionary[word] = dictionary.get(word, 0) + 1
    max_count = max(dictionary.values())
    top_words = [word for word, count in dictionary.items() if count == max_count]
    return ((dictionary, top_words))
        

print("--------Problem 4---------")
text = "The quick brown fox jumps over the lazy dog. The dog was not amused."
print(word_frequency_analysis(text))

text_2 = "Digital nomads love to travel. Travel is their passion."
print(word_frequency_analysis(text_2))

text_3 = "Stay connected. Stay productive. Stay happy."
print(word_frequency_analysis(text_3))
print("Time Complexity: O(n)")
print("Space Complexity: O(K), where k is the number of top tied words")

"""
Problem 5: Validating HTML Tags
As a digital nomad who frequently writes and edits HTML for your blog, you want to ensure that your HTML code is properly structured. 
One important aspect of HTML structure is ensuring that all opening tags have corresponding closing tags and that they are properly nested.
Given a string of HTML-like tags (simplified for this problem), write a function to determine if the tags are properly nested and closed. 
The tags will be in the form of <tag> for opening tags and </tag> for closing tags.
The function should return True if the tags are properly nested and closed, and False otherwise.
Assumptions:
You can assume that tags are well-formed (e.g., <div>, </div>, <a>, </a>, etc.).
Tags can be nested but cannot overlap improperly (e.g., <div><p></div></p> is invalid).
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
import re
def validate_html_tags(html):
    if len(html) < 2:
        return False
    stack = []
    tag_pattern = re.compile(r"</?([a-zA-Z0-9]+)>")
    for match in tag_pattern.finditer(html):
        full_tag = match.group(0)
        tag_name = match.group(1)
        if full_tag.startswith("</"):
            if not stack or stack.pop() != tag_name:
                return False
        else:
            stack.append(tag_name)
    return not stack


print("--------Problem 5---------")
html = "<div><p></p></div>"
print(validate_html_tags(html))

html_2 = "<div><p></div></p>"
print(validate_html_tags(html_2))

html_3 = "<div><p><a></a></p></div>"
print(validate_html_tags(html_3))

html_4 = "<div><p></a></p></div>"
print(validate_html_tags(html_4))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")

"""
Problem 6: Task Prioritization with Limited Time
You often have a long list of tasks to complete, but limited time to do so. Each task has a specific duration, 
and you only have a certain amount of time available in your schedule. You need to prioritize and complete 
as many tasks as possible within the given time limit.
Given a list of task durations and a time limit, determine the maximum number of tasks you can complete within that time.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def max_tasks_within_time(tasks, time_limit):
    if not tasks:
        return 0
    if time_limit and len(tasks) < 2 and sum(tasks) < time_limit:
        return tasks[0]
    tasks.sort()
    sum = 0
    count = 0
    for task in tasks:
        sum += task
        if sum <= time_limit:
            count += 1
    return count


print("--------Problem 6---------")
tasks = [5, 10, 7, 8]
time_limit = 20
print(max_tasks_within_time(tasks, time_limit))

tasks_2 = [2, 4, 6, 3, 1]
time_limit = 10
print(max_tasks_within_time(tasks_2, time_limit))

tasks_3 = [8, 5, 3, 2, 7]
time_limit = 15
print(max_tasks_within_time(tasks_3, time_limit))
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")

"""
Problem 7: Frequent Co-working Spaces
You often work from various co-working spaces. You want to analyze your usage patterns to identify which co-working spaces 
you visit the most frequently. Given a list of co-working spaces you visited over the past month, 
write a function to determine which co-working space(s) you visited most frequently. If there is a tie, return all of the most visited spaces.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def most_frequent_spaces(visits):
    if not visits:
        return []
    if len(visits) < 2:
        return visits
    dictionary = {}
    for visit in visits:
        dictionary[visit] = dictionary.get(visit, 0) + 1
    max_count = max(dictionary.values())
    result = [visit for visit, count in dictionary.items() if count == max_count]
    return result

print("--------Problem 7---------")
visits = ["WeWork", "Regus", "Spaces", "WeWork", "Regus", "WeWork"]
print(most_frequent_spaces(visits))

visits_2 = ["IndieDesk", "Spaces", "IndieDesk", "WeWork", "Spaces", "IndieDesk", "WeWork"]
print(most_frequent_spaces(visits_2))

visits_3 = ["Hub", "Regus", "WeWork", "Hub", "WeWork", "Regus", "Hub", "Regus"]
print(most_frequent_spaces(visits_3))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")

"""
Problem 8: Track Popular Destinations
You want to track the most popular destinations you visited based on the number of times you have visited them. 
Given a list of visited destinations with timestamps, your goal is to determine the destination that has been visited the most 
and the total number of times it was visited. If there is a tie, return the one with the latest visit.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
def most_popular_destination(visits):
    if not visits:
        return ()
    if len(visits) < 2:
        visit, _ = visits[0]
        return (visit, 1)
    dictionary = {}
    latest = {}
    for visit, timestamp in visits:
        dictionary[visit] = dictionary.get(visit, 0) + 1
        if visit not in latest or timestamp > latest[visit]:
            latest[visit] = timestamp
    best_visit = None
    best_count = 0
    best_timestamp = None
    for visit, count in dictionary.items():
        timestamp = latest[visit]
        if (count > best_count) or (count == best_count and (best_timestamp is None or timestamp > best_timestamp)):
            best_visit = visit
            best_count = count
            best_timestamp = timestamp
    return (best_visit, best_count)


print("--------Problem 8---------")
visits = [("Paris", "2024-07-15"), ("Tokyo", "2024-08-01"), ("Paris", "2024-08-05"), ("New York", "2024-08-10"), ("Tokyo", "2024-08-15"), ("Paris", "2024-08-20")]
print(most_popular_destination(visits))

visits_2 = [("London", "2024-06-01"), ("Berlin", "2024-06-15"), ("London", "2024-07-01"), ("Berlin", "2024-07-10"), ("London", "2024-07-15")]
print(most_popular_destination(visits_2))

visits_3 = [("Sydney", "2024-05-01"), ("Dubai", "2024-05-15"), ("Sydney", "2024-05-20"), ("Dubai", "2024-06-01"), ("Dubai", "2024-06-15")]
print(most_popular_destination(visits_3))
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")