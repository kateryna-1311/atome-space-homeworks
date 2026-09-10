numbers = [6, 2, -3, 1, 5, 10, 7]
names = ["Anna", "Bob", "Christopher"]
text = "Tun tun sahur"


# 1
def only_even(numbers: list[int]) -> list[int]:
    return [num for num in numbers if num % 2 == 0]


print(only_even(numbers))


# 2
def squares(numbers: list[int]) -> list[int]:
    return [num**2 for num in numbers]


print(squares(numbers))


# 3
def name_lengths(names: list[str]) -> list[int]:
    return [len(name) for name in names]


print(name_lengths(names))


# 4
def clamp_negatives(numbers: list[int]) -> list[int]:
    return [num if num >= 0 else 0 for num in numbers]


print(clamp_negatives(numbers))


# 5
def count_long_words(words: list[str], min_length: int) -> int:
    return len([word for word in words if len(word) >= min_length])


print(count_long_words(names, 4))


# 6
def count_vowels(text: str) -> int:
    vowels = "aeiou"
    return len([char for char in text.lower() if char in vowels])


print(count_vowels(text))


# 7
def average(numbers: list[float]) -> float:
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


print(average(numbers))


# 8
def min_max(numbers: list[int]) -> tuple[int, int]:
    return (min(numbers), max(numbers))


print(min_max(numbers))


# 9
def unique_sorted(numbers: list[int]) -> list[int]:
    return sorted(list(set(numbers)))


print(unique_sorted(numbers))
