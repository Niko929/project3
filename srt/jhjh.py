def filter_by_state(rey_fultr, state ='EXECUTED'):
    result =  []
    here = []
    for req in rey_fultr:
        if req['state'] == state:
            result.append(req)
        else:
            here.append(req)
    return f"{result} \n {here}"


def sort_by_date(sort_dat, reverse = True):
    hg = sorted(sort_dat, key=lambda x: x['date'], reverse=reverse)
    return hg