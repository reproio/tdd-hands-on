# Usage : $ pytest
from hiker import fizzbuzz
import subprocess


def test_fizzbuzz_return_n():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2


def test_fizzbuzz_return_fizz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(99) == "Fizz"


def test_fizzbuzz_return_buzz():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(100) == "Buzz"


def test_fizzbuzz_return_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"
    assert fizzbuzz(90) == "FizzBuzz"


def test_fizzbuzz_get_lines():
    """
    :param cmd: str 実行するコマンド.
    :rtype: generator
    :return: 標準出力 (行毎).
    """
    cmd = "python hiker.py"
    proc = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    line = proc.stdout.readline().decode("utf-8")
    assert line.split("\n")[0] == "1"

    line = proc.stdout.readline().decode("utf-8")
    assert line.split("\n")[0] == "2"

    line = proc.stdout.readline().decode("utf-8")
    assert line.split("\n")[0] == "Fizz"
