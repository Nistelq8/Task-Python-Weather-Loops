# # printer(elements)
# # - Accepts a list
# # - Prints every element of the list
# elements = [1,2,3,4]
# def printer(elements):
#     # Your code here
#     for element in elements:
#         print(element)
# printer(elements)


# to_celsius(temperatures)
# - Accepts a list of temperatures
#   in degrees Fahrenheit
# - Returns a list of temperatures
#   in degrees Celsius
# The conversion is:
#   C = (F - 32) * (5/9)
temperatures_list = [110,100,120,125]
def to_celsius(temperatures):
    # Your code here
    ctemp = []
    for temp in temperatures:
        ctemp.append((temp - 32) * (5/9))
        return ctemp
    # print(ctemp)
# to_celsius(temperatures)



# hottest_days(temperatures, threshold)
# - Accepts a list of temperatures
# - Accepts a threshold temperature
# - Returns a list of temperatures
#   that exceed the threshold
threshold_number = 111
def hottest_days(temperatures, threshold):
    # Your code here
    over_threshold = []
    for temp in temperatures:
        if temp > threshold:
            over_threshold.append(temp)
        # return over_threshold
    # print(over_threshold)
# hottest_days(temperatures, threshold)



# log_hottest_days(temperatures, threshhold)
# - Accepts a list of temperatures
#   IN DEGREES FAHRENHEIT
# - Accepts a threshold temperature
#   IN DEGREES FAHRENHEIT
# - Prints temperatures that exceed the
#   threshold IN DEGREES CELSIUS
# hint: you can combine
#       all previous functions

def print_hottest_days(temperatures, threshold):
    # # Your code here
    to_celsius(temperatures)
    hottest_days(temperatures, threshold)
    # threshold = (threshold - 32) * (5/9)
    c_threshold = []
    for temp in temperatures:
        if temp > threshold:
            c_threshold.append((temp - 32) * (5/9))
    print(c_threshold)
    return c_threshold
print_hottest_days(temperatures_list, threshold_number)
