import json
import emoji
from pprint import pprint
from collections import Counter
from urllib.parse import urlparse

## Load file
#load in json'
print("loading in")
with open('merged_filebig.json') as f:
    data = json.load(f)

print("json loaded")
#Get rid of duplicate Transactions
z = [];

print("appending data")
for x in range(len(data)):
    if 'error' not in data[x]:
        z.append(data[x]['data']);

noDupList = [];
for x in range(len(z)):
    for y in range(len(z[x])):
        noDupList.append(z[x][y])
        
print("now analyze")
## Remove duplicate transactions
print("removing duplicates")
noDupList = [];
for x in range(len(z)):
    
    for y in range(len(z[x])):
        if z[x][y] not in noDupList:
            noDupList.append(z[x][y])
        else:
            print((x,"duplicate"))

#  Scripts for Profile Pictures
#######################################################################
#Get all of the profile picture hosts
picList = [];
noPicList = [];
u = 0;
for x in range(len(noDupList)):
    if 'picture' in noDupList[x]['transactions'][0]['target']:
        picList.append(noDupList[x]['transactions'][0]['target']['picture'])
    else:
        if 'redeemable_target' not in noDupList[x]['transactions'][0]['target']:
            noPicList.append(noDupList[x]['transactions'][0]['target'])
        else:
            noPicList.append(noDupList[x]['transactions'][0]['target']['redeemable_target']['type'])
        
    if 'picture' in noDupList[x]["actor"]:
        picList.append(noDupList[x]["actor"]['picture']);
    else:
        if 'redeemable_target' not in noDupList[x]["actor"]:
            noPicList.append(noDupList[x]["actor"])
        else:
            noPicList.append(noDupList[x]["actor"]['redeemable_target']['type'])
#Parse out information we don't care about
for x in range(len(picList)):
	picList[x] = urlparse(picList[x]).netloc

for x in noPicList:
    picList.append(x);
#count each picture host
picHostCount = Counter(picList)


print(picHostCount)
#####################################################################
#count how many payments and how many charges among transactions

paymentsVsTransactions = [];

for x in range(len(noDupList)):
    paymentsVsTransactions.append(noDupList[x]['type'])

pVTCount = Counter(paymentsVsTransactions)

print(pVTCount)
####################################################################
#find most popular actors
actors = [];
for x in range(len(noDupList)):
    actors.append(noDupList[x]['actor']['username'])

rankedActors = Counter(actors).most_common(100)
print(rankedActors)
####################################################################
#find most popular targets
targets = [];
tu = 0;
for x in range(len(noDupList)):
    if 'username'in noDupList[x]['transactions'][0]['target']:
        targets.append(noDupList[x]['transactions'][0]['target']['username'])
    else:
        if 'redeemable_target' not in noDupList[x]['transactions'][0]['target']:
            #print(noDupList[x]['transactions'][0]['target'])
            targets.append(noDupList[x]['transactions'][0]['target'])
        else:
            #print(noDupList[x]['transactions'][0]['target']['redeemable_target'])
            targets.append(noDupList[x]['transactions'][0]['target']['redeemable_target']['display_name'])
        

rankedTargets = Counter(targets).most_common(100)
print(rankedTargets)
####################################################################
###When accounts were created
accountCreationDates = []
for x in range(len(noDupList)):
    if 'date_created' in noDupList[x]['transactions'][0]['target']:
        accountCreationDates.append(noDupList[x]['transactions'][0]['target']['date_created'][0:7])
    else:
        accountCreationDates.append('No date Provided')
    accountCreationDates.append(noDupList[x]['actor']['date_created'][0:7])

countedDates = Counter(accountCreationDates)
####################################################################
#targetIsBusiness
targetIsBusiness = []

for x in range(len(noDupList)):
    if 'is_business' in noDupList[x]['transactions'][0]['target']:
        targetIsBusiness.append(noDupList[x]['transactions'][0]['target']['is_business'])
    else:
        targetIsBusiness.append(False)

targetBusinessCount = Counter(targetIsBusiness)
print(targetBusinessCount.most_common(10))
#####################################################################
#actorIsBusiness
actorIsBusiness = []

for x in range(len(noDupList)):
    actorIsBusiness.append(noDupList[x]['actor']['is_business'])

actorBusinessCount = Counter(actorIsBusiness)

print(actorBusinessCount.most_common(10))
###################################################################
#find most popular emojis overall
allMessages = []
for x in range(len(noDupList)):
    allMessages.append(noDupList[x]['message'])

popularEmojis = []
for x in allMessages:
    separate = list(x)
    for character in separate:
        if character in emoji.UNICODE_EMOJI:
            popularEmojis.append(character);

topHundredEmojis = Counter(popularEmojis).most_common(100)        

#find most popular emojis on different days of week
messagesOnDate = []
for x in range(len(noDupList)):
    if 'updated_time' in noDupList[x]:
        
        if noDupList[x]['updated_time'][0:10] == '2018-11-06':
            messagesOnDate.append(noDupList[x]['message'])
    
####################################################################
#MAYBE? Find most popular words in message
popularWords = []
for x in allMessages:
    split = x.split(" ")
    for word in split:
        popularWords.append(word)

topHundredWords = Counter(popularWords).most_common(100)
#####################################################################
#Information for Sunday
messagesOnSunday = []
for x in range(len(noDupList)):
    if 'updated_time' in noDupList[x]:
        
        if noDupList[x]['updated_time'][0:10] == '2018-11-18':
            messagesOnSunday.append(noDupList[x]['message'])

