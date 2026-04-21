'''
rate = 0.1
def calculate_interest(amount):
return amount*rate
print(calculate_interest(1000))
'''
# Refactor the above code to eliminate global variables by passing values as parameters or using configuration objects.
def calculate_interest(amount, rate):
    return amount * rate
# Example usage
interest_rate = 0.1
print(calculate_interest(1000, interest_rate)) 
print(calculate_interest(1000,0.5))


'''
score = 78
if score >= 90: 
print("Excellent") 
else:
if score >= 75:
print("Very Good") 
else: if score >= 60: 
print("Good") else:
print("Needs Improvement")
'''
# Simplify nested if–elif–else logic using guard clauses or mapping structures for readability and maintainability
def evaluate_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Very Good"
    elif score >= 60:
        return "Good"
    else:
        return "Needs Improvement"
# Example usage
score = 78
print(evaluate_score(78))
print(evaluate_score(95))
print(evaluate_score(67))


'''
f = open("data1.txt") 
print(f.read())
f.close()
f = open("data2.txt") 
print(f.read())
f.close() 
'''
'''# Apply DRY principles by refactoring repeated file open/read/close code into a reusable function with context managers
def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()'''


'''
users = ["admin", "guest", "editor", "viewer"]
name = input("Enter username: ")
found = False for u in users: 
if u == name:
found = True 
print("Access Granted" if found else "Access Denied")'''
# Replace inefficient linear searches with sets or dictionaries to achieve faster lookups
def check_access(username, users):
    user_set = set(users)  # Convert list to set for O(1) lookups
    if username in user_set:
        return "Access Granted"
    else:
        return "Access Denied"
# Example usage
users = ["admin", "guest", "editor", "viewer"]
username = input("Enter username: ")
print(check_access(username, users))

