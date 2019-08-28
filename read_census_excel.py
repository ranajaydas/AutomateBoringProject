""" Takes a boring excel file containing census data and tabulates the totals """
import openpyxl
import pprint

print('Opening Census Population Data excel file...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
county_data = {}

for row in range(2, sheet.max_row+1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    county_data.setdefault(state, {})                                       # Creates a dict within dict
    county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})          # Make sure key for county exists
    county_data[state][county]['tracts'] += 1                               # Increment each unique tract
    county_data[state][county]['pop'] += int(pop)                           # Sum up the population for each county


# Create another Python program to store this data!
print('Writing results...')
with open('census2010.py', 'w') as result_file:                            # 'w' is for writing. Can also use 'a+' for appending and writing
    result_file.write('all_data = ' + pprint.pformat(county_data))
print('Done.\n')

# An example of how to access the data easily from census2010.py
import census2010
print('The population of Anchorage, AK was:', census2010.all_data['AK']['Anchorage']['pop'])
print('The population of Sweetwater, WY was:', census2010.all_data['WY']['Sweetwater']['pop'])

