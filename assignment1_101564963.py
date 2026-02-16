"""
Author: Ghazaleh AzimiKorf
Assignment: #1
""" 


# Step b: Create 4 variables
# here I created 4 different variables with different data types

gym_member = "Alex Alliton"        # string value
preferred_weight_kg = 20.5         # float number
highest_reps = 25                  # integer number
membership_active = True           # boolean (True or False)


# Step c: Create a dictionary named workout_stats
# this dictionary stores friend names and their workout minutes (yoga, running, weightlifting)

workout_stats = {
    "Alex": (50, 40, 35),
    "Madeline": (30, 35, 25),
    "Sophia": (45, 50, 30)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
# I loop through each friend and calculate the total of their 3 activities

for friend in list(workout_stats.keys()):
    total_minutes = sum(workout_stats[friend])   # add yoga + running + weightlifting
    workout_stats[friend + "_Total"] = total_minutes  # save total in dictionary


# Step e: Create a 2D nested list called workout_list
# this is a list of lists that only keeps the workout activity numbers

workout_list = []

for friend in workout_stats:
    if "_Total" not in friend:   # I skip the total keys
        workout_list.append(list(workout_stats[friend]))


# Step f: Slice the workout_list
# here I use slicing to extract specific activity minutes

# Extract and print yoga and running minutes for all friends
print("Yoga and Running minutes:")
for row in workout_list:
    print(row[:2])   # first two values

# Extract and print weightlifting minutes for the last two friends
print("\nWeightlifting minutes (last two friends):")
for row in workout_list[-2:]:
    print(row[2])   # third value


# Step g: Check if any friend's total workout minutes are >= 120
# if the total is 120 or more, print a motivational message

for friend in workout_stats:
    if "_Total" in friend and workout_stats[friend] >= 120:
        name = friend.replace("_Total", "")
        print(f"\nGreat job staying active, {name}!")


# Step h: User input to look up a friend
# I ask the user to type a friend's name and check if it exists

user_input = input("\nEnter a friend's name: ")

if user_input in workout_stats:
    yoga, running, weightlifting = workout_stats[user_input]
    total = workout_stats[user_input + "_Total"]
    print(f"\nWorkout details for {user_input}:")
    print("Yoga:", yoga, "minutes")
    print("Running:", running, "minutes")
    print("Weightlifting:", weightlifting, "minutes")
    print("Total:", total, "minutes")
else:
    print(f"\nFriend {user_input} not found in the records.")


# Step i: Friend with highest and lowest total workout minutes
# here I find who has the highest and lowest total workout time

totals = {}

for friend in workout_stats:
    if "_Total" in friend:
        name = friend.replace("_Total", "")
        totals[name] = workout_stats[friend]

highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print("\nFriend with highest total workout minutes:", highest_friend)
print("Friend with lowest total workout minutes:", lowest_friend)
