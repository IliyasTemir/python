def count_lines(filename):
    """Counts the number of lines in a text file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return sum(1 for _ in file)
    except FileNotFoundError:
        print(f"❌ The file '{filename}' was not found.")
        return None
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        return None

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    lines = count_lines(filename)
    
    if lines is not None:
        print(f"✅ The file '{filename}' has {lines} lines.")
