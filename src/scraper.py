from duckduckgo_search import DDGS
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import time
import random

USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
]


def fetch_html(url):
    try:
        headers = {
            "User-Agent": random.choice(USER_AGENT_LIST),
            "Sec-Ch-Ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Mobile": "Windows",
        }
        req = Request(url, headers=headers)
        with urlopen(req) as response:
            return response.read()
    except Exception as e:
        print(f"Failed to fetch HTML for {url}: {e}")
        return None


def extract_text_from_html(html_content):
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        text = soup.get_text()
        return text
    except Exception as e:
        print(f"Failed to extract text: {e}")
        return None


def extract_html_content(query, regionCode, num_results=5):
    html_contents = []

    # Use DuckDuckGo search results
    with DDGS() as ddgs:
        for result in ddgs.text(
            query, region=regionCode, safesearch="off", timelimit="y"
        ):
            html = fetch_html(result["href"])
            if html:
                html_contents.append(html)
            if len(html_contents) >= num_results:
                break
            time.sleep(
                random.uniform(3, 5)
            )  # Add a random delay between requests to avoid rate limiting

    return html_contents


# if __name__ == "__main__":
#     query = "How to delete all lines in vim"  # Replace with your desired query
#     num_results = 1  # Number of results to fetch

#     html_contents = extract_html_content(query, num_results)

#     for i, html_content in enumerate(html_contents, start=1):
#         text_content = extract_text_from_html(html_content)
#         if text_content:
#             print(f"Text content for result {i}:")
#             print(text_content)
#             print("=" * 50)


def scrapeDuck(query, regionCode, numResults):
    # print(type(query))
    # print(query)
    # print("Scraping Web")
    html_contents = extract_html_content(query, regionCode, numResults)

    # print(type(html_contents))

    textContent = []
    ## TODO:  Fix Variable Naming
    for i, html_content in enumerate(html_contents, start=1):
        text_content = extract_text_from_html(html_content)
        if text_content:
            textContent.append(text_content)

            # print("{} Done.".format(i))
    return textContent


# query = "University Ranking in US for students with Low GPA"  # Replace with your desired query

# scrapeDuck(query)
