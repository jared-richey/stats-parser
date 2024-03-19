#!/usr/bin/env python3

from pyquery import PyQuery as pq
import sys

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
            if arr[j][4] < arr[j + 1][4]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we 
            # can just exit the main loop.
            return

def print_stats(array, chunk_size=5):

    teams = []
    n = len(array)
    if n%5==0:
        for i in range(0, len(array), chunk_size):
            # Extract the current chunk of 5 elements
            current_chunk = array[i:i + chunk_size]
            teams.append(current_chunk)
    else:
        print("Problem with array size; incomplete data")
        sys.exit(1)

    teams_to_bet = False
    print("<p><b>Teams over 70% & ML less than -400</b></p>\n")
    print("<table><tbody>")

    for team in teams:
        if str(team[4]) != "--":
            percentage_float = float(team[4].rstrip('%'))
            team[4] = percentage_float

    bubbleSort(teams)

    for team in teams:
        if str(team[3]) != "--":
            positive_ml = abs(int(team[3]))
            if (team[4] >= 70.0 and positive_ml <=400):
                teams_to_bet = True
                print("<tr><td>" + str(team[0]) + " " + str(team[2]) + " " \
                    + str(team[3]) + " " + str(team[4]) + "%</td></tr>")

    if not teams_to_bet:
        print("<tr><td><i>No teams to bet</i></td></tr>")

    print("</tbody></table>\n")

try:
    # Attempt to open and read from the file
    with open('basketball_lines.html','r') as file_object:
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
tag = doc('.margin-date')

for date in doc('.Table__Title.margin-subtitle').items():
    today = date.text()

print("<!DOCTYPE html><html><head><title>DailyLines</title><style>")
print("body,h1,h5 {font-family: sans-serif}")
print("body, html {height: 100%}")
print("body, html {background-color: whitesmoke;}")
print("</style></head><body><div><p>")

print("<p><b>DAILY LINES FOR: " + str(today) + "</b></p>\n")

stats = []
for td in doc('table tr td').items():
    stats.append(td.text())

print_stats(stats)

print('</p></div><div><table><tr><td><img src = \
    "https://a.espncdn.com/redesign/assets/img/logos/espn-404@2x.png">')
print('</td></tr></table><p><a href = \
    "https://www.espn.com/mens-college-basketball/lines"> \
    ESPN Mens College Basketball Daily Lines </a>')
print("</p></div></body></html>")