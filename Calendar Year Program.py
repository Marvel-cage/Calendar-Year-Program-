# Calendar Year Program

#initialization
month_names = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month_separator = format(' ', '8')
column_width = 3
blank_column = format(' ', str(column_width))
blank_week = blank_column * 7

# Program Greeting
print('This program generates a Calendar year')

# requests for year
year = int(input('Enter a year(-1 to terminate): '))
terminate = False

# main loop
while not terminate:
    if year == -1:
        terminate = True
    else:
        
        # checks user's input
        while year < 1800 or year > 2099:
            year = int(input('\nINVALID INPUT \n Enter a year(-1 to terminate): '))
         
        calendar_year = []   
        #checks if leap year
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            leap_year = True
        else:
            leap_year = False
            
        if leap_year:
            days_in_month[1] = 29
            
        else:
            days_in_month[1] = 28
            
        #calculates first day of year
        century_digits = year // 100
        year_digits = year % 100
        value = year_digits + year_digits // 4
        if century_digits == 18:
            value += 2
        elif century_digits == 20:
            value += 6
        if not leap_year:
            value += 1
        value = (value + 1) % 7
        
        if value == 0:
            starting_column = 7
        else:
            starting_column = value
      
        
        #construct calendar year for 12 months
        for month_num in range(12):
            num_days_in_month = days_in_month [month_num]
                  
            # init for calendar year
            calendar_month = []
            current_column = 1
            current_day = 1
            calendar_week = ''
            
            # fill the first row with required blanks
            while current_column < starting_column:
                calendar_week = calendar_week + blank_column
                current_column += 1
                
            #fills in days of month
            while current_day <= num_days_in_month:
                calendar_week = calendar_week + format(current_day, str('>' + str(column_width)))
                if current_column < 7:
                    current_column += 1
                else:
                    calendar_month.append(calendar_week)
                    current_column = 1
                    calendar_week = ''
                current_day += 1
                
            # fillls remaining spaces with blank columns
            if calendar_week:
                num_spaces_left = (8 - current_column) * column_width
                last_spaces = blank_week[0: num_spaces_left]
                calendar_week = calendar_week + last_spaces
                calendar_month = calendar_month + [calendar_week]
            calendar_year = calendar_year + [calendar_month]
           
           #prepares for next month
            calendar_week = ''
            calendar_month = []
            starting_column = current_column
        
        print('\n', year, '\n')    
        # displays the year
        for month_row in(0, 3, 6, 9):
            
            #checks the number of lines to print for each week
            lines_month1 = len(calendar_year[month_row])
            lines_month2 = len(calendar_year[month_row + 1])
            lines_month3 = len(calendar_year[month_row + 2])
            
            if lines_month1 > lines_month2 and lines_month1 > lines_month3:
                num_lines_to_print = lines_month1
            elif lines_month2 > lines_month3:
                num_lines_to_print = lines_month2
            else:
                num_lines_to_print = lines_month3
            
            #prints the names of month
            for month_num in range(month_row , month_row + 3):
                print(format(month_names[month_num], str('<' + str(len(blank_week)))) + month_separator, end='')
            print()   
                 
           # prints the days of month
            current_line = 0
            while current_line < num_lines_to_print:
                    for month in range(month_row, month_row + 3):
                        if current_line < len(calendar_year[month]):
                            print(calendar_year[month][current_line] + month_separator, end='')
                        else:
                            print(blank_week + month_separator, end='')
                    print()
                    current_line += 1
                    
        year = int(input('\nEnter a year(-1 to terminate) :'))
                
print('\n Goodbye \n')                   