#1 basic function
def count_vowels(i):
    vowels = "aeiouAEIOU"
    count= sum(1 for char in i if char in vowels)
    return count

#2 Default & Keyword Arguments
def make_shirt(size = "large", message = "I love python" ):
    print(f"The shirt size is {size} and it will have the message: {message}.")

#3 *args Practice
def merge_string(*args):
    return " ".join(args)

#4 **kwargs Practice
def setup_application(app_name, version, **kwargs):
    config = {"app_name": app_name, "version": version}
    config.update(kwargs)
    return config

#========================execution==========================

print("Task 1 set C of mastering function")

word = "Christian Paul Simbulan"
print(f"there are {count_vowels(word)} vowels in a string {word}")

print("Task 2 set C of mastering function")
make_shirt()
make_shirt("Xlarge", "SmallPP")

print("Task 3 set C of mastering function")
print(merge_string("NEVER","GONNA","GIVE","YOU","UP","NEVER","GONNA","LET","YOU","DOWNN"))

print("Task 4 set C of mastering function")
app_config = setup_application("MyApp", "1.0", debug=True, port=3000, environment="production")
print(app_config)

