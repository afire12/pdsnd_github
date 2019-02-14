import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

print('Hello! Let\'s explore some US bikeshare data!')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Which city would you like to see, Chicago, New York or Washington? ')
    if city.lower() == 'chicago':
        city = 'chicago'
    elif city.lower() == 'new york':
        city = 'new york city'
    elif city.lower() == 'washington':
        city = 'washington'
    else:
        print('Sorry, we are not sure the city you input. Could you try again? ')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month do you want to choose? ')
    if month.lower() == 'janurary':
        month = '01'
    elif month.lower() == 'feburary':
        month = '02'
    elif month.lower() == 'march':
        month = '03'
    elif month.lower() == 'april':
        month = '04'
    elif month.lower() == 'may':
        month = '05'
    elif month.lower() == 'june':
        month = '06'
    else:
        print('Sorry, we are not sure the month you input. Could you try again?')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day do you want to choose? ')
    if day.lower() == 'monday':
        day = 0
    elif day.lower() == 'tuesday':
        day = 1
    elif day.lower() == 'wednesday':
        day = 2
    elif day.lower() == 'thursday':
        day = 3
    elif day.lower() == 'friday':
        day = 4
    elif day.lower() == 'saturday':
        day = 5
    elif day.lower() == 'sunday':
        day = 6
    else:
        print('Sorry, we are not sure the day of the week you input. Could you try again?')

    return  city, month, day

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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
    # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

    """
    Displays statistics on the most frequent times of travel.
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time_1 = time.time()

    # TO DO: display the most common month
    common_month = df['Month'].mode()[0]
    print('The Most Common Month:', common_month)

    # TO DO: display the most common day of week
    df['Day Of Week'] = df['Start Time'].dt.weekday_name
    common_day_of_week = df['Day Of Week'].mode()[0]
    print('The Most Common Day Of Week:', common_day_of_week)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Hour'] = df['Start Time'].dt.hour
    common_start_hour = df['Hour'].mode()[0]
    print('The Most Common Start Hour:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time_1))
    print('-'*40)

    """
    Displays statistics on the most popular stations and trip.
    """
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time_2 = time.time()

    # TO DO: display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station is:', most_commonly_used_start_station)

    # TO DO: display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station is:', most_commonly_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = df['End Station'].groupby(['Start Station']['End Station']).mode()[0]
    print('Most frequent combination of start station and end station trip is:', most_frequent_combination)
    print("\nThis took %s seconds." % (time.time() - start_time_2))
    print('-'*40)

    """
    Displays statistics on the total and average trip duration.
    """

    print('\nCalculating Trip Duration...\n')
    start_time_3 = time.time()

    # TO DO: display total travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Duration'] = df['End Time'] - df['Start Time']
    total_travel_time = df['Duration'].sum()
    print("Total travel time is:", total_travel_time)

    # TO DO: display mean travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Duration'] = df['End Time'] - df['Start Time']
    mean_travel_time = df['Duration'].mean()
    print("Total mean time is:", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time_2))
    print('-'*40)

    """
    Displays statistics on bikeshare users.
    """

    print('\nCalculating User Stats...\n')
    start_time_3 = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types:", user_types)

    # TO DO: Display counts of gender
    gender_types = df['Gender'].value_counts()
    print("Counts of gender types:", gender_types)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth = df['Birth Year'].min()
    most_recent_birth = df['Birth Year'].max()
    most_common_birth = df['Birth Year'].mode()[0]
    print("Earliest year of birth:", earliest_birth)
    print("Most recent year of birth:", most_recent_birth)
    print("Most common year of birth:", most_common_birth)

    print("\nThis took %s seconds." % (time.time() - start_time_3))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        load_data(city, month, day)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
