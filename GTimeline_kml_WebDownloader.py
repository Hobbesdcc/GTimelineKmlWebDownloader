import webbrowser
import datetime

# Google timeline url format:
# pb=!1m8!1m3!1iYYYY!2iMM!3iDD!2m3!1iYYYY!2iMM!3iDD
# to download kml: kml?authuser=0&
# Note: Months start at "0", days start at "1"
# So for example "2017 6 20" itput "2017 5 20" for url, like this:
# https://www.google.com/maps/timeline/kml?authuser=0&pb=!1m8!1m3!1i2017!2i5!3i20!2m3!1i2017!2i5!3i20


#Input Start Date
print('=============')
print('Start Year: YYYY')
input_Startyear = input()
print('Start Month: MM')
input_Startmonth = input()
print('Start Day: DD')
input_Startday = input()

#Input how many days you want
print('=============')
print('Input # of days to download: ')
input_dayCount = input()

#Confirm correct dates
print("Inputed Start date: (" + str(input_Startyear) + "/" + str(input_Startmonth) + "/" + str(input_Startday) + ")")

Start_date = datetime.datetime(int(input_Startyear), int(input_Startmonth), int(input_Startday))

print('=============')
index_date = Start_date
i = 1

while i < (int(input_dayCount) + 1):

    print("Download " + str(i) + ": (" + str(index_date.year) + "/" + str(index_date.month) + "/" + str(index_date.day) + ")")
    string = "https://www.google.com/maps/timeline/kml?authuser=0&pb=!1m8!1m3!1i" + str(index_date.year) + "!2i" + str(int(index_date.month)-1)  + "!3i" + str(index_date.day) + "!2m3!1i" + str(index_date.year) + "!2i" + str(int(index_date.month)-1) + "!3i" + str(index_date.day)
    print(string)
    webbrowser.open(string)

    index_date = index_date + datetime.timedelta(days=1)
    i += 1

    #Check to make sure its not past todays date
    # if (index_date < datetime):
    #    i = input_dayCount