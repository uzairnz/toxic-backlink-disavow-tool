from urllib.parse import urlparse
import pandas as pd

def load_backlink_data(file_path):
    """
    Load backlink data from a CSV file and ensure correct data types.
    """
    backlink_data = pd.read_csv(file_path, delimiter=",", header=0)

    # Convert relevant columns to numeric
    numeric_columns = ["Page ascore", "External links", "Internal links"]
    for column in numeric_columns:
        backlink_data[column] = pd.to_numeric(backlink_data[column], errors='coerce')
    backlink_data.fillna({col: 0 for col in numeric_columns}, inplace=True)

    # Ensure string columns are treated as strings
    string_columns = ["Anchor", "Sitewide"]
    for column in string_columns:
        backlink_data[column] = backlink_data[column].astype(str)

    print(f"Loaded {len(backlink_data)} backlinks from {file_path}")
    return backlink_data

def analyze_backlinks(backlink_data):
    """
    Analyze backlinks to identify toxic ones based on given criteria.
    """
    print("Applying toxicity criteria...")

    toxic_links = backlink_data[
        (backlink_data['Page ascore'] > 30) |
        (backlink_data['External links'] > 500) |
        (backlink_data['Anchor'].str.contains("spam", case=False, na=False)) |
        (backlink_data['Sitewide'].str.lower() == "true")
    ]

    print(f"Total toxic links identified: {len(toxic_links)}")
    return toxic_links

def extract_domain(url):
    """
    Extract domain name from a URL.
    """
    parsed_url = urlparse(url)
    return parsed_url.netloc  # Returns the domain part of the URL

def prepare_disavow_file(toxic_links, output_file):
    """
    Create a Disavow file in the required format.
    """
    with open(output_file, 'w') as file:
        file.write("# Disavow file generated for toxic backlinks\n")
        for url in toxic_links['Source url']:
            domain = extract_domain(url)
            if domain:  # Ensure the domain is valid
                file.write(f"domain:{domain}\n")
    print(f"Disavow file saved as {output_file}")

def main():
    input_file = "backlinks_data.csv"  # Replace with your actual CSV file name
    output_file = "disavow_corrected.txt"  # File to save the disavow list

    # Load backlink data
    backlink_data = load_backlink_data(input_file)

    # Analyze backlinks
    toxic_links = analyze_backlinks(backlink_data)
    print(f"Identified {len(toxic_links)} toxic backlinks.")

    # Prepare Disavow file if there are toxic links
    if len(toxic_links) > 0:
        prepare_disavow_file(toxic_links, output_file)
    else:
        print("No toxic backlinks identified. No disavow file created.")

if __name__ == "__main__":
    main()
