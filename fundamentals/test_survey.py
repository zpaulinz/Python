import pytest
from survey import AnonymousSurvey

@pytest.fixture 
def language_survey(): 
    """
    Create a survey for use in all test functions.
    """
    question = "What is your native language?"
    language_survey = AnonymousSurvey(question)
    return language_survey
    

def test_store_single_response(language_survey): 
    """Check if a single response is stored correctly."""
    language_survey.store_response('Polish')
    assert 'Polish' in language_survey.responses


def test_store_three_responses(language_survey):
    """Check if three individual responses are correctly stored."""
    responses = ['English', 'Spanish', 'Polish']
    for response in responses:
        language_survey.store_response(response)
        
    for response in responses:
        assert response in language_survey.responses



