from firecrawl import FirecrawlApp
import os 
import re 
import dotenv 
dotenv.load_dotenv()
firecrawl_api_key = os.getenv('firecrawl_api_key')
app = FirecrawlApp(api_key=firecrawl_api_key)
def remove_image_links(markdown_text):
    cleaned_text = re.sub(r'!\[.*?\]\(.*?\)', '', markdown_text)
    return cleaned_text

def web_content(url):
    response = app.scrape_url(url=url, params={
        'formats': [ 'markdown' ],
    })
    cleaned_markdown = remove_image_links(response['markdown'])
    return cleaned_markdown
