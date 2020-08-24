# python3
def max_pairwise_product_fast(numbers):
    max1 = max(numbers)
    numbers.remove(max1)
    max2 = max(numbers)
    max_product = max1 * max2
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
