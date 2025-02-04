# Simple To-Do List CLI
import sys

tasks = ['Complete GitHub project', 'Write Python script', 'Fix bug in code', 'Task 50: Complete GitHub project', 'Task 49: Write Python script', 'Task 48: Task 50: Complete GitHub project', 'Task 47: Task 48: Task 50: Complete GitHub project', 'Task 46: Write Python script', 'Task 45: Task 48: Task 50: Complete GitHub project', 'Task 44: Fix bug in code', 'Task 43: Fix bug in code', 'Task 42: Task 44: Fix bug in code', 'Task 41: Task 49: Write Python script', 'Task 40: Complete GitHub project', 'Task 39: Task 42: Task 44: Fix bug in code', 'Task 38: Task 49: Write Python script', 'Task 37: Task 41: Task 49: Write Python script', 'Task 36: Task 44: Fix bug in code', 'Task 35: Task 50: Complete GitHub project', 'Task 34: Task 50: Complete GitHub project', 'Task 33: Task 41: Task 49: Write Python script', 'Task 32: Task 50: Complete GitHub project', 'Task 31: Fix bug in code', 'Task 30: Task 49: Write Python script', 'Task 29: Task 45: Task 48: Task 50: Complete GitHub project', 'Task 28: Task 33: Task 41: Task 49: Write Python script', 'Task 27: Task 34: Task 50: Complete GitHub project', 'Task 26: Task 27: Task 34: Task 50: Complete GitHub project', 'Task 25: Task 30: Task 49: Write Python script', 'Task 24: Task 50: Complete GitHub project', 'Task 23: Complete GitHub project']

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
