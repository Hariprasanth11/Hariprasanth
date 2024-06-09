def find_largest_and_smallest():
    num_elements = int(input("Enter no. of elements: "))
    elements = []
    for i in range(1, num_elements + 1):
        element = int(input(f"Enter element {i}: "))
        elements.append(element)
    largest = max(elements)
    smallest = min(elements)
    print(f"Largest element: {largest}")
    print(f"Smallest element: {smallest}")
if __name__ == "__main__":
    find_largest_and_smallest()
