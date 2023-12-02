import json
from datetime import datetime

def load_users_from_file():
    with open('User.json', 'r') as file:
        data = json.load(file)
        return data


def load_projects_from_file():
    with open('project.json', 'r') as file:
        data = json.load(file)
        return data

def validate_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False



def create_project(user_id):
    title = input("Enter the project title: ")
    details = input("Enter the project details: ")
    total_target = float(input("Enter the total target amount: "))
    start_time = input("Enter the start time (YYYY-MM-DD HH:MM:SS): ")
    while not validate_date(start_time):
        print("Invalid date format. Please try again.")
        start_time = input("Enter the start time (YYYY-MM-DD HH:MM:SS): ")
    end_time = input("Enter the end time (YYYY-MM-DD HH:MM:SS): ")
    while not validate_date(end_time):
        print("Invalid date format. Please try again.")
        end_time = input("Enter the end time (YYYY-MM-DD HH:MM:SS): ")

    project = {
        "title": title,
        "details": details,
        "total_target": total_target,
        "start_time": start_time,
        "end_time": end_time,
        "user_id": user_id
    }

    projects = load_projects_from_file()
    projects.append(project)

    with open('project.json', 'w') as file:
        json.dump(projects, file, indent=4)

    print("Project created successfully!")



def view_projects(user_id):
    projects = load_projects_from_file()
    user_projects = [project for project in projects if project["user_id"] == user_id]

    if len(user_projects) == 0:
        print("No projects found.")
    else:
        for i, project in enumerate(user_projects):
            print(f"Project {i+1}:")
            print(f"Title: {project['title']}")
            print(f"Details: {project['details']}")
            print(f"Total Target: {project['total_target']}")
            print(f"Start Time: {project['start_time']}")
            print(f"End Time: {project['end_time']}")
            print()

def view_all_projects():
    projects = load_projects_from_file()
    all_projects = [project for project in projects]

    if len(all_projects) == 0:
        print("No projects found.")
    else:
        for i, project in enumerate(all_projects):
            print(f"Project {i+1}:")
            print(f"Title: {project['title']}")
            print(f"Details: {project['details']}")
            print(f"Total Target: {project['total_target']}")
            print(f"Start Time: {project['start_time']}")
            print(f"End Time: {project['end_time']}")
            print()





def edit_project(user_id):
    projects = load_projects_from_file()
    user_projects = [project for project in projects if project["user_id"] == user_id]

    if len(user_projects) == 0:
        print("No projects found.")
        return

    view_projects(user_id)

    project_index = int(input("Enter the project number to edit: ")) - 1
    if project_index < 0 or project_index >= len(user_projects):
        print("Invalid project number.")
        return

    project = user_projects[project_index]

    print("Enter new project details (leave blank to keep existing value):")
    title = input(f"Title ({project['title']}): ")
    details = input(f"Details ({project['details']}): ")
    total_target = input(f"Total Target ({project['total_target']}): ")
    start_time = input(f"Start Time ({project['start_time']}): ")
    if validate_date(start_time):
        project['start_time'] = start_time
    end_time = input(f"End Time ({project['end_time']}): ")
    if validate_date(end_time):
        project['end_time'] = end_time

    if title:
        project['title'] = title
    if details:
        project['details'] = details
    if total_target:
        project['total_target'] = float(total_target)

    with open('project.json', 'w') as file:
        json.dump(projects, file, indent=4)

    print("Project edited successfully!")

# edit_project(1)

def delete_project(user_id):
    projects = load_projects_from_file()
    user_projects = [project for project in projects if project["user_id"] == user_id]

    if len(user_projects) == 0:
        print("No projects found.")
        return

    view_projects(user_id)

    project_index = int(input("Enter the project number to delete: ")) - 1
    if project_index < 0 or project_index >= len(user_projects):
        print("Invalid project number.")
        return

    del projects[projects.index(user_projects[project_index])]

    with open('project.json', 'w') as file:
        json.dump(projects, file, indent=4)

    print("Project deleted successfully!")


# delete_project(2)

def main_menu():
    while True:
        print("1. Create a project")
        print("2. View all projects")
        print("3. View User projects")
        print("4. Edit a project")
        print("5. Delete a project")
        print("6. Search projects by date")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_project(id)
        elif choice == "2":
            view_all_projects()
        elif choice == "3":
            view_projects()
        elif choice == "4":
            edit_project()
        elif choice == "5":
            delete_project()
        elif choice == "6":
            search_projects_by_date()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


