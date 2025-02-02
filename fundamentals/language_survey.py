from survey import AnonymousSurvey

# Define the question and create the survey.
question = "What is your native language?"
language_survey = AnonymousSurvey(question)

# Display the question and store the responses.
language_survey.show_questions()
print("Type 'q' to quit the program.\n")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

# Display the survey results.
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()
