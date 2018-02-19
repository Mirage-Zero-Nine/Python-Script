__author__ = 'BorisMirage'
# --- coding:utf-8 ---

import re
import requests
import string


def get_content():
    library_url = 'http://library.gwu.edu/library-hours'
    library_hours_page = requests.get(library_url)

    # Find today's tag
    time_today = re.findall(r'(?<=<div class=\'equalHMR eq\'><span class=\'hoursToday\'>).*(?=</div>)',
                            library_hours_page.content)
    # Find other day's tag
    time_others = re.findall(r'(?<=<div class=\'equalHMR eq\'><span class=\'hoursDay\'>).*(?=</div>)',
                             library_hours_page.content)
    result = string.replace(str(time_today[0]), '</span><br>', ': ')

    # Find whether today is 24 hours.
    if not re.findall(r'24 hours', result):
        today_hours = 'Today is not 24 Hours!' + result
        print(today_hours)
    else:
        print(result)

    i = 0
    while i < 6:
        str_hours = string.replace(str(time_others[i]), '</span><br>', ': ')

        # If this day is not 24 hours.
        if not re.findall(r'24 hours', str_hours):
            not_24hours = re.findall(r'.*(?=:)')
            not_24hours = str(not_24hours[0]) + ' is different! ' + str_hours
            print(not_24hours)
        else:
            print(str_hours)
        i += 1


if __name__ == '__main__':
    get_content()