#Top words on Sunday
popularWordsSun = []
for x in messagesOnSunday:
    split = x.split(" ")
    for word in split:
        popularWordsSun.append(word)

topHundredWordsSun = Counter(popularWordsSun).most_common(100)

#top Emojis on Sunday
popularEmojisSun = []
for x in messagesOnSunday:
    separate = list(x)
    for character in separate:
        if character in emoji.UNICODE_EMOJI:
            popularEmojisSun.append(character);

topHundredEmojisSun = Counter(popularEmojisSun).most_common(100)
####################################################################

#Information for Monday
messagesOnMonday = []
for x in range(len(noDupList)):
    if 'updated_time' in noDupList[x]:
        
        if noDupList[x]['updated_time'][0:10] == '2018-11-12':
            messagesOnMonday.append(noDupList[x]['message'])

#Top words on Monday
popularWordsMon = []
for x in messagesOnMonday:
    split = x.split(" ")
    for word in split:
        popularWordsMon.append(word)

topHundredWordsMon = Counter(popularWordsMon).most_common(100)
#top Emojis on Monday
popularEmojisMon = []
for x in messagesOnMonday:
    separate = list(x)
    for character in separate:
        if character in emoji.UNICODE_EMOJI:
            popularEmojisMon.append(character);

topHundredEmojisMon = Counter(popularEmojisMon).most_common(100)
###################################################################       
#Information for Tuesday
messagesOnTuesday = []
for x in range(len(noDupList)):
    if 'updated_time' in noDupList[x]:
        
        if noDupList[x]['updated_time'][0:10] == '2018-11-13':
            messagesOnTuesday.append(noDupList[x]['message'])

#Top words on Tuesday
popularWordsTu = []
for x in messagesOnTuesday:
    split = x.split(" ")
    for word in split:
        popularWordsTu.append(word)

topHundredWordsTu = Counter(popularWordsTu).most_common(100)
#top Emojis on Tuesday
popularEmojisTu = []
for x in messagesOnTuesday:
    separate = list(x)
    for character in separate:
        if character in emoji.UNICODE_EMOJI:
            popularEmojisTu.append(character);

topHundredEmojisTu = Counter(popularEmojisTu).most_common(100)
##################################################################
#Information for Wednesday
messagesOnWednesday = []
for x in range(len(noDupList)):
    if 'updated_time' in noDupList[x]:
        
        if noDupList[x]['updated_time'][0:10] == '2018-11-14':
            messagesOnWednesday.append(noDupList[x]['message'])

#Top words on Wed
popularWordsWed = []
for x in messagesOnWednesday:
    split = x.split(" ")
    for word in split:
        popularWordsWed.append(word)

topHundredWordsWed = Counter(popularWordsWed).most_common(100)
#top Emojis on Wed
popularEmojisWed = []
for x in messagesOnWednesday:
    separate = list(x)
    for character in separate:
        if character in emoji.UNICODE_EMOJI:
            popularEmojisWed.append(character);

topHundredEmojisWed = Counter(popularEmojisWed).most_common(100)
##################################################################
#Information for Thursday
messagesOnThursday = []
for x in range(len(noDupList)):
    if 'updated_time' in noDupList[x]:
        
        if noDupList[x]['updated_time'][0:10] == '2018-11-15':
            messagesOnThursday.append(noDupList[x]['message'])

#Top words on Thur
popularWordsThur = []
for x in messagesOnThursday:
    split = x.split(" ")
    for word in split:
        popularWordsThur.append(word)

topHundredWordsThur = Counter(popularWordsThur).most_common(100)

#top Emojis on Thur
popularEmojisThur = []
for x in messagesOnThursday:
    separate = list(x)
    for character in separate:
        if character in emoji.UNICODE_EMOJI:
            popularEmojisThur.append(character);

topHundredEmojisThur = Counter(popularEmojisThur).most_common(100)

##################################################################
#Information for Friday
messagesOnFriday = []
for x in range(len(noDupList)):
    if 'updated_time' in noDupList[x]:
        
        if noDupList[x]['updated_time'][0:10] == '2018-11-16':
            messagesOnFriday.append(noDupList[x]['message'])

#Top words on Friday
popularWordsFri = []
for x in messagesOnFriday:
    split = x.split(" ")
    for word in split:
        popularWordsFri.append(word)

topHundredWordsFri = Counter(popularWordsFri).most_common(100)

#top Emojis on Friday
popularEmojisFri = []
for x in messagesOnFriday:
    separate = list(x)
    for character in separate:
        if character in emoji.UNICODE_EMOJI:
            popularEmojisFri.append(character);

topHundredEmojisFri = Counter(popularEmojisFri).most_common(100)

##################################################################
#Information for Saturday
messagesOnSaturday = []
for x in range(len(noDupList)):
    if 'updated_time' in noDupList[x]:
        
        if noDupList[x]['updated_time'][0:10] == '2018-11-17':
            messagesOnSaturday.append(noDupList[x]['message'])

#Top words on Saturday
popularWordsSat = []
for x in messagesOnSaturday:
    split = x.split(" ")
    for word in split:
        popularWordsSat.append(word)

topHundredWordsSat = Counter(popularWordsSat).most_common(100)

#top Emojis on Monday
popularEmojisSat = []
for x in messagesOnSaturday:
    separate = list(x)
    for character in separate:
        if character in emoji.UNICODE_EMOJI:
            popularEmojisSat.append(character);

topHundredEmojisSat = Counter(popularEmojisSat).most_common(100)
## End Analysis Script