from datetime import datetime, timedelta


def get_time():
    return datetime.now() + timedelta(hours=3)
    # we add 3 hourse because the clock is GMT+0