# Tradingview scrap
Basic Selenium [Trading View](https://www.tradingview.com/) scrapper. This script is meant to be used with a cronjob or any other scheduling service.

To execute it once you need to call it and pass the file path where your `.csv` data will be saved and then the names of the Trading View stock addres. Example:

`./scrap_stock.py data.csv BMFBOVESPA-B3SA3 BMFBOVESPA-DI1F2025 BMFBOVESPA-DI1F2033`

This comand will take the current B3SA3, DI1F2025 and DI1F2033 price and save it in an already existing `data.csv` file.

You also need [Selenium](https://www.selenium.dev/documentation/webdriver/) installed with the coresponding [Gecko](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/#quick-reference) driver.
