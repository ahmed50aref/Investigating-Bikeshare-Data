import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter the city you want to explore (chicago, new york city, washington) correctly:\n").lower()
    while city not in CITY_DATA :
        print ("please write the name of city correctly\nfor example: chicago")
        city = input().lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter the month you want to explore (all, january, february, march, april, may, june) correctly:\n").lower()
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while month not in months :
        print ("please write the name of month correctly\nfor example: january")
        month = input().lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter the day you want to explore (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday) correctly:\n").lower()
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while day not in days :
        print ("please write the name of  correctly\nfor example: january")
        day = input().lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['month name'] = pd.DatetimeIndex(df['Start Time']).month_name()
    df['day of week'] = pd.DatetimeIndex(df['Start Time']).day_name()
    df['hour'] = pd.DatetimeIndex(df['Start Time']).hour

    # filter by both month and day if applicable 
    if (month != 'all') and (day != 'all'):
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        # filter by both month and day to create the new dataframe
        df = df.loc[(df['month'] == month) & (df['day of week'] == day.title())]
        
    # filter by month if applicable
    elif month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    elif day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day of week'] == day.title()]
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month name'].mode()[0]

    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day_of_week = df['day of week'].mode()[0]

    print('Most Popular day of week:', popular_day_of_week)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]

    print('Most Popular Start Station:', popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]

    print('Most Popular End Station:', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    popular_sande = (df['Start Station']+' // '+df['End Station']).mode()[0]

    print('Most Popular Combination of Start Station and End Station:', popular_sande)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()

    print('Total Time Travel:', total_time,'seconds.')

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean().round()

    print('Mean Time Travel:', int(mean_time),'seconds.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    
    print('Count of User types:\n{}'.format(user_types.to_string()))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns :
        gender_types = df['Gender'].value_counts()
    
        print('Count of Gender types:\n{}'.format(gender_types.to_string()))
    
    else :
        print('there is no information about gender')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns :
        early_year = int(df['Birth Year'].min())
        
        print('Earliest year of birth :',early_year)
        
        recent_year = int(df['Birth Year'].max())
        
        print('Most recent year of birth :',recent_year)
        
        common_year = int(df['Birth Year'].mode()[0])
        
        print('Most commom year of birth :',common_year)
        
    else :
        print ('there is no information about year of birth')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_row_data(df):
    """asks the user if he wast to see some rows of data."""
    
    #get input from asking if user want to see some rows of data
    answer = input('\nwould you like to see 5 rows of data? Enter yes or no.\n').lower()
    #check if he write a valid answer
    while (answer != 'yes') and (answer != 'no') :
        print ('please enter a valid answer.')
        answer = input().lower()
    #show the data based on the answer
    i = 0
    j = 5
    while answer == 'yes':
        if i <= df.shape[0] :
            pd.set_option('display.max_columns',200)
            print (df.iloc[i:j])
            i += 5
            j += 5
        else :
            print ('all rows has been shown')
            break
        answer = input('\nwould you like to see more 5 rows of data? Enter yes or no.\n').lower()
        while (answer != 'yes') and (answer != 'no') :
            print ('please enter a valid answer.')
            answer = input().lower()
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_row_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        while (restart != 'yes') and (restart != 'no') :
            print ('please enter a valid answer.')
            restart = input().lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
