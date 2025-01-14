# Toxic Backlink Analyzer and Disavow Tool

This Python tool helps website owners analyze and identify toxic backlinks and generate a properly formatted disavow file for Google Search Console. It uses SEMrush-exported backlink data as input to streamline the process of managing harmful links and improving SEO performance.

## Features

- **Analyze SEMrush Backlink Data**: Automatically filter toxic backlinks based on spam score, excessive external links, spammy anchor text, and sitewide links.
- **Domain-Level Disavow File**: Generate a Google-compliant disavow file by extracting domain-level URLs.
- **Customizable Criteria**: Easily modify toxicity thresholds to suit specific needs.
- **Error Handling**: Ensures malformed or incomplete data is handled gracefully.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/uzairnz/disavow-tool.git
   cd disavow-tool
   ```
2. Install dependencies:
   ```bash
   pip install pandas
   ```

---

## Usage

### Step 1: Export Backlink Data from SEMrush

1. Log in to your [SEMrush account](https://www.semrush.com/).
2. Navigate to the **Backlink Audit** tool.
3. Export your backlink list in CSV format.
4. Save the file as `backlinks_data.csv` in the project directory.

### Step 2: Run the Script

1. Execute the script:
   ```bash
   python generate_disavow.py
   ```
2. The script will analyze the backlinks and create a disavow file named `disavow_corrected.txt` in the project directory.

### Step 3: Upload the Disavow File to Google

1. Go to the [Google Disavow Tool](https://search.google.com/search-console/disavow-links).
2. Upload the generated `disavow_corrected.txt` file.

---

## Configuration

- You can customize the analysis thresholds in the `analyze_backlinks` function:
  - **Spam Score**: Default is `> 30`.
  - **External Links**: Default is `> 500`.
  - **Anchor Text**: Flags anchor text containing "spam".
  - **Sitewide Links**: Flags sitewide backlinks marked as `TRUE`.

---

## Example Input

Ensure the SEMrush-exported CSV file has the following structure:

| Page ascore | Source title               | Source url                              | Target url                        | Anchor          | External links | Internal links | Sitewide | ... |
|-------------|----------------------------|-----------------------------------------|-----------------------------------|-----------------|----------------|----------------|----------|-----|
| 50          | Example Title              | http://example.com/spam-link           | https://yourwebsite.com/page1     | spam anchor     | 1000           | 500            | TRUE     | ... |
| 25          | Legit Title                | https://legitwebsite.com/good-link     | https://yourwebsite.com/page2     | good anchor     | 50             | 20             | FALSE    | ... |

---

## Output

The generated disavow file will contain entries like:

```
# Disavow file generated for toxic backlinks
domain:example.com
domain:another-spam-site.com
```

---

## Contribution

We welcome contributions! Here’s how you can help:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
