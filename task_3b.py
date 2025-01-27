def which_school(age: int) -> str:
    # Prevent negative ages
    if age < 0:
        raise ValueError("Bro has NOT been born yet")
    elif age < 3:
        return "You are too young for school"
    elif age < 5:
        return "You can go to preschool"
    elif age < 12:
        return "You can go to primary school"
    elif age < 18:
        return "You can go to secondary school"
    # 18 and over
    else:
        return "You do not have to go to school"
    
# Test cases
for age in range(-1, 21):
    try:
        print(f"Age {age}: {which_school(age)}")
    except ValueError as e:
        print(f"Age {age}: Error: {e}")