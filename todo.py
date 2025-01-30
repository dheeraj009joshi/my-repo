# Simple To-Do List CLI
import sys

tasks = ['Complete GitHub project', 'Write Python script', 'Fix bug in code', 'Task 30-1: Write Python script', 'Task 30-2: Complete GitHub project', 'Task 30-3: Task 30-1: Write Python script', 'Task 30-4: Task 30-1: Write Python script', 'Task 29-1: Task 30-2: Complete GitHub project', 'Task 29-2: Task 30-2: Complete GitHub project', 'Task 29-3: Task 30-1: Write Python script', 'Task 29-4: Task 29-1: Task 30-2: Complete GitHub project', 'Task 29-5: Task 30-2: Complete GitHub project', 'Task 29-6: Write Python script', 'Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 28-3: Task 29-5: Task 30-2: Complete GitHub project']

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
