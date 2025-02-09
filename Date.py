import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get_day_of_week(year, month, day):
    date_obj = datetime.date(year, month, day)
    day_of_week = date_obj.strftime("%A")
    return day_of_week

def ordinal(n):
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix

def main(update_console):
    current_date = datetime.date.today()
    day = current_date.day
    month = current_date.month
    year = current_date.year
    month_name = current_date.strftime("%B")
    day_of_week = get_day_of_week(year, month, day)
    update_console("The current date is {} {}, {}.{}.".format(day_of_week, ordinal(day), month_name,year, ))
    speak("The current date is {} {}, {}.{}.".format(day_of_week, ordinal(day), month_name,year, ))

if __name__ == "__main__":
    main()
