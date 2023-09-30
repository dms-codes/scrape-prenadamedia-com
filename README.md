# Prenada Media Scraper

This Python script is designed to scrape book information from the [Prenada Media website](https://prenadamedia.com/). It gathers data such as book titles, authors, prices, publication years, descriptions, availability, ISBNs, weights, dimensions, page counts, cover types, and image URLs. The scraped data is then stored in a CSV file for further analysis or use.

## Features

- Scrapes book data from the Prenada Media website.
- Retrieves a variety of book information.
- Supports scraping multiple pages within each category.
- Automatically determines if a book is out of stock.

## Prerequisites

Before running the script, make sure you have the following Python libraries installed:

- `requests`: To make HTTP requests.
- `BeautifulSoup`: For web scraping.

You can install these libraries using `pip`:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Modify the script to specify the `HOME_URL` variable with the URL of the Prenada Media category you want to scrape.

2. Run the script by executing the following command in your terminal:

```bash
python your_script_name.py
```

3. The script will scrape book data from the specified category, including details like titles, authors, prices, and more.

4. The scraped data will be stored in a CSV file named 'data.csv' in the same directory as the script.

## Configuration

- `HOME_URL`: The URL of the Prenada Media category you want to scrape.
- `COLUMNS`: The column names for the CSV file where the data will be saved.
- `STOCK`: The default stock value for in-stock items (modify as needed).

## Example

Suppose you want to scrape books from a specific Prenada Media category. After running the script, you will find the scraped data saved in 'data.csv' in the script's directory.

## License

This script is provided under the [MIT License](LICENSE).
```

Replace `"your_script_name.py"` with the actual name of your script. You can also add more details to the README.md file, such as installation instructions and additional usage examples, based on your project's specific needs.
