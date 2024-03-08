class scheduler:

    def __init__(self):
        self.working_schedule = {}

    def open_schedule(self):
        schedule = open('schedule.txt')
        sched_string = schedule.read()
        print(sched_string)
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
            y = int(values[num])
            schedule_dict.update({x : y})
        
        self.working_schedule = schedule_dict
        print("Schedule opened")

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
        self.sort_schedule()
        working_schedule = ""
        keys = self.working_schedule.keys()
        for item in keys:
            item_string = ',' + str(item) + ':' + str(self.working_schedule[item])
            working_schedule = working_schedule + item_string
        working_schedule = working_schedule.strip(',')
        schedule = open('schedule.txt', 'w')
        schedule.write(f'{working_schedule}')
        schedule.close()
        print("Schedule saved")


    def change_priority(self, task, priority):
        task = task.lower()
        self.working_schedule[task] = priority
        print(f"Priority of {task} changed to {priority}")

    def show_schedule(self): # Display each item on different lines, should be super easy
        print('Your working schedule:')
        for item in self.working_schedule:
            print(f'{item} : {self.working_schedule[item]}')
        
    def sort_schedule(self):
        sorted_dict = dict(sorted(self.working_schedule.items(), key=lambda 
                                  item: item[1], reverse=True))
        self.working_schedule = sorted_dict


schedule1 = scheduler()

schedule1.open_schedule()
schedule1.save_schedule()