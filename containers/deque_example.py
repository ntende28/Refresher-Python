'''
Working with Deque containers

These are similar to lists, but they are optimized for appending and popping to the front 
and back, rather than having optimized accessing. Because of this, they are great for 
working with data where you don’t need to access elements in the middle very often or at all. 
'''

from collections import deque

bug_data = deque()

loaded_bug_reports = get_all_bug_reports()

for bug in loaded_bug_reports:
    if bug['priority'] == 'high':
        # With a deque, we can append to the front directly
        bug_data.appendleft(bug)
    else:
        bug_data.append(bug)

# With a deque, we can pop from the front directly
next_bug_to_fix = bug_data.popleft()
