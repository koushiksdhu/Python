# Slicing: Slicing in Python is a feature that enables accessing parts of sequences like strings, tuples, and lists.

piano_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]    # List containing alphabets upto k.
piano_tuple = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]    # Tuple containing alphabets upto k.
sliced_piano_list = piano_list[2:5] # Slicing (first index is inclusive, whereas second index is exclusive)
sliced_piano_tuple = piano_tuple[2:5] # Slicing (first index is inclusive, whereas second index is exclusive)

print("Piano List:", piano_list)
print("Piano Tuple:", piano_tuple)
print("Sliced Piano List:", sliced_piano_list)
print("Sliced Piano Tuple:", sliced_piano_tuple)
print("\nList:")
print("Index 2 to last: ", piano_list[2:])   # slicing from index 2 to the last.
print("From first position to index 5: ", piano_list[:5])   # slicing from first index upto index 5.
print("Reverse: ", piano_list[::-1])    # List in reverse order.
print("\nTuple:")
print("Index 2 to last: ", piano_tuple[2:])   # slicing from index 2 to the last.
print("From first position to index 5: ", piano_tuple[:5])   # slicing from first index upto index 5.
print("Reverse: ", piano_tuple[::-1])    # List in reverse order.