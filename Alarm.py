import datetime 
import winsound # pip install Playsound

def alarm(timing):
    altime = str(datetime.datetime.now().strptime(timing,"%I:%M %p"))
    print(altime)
    altime = altime[11:-3]
    Horeal = altime[:2]
    Horeal = int(Horeal)
    Mireal = altime[3:5]
    Mireal = int(Mireal)
    print(f"Done, alarm is set for {timing}")

    while True:
        if Horeal==datetime.datetime.now().hour:
            if Mireal==datetime.datetime.now().minute:
                print("Alarm is running boss")
                winsound.PlaySound('abc',winsound.SND_LOOP)

            elif Mireal<datetime.datetime.now().minute:
                break                          
