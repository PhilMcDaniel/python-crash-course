# bad import method because I want to keep file names starting with a number.
testing_your_code  = __import__('11_testing_your_code')

print("Enter 'q' at any time to quite")

while True:
    first = input("/nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("/nPlease give me a last name:")
    if last == 'q':
        break

    formatted_name = testing_your_code.get_formatted_name(first,last)
    print(f"\tNeatly formatted name: {formatted_name}.")