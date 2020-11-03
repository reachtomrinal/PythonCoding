from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple

print(platform())
print(platform(aliased=True, terse=True))
print(platform(aliased=True, terse=False))
print(platform(aliased=False, terse=True))

print(f"my machine is {machine()}")


print(f"my processor is : {processor()}")


print(f"my system is: {system()}")


print(f"my {platform()} version is: {version()}")


print(python_implementation())

print(python_version_tuple())


for attr in python_version_tuple():
    print(attr)



print(__name__) # If execute from here will print __main__
# if execute from another file print name of the file


x = """
"""
print(len(x))