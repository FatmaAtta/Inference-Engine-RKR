# def read_rules(file):
#     rules=[]
#     rule = {}
#     file = open(file,'r')
#     for line in file:
#         if "IF" in line and "THEN" in line:
#             _, item = line.split("IF")
#             condition, conclusion = item.split("THEN")
#             rule[condition.strip()] = conclusion.strip()
#             rules.append(rule)
#             # print(rules)
#     for rule in rules:
#         for key, val in rule.items():
#             tokenize(key, val)
# rules=[]
# def tokenize(condition, conclusion):
#     rule = {}
#     inner_rule = {}
#     inner_conc = {}
#     if 'is' in conclusion:
#         key, val = conclusion.split('is')
#         inner_conc[key.strip()] = val.strip()
#     if 'OR' in condition:
#         conditions = condition.split('OR')
#         for condition in conditions:
#             tokenize(condition, conclusion)
#     elif 'AND' in condition:
#         conditions = condition.split('AND')
#         for condition in conditions:
#
#
#             if 'is' in condition:
#                 key, val = condition.split('is')
#                 inner_rule[key.strip()] = val.strip()
#
#
#
#             rule[inner_rule] = inner_conc
#             rules.append(rule)
#
# print(rules)
#
#
#
# def read_facts(file):
#     facts = []
#     file = open(file,'r')
#     for line in file:
#         facts.append(line.strip().replace('skin_smell','perfumed'))
#     processed_facts = []
#     processed_fact = {}
#     for fact in facts:
#         if '=' in fact:
#             key, value = fact.split('=')
#             processed_fact[key.strip()] = value.strip()
#             processed_facts.append(processed_fact)
#             processed_fact = {}
#         elif 'is' in fact:
#             key, val = fact.split('is')
#             processed_fact[key.strip()] = val.strip()
#             processed_facts.append(processed_fact)
#             processed_fact = {}
#         elif '=' not in fact:
#             processed_fact[fact.strip()] = True
#             processed_facts.append(processed_fact)
#             processed_fact = {}
#
#     # print(processed_facts)
#
# def BackPropagation(rules,facts,goal):
#     pass
#
# read_rules("rules.txt")
# read_facts("facts.txt")
# goal = "citrus_fruit"
# print(rules)
#
#
#
# #         rule = line.split('\n')
# #         rules.append(rule)
# #     rule_dict = []
# #     for rule in rules:
# #         item = {}
# #         key, value = rule.split('THEN')
# #         item[key[3:]] = value
# #         print(key, value)
# #
# #     return rules
# # read_rules("rules.txt")



print(eval('"7" > 3'))