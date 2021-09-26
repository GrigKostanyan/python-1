import argparse
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

parser = argparse.ArgumentParser()

parser.add_argument('--num_y', type = int)
parser.add_argument('--num_d', type = int)

args = parser.parse_args()

now = datetime.now()
print('Current date: ', str( now ) )

givenYears = args.num_y if args.num_y else 0
print( 'Given years: ', givenYears )

givenDays = args.num_d if args.num_d else 0
print( 'Given days: ', givenDays )

res = now + relativedelta(years = givenYears) + timedelta(days = givenDays)
print('Final date: ', str( res ) )
