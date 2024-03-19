#!/usr/bin/env python3

from pyquery import PyQuery as pq
import sys
import re

def bubbleSort(arr):
    n = len(arr)
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            pattern = r"\d+"
            firstMatch = re.search(pattern, arr[j])
            secondMatch = re.search(pattern, arr[j+1])

            if (firstMatch and secondMatch):
            # Extracting the matched pattern and converting it to an integer
                firstNumber = abs(int(firstMatch.group()))
                secondNumber = abs(int(secondMatch.group()))

            if firstNumber < secondNumber:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we 
            # can just exit the main loop.
            return

try:
    # Attempt to open and read from the file
    with open('soccer_lines.html','r') as file_object:
        body = file_object.read()

except FileNotFoundError:
    # Handle the case where the file doesn't exist
    print("ERROR: Input file does not exist.")
    sys.exit(1)
except PermissionError:
    # Handle the case where you don't have permission to read the file
    print("ERROR: Check input file permissions.")
    sys.exit(1)
except Exception as e:
    # Handle any other exceptions that might be raised
    print(f"An error occurred: {e}")
    sys.exit(1)

doc = pq(body)
tag = doc('.Card.gameModules')

for date in doc('.Card__Header.Card__Header--presby.SBCardHeader').items():
    today = date.text()

print("<!DOCTYPE html><html><head><title>DailyLines</title><style>")
print("body,h1,h5 {font-family: sans-serif}")
print("body, html {height: 100%}")
print("body, html {background-color: whitesmoke;}")
print("</style></head><body><div><p>")

print("<p><b>DAILY LINES FOR: " + str(today) + "</b></p>\n")

teams = []
odds = []

for team in \
    doc('.ScoreCell__TeamName.ScoreCell__TeamName--shortDisplayName.truncate.db').items():    
    teams.append(team.text())

i = 0
for odd in doc('.Odds__Message').items():
    trimmed_string = odd.text().split('\n', 1)[0]
    odds.append(trimmed_string)
    i += 1

if i >= 30:
    loops = 30
    print("<p><b>Top 30 Matches & Lines under 200</b></p>\n")
elif i < 30:
    loops = i
    print("<p><b>Top " + str(i) + " Matches & Lines under 200</b></p>\n")
else:
    print("<p><i>No teams to bet</i></p>\n")

odds_sorted = []
for i in range(0,loops):
    odds_sorted.append(odds[i])

bubbleSort(odds_sorted)

match = []
soccer_matches = []
for j in range(0,loops):
    match = [teams[j],teams[j+1]]
    soccer_matches.append(match)
    # Removing merged elements
    teams.remove(teams[j+1])

print("<table><tbody>")

for k in range(0,loops):
    pattern = r"\d+"
    match = re.search(pattern, odds_sorted[k])
    positive_ml = abs(int(match.group()))
    if positive_ml >= 200:
        print("<tr><td>" + str(odds_sorted[k]) + "</tr></td>")

print("<tr><td><b>----------MATCHES----------</b></td></tr>")

for list_item in soccer_matches:
    print("<tr><td>" + str(list_item[0]) + " vs. " + str(list_item[1]) \
          + "</tr></td>")

print("</tbody></table>\n")

print('</p></div><div><table><tr><td><img src = \
    "https://a.espncdn.com/redesign/assets/img/logos/espn-404@2x.png">')
print('</td></tr></table><p><a href = \
    "https://www.espn.com/soccer/scoreboard"> \
    ESPN Soccer Daily Lines </a>')
print("</p></div></body></html>")