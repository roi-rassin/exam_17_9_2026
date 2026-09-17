# Start

def special_percentile(percent: int, numbers: list) -> float:
    sorted_numbers = sorted(numbers)
    position = (percent / 100) * (len(sorted_numbers) - 1)
    index = int(position)
    return sorted_numbers[index]

print(special_percentile(0, [50, 10, 40, 20, 30]))   # 10
print(special_percentile(25, [50, 10, 40, 20, 30]))  # 20
print(special_percentile(50, [50, 10, 40, 20, 30]))  # 30
print(special_percentile(100, [50, 10, 40, 20, 30])) # 50

# Stop