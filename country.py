# Data Container class for a Country's current Coronavirus stats


class Country:
    def __init__(self, cCode, cName, totCases, totRec, totUnr, totDeaths, ndCase, ndDeath, totAct, totSer, tLine):
        self.code = cCode
        self.name = cName
        self.totalCases = totCases
        self.totalRecovered = totRec
        self.totalUnresolved = totUnr
        self.totalDeaths = totDeaths
        self.newDailyCases = ndCase
        self.newDailyDeaths = ndDeath
        self.totalActive = totAct
        self.totalSerious = totSer
        self.timeLine = tLine


    def tostring(self):
        retstr = "Code, Name, Total Cases, Total Recovered, Total Unresolved, Total Dead, Daily Cases, Daily Dead,"
        retstr += " Total Active, Total Serious\r\n"
        retstr += self.tocommas()
        retstr += "\r\nTime Line :\r\n"
        retstr += self.timelinestring()
        return retstr
               


    def tocommas(self):
        return(self.code + "," + self.name + "," + str(self.totalCases) + "," + str(self.totalRecovered) + "," +
               str(self.totalUnresolved) + "," + str(self.totalDeaths) + "," + str(self.newDailyCases) + "," +
               str(self.newDailyDeaths) + "," + str(self.totalActive) + "," + str(self.totalSerious) + "\r\n")


    def timelinestring(self):
        retstr = "Date, Daily Cases, Daily Deaths, Total Cases, Total Recoveries, Total Deaths\r\n"
        for t in self.timeLine:
            retstr += t.tocommas()
        return retstr
    
    def timelinecommas(self):
        retstr = ""
        for t in self.timeLine:
            retstr += t.tocommas()
        return retstr
