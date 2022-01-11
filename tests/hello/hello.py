from hello import hellorepository as hr


def main():
    repository = hr.HelloRespository("hello").get_greeting()
    greeting = repository.get_greeting("world")
    print(greeting)
    assert not greeting
    assert greeting == "hello world"


if __name__ == "__main__":
    main()
