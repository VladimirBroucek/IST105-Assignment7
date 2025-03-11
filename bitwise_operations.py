import sys

def validate_input(numbers):
    try:
        return [int(num.strip()) for num in numbers.split(",")]
    except ValueError:
        return None

def bitwise_operations(numbers):
    if not numbers:
        return "Error: No valid numbers provided."

    and_result = numbers[0]
    or_result = numbers[0]
    xor_result = numbers[0]

    for num in numbers[1:]:
        and_result &= num
        or_result |= num
        xor_result ^= num

    return and_result, or_result, xor_result

def filter_numbers(numbers, threshold):
    return [num for num in numbers if num > threshold]

def main():
    if len(sys.argv) < 3:
        print("Error: Invalid input. Provide a list of numbers and a threshold.")
        return

    numbers_str = sys.argv[1]
    threshold_str = sys.argv[2]

    numbers = validate_input(numbers_str)

    if numbers is None:
        print("Error: Invalid input. Ensure you provide integers separated by commas.")
        return

    try:
        threshold = int(threshold_str)
    except ValueError:
        print("Error: Invalid threshold. Provide a valid integer.")
        return

    and_result, or_result, xor_result = bitwise_operations(numbers)
    filtered_numbers = filter_numbers(numbers, threshold)

    print("<pre>")
    print("Bitwise Operations Result:")
    print(f"- AND result: {and_result}")
    print(f"- OR result: {or_result}")
    print(f"- XOR result: {xor_result}\n")

    print(f"Numbers greater than {threshold}: {', '.join(map(str, filtered_numbers)) if filtered_numbers else 'None'}")
    print("</pre>")

if __name__ == "__main__":
    main()