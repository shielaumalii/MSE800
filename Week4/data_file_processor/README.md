1. main.py (Main Entry Point)
This file is responsible for running the program and invoking the necessary functions to load and process data. 

What’s happening in main.py?

File/Folder Discovery: It lists all files and subfolders inside the data/ folder. Each item (file or folder) is passed to the DataProcessor for processing.

Processing Files: For each item, it checks whether it's a file or folder. Based on the file extension, it delegates the task to DataProcessor to load and process the file.

Error Handling: If an error occurs (e.g., unsupported file type), the program catches it and continues processing the next file.

2. data_processor.py (Data Processing Logic)
This file contains the DataProcessor class, which is responsible for loading and processing different types of files.

Key Components of DataProcessor:

__init__: Initializes with the file path. The data is initially set to None.

load_data: Based on the file extension, it loads the data:

CSV (.csv): Uses pandas.read_csv.

Parquet (.parquet): Uses pandas.read_parquet.

Text (.txt): Reads the entire file content into a string.

Image Folder: Uses TensorFlow to load images from a directory.

initial_processing: Depending on the type of data:

For DataFrame (CSV/Parquet): It prints basic summary info, missing values, and descriptive statistics.

For Text: It displays the first 500 characters.

For Images: It previews a batch (if images are available) and shows the shape of the images and labels.

🚀 How It Works
Execution Flow:

When you run main.py, it looks inside the data/ directory for files to process.

It processes each file by:

Loading the data using DataProcessor.

Showing basic statistics or previews for CSV, Parquet, text, and images.

Supported File Types:

CSV: Loaded into a pandas.DataFrame for analysis.

Parquet: Loaded into a pandas.DataFrame for analysis.

Text Files: Simply reads and displays the content.

Image Folders: Loaded into TensorFlow as image datasets, ready for machine learning.

Processing Output:

Each file type outputs a summary or preview, such as the shape of images, missing values in a DataFrame, or the first few lines of a text file.

🛠 Next Steps 
Extend the Project:

Add Support for More File Types: For example, you could add support for JSON, Excel, etc.

Handle More Complex Image Processing: You could resize images, apply transformations, or even label them for training ML models.

Error Handling:

Logging: Add logging to track errors or successful processing into a file.

Advanced Error Handling: Handle scenarios where files are partially loaded, corrupted, or mismatched.
