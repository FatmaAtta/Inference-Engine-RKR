def read_facts(file):
    facts = []
    file = open(file,'r')
    for line in file:
        facts.append(line.strip().replace('skin_smell','perfumed'))
    # processed_facts = []
    processed_fact = {}
    for fact in facts:
        if '=' in fact:
            key, value = fact.split('=')
            processed_fact[key.strip()] = value.strip()
        elif 'is' in fact:
            key, value = fact.split('is')
            processed_fact[key.strip()] = value.strip()
        else:
            processed_fact[fact.strip()] = True
    print(processed_fact)
    return processed_fact
# read_facts("facts.txt")


def read_rules(file):
    rules=[]
    rule = {}
    file = open(file,'r')
    for line in file:
        if "IF" in line and "THEN" in line:
            _, item = line.split("IF")
            condition, conclusion = item.split("THEN")
            rule[condition.strip().replace('AND','and').replace('OR','or')] = conclusion.strip()
    print(rule)
    return rule
# read_rules("rules.txt")

def split_and(condition):
    split =[]
    if 'and' in condition:
        split = condition.split(' and ')
        split = [word.strip() for word in split]
    return split
def split_or(condition):
    split = []
    if 'or' in condition:
        split = condition.split(' or ')
        split = [word.strip() for word in split]
    return split

def add_to_KB(item):
    if 'is' in item:
        key, val = item.split('is')
        knowledge_base[key.strip()] = val.strip()
    else:
        knowledge_base[item] = True
    return knowledge_base


rules = read_rules("rules.txt")
knowledge_base = read_facts("facts.txt")
goal = "citrus_fruit"
def back_chaining(knowledge_base, goal) -> bool:
    for key, val in rules.items():
        if val == goal:
            or_split = split_or(key)
            and_split = split_and(key)
            if len(or_split) > 1 and len(and_split) <= 1:
                found = False
                for word in or_split:
                    print(word)
                    print("YAYAYAYAYAY")
                    if word.split()[0] in knowledge_base:
                        knowledge_base = add_to_KB(goal)
                        found = True
                        return True
                if found == False:
                    for word in or_split:
                        if back_chaining(knowledge_base, word):
                            knowledge_base = add_to_KB(goal)
                            return True
            elif len(or_split) <= 1 and len(and_split) > 1:
                key_copy = key.replace('is', '==')
                for word in and_split:
                    if word.split()[0] in knowledge_base:
                        key_copy = key_copy.replace(word.split()[0],str(knowledge_base[word.split()[0]]))
                    elif word.split()[0] not in knowledge_base:
                        if back_chaining(knowledge_base, word):
                            knowledge_base = add_to_KB(word)
                            key_copy = key_copy.replace(word.split()[0],str(knowledge_base[word.split()[0]]))
                        else:
                            return False
                print(key_copy)
                for item in key_copy.split():
                    if isinstance(item, str):
                        key_copy = key_copy.replace(item, "'item'")

                if eval(key_copy):
                    knowledge_base = add_to_KB(val)
                    return True
                else:
                    return False
        else:
            continue





            # if key in knowledge_base:
            #     return True
            # else:
            #     for
            #     back_chaining(knowledge_base, key)


    # for rule in rules:
    #     and_words = split_and(rule)
    #     or_words = split_or(rule)
    #     if len(and_words) > 0:
    #         pass

if back_chaining(knowledge_base, goal):
    print("WOOOOW")
else:
    print("oh nOOOOOOO")


            # for word in and_words:
            #     if word in knowledge_base:
            #         if eval(rule.replace(word,knowledge_base[word])):
            #             print("yes")
            #             if 'is' in rules[rule]:
            #                 key, val = rules[rule].split('is')
            #                 knowledge_base[key.strip()] = val.strip()
            #             return True
            #     else:



# rule1 = "IF diameter > 2 AND diameter < 10 THEN size is medium"
# _, rule1 = rule1.split("IF")
# condition,conclusion = rule1.split("THEN")
#
# and_words =[]
# or_words = []

# if 'AND' in condition:
#     and_words = condition.split('AND')
# if 'OR' in condition:
#     or_words = condition.split('OR')
# print(and_words)
#
# for word in and_words:
#     word.strip()
#     rules = word.split()
#     if rules[0] in knowledge_base:
#         print("YAY")
#     else:
#         print("NAY")





# for key, val in knowledge_base.items():
#     for word in and_words:
#
#         print(word.split(' '))




# print(condition.replace('diameter',knowledge_base['diameter']))
# print(eval(condition.replace('diameter',knowledge_base['diameter']).replace('AND','and')))
#
# if eval(condition.replace('diameter',knowledge_base['diameter']).replace('AND','and')):
#     print("yes")
#     if 'is' in conclusion:
#         key, val = conclusion.split('is')
#         knowledge_base[key.strip()] = val.strip()
# print(knowledge_base)

#------------------------------------------------
