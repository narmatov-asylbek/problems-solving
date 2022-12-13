# RList interpetes a reversed linked list

# RList Rlist -> List
# Adds number of linked list and returns it's head
def add(l1, l2):
    if not l1.next and not l2.next:
        return None