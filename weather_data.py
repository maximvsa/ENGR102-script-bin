# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   11.17 LAB: Weather data
# Date:         2 November 2025

def maximum_temperature_fetcher(data_file):
    with open(data_file, mode="r", newline='') as csv_data_file:
        maximum_temperature = None
        for line in csv_data_file:
            parts = line.strip().split(',')
            if len(parts) <= 8:
                continue
            try:
                temperature = int(parts[8])
            except ValueError:
                continue
            if maximum_temperature is None or temperature > maximum_temperature:
                maximum_temperature = temperature
        return maximum_temperature

def minimum_temperature_fetcher(data_file):
    with open(data_file, mode="r", newline='') as csv_data_file:
        minimum_temperature = None
        for line in csv_data_file:
            parts = line.strip().split(',')
            if len(parts) <= 9:
                continue
            try:
                temperature = int(parts[9])
            except ValueError:
                continue
            if minimum_temperature is None or temperature < minimum_temperature:
                minimum_temperature = temperature
        return minimum_temperature

def mean_average_pressure_calculator(month, year, data_file):
    with open(data_file, mode="r", newline='') as csv_data_file:
        pressures = []
        for line in csv_data_file:
            parts = line.split(',')
            if len(parts) < 3:
                continue
            date_str = parts[0]
            try:
                date_parts = date_str.split('/')
                if len(date_parts) != 3:
                    continue
                m = int(date_parts[0])
                y = int(date_parts[2])
                if m == int(month) and y == int(year):
                    pressure = float(parts[2])
                    pressures.append(pressure)
            except ValueError:
                continue
        return sum(pressures) / len(pressures)

def mean_average_temperature_calculator(month, year, data_file):
    with open(data_file, mode="r", newline='') as csv_data_file:
        temperatures = []
        for line in csv_data_file:
            parts = line.split(',')
            if len(parts) < 8:
                continue
            date_str = parts[0]
            try:
                date_parts = date_str.split('/')
                if len(date_parts) != 3:
                    continue
                m = int(date_parts[0])
                y = int(date_parts[2])
                if m == int(month) and y == int(year):
                    temp = float(parts[7])
                    temperatures.append(temp)
            except ValueError:
                continue
        return sum(temperatures) / len(temperatures)


def mean_average_wet_bulb_temperature_calculator(month, year, data_file):
    with open(data_file, mode="r", newline='') as csv_data_file:
        wet_bulbs = []
        for line in csv_data_file:
            parts = line.split(',')
            if len(parts) < 4:
                continue
            date_str = parts[0]
            try:
                date_parts = date_str.split('/')
                if len(date_parts) != 3:
                    continue
                m = int(date_parts[0])
                y = int(date_parts[2])
                if m == int(month) and y == int(year):
                    wet_bulb = float(parts[3])
                    wet_bulbs.append(wet_bulb)
            except ValueError:
                continue
        return sum(wet_bulbs) / len(wet_bulbs)

def mean_average_dew_point_calculator(month, year, data_file):
    with open(data_file, mode="r", newline='') as csv_data_file:
        dew_points = []
        for line in csv_data_file:
            parts = line.split(',')
            if len(parts) < 2:
                continue
            date_str = parts[0]
            try:
                date_parts = date_str.split('/')
                if len(date_parts) != 3:
                    continue
                m = int(date_parts[0])
                y = int(date_parts[2])
                if m == int(month) and y == int(year):
                    dew_point = float(parts[1])
                    dew_points.append(dew_point)
            except ValueError:
                continue
        return sum(dew_points) / len(dew_points)

def mean_average_relative_humidity_calculator(month, year, data_file):
    with open(data_file, mode="r", newline='') as csv_data_file:
        humidities = []
        for line in csv_data_file:
            parts = line.split(',')
            if len(parts) < 7:
                continue
            date_str = parts[0]
            try:
                date_parts = date_str.split('/')
                if len(date_parts) != 3:
                    continue
                m = int(date_parts[0])
                y = int(date_parts[2])
                if m == int(month) and y == int(year):
                    humidity = float(parts[6])
                    humidities.append(humidity)
            except ValueError:
                continue
        return sum(humidities) / len(humidities)

