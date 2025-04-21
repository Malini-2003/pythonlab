class InvalidScoreError(Exception):
    pass

def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError("Score must be between 0 and 100.")
    return "Score is valid!"

try:
    score = float(input("Enter exam score (0 to 100): "))
    print(validate_score(score))

except InvalidScoreError as e:
    print("Invalid score:", e)

except ValueError:
    print("Please enter a number.")
