#list
counties = ["Arapahoe","Denver","Jefferson"]
#if statement with and and not in
if  "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")
#prints items in the list
for county in counties:
    print(county)
#prints items in the list with variable
for i in range(len(counties)):
    print(counties[i])

#dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#returns the keys of the dictionary
for county in counties_dict.keys():
    print(county)

#returns the value
for voters in counties_dict.values():
    print(voters)

#returns the value of the key
for county in counties_dict:
    print(counties_dict[county])

#return the value with get()
for county in counties_dict:
    print(counties_dict.get(county))

#get the key-value pair
#for key, value in dictionary_name.items():
    #print(key, value)
for county, voters in counties_dict.items():
    print(county, voters)

#skill drill
for county, voters in counties_dict.items():
    print(county + ' county has', str(voters) + ' registered voters')

#skill drill with f string
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver","registered_voters": 463353},
                {"county":"Jefferson","registered_voters":432438}]

#get each dictionary from a list of dictionaries
for county_dict in voting_data:
    print(county_dict)

#iterate with range(function)
for i in range(len(voting_data)):
    print(voting_data[i])

#get values form a list of dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#get number of registered voters
for county_dict in voting_data:
    print(county_dict['registered_voters'])

#get the county name
for county_dict in voting_data:
    print(county_dict['county'])