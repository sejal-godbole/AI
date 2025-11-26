facts = [
    ('John', 'Jim'),
    ('John', 'Ann'),
    ('Jim', 'Peter'),
    ('Jim', 'Mary'),
    ('Peter', 'Tom')
]

def get_children(parent_name):
    found_children = []
    for fact in facts:
        current_father = fact[0]
        current_child = fact[1]
        if current_father == parent_name:
            found_children.append(current_child)
    return found_children

def get_grandfather(grandchild_name):
    list_of_parents = []
    for fact in facts:
        current_father = fact[0]
        current_child = fact[1]
        if current_child == grandchild_name:
            list_of_parents.append(current_father)

    list_of_grandfathers = []
    for parent in list_of_parents:
        for fact in facts:
            current_father = fact[0]
            current_child = fact[1]
            if current_child == parent:
                list_of_grandfathers.append(current_father)
    return list_of_grandfathers

def get_siblings(person_name):
    my_parents = []
    for fact in facts:
        current_father = fact[0]
        current_child = fact[1]
        if current_child == person_name:
            my_parents.append(current_father)
            
    my_siblings = []
    for parent in my_parents:
        for fact in facts:
            current_father = fact[0]
            current_child = fact[1]
            if current_father == parent:
                if current_child != person_name:
                    my_siblings.append(current_child)
                    
    return my_siblings

print("Children of Jim:", get_children('Jim'))
print("Grandfather of Tom:", get_grandfather('Tom'))
print("Siblings of Jim:", get_siblings('Jim'))