logs = [
    "[2026-4-12][Error]Error from Database", 
    "[2026-4-3][Database]Error from Database", 
    "[2026-4-2][Backend]Successful", 
    "[2026-4-21][Error]Error from Backend", 
    "[2026-4-16][Backend]Denied"
]

error = 0
db = 0
backend = 0

for log in logs:
    parts = log.split(']')
    print(parts)

    category = parts[1].replace('[','')

    if category == "Error":
        error+=1
    elif category == "Database":
        db+=1
    else:
        backend+=1

print(f"Errors: {error}")
print(f"Database: {db}")
print(f"Backend: {backend}")