import boto3
from pyquery import PyQuery as pq
import datetime
import requests
import sys

def lambda_handler(event, context):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Lambda function executed at:", current_time)

def write_data_to_s3(bucket_name, file_key, data):
    """
    Write data to a file on S3

    :param bucket_name: Name of the S3 bucket
    :param file_key: Key (path) of the file in the bucket
    :param data: Data to write to the file
    """
    s3_client = boto3.client('s3')
    try:
        response = s3_client.put_object(Bucket=bucket_name, Key=file_key, Body=data, ContentType='text/html')
        print("Data written to S3 file successfully:", response)
    except Exception as e:
        print(f"Error writing data to S3 file: {e}")

def read_data_from_s3(bucket_name, file_key):
    """
    Read data from a file on S3

    :param bucket_name: Name of the S3 bucket
    :param file_key: Key (path) of the file in the bucket
    :return: Content of the file as a string
    """
    s3_client = boto3.client('s3')
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        file_content = response['Body'].read().decode('utf-8')
        return file_content
    except Exception as e:
        print(f"Error reading data from S3 file: {e}")
        return None

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
            if arr[j][2] < arr[j + 1][2]:
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
    print("<p><b>Teams with stats between -175 and -400</b></p>\n")
    print("<table><tbody>")

    bubbleSort(teams)

    string_results = []
    for team in teams:
        if str(team[2]) not in ["EVEN", "--"]:
            positive_ml = int(team[2])
            if (positive_ml <= -175 and positive_ml >= -400):
                teams_to_bet = True
                first_element = team[0]
                words = first_element.split()[:1]
                team_name = ' '.join(words)
                print("<tr><td>" + team_name + " " + str(team[2]) + "</td></tr>")
                #string_teams = "<table><tbody>" + "<tr><td>" + str(team[0]) + " " + str(team[2]) + "</td></tr>" + "</tbody></table>\n"
                string_teams = "<table><tbody>" + "<tr><td>" + team_name + " " + str(team[2]) + "</td></tr>" + "</tbody></table>\n"
                string_results.append(string_teams)

    if not teams_to_bet:
        print("<tr><td><i>No team stats</i></td></tr>")

    print("</tbody></table>\n")
    return(string_results)


#make HTTP request
url = 'https://www.espn.com/mlb/odds'
headers = {
    'Content-Type': 'text/html',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}

response = requests.get(url, headers=headers)

# S3 bucket and key where the file will be saved
bucket_name = 'mlb-stats-incoming'
file_key = 'baseball_stats.html' 

if response.status_code == 200:
    content = response.text

    # Write data to the file on S3
    write_data_to_s3(bucket_name, file_key, content)

else:
    print("Request failed")
    sys.exit(1)

file_content = read_data_from_s3(bucket_name, file_key)

doc = pq(file_content)
tag = doc('.page-container.cf')

string_header = """
<!DOCTYPE html><html><head><title>Daily Stats</title><style>
body,h1,h5 {font-family: sans-serif}
body, html {height: 100%}")
body, html {background-color: whitesmoke;}
</style></head><body><div><p>
<p><b>DAILY STATS FOR: </b></p>\n
"""
print("<!DOCTYPE html><html><head><title>Daily Stats</title><style>")
print("body,h1,h5 {font-family: sans-serif}")
print("body, html {height: 100%}")
print("body, html {background-color: whitesmoke;}")
print("</style></head><body><div><p>")
print("<p><b>DAILY STATS FOR: </b></p>\n")

# Get the current date and time
now = datetime.datetime.now()

# Extract the day, month, and year
day = now.day
month_name = now.strftime("%B")
year = now.year

# Alternatively, format the date as a string
#formatted_date = now.strftime("%m-%d-%Y")
formatted_date = f"{month_name} {day}, {year}"
print(f"<p><b>{month_name} {day} {year}</b></p>\n")

stats = []
for td in doc('div#topOdd').items():
    stats.append(td.text())

string_footer = """
</p></div><div><table><tr><td><img src = "https://a.espncdn.com/redesign/assets/img/logos/espn-404@2x.png">
</td></tr></table><p><a href = "https://www.espn.com/mlb/odds"> ESPN MLB Daily Stats </a>
</p></div></body></html>
"""

final_results = ' '.join(map(str, print_stats(stats)))

string_final = string_header + formatted_date + "<p><b>Teams with stats between -175 and -400</b></p>\n" + str(final_results) + string_footer

bucket_name = 'mlb-stats-outgoing'
file_key = 'index.html'
content = string_final
write_data_to_s3(bucket_name, file_key, content)
