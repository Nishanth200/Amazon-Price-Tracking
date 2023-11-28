# Amazon Price Tracker

This Python script tracks the price of a product on Amazon and sends an email notification if the price drops below a specified threshold.

## Usage

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Nishanth200/Amazon-Price-Tracking.git
    cd amazon-price-tracker
    ```

2. **Install Dependencies:**
    ```bash
    pip install requests beautifulsoup4
    ```
3. **Configure the Script**

Open the script and replace the placeholder values with your actual information:

- `my_email`: Your Gmail email address.
- `password`: Your Gmail password.
- `recipient_email`: The email address where you want to receive notifications.
- `product_link`: The link to the Amazon product you want to track.

## Script Details

- The script uses the `requests` library to fetch the Amazon webpage and `BeautifulSoup` for HTML parsing.
- It extracts the product's title and price from the Amazon webpage.
- If the price is below or equal to Rs. 50,000, it sends an email notification using the Gmail SMTP server.

## Note

Make sure to enable "Less secure app access" for your Gmail account if you're using your Gmail password for authentication.
