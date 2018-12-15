from collections import defaultdict, Counter

import datetime
import re

a = [
    # DAY 4 puzzle input snipped
]


def get_time(x):
    time_field = ' '.join(x.split(' ')[0:2])
    return datetime.datetime.strptime(time_field, '[%Y-%m-%d %H:%M]')


sorted_a = sorted(a, key=get_time)

starters = filter(lambda x: x.endswith('begins shift'), sorted_a)
sleeping_events = filter(lambda x: not x.endswith('begins shift'), sorted_a)

guards = defaultdict(dict)
shifts = {}

for starter in starters:
    pattern = '(#[\d]+)'
    x = re.search(pattern, starter)
    guard = x.group(0)
    the_datetime = get_time(starter)
    the_date = datetime.datetime.date(the_datetime)
    if the_datetime.hour >= 20:
        the_date += datetime.timedelta(days=1)
    guards[guard][the_date] = []
    shifts[the_date] = guard

sleeping_events_iter = iter(sleeping_events)

for sleeping_event in sleeping_events_iter:
    waking_event = next(sleeping_events_iter)
    time_of_guard = get_time(sleeping_event)
    sleep_min = time_of_guard.minute
    waking_min = get_time(waking_event).minute
    event_date = datetime.datetime.date(time_of_guard)
    guard = shifts[event_date]
    guards[guard][event_date].append((sleep_min, waking_min))

min_asleep = defaultdict(lambda: 0)

for guard in guards:
    for date_ in guards[guard]:
        for interval in guards[guard][date_]:
            min_asleep[guard] += (interval[1] - interval[0])


def get_most_common_minute(guard):
    all_minutes = []
    for date_datum in guards[guard]:
        for interval_datum in guards[guard][date_datum]:
            all_minutes.extend(list(range(interval_datum[0], interval_datum[1])))
    count = Counter(all_minutes)
    try:
        returning_value = count.most_common(1)[0]
    except IndexError:
        returning_value = (None, 0)
    return returning_value


# PART 1

max_guard = Counter(min_asleep).most_common(1)[0][0]

most_common = get_most_common_minute(max_guard)[0]

print(int(max_guard.lstrip('#')) * most_common)


# PART 2
all_guard_minutes = {}
for guard in guards:
    all_guard_minutes[guard] = get_most_common_minute(guard)

max_guard = None
max_minutes = 0
for guard in all_guard_minutes:
    if all_guard_minutes[guard][1] > max_minutes:
        max_minutes = all_guard_minutes[guard][1]
        max_guard = guard

print(int(max_guard.lstrip('#')) * all_guard_minutes[max_guard][0])
