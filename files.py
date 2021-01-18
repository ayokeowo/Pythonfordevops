file_path ='bookofdreams.txt'

with open('bookofdreams.txt','r') as f:
    data = f.read()
    #print(len(data))


with open('policy.txt', 'r') as po:
    policy = po.readlines()
    #print (type(policy))
    #print (policy)

#Policy is a JSON doc, readline is not efficient. Importing json module for proper processiong.
#pprint parses JSON format
import json
from pprint import pprint

with open('policy.txt', 'r') as po1:
    policy1 = json.load(po1)
    print (type(policy1))
    print (policy1,'\n')
    pprint(policy1)






