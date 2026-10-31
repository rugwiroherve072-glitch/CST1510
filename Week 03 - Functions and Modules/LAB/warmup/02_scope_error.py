# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"
    print(status) #status is a local variable, it is not defined outside the function

check(87, 100)


