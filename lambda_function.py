import json
import os
from shutil import copyfile
#import precompute
import travelingmissionman


missions = """Bridi
Daran
Keshirou
Noranim,Petidu
Sibot
Porsharrah
Gayar
Jedandan
Sifilar,Saikamon"""

nullsec = "false"

def lambda_handler(missions, nullsec):
    #print("Received event: " + json.dumps(event, indent=2))
    #print("value1 = " + event['key1'])
    #print("value2 = " + event['key2'])
    #print("value3 = " + event['key3'])
    #return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')

    copyfile('systems.csv', '/tmp/systems.csv')
    copyfile('output.json', '/tmp/output.json')
    os.chdir('/tmp')
    print('Loading function')

    missions = """Bridi
    Daran
    Keshirou
    Noranim,Petidu
    Sibot
    Porsharrah
    Gayar
    Jedandan
    Sifilar,Saikamon"""

    nullsec = "false"

    f = open("missions.txt", "w")
    f.write(missions)
    f.close()
    travelingmissionman.main()


if __name__ == '__main__':
    # service.py executed as script
    # do something
    lambda_handler(missions, nullsec)
