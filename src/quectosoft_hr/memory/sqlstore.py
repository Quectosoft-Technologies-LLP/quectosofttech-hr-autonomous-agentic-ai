class SQLStore:
    def __init__(self):
        self.tasks = {}
        self.deadletters = []
    def upsert_task(self, task):
        self.tasks[task.id] = task
    def get_task(self, task_id):
        return self.tasks.get(task_id)
    def add_deadletter(self, task_id, role, error):
        self.deadletters.append({"task_id": task_id, "role": role, "error": error})
