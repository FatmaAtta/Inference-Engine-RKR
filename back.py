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
            rule[condition.strip()] = conclusion.strip()
    print(rule)
read_rules("rules.txt")

knowledge_base = read_facts("facts.txt")


# rule1 = "IF diameter > 2 AND diameter < 10 THEN size is medium"
# _, rule1 = rule1.split("IF")
# condition,conclusion = rule1.split("THEN")

and_words =[]
or_words = []

if 'AND' in condition:
    and_words = condition.split('AND')
if 'OR' in condition:
    or_words = condition.split('OR')
print(and_words)

for word in and_words:
    word.strip()
    rules = word.split()
    if rules[0] in knowledge_base:
        print("YAY")
    else:
        print("NAY")






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
