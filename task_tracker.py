import json

def list_task(data_list):
    print("\n---- Task Tracker List ----")    
    counter = 0
    for key, value in data.items():
        counter += 1
        print(f"{counter}. " + key + " : " + value)

def add_task(data_list):
    while True:
        key_task = input("What task will you list? ").strip()
        if key_task in data_list.keys():
            print("Task is already in the list.")
        else:
            break

    while True:
        try:
            value_task = int(input("(1)In Progress, (2)Done, or (3)Pending?: "))
        except ValueError:
            print("Invalid Input! Please enter a number.")
            continue

        if value_task not in [1,2,3]:
            print("Invalid Input! Please input a number from the selection.")
        else:
            if value_task == 1:
                value_task = "In Progress"
            elif value_task == 2:
                value_task = "Done"
            else:
                value_task = "Pending"
            break

    data_list[key_task] = value_task

    return data_list

def update_task(data_list, choice):
    data_keys = list(data_list.keys())
    if choice < 1 or choice > len(data_keys):
        print("Invalid Input! Selection is out of range.")
        return False
    
    selected_key = data_keys[choice - 1]

    while True:
        try:
            value_task = int(input("(1)In Progress, (2)Done, or (3)Pending?: "))
        except ValueError:
            print("Invalid Input! Input a number.")
            continue

        if value_task == 1:
            value_task = "In Progress"
        elif value_task == 2:
            value_task = "Done"
        else:
            value_task = "Pending"

        data_list[selected_key] = value_task
        break

    return data_list

def delete_task(data_list, choice):
    data_keys = list(data_list.keys())
    if choice < 1 or choice > len(data_keys):
        print("Invalid Input! Selection is out of range.")
        return False
        
    selected_key = data_keys[choice - 1]

    data_list.pop(selected_key, None)
    print(f"{selected_key} has been successfully deleted.")

    return data_list

try:
    with open("task.json", "r") as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    data = {}

print("""
Select Action:
1. List all Task.
2. Add Task.
3. Update Task.
4. Delete Task.
5. List all Done Task.
6. List all Pending Task.
7. List all In Progress Task.
""")

while True:
    try:
        selection = int(input("Choose an action(1-7): "))
    except ValueError:
        print("Input a number.")
        continue

    if selection == 1: #list task
        list_task(data)
        break

    elif selection == 2: #add task
        add_task(data)
        break

    elif selection == 3: #update task
        list_task(data)
        while True:
            try:
                choice = int(input("What task will you update?(Select number): "))
            except ValueError:
                print("Invalid Input! Enter a number.")
                continue

            if update_task(data, choice) == False:
                continue
    
            break
        break

    elif selection == 4:
        list_task(data)
        while True:
            try:
                choice = int(input("What task will you delete?(Select number): "))
            except ValueError:
                print("Invalid Input! Enter a number.")
                continue

            if delete_task(data, choice) == False:
                continue
    
            break
        break

    elif selection == 5:
        print("-All Done tasks-")
        for key, value in data.items():
            if value == "Done":
                print(key)
        break

    elif selection == 6:
        print("-All Pending tasks-")
        for key, value in data.items():
            if value == "Pending":
                print(key)
        break

    elif selection == 7:
        print("-All In Progress tasks-")
        for key, value in data.items():
            if value == "In Progress":
                print(key)
        break

    else:
        print("Please input a valid selection.")

with open("task.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("Done")   