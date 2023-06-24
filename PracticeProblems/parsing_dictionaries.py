# Jesus Carlos Martinez Gonzalez
# 15/06/2023
# Parsing Dictionaries

# Write a function called check_value. check_value should
# take as input two parameters: a dictionary and a string.
# Both the keys and the values in the dictionary will be
# strings. The string parameter will be the key to look up in
# the dictionary.
#
# check_value should look up the string in the dictionary and
# get its value. Its current value will always be a string;
# however, check_value should try to convert it to an integer
# and a float, then return a message indicating the success
# of those conversions:
#
# - If the key is not found in the dictionary, check_value
#   should return the string: "Not found!"
# - If the value corresponding to the key can be converted
#   to an integer, check_value should return the string:
#   "Integer!"
# - Otherwise, if the value corresponding to the key can be
#   converted to a float, check_value should return the
#   string: "Float!"
# - Otherwise, check_value should return the string:
#   "String!"
#
# You do not need to check for any other types. We suggest
# using error handling to try to convert the values to the
# corresponding data types.
#
# For example, given this dictionary:
#
# d = {"k1": "1.1", "k2": "1", "k3": "1.4.6", "k4": "a"}
#
# Here are some calls and their results:
#
# - check_value(d, "k1") -> "Float!"
# - check_value(d, "k2") -> "Integer!"
# - check_value(d, "k3") -> "String!"
# - check_value(d, "k4") -> "String!"
# - check_value(d, "k5") -> "Not found!"
#
# Hint: The error that arises when trying to convert a
# string to a type it can't convert to (e.g. "ABC" to a
# float) is a ValueError. The error that arises when
# trying to access a key that doesn't exist in a
# dictionary is a KeyError.


def check_value(d, k):
    if k not in d:
        return "Not found!"
    val = d[k]
    try:
        int(val)
        return "Integer!"
    except:
        pass
    try:
        float(val)
        return "Float!"
    except:
        pass
    return "String!"


# The lines below will test your code. Their output should
# match the examples above.
d = {"k1": "1.1", "k2": "1", "k3": "1.4.6", "k4": "a"}

print(check_value(d, "k1"))
print(check_value(d, "k2"))
print(check_value(d, "k3"))
print(check_value(d, "k4"))
print(check_value(d, "k5"))
