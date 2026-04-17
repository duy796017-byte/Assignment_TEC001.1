def count_non_empty_lines(filename):
    count = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip() != "":
                count += 1
    return count


def find_keyword_lines(filename, keyword):
    result = []
    with open(filename, 'r', encoding='utf-8') as f:
        for index, line in enumerate(f, start=1):
            if keyword in line:
                result.append(index)
    return result


def write_uppercase_file(input_file, output_file="output.txt"):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content.upper())


def average_score(filename):
    total = 0
    count = 0

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            name, score = line.strip().split(',')
            total += float(score)
            count += 1

    return total / count if count > 0 else 0


if __name__ == "__main__":
    while True:
        print("\n--- MENU ---")
        print("1. Count non-empty lines")
        print("2. Find lines containing a keyword")
        print("3. Convert file to uppercase")
        print("4. Calculate average score")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            file = input("Enter filename: ")
            print("Number of non-empty lines:", count_non_empty_lines(file))

        elif choice == "2":
            file = input("Enter filename: ")
            keyword = input("Enter keyword: ")
            print("Keyword found at lines:", find_keyword_lines(file, keyword))

        elif choice == "3":
            file = input("Enter filename: ")
            write_uppercase_file(file)
            print("output.txt has been created")

        elif choice == "4":
            file = input("Enter score file: ")
            print("Average score:", average_score(file))

        elif choice == "0":
            break

        else:
            print("Invalid choice, please try again!")