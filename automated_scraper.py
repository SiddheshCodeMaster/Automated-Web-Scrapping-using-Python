from autoscraper import AutoScraper

amazon_url = "https://www.amazon.in/s?k=headphones"

wanted_list = ["₹498","ZEBRONICS-Zeb-Thunder-Connectivity-Sea-Green","54,499"]

# Building an autoscraper:

scraper = AutoScraper()
result =scraper.build(amazon_url,wanted_list)

print(result)