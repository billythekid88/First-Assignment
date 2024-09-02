Billy Goddard
MMIS 6391
Assignment 2
08/31/2024
def main():
    prices = map(float, input("Enter prices: ").split())
    quantities = map(int, input("Enter quantities: ").split())
    total_sales = sum(p * q for p, q in zip(prices, quantities))
    print(f"Total Sales: ${total_sales:.2f}")

if __name__ == "__main__":
    main()