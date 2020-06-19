import numpy as np

def extract_time_events(cardiac_events):

    times = np.zeros(len(cardiac_events))
    for i in range(len(times)):
        times[i] = cardiac_events[i][0]
    return times

def extract_type_events(cardiac_events):
    types = []
    for i in range(len(cardiac_events)):
        types.append(cardiac_events[i][1])
    return types

def find(condtion, max_index=-1, order='ascend'):

    assert order=='ascend' or order=='descend'


    indx_array = np.nonzero(condtion)[0]
    if max_index==-1:
        max_index=len(indx_array)

    if order == 'ascend':
        return indx_array[:min(len(indx_array),max_index)]

    elif order == 'descend':
        return indx_array[-min(len(indx_array), max_index):]


def EventColor(evt):
    if (evt == 'NSR'):
        ec = (0, 1, 0)
    elif (evt == 'NSR (paced)'):
        ec = (0, 0.8, 0)
    elif (evt == 'VF'):
        ec = (1, 0, 0)
    elif (evt == 'NOISE'):
        ec = (0.6, 0.6, 0.6)
    elif (evt == 'SHOCK'):
        ec = (0, 0, 0)
    elif (evt == 'SAISPAS'):
        ec = (0, 0, 1)
    elif (evt == 'VT'):
        ec = (0.6, 0, 0.2)
    elif (evt == 'ST'):
        ec = (0.6, 0.2, 0.2)
    elif (evt == 'SV'):
        ec = (0.2, 0.6, 0.2)
    elif (evt == 'AF'):
        ec = (0.6, 0.2, 0.6)
    else:
        ec = (0, 0, 0)

    return ec


def TextColor(evt):
    if (evt == 'SHOCK'):
        tc = 'r'
    elif (evt == 'NOISE'):
        tc = 'w'
    elif (evt == 'SHOCK'):
        tc = 'w'
    elif (evt == 'SAISPAS'):
        tc = 'w'
    elif (evt == 'ST'):
        tc = 'w'
    elif (evt == 'SVT'):
        tc = 'w'
    else:
        tc = 'k'

    return tc

if __name__ == "__main__":
    a = [0,1,0,0,0,0,1,1,1,0]
    indx = find(a,3,'descend')
    # indx = find(a)
    print(indx)