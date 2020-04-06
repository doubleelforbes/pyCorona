# Data Container class for a Country's Coronavirus Timeline datapoint


class Timeline:
    def __init__(self, tlDate, ndCases, ndDeaths, totCases, totRecovs, totDeaths):
        self.tlDate = tlDate
        self.newDayCases = ndCases
        self.newDayDeaths = ndDeaths
        self.totalCases = totCases
        self.totalRecoveries = totRecovs
        self.totalDeaths = totDeaths
        

    def tostring(self):
        retstr = "Date, Daily Cases, Daily Deaths, Total Cases, Total Recoveries, Total Deaths\r\n"
        retstr += self.tocommas()
        return retstr
               


    def tocommas(self):
        return(self.tlDate.strftime("%Y-%m-%d") + "," + str(self.newDayCases) + "," + str(self.newDayDeaths) + "," + str(self.totalCases)
               + "," + str(self.totalRecoveries) + "," + str(self.totalDeaths) + "\r\n")
