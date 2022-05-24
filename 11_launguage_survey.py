# bad import method because I want to keep file names starting with a number.
Survey  = __import__('11_survey')

# define a question, and make a survey.
question = "What language did you first learn to speak?"
my_survey = Survey.AnonymousSurvey(question)

# Show the question and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# show the results
my_survey.show_results()