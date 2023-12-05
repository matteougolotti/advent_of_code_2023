def solve(file_name: str) -> int:
    numbers = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            digits = [c for c in line if c.isdigit()]
            number = int(digits[0] + digits[-1])
            numbers.append(number)
    return sum(numbers)

if __name__ == "__main__":
    result = solve("input.txt")
    print(result)
