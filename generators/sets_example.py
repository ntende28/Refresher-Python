song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth']}

user_tag_data = {'Lowkey Space': ['party', 'synth', 'fast', 'upbeat'],
                 'Retro Words': ['happy', 'electronic', 'fun', 'exciting'],
                 'Wait For Limit': ['romance', 'chill', 'rap', 'rhythmic'], 
                 'Stomping Cue': ['country', 'swing', 'party', 'instrumental']}

# Checkpoint 1
new_song_data = {}

# Checkpoint 2
for key, val in song_data.items():
    song_tag_set = set(val)
    user_tag_set = set(user_tag_data[key])
    # combining two sets i.e. union operation 
    # you can either use my_set.union(other_set) or pipe (|) character
    new_song_data[key] = song_tag_set | user_tag_set

print(new_song_data)
print("\n")

'''
Other set operations
- Intersection; you can use ampersand operator(&) i.e.song_set & tag_set or .intersection()
- Difference; you can apply the minus (-) operator i.e song_set - tag_set or song_set.difference(tag_set)
- Symmetric difference : opposite of intersection. Use the .symmetric_difference() or caret (^) operation
'''

# Given a set and frozenset of song tags for two python related hits
prepare_to_py = {'rock', 'heavy metal', 'electric guitar', 'synth'}

py_and_dry = frozenset({'classic', 'rock', 'electric guitar', 'rock and roll'})

# Find the elements which are only in prepare_to_py
only_in_prepare_to_py = prepare_to_py.difference(py_and_dry)

print(only_in_prepare_to_py)

# Find the elements which are only in py_and_dry
only_in_py_and_dry = py_and_dry - prepare_to_py
print(only_in_py_and_dry)
print("\n")

# Find the elements which are exclusive to each song and not shared using the method
exclusive_tags = prepare_to_py.symmetric_difference(py_and_dry)
print(exclusive_tags)
frozen_exclusive_tags = py_and_dry ^ prepare_to_py
print(frozen_exclusive_tags)