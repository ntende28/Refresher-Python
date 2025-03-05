from collections import ChainMap

year_profit_data = [
    {'jan_profit': 15492.30, 'jan_holiday_profit': 2589.12},
    {'feb_profit': 17018.05, 'feb_holiday_profit': 3701.88},
    {'mar_profit': 11849.13},
    {'apr_profit': 9870.68},
    {'may_profit': 13662.34},
    {'jun_profit': 12903.54},
    {'jul_profit': 16965.08, 'jul_holiday_profit': 4360.21},
    {'aug_profit': 17685.69},
    {'sep_profit': 9815.57},
    {'oct_profit': 10318.28},
    {'nov_profit': 23295.43, 'nov_holiday_profit': 9896.55},
    {'dec_profit': 21920.19, 'dec_holiday_profit': 8060.79}
]

new_months_data = [
    {'jan_profit': 13977.85, 'jan_holiday_profit': 2176.43},
    {'feb_profit': 16692.15, 'feb_holiday_profit': 3239.74},
    {'mar_profit': 17524.35, 'mar_holiday_profit': 4301.92}
]

# Write your code below!
profit_map = ChainMap(*year_profit_data)

def get_profits(chainmap_var):
  last_year_standard_profit = 0.0
  last_year_holiday_profit = 0.0
  
  for key, val in chainmap_var.items():
    if 'holiday' in key:
      last_year_holiday_profit += val
    else:
      last_year_standard_profit += val

  return last_year_standard_profit, last_year_holiday_profit

last_year_standard_profit, last_year_holiday_profit = get_profits(profit_map)
print(f"Last year standard profit - {last_year_standard_profit}")
print(f"Last year holiday profit - {last_year_holiday_profit}")

for el in new_months_data:
  profit_map = profit_map.new_child(el)

current_year_standard_profit, current_year_holiday_profit = get_profits(profit_map)
print(f"Current year standard profit -  {current_year_standard_profit}")
print(f"Current year holiday profit -  {current_year_holiday_profit}")

year_diff_standard_profit = current_year_standard_profit - last_year_standard_profit
year_diff_holiday_profit = current_year_holiday_profit - last_year_holiday_profit

print(f"Difference in standard profits: {year_diff_standard_profit}")
print(f"Difference in holiday profits: {current_year_holiday_profit}")