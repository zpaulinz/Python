from survey import AnonymousSurvey

def test_store_single_response(): 
    """Check if a single response is stored correctly."""
    question = "What is your native language?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('Polish')
    assert 'Polish' in language_survey.responses


def test_store_three_responses():
    """Check if three individual responses are correctly stored."""
    question = "What is your native language?"
    language_survey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Polish']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses
