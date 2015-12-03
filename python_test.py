
# General Python

def example0(status):
    if status in ['in production', 'in_production', 'In Production', 'In_Production', 'IN PRODUCTION', 'IN_PRODUCTION', 'In production', 'In_production']:
        do_something()


def example1(task):
    if task.get('status') == 'Pending':
        color = "#d7d7d7"
    if task.get('status') == 'Ready':
        color = "#b2cee8"
    if task.get('status') == 'On_Hold':
        color = "#e8b2b8"
    if task.get('status') == 'Client Response':
        color = "#ddd5b8"
    if task.get('status') == 'Internal Rejection':
        color = "#ff0000"
    if task.get('status') == 'External Rejection':
        color = "#ff0000"
    if task.get('status') == 'Failed QC':
        color = "#ff0000"
    if task.get('status') == 'Rejected':
        color = "#ff0000"
    if task.get('status') == 'Fix Needed':
        color = "#c466a1"
    if task.get('status') == 'In_Progress':
        color = "#f5f3a4"
    if task.get('status') == 'DR In_Progress':
        color = "#d6e0a4"
    if task.get('status') == 'BATON In_Progress':
        color = "#c6e0a4"
    if task.get('status') == 'Export In_Progress':
        color = "#796999"
    if task.get('status') == 'Need Buddy Check':
        color = "#e3701a"
    if task.get('status') == 'Buddy Check In_Progress':
        color = "#1aade3"
    if task.get('status') == 'Completed':
        color = "#b7e0a5"
    widget = Widget()
    widget.set_background_color(color)
    return widget


def example2(titles, order_code):
    # titles is a dictionary, order code is a string
    try:
        t = titles[order_code]
    except:
        pass
    do_something(t)


def example3(objects):
    # objects is a list of dictionaries
    do_it = True
    for obj in objects:
        if obj.get('some_value') not in [None, '', (), [], {}]:
            if do_it == True:
                if obj.get('some_value') != 'do_the_thing':
                    do_something_else(obj)
                else:
                    do_the_thing(obj)
                    do_it = False


def make_8_digits(number):
    number_str = str(number)
    number_str_len = len(number_str)
    if number_str_len < 8:
        zeros = 8 - number_str_len
        for num in range(0, zeros):
            number_str = '0%s' % number_str
    return number_str


def make_version_string(version):
    version = int(version)
    if version > 9:
        version = 'v0%s' % version
    elif version > 99:
        version = 'v%s' % version
    else:
        version = 'v00%s' % version
    return version


# Server Optimization

def func0(this_user):
    # get all the non-retired tasks
    tasks = server.query('sthpw/task', filters=[('state', '!=', 'RETIRED')])
    # iterate through them, task is a dictionary
    for task in tasks:
        # we only care about tasks assigned to this user
        if task.get('assigned') == this_user:
            # do something with the task
            add_to_some_list(task)


def func1(order_ids):
    for order_id in order_ids:
        # query for this order object
        order_object = server.query('twog/order', filters=[('id', '=', order_id)])[0]
        # do something with the object
        print order_object.get('name')


def func2(tasks):
    # tasks is a list of dictionaries
    for task in tasks:
        # update the object in the database
        server.update(task.get('__search_key__'), {'status': 'In Progress'})
