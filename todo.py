# Simple To-Do List CLI
import sys

tasks = ['Complete GitHub project', 'Write Python script', 'Fix bug in code', 'Task 30-1: Write Python script', 'Task 30-2: Complete GitHub project', 'Task 30-3: Task 30-1: Write Python script', 'Task 30-4: Task 30-1: Write Python script', 'Task 29-1: Task 30-2: Complete GitHub project', 'Task 29-2: Task 30-2: Complete GitHub project', 'Task 29-3: Task 30-1: Write Python script', 'Task 29-4: Task 29-1: Task 30-2: Complete GitHub project', 'Task 29-5: Task 30-2: Complete GitHub project', 'Task 29-6: Write Python script', 'Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 28-3: Task 29-5: Task 30-2: Complete GitHub project', 'Task 28-4: Task 30-1: Write Python script', 'Task 28-5: Task 29-2: Task 30-2: Complete GitHub project', 'Task 28-6: Fix bug in code', 'Task 28-7: Write Python script', 'Task 27-1: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 27-2: Task 29-3: Task 30-1: Write Python script', 'Task 27-3: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 27-4: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 27-5: Task 30-2: Complete GitHub project', 'Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 26-2: Task 27-4: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 26-3: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 26-4: Task 30-2: Complete GitHub project', 'Task 26-5: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 26-6: Task 26-5: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 25-1: Task 28-6: Fix bug in code', 'Task 25-2: Complete GitHub project', 'Task 25-3: Task 28-4: Task 30-1: Write Python script', 'Task 25-4: Task 29-1: Task 30-2: Complete GitHub project', 'Task 25-5: Write Python script', 'Task 24-1: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 24-2: Task 25-4: Task 29-1: Task 30-2: Complete GitHub project', 'Task 24-3: Task 26-5: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 24-4: Task 27-2: Task 29-3: Task 30-1: Write Python script', 'Task 24-5: Task 25-2: Complete GitHub project', 'Task 24-6: Task 26-6: Task 26-5: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 23-1: Task 26-2: Task 27-4: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 23-2: Task 24-4: Task 27-2: Task 29-3: Task 30-1: Write Python script', 'Task 23-3: Fix bug in code', 'Task 23-4: Task 28-6: Fix bug in code', 'Task 23-5: Task 29-5: Task 30-2: Complete GitHub project', 'Task 23-6: Task 29-2: Task 30-2: Complete GitHub project', 'Task 22-1: Task 27-5: Task 30-2: Complete GitHub project', 'Task 22-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 22-3: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 21-1: Task 28-5: Task 29-2: Task 30-2: Complete GitHub project']

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
