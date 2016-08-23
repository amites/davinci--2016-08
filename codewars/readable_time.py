def make_readable(seconds):
    return ':'.join(['{:0>2d}'.format(n) for n in
                     [seconds / 60 / 60, (seconds / 60) % 60, seconds % 60]])