def mean_average_daily_wind_speed_calculator(month, year, data_file):
    with open(data_file, mode="r", newline='') as csv_data_file:
        wind_speeds = []
        for line in csv_data_file:
            parts = line.split(',')
            if len(parts) < 5:
                continue
            date_str = parts[0]
            try:
                date_parts = date_str.split('/')
                if len(date_parts) != 3:
                    continue
                m = int(date_parts[0])
                y = int(date_parts[2])
                if m == int(month) and y == int(year):
                    wind_speed = float(parts[4])
                    wind_speeds.append(wind_speed)
            except ValueError:
                continue
        return sum(wind_speeds) / len(wind_speeds)

def non_zero_precipitation_day_percentage_calculator(month, year, data_file):
    with open(data_file, mode="r", newline='') as csv_data_file:
        total_days = 0
        non_zero_days = 0
        for line in csv_data_file:
            parts = line.split(',')
            if len(parts) < 6:
                continue
            date_str = parts[0]
            try:
                date_parts = date_str.split('/')
                if len(date_parts) != 3:
                    continue
                m = int(date_parts[0])
                y = int(date_parts[2])
                if m == int(month) and y == int(year):
                    total_days += 1
                    precip = float(parts[5])
                    if precip > 0:
                        non_zero_days += 1
            except ValueError:
                continue
        return (non_zero_days / total_days) * 100

# Maximus was here :)
def main():
    data_file = "WeatherDataCLL.csv"
    maximum_temperature = maximum_temperature_fetcher(data_file)
    minimum_temperature = minimum_temperature_fetcher(data_file)
    
    print(f"10-year maximum temperature: {maximum_temperature} F")
    print(f"10-year minimum temperature: {minimum_temperature} F")
    print()
    
    input_month = input("Please enter a month: ")
    input_year = input("Please enter a year: ")
    print()
    
    month_dict = {
        "January": "1",
        "February": "2",
        "March": "3",
        "April": "4",
        "May": "5",
        "June": "6",
        "July": "7",
        "August": "8",
        "September": "9",
        "October": "10",
        "November": "11",
        "December": "12"
    }
    
    month = month_dict[input_month]
    
    mean_average_pressure = mean_average_pressure_calculator(month, input_year, data_file)
    mean_average_temperature = mean_average_temperature_calculator(month, input_year, data_file)
    mean_average_wet_bulb_temperature = mean_average_wet_bulb_temperature_calculator(month, input_year, data_file)
    mean_average_dew_point = mean_average_dew_point_calculator(month, input_year, data_file)
    mean_average_relative_humidity = mean_average_relative_humidity_calculator(month, input_year, data_file)
    mean_average_daily_wind_speed = mean_average_daily_wind_speed_calculator(month, input_year, data_file)
    non_zero_precipitation_day_percentage = non_zero_precipitation_day_percentage_calculator(month, input_year, data_file)
    
    print(f"For {input_month} {input_year}:")
    print(f"Mean average daily pressure: {mean_average_pressure:.2f} in Hg")
    print(f"Mean average daily temperature: {mean_average_temperature:.1f} F")
    print(f"Mean average daily wet bulb temperature: {mean_average_wet_bulb_temperature:.1f} F")
    print(f"Mean average daily dew point: {mean_average_dew_point:.1f} F")
    print(f"Mean average daily relative humidity: {mean_average_relative_humidity:.1f}%")
    print(f"Mean average daily wind speed: {mean_average_daily_wind_speed:.2f} mph")
    print(f"Percentage of days with precipitation: {non_zero_precipitation_day_percentage:.1f}%")

if __name__ == "__main__":
    main()