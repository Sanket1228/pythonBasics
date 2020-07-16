def my_function(country="Norway"):
    print("I am from " + country)

my_function("India")
my_function("Australia")
my_function()               # Only this time value of country will be default i.e. "Norway"
my_function("England")