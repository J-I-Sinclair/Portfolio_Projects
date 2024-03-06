def open_schedule():
    schedule = open('schedule.txt')
    sched_string = schedule.read()
    schedule_list = sched_string.split(',')
    schedule.close()
    keys = []
    values = []

    print(schedule_list)
    for item in schedule_list:
        print(item)
        new = item.split(':')
        print(new[0], new[1])
        keys.append(new[0])
        values.append(new[1])
    
    print(keys, values)

open_schedule()