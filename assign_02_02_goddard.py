def main():
    salary = float(input("Enter salary: "))
    bonus_percentage = float(input("Enter bonus percentage: "))
    bonus = salary * (bonus_percentage / 100)
    print(f"Employee Bonus: ${bonus:.2f}")

if __name__ == "__main__":
    main()