"""
Below are several examples of some bad code. Identify what is wrong with each one
and what you would do to fix it.
"""


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
    # titles is a dictionary, order_code is a string
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


def example4(number):
    number_str = str(number)
    number_str_len = len(number_str)
    if number_str_len < 8:
        zeros = 8 - number_str_len
        for num in range(0, zeros):
            number_str = '0%s' % number_str
    return number_str


def example5(version):
    version = int(version)
    if version > 9:
        version = 'v0%s' % version
    elif version > 99:
        version = 'v%s' % version
    else:
        version = 'v00%s' % version
    return version


def example6(delivs):
    linked = []
    for d in delivs:
        linked_delivs.append(d.get_value('satisfied'))
    satisfied = 0
    unsatisfied = 0
    for link in linked:
        if link == True:
            satisfied = satisfied + 1
        else:
            unsatisfied = unsatisfied + 1
    return '(%s/%s)' % (satisfied, satisfied + unsatisfied)


def example7(barcodes, server):
    for bc in barcodes:
        if 'EMP' in bc:
            that_user = server.eval("@SOBJECT(sthpw/login['barcode','%s'])" % bc)
            if that_user:
                that_user = that_user[0]
            else:
                that_user = {'login': 'UNKNOWN USER'}
    for bc in barcodes:
        if 'LOC' in bc:
            that_location = server.eval("@SOBJECT(twog/inhouse_locations['barcode','%s'])" % bc)
            if that_location:
                that_location = that_location[0]
            else:
                that_location = {'name': 'UNKNOWN LOCATION'}
    for bc in barcodes:
        if 'LOC' not in bc and 'EMP' not in bc:
            that_src = server.eval("@SOBJECT(twog/source['barcode','%s'])" % bc)
            if that_src:
                that_src = that_src[0]
            else:
                that_src = {'title': 'UNKNOWN SOURCE', 'episode': '', 'season': '', 'part': ''}
    return [that_user, that_location, that_src]


"""
Server Optimization
Since server calls are relatively expensive, they should be as optimized as possible.
Identify the problem with each example and what can be done to optimize it.
"""


def function0(this_user):
    # get all the non-retired tasks
    tasks = server.query('sthpw/task', filters=[('state', '!=', 'RETIRED')])
    # iterate through them, task is a dictionary
    for task in tasks:
        # we only care about tasks assigned to this user
        if task.get('assigned') == this_user:
            # do something with the task
            add_to_some_list(task)


def function1(order_ids):
    for order_id in order_ids:
        # query for this order object
        order_object = server.query('twog/order', filters=[('id', '=', order_id)])[0]
        # do something with the object
        print order_object.get('name')


def function2(tasks):
    # tasks is a list of dictionaries
    for task in tasks:
        # update the object in the database
        server.update(task.get('__search_key__'), {'status': 'In Progress'})
