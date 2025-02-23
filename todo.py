# Simple To-Do List CLI
import sys

tasks = ['Complete GitHub project', 'Write Python script', 'Fix bug in code', 'Task 30-1: Write Python script', 'Task 30-2: Complete GitHub project', 'Task 30-3: Task 30-1: Write Python script', 'Task 30-4: Task 30-1: Write Python script', 'Task 29-1: Task 30-2: Complete GitHub project', 'Task 29-2: Task 30-2: Complete GitHub project', 'Task 29-3: Task 30-1: Write Python script', 'Task 29-4: Task 29-1: Task 30-2: Complete GitHub project', 'Task 29-5: Task 30-2: Complete GitHub project', 'Task 29-6: Write Python script', 'Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 28-3: Task 29-5: Task 30-2: Complete GitHub project', 'Task 28-4: Task 30-1: Write Python script', 'Task 28-5: Task 29-2: Task 30-2: Complete GitHub project', 'Task 28-6: Fix bug in code', 'Task 28-7: Write Python script', 'Task 27-1: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 27-2: Task 29-3: Task 30-1: Write Python script', 'Task 27-3: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 27-4: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 27-5: Task 30-2: Complete GitHub project', 'Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 26-2: Task 27-4: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 26-3: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 26-4: Task 30-2: Complete GitHub project', 'Task 26-5: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 26-6: Task 26-5: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 25-1: Task 28-6: Fix bug in code', 'Task 25-2: Complete GitHub project', 'Task 25-3: Task 28-4: Task 30-1: Write Python script', 'Task 25-4: Task 29-1: Task 30-2: Complete GitHub project', 'Task 25-5: Write Python script', 'Task 24-1: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 24-2: Task 25-4: Task 29-1: Task 30-2: Complete GitHub project', 'Task 24-3: Task 26-5: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 24-4: Task 27-2: Task 29-3: Task 30-1: Write Python script', 'Task 24-5: Task 25-2: Complete GitHub project', 'Task 24-6: Task 26-6: Task 26-5: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 23-1: Task 26-2: Task 27-4: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 23-2: Task 24-4: Task 27-2: Task 29-3: Task 30-1: Write Python script', 'Task 23-3: Fix bug in code', 'Task 23-4: Task 28-6: Fix bug in code', 'Task 23-5: Task 29-5: Task 30-2: Complete GitHub project', 'Task 23-6: Task 29-2: Task 30-2: Complete GitHub project', 'Task 22-1: Task 27-5: Task 30-2: Complete GitHub project', 'Task 22-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 22-3: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 21-1: Task 28-5: Task 29-2: Task 30-2: Complete GitHub project', 'Task 21-2: Task 27-5: Task 30-2: Complete GitHub project', 'Task 21-3: Task 26-6: Task 26-5: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 21-4: Task 27-1: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 21-5: Task 27-2: Task 29-3: Task 30-1: Write Python script', 'Task 21-6: Task 27-3: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 21-7: Task 23-5: Task 29-5: Task 30-2: Complete GitHub project', 'Task 20-1: Task 28-5: Task 29-2: Task 30-2: Complete GitHub project', 'Task 20-2: Task 27-2: Task 29-3: Task 30-1: Write Python script', 'Task 20-3: Task 29-1: Task 30-2: Complete GitHub project', 'Task 19-1: Task 28-5: Task 29-2: Task 30-2: Complete GitHub project', 'Task 19-2: Task 30-4: Task 30-1: Write Python script', 'Task 19-3: Task 23-2: Task 24-4: Task 27-2: Task 29-3: Task 30-1: Write Python script', 'Task 19-4: Task 30-3: Task 30-1: Write Python script', 'Task 19-5: Task 27-3: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 18-1: Task 27-1: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 18-2: Task 22-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 18-3: Task 23-3: Fix bug in code', 'Task 18-4: Task 26-2: Task 27-4: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 18-5: Task 18-2: Task 22-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 18-6: Task 29-4: Task 29-1: Task 30-2: Complete GitHub project', 'Task 18-7: Fix bug in code', 'Task 17-1: Task 18-3: Task 23-3: Fix bug in code', 'Task 17-2: Task 27-5: Task 30-2: Complete GitHub project', 'Task 17-3: Task 27-1: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 16-1: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 16-2: Task 22-1: Task 27-5: Task 30-2: Complete GitHub project', 'Task 16-3: Task 27-4: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 16-4: Task 21-5: Task 27-2: Task 29-3: Task 30-1: Write Python script', 'Task 16-5: Task 25-5: Write Python script', 'Task 16-6: Task 30-2: Complete GitHub project', 'Task 16-7: Task 26-6: Task 26-5: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 15-1: Task 24-3: Task 26-5: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 15-2: Task 30-3: Task 30-1: Write Python script', 'Task 15-3: Task 17-2: Task 27-5: Task 30-2: Complete GitHub project', 'Task 15-4: Task 26-5: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 14-1: Task 21-5: Task 27-2: Task 29-3: Task 30-1: Write Python script', 'Task 14-2: Task 15-1: Task 24-3: Task 26-5: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 14-3: Task 16-5: Task 25-5: Write Python script', 'Task 14-4: Task 25-3: Task 28-4: Task 30-1: Write Python script', 'Task 14-5: Task 27-1: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 14-6: Task 28-6: Fix bug in code', 'Task 14-7: Task 18-6: Task 29-4: Task 29-1: Task 30-2: Complete GitHub project', 'Task 13-1: Task 21-7: Task 23-5: Task 29-5: Task 30-2: Complete GitHub project', 'Task 13-2: Task 16-7: Task 26-6: Task 26-5: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 13-3: Task 19-2: Task 30-4: Task 30-1: Write Python script', 'Task 13-4: Task 30-3: Task 30-1: Write Python script', 'Task 12-1: Task 28-5: Task 29-2: Task 30-2: Complete GitHub project', 'Task 12-2: Task 15-2: Task 30-3: Task 30-1: Write Python script', 'Task 12-3: Task 24-2: Task 25-4: Task 29-1: Task 30-2: Complete GitHub project', 'Task 12-4: Task 18-1: Task 27-1: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 12-5: Task 18-6: Task 29-4: Task 29-1: Task 30-2: Complete GitHub project', 'Task 11-1: Task 29-1: Task 30-2: Complete GitHub project', 'Task 11-2: Task 14-1: Task 21-5: Task 27-2: Task 29-3: Task 30-1: Write Python script', 'Task 11-3: Task 29-5: Task 30-2: Complete GitHub project', 'Task 11-4: Task 21-4: Task 27-1: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 10-1: Task 16-4: Task 21-5: Task 27-2: Task 29-3: Task 30-1: Write Python script', 'Task 10-2: Task 14-1: Task 21-5: Task 27-2: Task 29-3: Task 30-1: Write Python script', 'Task 10-3: Task 25-5: Write Python script', 'Task 10-4: Task 15-2: Task 30-3: Task 30-1: Write Python script', 'Task 10-5: Task 28-7: Write Python script', 'Task 10-6: Task 10-1: Task 16-4: Task 21-5: Task 27-2: Task 29-3: Task 30-1: Write Python script', 'Task 9-1: Task 21-3: Task 26-6: Task 26-5: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 9-2: Task 10-5: Task 28-7: Write Python script', 'Task 9-3: Task 18-1: Task 27-1: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 9-4: Task 10-4: Task 15-2: Task 30-3: Task 30-1: Write Python script', 'Task 9-5: Task 14-2: Task 15-1: Task 24-3: Task 26-5: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 9-6: Task 19-3: Task 23-2: Task 24-4: Task 27-2: Task 29-3: Task 30-1: Write Python script', 'Task 8-1: Task 18-6: Task 29-4: Task 29-1: Task 30-2: Complete GitHub project', 'Task 8-2: Task 10-6: Task 10-1: Task 16-4: Task 21-5: Task 27-2: Task 29-3: Task 30-1: Write Python script', 'Task 8-3: Task 24-6: Task 26-6: Task 26-5: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 7-1: Task 18-6: Task 29-4: Task 29-1: Task 30-2: Complete GitHub project', 'Task 7-2: Task 19-5: Task 27-3: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 7-3: Task 10-4: Task 15-2: Task 30-3: Task 30-1: Write Python script', 'Task 7-4: Task 28-5: Task 29-2: Task 30-2: Complete GitHub project', 'Task 7-5: Task 9-2: Task 10-5: Task 28-7: Write Python script', 'Task 7-6: Task 22-3: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 6-1: Task 19-5: Task 27-3: Task 28-1: Task 29-3: Task 30-1: Write Python script', 'Task 6-2: Task 10-2: Task 14-1: Task 21-5: Task 27-2: Task 29-3: Task 30-1: Write Python script', 'Task 6-3: Task 14-7: Task 18-6: Task 29-4: Task 29-1: Task 30-2: Complete GitHub project', 'Task 6-4: Task 25-4: Task 29-1: Task 30-2: Complete GitHub project', 'Task 5-1: Task 27-5: Task 30-2: Complete GitHub project', 'Task 5-2: Task 16-7: Task 26-6: Task 26-5: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 5-3: Task 24-6: Task 26-6: Task 26-5: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 5-4: Task 12-5: Task 18-6: Task 29-4: Task 29-1: Task 30-2: Complete GitHub project', 'Task 5-5: Task 21-1: Task 28-5: Task 29-2: Task 30-2: Complete GitHub project', 'Task 5-6: Task 16-1: Task 26-1: Task 28-2: Task 29-2: Task 30-2: Complete GitHub project', 'Task 5-7: Task 18-6: Task 29-4: Task 29-1: Task 30-2: Complete GitHub project', 'Task 4-1: Task 14-3: Task 16-5: Task 25-5: Write Python script']

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
