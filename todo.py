# Simple To-Do List CLI
import sys

tasks = ['Complete GitHub project', 'Write Python script', 'Fix bug in code', 'Task 50: Complete GitHub project', 'Task 49: Write Python script', 'Task 48: Task 50: Complete GitHub project', 'Task 47: Task 48: Task 50: Complete GitHub project', 'Task 46: Write Python script', 'Task 45: Task 48: Task 50: Complete GitHub project', 'Task 44: Fix bug in code', 'Task 43: Fix bug in code', 'Task 42: Task 44: Fix bug in code', 'Task 41: Task 49: Write Python script']

def show_tasks():
    print("\nYour To-Do List:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")

def add_task(new_task):
    tasks.append(new_task)
    print(f"Added: {new_task}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        add_task(" ".join(sys.argv[1:]))
    show_tasks()
