def random_num():
    # Import the random module:
    import random
    random.randint(20,31)
    # Use random.randint to produce a random integer between
    # 20 and 30 and save it to a variable called answer:
    answer = random.randint(20,31)
    return answer
print(random_num())