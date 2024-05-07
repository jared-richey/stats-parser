from django.http import HttpResponse

# Create your views here.
def home(request):
    soccer_path = "<a href = /soccer/>Check soccer stats here</a href>"
    basketball_path = "<a href = /basketball/>Check basketball stats here</a href>"
    baseball_path = "<a href = /baseball/>Check baseball stats here</a href>"
    nba_path = "<a href = /nba/>Check nba stats here</a href>"
    footer_url = "https://a.espncdn.com/redesign/assets/img/logos/espn-404@2x.png"
    return HttpResponse(soccer_path + "<p></p>" + basketball_path + "<p></p>" + baseball_path + "<p></p>" + nba_path + "<p></p>" + "<div><img src =" + footer_url + "></div>")

def soccer(request):
    with open('./tools/soccer_stats.txt','r') as file_object:
        data = file_object.read()
    
    html_content = ''
    for line in data:
        line_content = line.strip()  # Remove leading/trailing whitespace
        if line_content:  # Only add non-empty lines
            html_content += f"<p>{line_content}</p>\n"

    return HttpResponse(data)

def basketball(request):
    with open('./tools/basketball_stats.txt','r') as file_object:
        data = file_object.read()
    
    html_content = ''
    for line in data:
        line_content = line.strip()  # Remove leading/trailing whitespace
        if line_content:  # Only add non-empty lines
            html_content += f"<p>{line_content}</p>\n"

    return HttpResponse(data)

def baseball(request):
    with open('./tools/baseball_stats.txt','r') as file_object:
        data = file_object.read()
    
    html_content = ''
    for line in data:
        line_content = line.strip()  # Remove leading/trailing whitespace
        if line_content:  # Only add non-empty lines
            html_content += f"<p>{line_content}</p>\n"
        
    return HttpResponse(data)

def nba(request):
    with open('./tools/nba_stats.txt','r') as file_object:
        data = file_object.read()
    
    html_content = ''
    for line in data:
        line_content = line.strip()  # Remove leading/trailing whitespace
        if line_content:  # Only add non-empty lines
            html_content += f"<p>{line_content}</p>\n"

    return HttpResponse(data)