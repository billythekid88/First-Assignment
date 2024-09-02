def main():
    original_price = float(input("Enter original price: "))
    discount_percentage = float(input("Enter discount percentage: "))
    discounted_price = original_price * (1 - discount_percentage / 100)
    print(f"Discounted Price: ${discounted_price:.2f}")

if __name__ == "__main__":
    main()