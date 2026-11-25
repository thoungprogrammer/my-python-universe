my_guest = [ 'nikola tesla' , 'linus torvalds' , 'issac newton']
print(f"{my_guest[0].title()}, I would like to invite you to dinner.")
print(f"{my_guest[1].title()}, I would like to invite you to dinner.")
print(f"{my_guest[2].title()}, I would like to invite you to dinner.")


print(f"\nUnfortunately, {my_guest[2].title()} can't make the dinner.")

my_guest[2] = 'morn chanthoung'
print(f"Since {my_guest[2].title()} was replaced, the invitation should go to {my_guest[2].title()}.")

print(f"\n{my_guest[0].title()}, I would like to invite you to dinner.")
print(f"{my_guest[1].title()}, I would like to invite you to dinner.")
print(f"{my_guest[2].title()}, I would like to invite you to dinner.")

print("\nGood news! I found a bigger table,so I can invite more guests.")
my_guest.insert(0,'elon musk')
print(my_guest)
my_guest.insert(2,'albert einstein')
print(my_guest)
my_guest.append('ada lovelace')
print(my_guest)

print(f"\n{my_guest[0].title()}, I would like to invite you to dinner.")
print(f"{my_guest[1].title()}, I would like to invite you to dinner.")
print(f"{my_guest[2].title()}, I would like to invite you to dinner.")
print(f"{my_guest[3].title()}, I would like to invite you to dinner.")
print(f"{my_guest[4].title()}, I would like to invite you to dinner.")
print(f"{my_guest[5].title()}, I would like to invite you to dinner.")

print("\nUnfortunately, I can invite only two people to dinner.")
print(f"Sorry, {my_guest.pop().title()}, I can't invite you to dinner.")
print(f"Sorry, {my_guest.pop(0).title()}, I can't invite you to dinner.")
print(f"Sorry, {my_guest.pop(1).title()}, I can't invite you to dinner.")
print(f"Sorry, {my_guest.pop(1).title()}, I can't invite you to dinner.")
print(my_guest)

print(f"\n{my_guest[0].title()}, I would like to invite you to dinner.")
print(f"{my_guest[1].title()}, I would like to invite you to dinner.")

del my_guest[0]
del my_guest[0]
print(f"\nThe list is {my_guest}")