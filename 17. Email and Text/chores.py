#! python3

import json, math, random, smtplib, sys

volunteer_file = open('./volunteers.json')
volunteers = json.load(volunteer_file)
volunteer_file.close()

#identify chores done previously and remove current chores

def assignPreviousChoresAndRemoveCurrent(volunteer_data):
    volunteer_data["previous_chores"] = volunteer_data["chores"].copy()
    volunteer_data['chores'] = []
    return volunteer_data

volunteers = { k:assignPreviousChoresAndRemoveCurrent(v) for k,v in volunteers.items() }


chores = ['mop', 'vacuum', 'clean counters', 'dust', 'trash', 'organize', 'toilets', 'pull weeds', 'water plants']
chore_total = len(chores)

def assign(vol, chore):
    fair = False
    while fair != True:
        fair = True
        volunteer_name = random.choice(list(vol.keys()))
        #volunteer_name = volunteer[list(volunteer.keys()[0])]
        assigned_chores = vol[volunteer_name]['chores']
        if (len(assigned_chores) == math.ceil(chore_total/len(volunteers))) or (chore in vol[volunteer_name]['previous_chores']):
            fair=False
            continue
        else:
            vol[volunteer_name]['chores'].append(chore)
            
while chores != []:
    randomChore = random.choice(chores)
    assign(volunteers, randomChore)
    chores.remove(randomChore)
    
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(sys.argv[1], sys.argv[2])

for k in volunteers:
    email = volunteers[k]['email']
    vol_chores = volunteers[k]['chores']
    chore_string = ', '.join(vol_chores)

    body = "Subject: Weekly Chores\n\nHere are your assigned chores: %s" % (chore_string)
    
    print('Sending email %s...' % email)
    sendmailStatus = smtpObj.sendmail(sys.argv[1], email, body)
    
    if sendmailStatus != {}:
       print('There was a problem sending email to %s: %s' % (email, sendmailStatus))
        
smtpObj.quit()

volunteer_file = open('./volunteers.json', 'w')
json.dump(volunteers, volunteer_file)
volunteer_file.close

print(volunteers)