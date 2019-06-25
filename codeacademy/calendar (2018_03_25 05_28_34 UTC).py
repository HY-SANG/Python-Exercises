"""
Command Line Calendar
So far, you've used Python to build a variety of things, including calculators and games. In this project, we'll build a
 basic calendar that the user will be able to interact with from the command line. The user should be able to choose to:

View the calendar
Add an event to the calendar
Update an existing event
Delete an existing event
The program should behave in the following way:

Print a welcome message to the user
Prompt the user to view, add, update, or delete an event on the calendar
Depending on the user's input: view, add, update, or delete an event on the calendar
The program should never terminate unless the user decides to exit
Let's begin!
"""


from time import sleep, strftime


first_name = 'Luis'
calendar = {}


def welcome():
    print 'Welcome, ' + first_name
    print('Today is ' + strftime('%A, %B %d, %Y'))
    print strftime('%H:%M:%S')
    sleep(1)
    print 'What would you like to do?'


def start_calendar():
    welcome()
    start = True
    while start:
        sleep(1)
        user_choice = raw_input('A to Add, U to Update, V to View, D to Delete, X to Exit: ')
        user_choice = user_choice.upper()
        print user_choice
        if user_choice == 'V':
            if len(calendar.keys()) < 1:
                print 'Calendar empty.'
            else:
                print calendar
        elif user_choice == 'U':
            date = raw_input('Enter date (MM/DD/YYYY): ')
            if len(date) != 10 or int(date[6:]) < 1000:
                print 'Invalid input'
                continue
            else:
                update = raw_input('Enter update: ')
                calendar[date] = update
                print 'Calendar successfully updated.'
            print calendar
        elif user_choice == 'A':
            event = raw_input('Enter event: ')
            date = raw_input('Enter date (MM/DD/YYYY): ')
            if len(date) != 10 or int(date[6:]) < int(strftime('%Y')):
                print 'Invalid input'
                continue
            else:
                calendar[date] = event
                print 'Event successfully added.'
                # This a very powerful (and possibly dangerous) line of code.
                # It blindly adds the event to the calendar, without checking if the date already exists
                # (which could override things).
        elif user_choice == 'D':
            if len(calendar.keys()) == 0:
                print 'Calendar empty.'
            else:
                event = raw_input('Enter event: ')
                for date in calendar.keys():
                    if event == calendar[date]:
                        del(calendar[date])
                        print 'Event successfully deleted.'
                        sleep(1)
                        print calendar
                    else:
                        print 'Incorrect event specified.'
        elif user_choice == 'X':
            start = False
        else:
            print'Invalid command.'


start_calendar()
