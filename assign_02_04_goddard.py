def main():
    principal = float(input("Enter principal: "))
    annual_rate = float(input("Enter annual rate: "))
    years = int(input("Enter years: "))
    monthly_rate = annual_rate / 12 / 100
    payments = years * 12
    payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** -payments)
    print(f"Monthly Payment: ${payment:.2f}")

if __name__ == "__main__":
    main()