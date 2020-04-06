###################
#  pyCorona       #
#  Allan Forbes   #
###################

Pulling data from : https://thevirustracker.com/api

Then building data classes and storing appropriate Dicts & Lists.

Types are usually numbers though date strings have been converted on the Timeline lists for sorting.

The API offers full timeline data, but we're iteratively pulling this anyway.

Classes :
	World
		VARS
			totalCases
			totalRecovered
			totalUnresolved
			totalDeaths
			newDailyCases
			newDailyDeaths
			totalActive
			totalSerious
			totalCountriesAffected
		METHODS
			tostring() - Returns data with headers
			tocommas() - Returns raw data.
	Country
		VARS
			code
			name
			totalCases
			totalRecovered
			totalUnresolved
			totalDeaths
			newDailyCases
			newDailyDeaths
			totalActive
			totalSerious
			timeLine - List of Timeline Objects
		METHODS
			tostring() - Full Country Printout including timeline
			tocommas() - Country Stats to commas
			timelinestring() - Timeline iterated and printed with headers
			timelinecommas() - Timeline iterated raw csv
	Timeline
		VARS
			tlDate
			newDayCases
			newDayDeaths
			totalCases
			totalRecoveries
			totalDeaths
		METHODS
			tostring() - Single Timeline entry printout with headers
			tocommas() - Single Timeline entry printout no headers

This framework does not print, it simply stores.  You can quickly demo the data via :
print(countryStats["USA"].tostring())
