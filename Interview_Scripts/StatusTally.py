# The "Status Tally" Problem
# The Goal: Fetch a list of tasks from a placeholder API and count how many are "completed" vs "pending."

import requests as rq

url = "https://jsonplaceholder.typicode.com/todos"

response = rq.get(url)

if response.status_code == 200:
    data = response.json()
    # print(data)

    completed = 0
    pending = 0

    for item in data:
        if item["completed"] == True:
            completed+=1
        else:
            pending+=1
        
    print(f"Completed: {completed}")
    print(f"Pending: {pending}")
else:
    print("Failed to grab data")