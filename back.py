def read_facts(file):
    facts = []
    file = open(file,'r')
    for line in file:
        facts.append(line.strip().replace('skin_smell','perfumed'))
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
    # print(processed_fact)
    return processed_fact

def read_rules(file):
    rules=[]
    rule = {}
    file = open(file,'r')
    for line in file:
        if "IF" in line and "THEN" in line:
            _, item = line.split("IF")
            condition, conclusion = item.split("THEN")
            rule[condition.strip().replace('AND','and').replace('OR','or')] = conclusion.strip()
    # print(rule)
    return rule

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
    print(f"***Adding {item} to KB***")
    if 'is' in item:
        key, val = item.split('is')
        knowledge_base[key.strip()] = val.strip()
    else:
        knowledge_base[item] = True
    print(f"***Current KB: {knowledge_base}***")
    return knowledge_base

rules = read_rules("rules.txt")
knowledge_base = read_facts("facts.txt")
goal = "citrus_fruit"

def back_chaining(knowledge_base, goal, level) -> bool:
    indentM = "    " * level
    indentR = "    " * (level+1)
    print(f"{indentM}Matching {goal}")
    i = 1
    for key, val in rules.items():
        if val == goal:
            print(f"{indentR}R{i}: IF {key} THEN {val}")
            or_split = split_or(key)
            and_split = split_and(key)
            if len(or_split) > 1 and len(and_split) <= 1:
                found = False
                for word in or_split:
                    # print(word)
                    # print("YAYAYAYAYAY")
                    if word.split()[0] in knowledge_base:
                        knowledge_base = add_to_KB(goal)
                        found = True
                        return True
                if found == False:
                    for word in or_split:
                        if back_chaining(knowledge_base, word, level+1):

                            print(f"{indentR}Return to R{i}")


                            knowledge_base = add_to_KB(goal)
                            return True
            elif len(or_split) <= 1 and len(and_split) > 1:
                key_copy = key.replace('is', '==')
                for word in and_split:
                    if word.split()[0] in knowledge_base:
                        key_copy = key_copy.replace(word.split()[0],str(knowledge_base[word.split()[0]]))
                    elif word.split()[0] not in knowledge_base:
                        if back_chaining(knowledge_base, word, level+1):

                            print(f"{indentR}Return to R{i}")

                            knowledge_base = add_to_KB(word)
                            key_copy = key_copy.replace(word.split()[0],str(knowledge_base[word.split()[0]]))
                        else:
                            return False
                # print(key_copy)
                for item in key_copy.split():
                    if isinstance(item, str):
                        key_copy = key_copy.replace(item, "'item'")

                if eval(key_copy):
                    knowledge_base = add_to_KB(val)
                    return True
                else:
                    return False
        # else:
        #     continue
        i += 1

if back_chaining(knowledge_base, goal, 0):
    print("GOAL REACHED :D")
else:
    print("Goal couldn't be reached :(")


