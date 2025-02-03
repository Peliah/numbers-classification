import pytest
from app.services.number_classifier import NumberClassifier

def test_is_armstrong():
    classifier = NumberClassifier()
    assert classifier.is_armstrong(371) == True
    assert classifier.is_armstrong(123) == False

def test_is_prime():
    classifier = NumberClassifier()
    assert classifier.is_prime(2) == True
    assert classifier.is_prime(4) == False
    assert classifier.is_prime(17) == True

def test_get_properties():
    classifier = NumberClassifier()
    assert classifier.get_properties(371) == ["armstrong", "odd"]
    assert classifier.get_properties(370) == ["armstrong", "even"]