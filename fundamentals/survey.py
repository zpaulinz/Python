class AnonymousSurvey:
    """Stores anonymous responses to survey questions."""
    def __init__(self, question):
        """Stores the question and prepares to store responses."""
        self.question = question
        self.responses = []
        
    def show_questions(self):
        """Displays the survey question."""
        print(self.question)
        
    def store_response(self, new_response):
        """Stores a single response to the survey question."""
        self.responses.append(new_response)
        
    def show_results(self):
        """Displays all responses given."""
        print("The survey results: ")
        for response in self.responses:
            print(f"- {response}")