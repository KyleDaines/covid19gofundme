from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

def indexView(request):
# this view will pull up the submit html template
        return render(request, "index.html", {})

def resultsView(request):
# this view receives parameters from the submit html template and calls the API in azure
# this contains API code for Python and Python3 
    # If you are using Python 3+, import urllib instead of urllib2
    #import urllib2.request
    import urllib
    import json 

    # assign all the parameters to variables which you put in the API like the commented code
    # or just put them in directly like I did farther down
    
    # age = str(request.POST['age'])
    # sex = str(request.POST['sex'])
    # bmi = str(request.POST['bmi'])
    # children = str(request.POST['children'])
    # smoker = str(request.POST['smoker'])
    # region = str(request.POST['region'])

    if 'auto_fb_post_mode' in request.POST:
        auto_fb_post_mode = "1"
    else:
        auto_fb_post_mode = "0"
    
    if 'has_beneficiary' in request.POST:
        has_beneficiary = "1"
    else:
        has_beneficiary = "0"

    if 'visible_in_search' in request.POST:
        visible_in_search = "1"
    else:
        visible_in_search = "0"

    if 'is_charity' in request.POST:
        is_charity = "1"
    else:
        is_charity = "0"
    
    if 'charity_valid' in request.POST:
        charity_valid = "1"
    else:
        charity_valid = "0"

    goal_cbrt = float(request.POST['goal_cbrt'])**1/3
    
    # formatting the data into a data object for the API call
    data =  {

            "Inputs": {

                    "input1":
                    {
                        "ColumnNames": ["Column 0", "auto_fb_post_mode", "category_id", "goal", "donators", "title", "description", "has_beneficiary", "visible_in_search", "launch_date", "location_country", "location_zip", "is_charity", "charity_valid", "average_amount", "goal_sqrt", "goal_cbrt", "goal_log2", "goal_ln", "goal_log10"],
                        "Values": [ [ "1", auto_fb_post_mode, request.POST['category_id'], "1000", "50", request.POST['title'], request.POST['description'], has_beneficiary, visible_in_search, request.POST['launch_date'], request.POST['location_country'], request.POST['location_zip'], is_charity, charity_valid, "0", "0", goal_cbrt, "1", "1", "1" ],  ]
                    },        },
                "GlobalParameters": {
    }
        }

    # the API call
    body = str.encode(json.dumps(data))
    url = 'https://ussouthcentral.services.azureml.net/workspaces/6ed52524903b4c4ab795ab5a4ca3e234/services/7549dc1a033543f182c8534a048b8156/execute?api-version=2.0&details=true'
    api_key = 'C8i+kfd7/pXzpwihe9CuqVQiDPgj1vpcWcHs+QXtZy4mE/oDUe9rHgfovdYzH2wEJn2z3rAfxJFY1OlbmWeryg==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    # If you are using Python 3+, replace urllib2 with urllib.request
    #req = urllib2.Request(url, body, headers)
    req = urllib.request.Request(url, body, headers) 

    # python3 uses urllib while python uses urllib2
    #response = urllib2.request.urlopen(req)
    response = urllib.request.urlopen(req)

    # this formats the results 
    result = response.read()
    result = json.loads(result) # turns bits into json object
    result = result["Results"]["output1"]["value"]["Values"][0][17]
    # azure send the response as a weird result object. It would be wise to postman to find the 
    # path to the response var value

    data =  {

            "Inputs": {

                    "input1":
                    {
                        "ColumnNames": ["Column 0", "auto_fb_post_mode", "category_id", "goal", "donators", "title", "description", "has_beneficiary", "visible_in_search", "launch_date", "location_country", "location_zip", "is_charity", "charity_valid", "average_amount", "goal_sqrt", "goal_cbrt", "goal_log2", "goal_ln", "goal_log10"],
                        "Values": [ [ "1", auto_fb_post_mode, request.POST['category_id'], "1000", "50", request.POST['title'], request.POST['description'], has_beneficiary, visible_in_search, request.POST['launch_date'], request.POST['location_country'], request.POST['location_zip'], is_charity, charity_valid, "0", "0", goal_cbrt, "1", "1", "1" ],  ]
                    },        },
                "GlobalParameters": {
                    "Minimum number of samples per leaf node": "1",
    }
        }

    # the API call
    body = str.encode(json.dumps(data))
    url = 'https://ussouthcentral.services.azureml.net/workspaces/7ad529b85401496aad6a69e0bc123bf3/services/2660b5d143eb4dcbbfcb1255dbe68f61/execute?api-version=2.0&details=true'
    api_key = 'KhGbbA7Be3kXwXanWUkieujOpKWQr+q9M/o3ZfyhWlpDElsCwQy1CXJ2BENHBdrIFE1mK/4wfKFg4UsLu0kcww==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    # If you are using Python 3+, replace urllib2 with urllib.request
    #req = urllib2.Request(url, body, headers)
    req = urllib.request.Request(url, body, headers) 

    # python3 uses urllib while python uses urllib2
    #response = urllib2.request.urlopen(req)
    response = urllib.request.urlopen(req)

    # this formats the results 
    result2 = response.read()
    result2 = json.loads(result2) # turns bits into json object
    result2 = result2["Results"]["output1"]["value"]["Values"][0][17]

    return render(request, "results.html", {"result": round(float(result), 2), "result2": int(round(float(result2), 0))}) # this path assumes that this file is in the root directory in a folder named templates
    # the third parameter sends the result (the response variable value) to the template to be rendered