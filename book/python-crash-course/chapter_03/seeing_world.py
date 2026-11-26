locations = ['Tokyo','Paris','New York','London','Sydney']
print("Original locations:")
print(locations)

print("\nSorted location without change the original: ")
print(sorted(locations))

print("\nOriginal locations: ")
print(locations)

print("\nSorted location in reverse without change the original: ")
print(sorted(locations, reverse=True))

print("\nOriginal locations: ")
print(locations)

locations.reverse()
print("\nReverse order of the location: ")
print(locations)

locations.sort()
print("\nSorted location by change the original: ")
print(locations)

locations.sort(reverse=True)
print("\nSorted location in reverse by change the original: ")
print(locations)

total_location = len(locations)
print("\nTotal location that I want to visit:",total_location)