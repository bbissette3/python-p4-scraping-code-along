class Course:
    def __init__(self, title="None", schedule="None", description="None"):
        self.title = title
        self.schedule = schedule
        self.description = description

    def __str__(self):
        return f'Title: {self.title}\nSchedule: {self.schedule}\nDescription: {self.description}\n------------------'
