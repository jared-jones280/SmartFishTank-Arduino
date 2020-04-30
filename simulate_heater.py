import requests

ON = "https://maker.ifttt.com/trigger/turn_on_heater/with/key/xxfXfeHekVc6diMURY5ix"
OFF = "https://maker.ifttt.com/trigger/turn_off_heater/with/key/xxfXfeHekVc6diMURY5ix"

SET_TEMP = 76
currentTemp = 76
status = OFF

def setHeater(url):
    requests.get(url=url)

if __name__ in '__main__':
    print("========== Smart Fish Tank Monitor - Heater Simulation ==========")
    print("Set temp is: " + str(76))

    while True:
        currentTemp = float(input("Enter the temperature of the temperature sensors: "))

        if (status == OFF and currentTemp < SET_TEMP - 1):
            setHeater(ON)
            status = ON
            print("\t~ Current temperature is lower than the set temperature.")
            print("\t Turning on heater...")
        elif (status == ON and currentTemp >= SET_TEMP):
            setHeater(OFF)
            status = OFF
            print("\t~ Current temperature is at or higher than the set temp.")
            print("\t Turning off heater...")
        else:
            print("~\tNo change")

        print()
            