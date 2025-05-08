from iris_loader import load_iris_data, print_flower_names, visualize_data

def main():
    df = load_iris_data()
    print_flower_names(df)
    visualize_data(df)  # Don't forget this line

if __name__ == "__main__":
    main()
