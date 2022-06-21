slot_text =  {'abv': '', 'flavor': '', 'taste': '', 'types': ''}

li = list(set([slot_text[k] for k in slot_text]))
print(li)

li = []
for k in slot_text:
    li.append(slot_text[k])
    
li = list(set([slot_text[k] for k in slot_text]))
print(li)