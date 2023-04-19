

# duration in Day
day = int(input(""))
# total food cost per day
food_cost = int(input(""))
# one-way flight cost
flight_cost = int(input(""))
# cost of one night in a hotel
hotel_cost_night = int(input(""))

print((food_cost * day) + (flight_cost * 2) + (hotel_cost_night * (day - 1)))
