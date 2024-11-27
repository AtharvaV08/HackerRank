# num_country_stamps = int(input())
# name_of_countries = set(input().split())
# for country in name_of_countries:
#     if num_country_stamps == name_of_countries:
#         name_of_countries.add(input())
#         print(len(name_of_countries))

num_country_stamps = int(input())  # First line: number of country stamps to be entered
name_of_countries = set()  # Initialize an empty set for country names

# Take input for 'num_country_stamps' number of countries
for i in range(num_country_stamps):
    country = input()  # Take one country name as input
    name_of_countries.add(country)  # Add country to the set

# Print the number of unique countries entered
print(len(name_of_countries))


