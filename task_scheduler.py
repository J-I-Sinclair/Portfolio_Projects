class scheduler:

    def __init__(self):
        self.working_schedule = {}

    def open_schedule(self):
        schedule = open('schedule.txt')
        sched_string = schedule.read()
        schedule_list = sched_string.split(',')
        schedule.close()
        keys = []
        values = []

        for item in schedule_list:
            new = item.split(':')
            keys.append(new[0])
            values.append(new[1])

        schedule_dict = {}
        for num in range(len(keys)):
            x = keys[num]
            y = values[num]
            schedule_dict.update({x : y})
        
        self.working_schedule = schedule_dict
        print(f"Schedule opened: {schedule_dict}")

    def add_task(self, task, priority):
        task = task.lower()
        self.working_schedule.update({task : priority})
        print("Task added")

    def remove_task(self, task):
        task = task.lower()
        working_copy = self.working_schedule
        working_copy.pop(task)
        self.working_schedule = working_copy
        print(f'{task} removed')


    def save_schedule(self):
        working_schedule = str(self.working_schedule)
        working_schedule.strip(',')
        working_schedule.strip('{}')
        schedule = open('schedule.txt', 'w')
        schedule.write(f'{working_schedule}')
        schedule.close()
        print("Schedule saved")
        print(f'Schedule: {working_schedule}')


    def change_priority(self, task, priority):
        task = task.lower()
        self.working_schedule[task] = priority
        print(f"Priority of {task} changed to {priority}")
        
        
schedule1 = scheduler()

schedule1.open_schedule()
schedule1.add_task('Fight monsters', 1000)
schedule1.remove_task('Fight monsters')
schedule1.add_task('Be the best', 100)
schedule1.change_priority('Be the best', 50)
schedule1.save_schedule()