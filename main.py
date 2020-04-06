import country, timeline, world

import datetime, json, urllib.request, ssl
from datetime import datetime

globalAPIParams = "global=stats"
countryAPIParams = "countryTotals=ALL"
timelineAPIParams = "countryTimeline=" # Needs + "US" etc.

def getAPIdata(params):
    requrl = "https://api.thevirustracker.com/free-api?" + params
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context
    response = urllib.request.urlopen(requrl).read()
    data = response.decode('utf-8')
    jsondata = json.loads(data)
    return jsondata

# Makes the calls then instantiates and returns a tmpObject
def getGlobalStats():
    globaldata = getAPIdata(globalAPIParams)
    if(globaldata["stat"] == "ok"):
        globaldata = globaldata["results"][0]
        totCases = globaldata["total_cases"]
        totRec = globaldata["total_recovered"]
        totUnr = globaldata["total_unresolved"]
        totDeaths = globaldata["total_deaths"]
        ndCase = globaldata["total_new_cases_today"]
        ndDeath = globaldata["total_new_deaths_today"]
        totAct = globaldata["total_active_cases"]
        totSer = globaldata["total_serious_cases"]
        totCountry = globaldata["total_affected_countries"]
        tmpWorld = world.World(totCases, totRec, totUnr, totDeaths, ndCase, ndDeath, totAct, totSer, totCountry)
        return tmpWorld
    else:
        return "API ERROR! " + globaldata["stat"]

# Makes the call then instantiates a dict of countris
def getCountryStats():
    allCountryData = getAPIdata(countryAPIParams)["countryitems"][0]
    if(allCountryData["stat"] == "ok"): # Why the hell is "stat" buried beneath "countryitems" ?!?!?!
        tmpCountryDict = {}
        for key in allCountryData: # See what I mean?!?! Now I have to manually exclude stat!!!
            if(key != "stat"): # Then to boot, the key is a useless arbitrary number
                tmpData = allCountryData[key]
                # Now we are at country-level
                cCode = tmpData["code"]
                cName = tmpData["title"]
                totCases = tmpData["total_cases"]
                totRec = tmpData["total_recovered"]
                totUnr = tmpData["total_unresolved"]
                totDeaths = tmpData["total_deaths"]
                ndCase = tmpData["total_new_cases_today"]
                ndDeath = tmpData["total_new_deaths_today"]
                totAct = tmpData["total_active_cases"]
                totSer = tmpData["total_serious_cases"]
                # print("Fetching timeline data for : " + cCode)
                tLine = getTimelineStats(cCode) # Pass the country code for timeline
                tmpCountry = country.Country(cCode, cName, totCases, totRec, totUnr, totDeaths, ndCase, ndDeath, totAct, totSer, tLine)
                tmpCountryDict[cName] = tmpCountry # Now the key is country name
        return tmpCountryDict
    else:
        return "API ERROR! " + allCountryData["stat"]

def getTimelineStats(ccode):
    tmpTimelineList = []
    timelineData = getAPIdata(timelineAPIParams + ccode)["timelineitems"][0]
    if(timelineData["stat"] == "ok"):
        for key in timelineData:
            if(key != "stat"): # Same again with this stat BS! Why check for failure after specifying data key?!
                tmpData = timelineData[key] # Sticking with the date as key here, 1x stat per day.
                # Now we have a single timeline item.
                tlDate = datetime.strptime(key , '%m/%d/%y')
                ndCases = tmpData["new_daily_cases"]
                ndDeaths = tmpData["new_daily_deaths"]
                totCases = tmpData["total_cases"]
                totRecovs = tmpData["total_recoveries"]
                totDeaths = tmpData["total_deaths"]
                tmpTimeline = timeline.Timeline(tlDate, ndCases, ndDeaths, totCases, totRecovs, totDeaths)
                tmpTimelineList.append(tmpTimeline)
    return tmpTimelineList

# api calls
worldStats = getGlobalStats()
#if ("API ERROR! " in worldStats):
#    print(worldStats)
#else:
#    print("GLOBAL STATS \r\n")
#    print(worldStats.tostring())

countryStats = getCountryStats()

# Dict of Country Timeline Objects for each Country
# https://api.thevirustracker.com/free-api?countryTimeline=US

# Build Dict of Country Codes

# Let's not put too much time into this unless lockdown goes too far.
# You could easily sort by deaths / infection rates etc.
# This is a bunch of looping and > 100 API calls just to get this one rank field.
# Then call all countries to pull their rank as this field doesn't exist
# https://api.thevirustracker.com/free-api?countryTotal=US , GB, AF, etc.
