# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   Lab: Topic 12 (individual)
# Date:         12 November 2025

# // IMPORTS //

import numpy as np
import matplotlib.pyplot as plt

# // CONFIGURATION //

data_file = "WeatherDataCLL.csv"

# // LE PROGRAMME //

# // PLOT 1 //

x_values = []
average_wet_bulb_temperature_values = []
average_pressure_values = []

with open(data_file, mode="r", newline="") as raw_data:
    for i, line in enumerate(raw_data):
        if i == 0:
            continue
        line = line.rstrip("\r\n")
        parts = line.split(",")
        x_values.append(i)
        if parts[3] == "":
            average_wet_bulb_temperature_values.append(np.nan)
        else:
            average_wet_bulb_temperature_values.append(float(parts[3]))
        if parts[2] == "":
            average_pressure_values.append(np.nan)
        else:
            average_pressure_values.append(float(parts[2]))

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

line1, = ax1.plot(x_values, average_wet_bulb_temperature_values, color="red", label="Avg Wet Bulb Temp")
ax1.set_xlabel("Days")
ax1.set_ylabel("Average Wet Bulb Temperature, F", rotation=90)

line2, = ax2.plot(x_values, average_pressure_values, color="blue", label="Avg Pressure")
ax2.set_ylabel("Average Pressure, in Hg", rotation=90)

lines = [line1, line2]
ax1.legend(lines, [l.get_label() for l in lines], loc="lower left")
plt.title("Average Wet Bulb Temperature and Average Pressure")

# // PLOT 2 //

plt.figure(2)

x_values = []
average_wind_speed_values = []

with open(data_file, mode="r", newline="") as raw_data:
    for i, line in enumerate(raw_data):
        if i == 0:
            continue
        line = line.rstrip("\r\n")
        parts = line.split(",")
        x_values.append(i)
        if parts[4] == "":
            average_wind_speed_values.append(np.nan)
        else:
            average_wind_speed_values.append(float(parts[4]))

plt.hist([v for v in average_wind_speed_values if not np.isnan(v)], bins=33, color="green", edgecolor="black")
plt.title("Histogram of Average Wind Speed")
plt.xlabel("Average Wind Speed, mph")
plt.ylabel("Number of Days")

# // PLOT 3 //

plt.figure(3)

average_dew_point_values = []
average_relative_humidity_values = []
point_bank = []

with open(data_file, mode="r", newline="") as raw_data:
    for i, line in enumerate(raw_data):
        if i == 0:
            continue
        line = line.rstrip("\r\n")
        parts = line.split(",")
        if parts[1] == "":
            continue
        if parts[6] == "":
            continue
        plt.scatter(float(parts[1]), float(parts[6]))

plt.title("Average Relative Humidity vs Average Dew Point")
plt.xlabel("Average Dew Point (F)")
plt.ylabel("Average Relative Humidity (%)")

# // PLOT 4 //

month_data = {
    month: {"average": [], "high": [], "low": [], "precip": []}
    for month in range(1, 13)
}
month_precip_totals = {month: {} for month in range(1, 13)}

with open(data_file, mode="r", newline="") as raw_data:
    for i, line in enumerate(raw_data):
        if i == 0:
            continue
        parts = line.rstrip("\r\n").split(",")
        if not parts[0]:
            continue
        try:
            date_parts = parts[0].split("/")
            month = int(date_parts[0])
            year = int(date_parts[2])
        except (ValueError, IndexError):
            continue
        if month not in month_data:
            continue
        column_map = {"average": 7, "high": 8, "low": 9, "precip": 5}
        for key, idx in column_map.items():
            if idx >= len(parts):
                continue
            value = parts[idx].strip()
            if value:
                val = float(value)
                month_data[month][key].append(val)
                if key == "precip":
                    totals = month_precip_totals.setdefault(month, {})
                    totals[year] = totals.get(year, 0.0) + val

months = np.arange(1, 13)
monthly_avg_temp = [
    np.mean(month_data[m]["average"]) if month_data[m]["average"] else np.nan
    for m in months
]
monthly_max_high = [
    max(month_data[m]["high"]) if month_data[m]["high"] else np.nan
    for m in months
]
monthly_min_low = [
    min(month_data[m]["low"]) if month_data[m]["low"] else np.nan
    for m in months
]
monthly_mean_total_precip = [
    np.mean(list(month_precip_totals[m].values()))
    if month_precip_totals[m]
    else np.nan
    for m in months
]

plt.figure(4)
ax4 = plt.gca()
ax4.bar(months, monthly_avg_temp, color="tab:orange")
ax4.plot(months, monthly_max_high, color="tab:red", label="High T")
ax4.plot(months, monthly_min_low, color="tab:blue", label="Low T")
ax4.plot(months, monthly_mean_total_precip, color="tab:green", label="Precip")
ax4.set_xticks(months)
ax4.set_xlabel("Month")
ax4.set_ylabel("Average Temperature, F\nMonthly Precipitation, in")
ax4.set_title("Temperature and Precipitation by Month")
ax4.legend(loc="upper left")

# // REVEAL THE GRAPHS //

plt.show()