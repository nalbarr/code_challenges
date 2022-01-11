import pytest

import hello
from hello import hellorepository as hr


@pytest.fixture
def repository():
    repository = hr.HelloRepository("hello")
    return repository


def test_get_greeting(repository):

    greeting = repository.get_greeting("world")
    assert greeting is not ""
    assert greeting == "hello world"
