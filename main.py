from csv_reader import csv_data

def main():
    a = csv_data("data/transactions.csv")
    b = csv_data("data/transactions_2.csv")
    
    print(a)
    print(b)

if __name__ == "__main__":
    main()