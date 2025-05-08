import os
from src.data_processor import DataProcessor

def main():
    base_path = os.path.join(os.getcwd(), 'data')

    # Process CSV file
    csv_path = os.path.join(base_path, 'sample_junk_mail.csv')
    processor_csv = DataProcessor(csv_path)
    processor_csv.load_data()
    processor_csv.initial_processing()

    # Process Parquet file
    parquet_path = os.path.join(base_path, 'Sample_data_2.parquet')
    processor_parquet = DataProcessor(parquet_path)
    processor_parquet.load_data()
    processor_parquet.initial_processing()

    # Process Text file
    text_path = os.path.join(base_path, 'sample_text.txt')
    processor_text = DataProcessor(text_path)
    processor_text.load_data()
    processor_text.initial_processing()

    # Process Images
    images_path = os.path.join(base_path, 'images')
    processor_images = DataProcessor(images_path)
    processor_images.load_data()
    processor_images.initial_processing()

if __name__ == "__main__":
    main()
