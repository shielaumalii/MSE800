from src.data_processor import DataProcessor
import os

def main():
    data_dir = 'Week4/data_file_processor/data' # Directory containing data files

    # Check if the directory exists
    if not os.path.exists(data_dir):
        print(f"Data directory does not exist: {data_dir}")
        return

    # Loop through files and directories inside /data
    for item in os.listdir(data_dir):
        item_path = os.path.join(data_dir, item)

        # Skip hidden files (like .DS_Store)
        if item.startswith('.'):
            continue

        try:
            print(f"\n📁 Processing: {item_path}")
            processor = DataProcessor(item_path) # Create DataProcessor object
            processor.load_data() # Load data based on file type
            processor.initial_processing() # Process and display initial data statistics
        except Exception as e:
            print(f"❌ Failed to process {item_path}: {e}")

if __name__ == "__main__":
    main()
