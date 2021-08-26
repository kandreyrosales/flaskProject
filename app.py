from flask import Flask, request

app = Flask(__name__)


def complete_fibonacci(random_number):
    number_seq = int(random_number)
    list_of_n = []
    for i in range(number_seq):
        list_of_n.append(fibonacci(i))
    return list_of_n


@app.route('/', methods=['GET'])
def hello_world():
    complete_fibonacci(request.args.get("number_of_seq"))


def fibonacci(number_of_seq: int):
    if number_of_seq <= 1:
        return number_of_seq
    else:
        return fibonacci(number_of_seq - 1) + fibonacci(number_of_seq - 2)


if __name__ == '__main__':
    # fibonacci(5)
    pass





