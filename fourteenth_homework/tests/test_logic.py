# import pytest
# from logic import add, divide, is_palindrome, Stack

# def test_add():
#     assert add(22.3, 10) == 32.3
#     assert add(-1, 1) == 0
#     assert add(0, 0) == 0

# def test_divide_by_zero():
#     with pytest.raises(ValueError):
#         divide(1, 0)

# def test_is_palindrom():
#     assert is_palindrome("apple") == False
#     assert is_palindrome("dad") == True

# def test_push_pop():
#     stack = Stack()
#     stack.push(1)
#     stack.push(2)
#     stack.push(3)
#     assert stack.pop() == 3
#     assert stack.pop() == 2
#     assert stack.pop() == 1

# def test_peek():
#     stack = Stack()
#     stack.push("a")
#     assert stack.peek() == "a"

# def test_is_empty_and_len():
#     stack = Stack()
#     assert stack.is_empty() is True
#     assert len(stack) == 0
#     stack.push(10)
#     assert stack.is_empty() is False
#     assert len(stack) == 1
#     stack.pop()
#     assert stack.is_empty() is True
#     assert len(stack) == 0

# def test_pop_raise_index():
#     stack = Stack()
#     with pytest.raises(IndexError):
#         stack.pop()

# def test_peek_raises_index():
#     stack = Stack()
#     with pytest.raises(IndexError):
#         stack.peek()
