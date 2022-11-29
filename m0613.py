import datetime
filename=("today.txt")
todays_date=datetime.date.today()
print(todays_date)
fin=open(filename,'w')
def create_file():
    with open(filename) as file:
        file.write(todays_date)
create_file
today_string=todays_date
print(today_string)