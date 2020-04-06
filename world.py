# Data Container class for global Coronavirus stats


class World:
    def __init__(self, totCases, totRec, totUnr, totDeaths, ndCase, ndDeath, totAct, totSer, totCountry):
        self.totalCases = totCases
        self.totalRecovered = totRec
        self.totalUnresolved = totUnr
        self.totalDeaths = totDeaths
        self.newDailyCases = ndCase
        self.newDailyDeaths = ndDeath
        self.totalActive = totAct
        self.totalSerious = totSer
        self.totalCountriesAffected = totCountry


    def tostring(self):
        retstr = "Total Cases, Total Recovered, Total Unresolved, Total Dead, Daily Cases, Daily Dead,"
        retstr += " Total Active, Total Serious, Total Countries\r\n"
        retstr += self.tocommas()
        return retstr
               


    def tocommas(self):
        return(str(self.totalCases) + "," + str(self.totalRecovered) + "," + str(self.totalUnresolved) + "," +
               str(self.totalDeaths) + "," + str(self.newDailyCases) + "," + str(self.newDailyDeaths) + "," +
               str(self.totalActive) + "," + str(self.totalSerious) + "," + str(self.totalCountriesAffected) + "\r\n")
