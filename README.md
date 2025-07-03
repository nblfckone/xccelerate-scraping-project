# xccelerate-scraping-project

Scraping app for Booking.com

<!DOCTYPE html>
<html lang="en">
<body>

<h1>Booking.com Web Scraping and EDA Project</h1>

<p>
This project automates the process of scraping hotel data from Booking.com based on user-defined parameters (location, check-in, and check-out dates). The scraped data is then cleaned, stored in an SQLite database, and analyzed using Exploratory Data Analysis (EDA).
</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#features">Features</a></li>
    <li><a href="#requirements">Requirements</a></li>
    <li><a href="#setup-instructions">Setup Instructions</a></li>
    <li><a href="#how-to-use">How To Use</a></li>
    <li><a href="#exploratory-data-analysis-eda">Exploratory Data Analysis (EDA)</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
</ul>

<h2 id="features">Features</h2>
<ul>
    <li><strong>Dynamic Input</strong>: Collects user inputs for location, check-in date, and check-out date.</li>
    <li><strong>Web Scraping</strong>: Uses Selenium to scrape hotel names, prices, distances, and ratings from Booking.com.</li>
    <li><strong>Data Storage</strong>: Stores the scraped data in an SQLite database for easy access and analysis.</li>
    <li><strong>Data Cleaning</strong>: Cleans the raw data to remove inconsistencies and prepare it for analysis.</li>
    <li><strong>EDA</strong>: Generates visualizations and summary statistics to analyze hotel pricing trends and relationships between variables.</li>
    <li><strong>Export Options</strong>: Saves cleaned data to both SQLite and CSV formats for further use.</li>
</ul>

<h2 id="requirements">Requirements</h2>
To run this project, you need the following installed on your system:
<ul>
    <li><strong>Python 3.x</strong></li>
    <li><strong>Libraries</strong>:
        <ul>
            <li>`selenium`: For web scraping.</li>
            <li>`pandas`: For data manipulation and analysis.</li>
            <li>`numpy`: For numerical operations.</li>
            <li>`matplotlib` and `seaborn`: For data visualization.</li>
            <li>`sqlite3`: For database operations.</li>
        </ul>
    </li>
    <li><strong>Chrome WebDriver</strong>: Ensure the Chrome WebDriver matches your browser version.</li>
    <li><strong>Booking.com Access</strong>: A stable internet connection to access Booking.com.</li>
</ul>
Install the required Python libraries using:
<pre><code>pip install selenium pandas numpy matplotlib seaborn</code></pre>

<h2 id="setup-instructions">Setup Instructions</h2>
<ol>
    <li><strong>Clone the Repository</strong>:
        <pre><code>git clone https://github.com/your-username/booking-scraper.git 
cd booking-scraper</code></pre>
    </li>
    <li><strong>Install Dependencies</strong>:
        Install the required Python libraries:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Download Chrome WebDriver</strong>:
        <ul>
            <li>Download the Chrome WebDriver from <a href="https://sites.google.com/chromium.org/driver/ ">here</a>.</li>
            <li>Ensure the WebDriver version matches your Chrome browser version.</li>
            <li>Place the WebDriver executable in your system's PATH or specify its location in the code.</li>
        </ul>
    </li>
    <li><strong>Update Input Parameters</strong>:
        Modify the `input_city`, `check_in`, and `check_out` variables in the scraping script to match your desired parameters.
    </li>
    <li><strong>Run the Script</strong>:
        Execute the scraping script:
        <pre><code>python scrape_booking.py</code></pre>
        The script will:
        <ol>
            <li>Open Google Chrome and navigate to Booking.com.</li>
            <li>Scrape hotel names, prices, distances, and ratings.</li>
            <li>Store the data in an SQLite database (`hotels.db`).</li>
        </ol>
    </li>
</ol>

<h2 id="how-to-use">How To Use</h2>

### Step 1: Input Parameters

When prompted, provide the following inputs:

<ul>
    <li><strong>Check-In Date</strong>: Enter the check-in date in `YYYY-MM-DD` format.</li>
    <li><strong>Check-Out Date</strong>: Enter the check-out date in `YYYY-MM-DD` format.</li>
    <li><strong>City</strong>: Choose a city from the available options (`Florence`, `Rome`, `Sardinia`).</li>
</ul>
Example:
Please Input Checkin Date(YYY-MM-DD): 2023-10-01
Please Input Checkout Date (YYY-MM-DD): 2023-10-05
Please input a city selection: Florence, Rome, Sardinia: Rome

### Step 2: Scrape Data

The script will:

<ol>
    <li>Open Google Chrome and navigate to Booking.com.</li>
    <li>Scrape hotel names, prices, distances, and ratings.</li>
    <li>Store the data in an SQLite database (`hotels.db`).</li>
</ol>

### Step 3: Run EDA

After scraping, execute the EDA script:

<pre><code>python eda_booking.py</code></pre>

The script will:

<ol>
    <li>Load the data from the SQLite database.</li>
    <li>Clean the data (e.g., remove non-numeric characters from prices and distances).</li>
    <li>Generate visualizations and summary statistics.</li>
    <li>Save the cleaned data to a new SQLite database (`hotels_cleaned.db`) and a CSV file (`hotel_prices_cleaned.csv`).</li>
</ol>

<h2 id="exploratory-data-analysis-eda">Exploratory Data Analysis (EDA)</h2>
The EDA script performs the following tasks:
<ol>
    <li><strong>Data Cleaning</strong>:
        <ul>
            <li>Removes non-numeric characters from the `Prices` and `Distances` columns.</li>
            <li>Converts these columns to numeric types for analysis.</li>
        </ul>
    </li>
    <li><strong>Visualizations</strong>:
        <ul>
            <li><strong>Histogram</strong>: Displays the distribution of hotel prices.</li>
            <li><strong>Scatter Plot</strong>: Shows the relationship between hotel prices and distances to the city center.</li>
        </ul>
    </li>
    <li><strong>Summary Statistics</strong>:
        <ul>
            <li>Provides descriptive statistics (mean, median, standard deviation, etc.) for numeric columns.</li>
        </ul>
    </li>
    <li><strong>Export Options</strong>:
        <ul>
            <li>Saves the cleaned data to an SQLite database (`hotels_cleaned.db`) and a CSV file (`hotel_prices_cleaned.csv`).</li>
        </ul>
    </li>
</ol>

<h2 id="contributing">Contributing</h2>
I welcome contributions from the community! If you’d like to contribute, please follow these steps:
<ol>
    <li>Fork the repository.</li>
    <li>Create a new branch for your feature or bug fix:
        <pre><code>git checkout -b feature-name</code></pre>
    </li>
    <li>Commit your changes:
        <pre><code>git commit -m "Add feature or fix"</code></pre>
    </li>
    <li>Push your branch:
        <pre><code>git push origin feature-name</code></pre>
    </li>
    <li>Submit a pull request with a detailed description of your changes.</li>
</ol>

<h2>Acknowledgments</h2>
<ul>
    <li>Inspired by real-world web scraping and data analysis projects.</li>
    <li>Built using Python, Selenium, Pandas, Matplotlib, Seaborn, and SQLite.</li>
</ul>

<p>
Feel free to reach out if you have any questions or suggestions! 😊
</p>

</body>
</html>
