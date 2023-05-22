import requests

steamID_64 = '76561197983130737'
steamID3 = '[U:1:22865009]'
numberOfLogs = 13

response = requests.get("http://logs.tf/api/v1/log?player=" + steamID_64 + "&limit=" + str(numberOfLogs) + "&offset=30")
logIDs = response.json()
#print(logIDs)

kills = 0; deaths = 0; dmg = 0; hr = 0

for i in range(numberOfLogs):
    currentLogId = logIDs['logs'][i]['id']
    specificLogResponse = requests.get("http://logs.tf/api/v1/log/" + str(currentLogId))
    specificLogJSON = specificLogResponse.json()
    kills += specificLogJSON['players'][steamID3]['kills']
    deaths += specificLogJSON['players'][steamID3]['deaths']
    dmg += specificLogJSON['players'][steamID3]['dmg']
    hr += specificLogJSON['players'][steamID3]['hr']

print("Avg. kills over " + str(numberOfLogs) + " maps: " + str(kills/numberOfLogs))
print("Avg. deaths over " + str(numberOfLogs) + " maps: " + str(deaths/numberOfLogs))
print("Avg. dmg over " + str(numberOfLogs) + " maps: " + str(dmg/numberOfLogs))
print("Avg. heals received over " + str(numberOfLogs) + " maps: " + str(hr/numberOfLogs))
