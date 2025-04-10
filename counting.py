feedback = input("Enter your feedback: ")

count = feedback.lower().split().count("good")

print(f"The word 'good' appears {count} times in your feedback.")
