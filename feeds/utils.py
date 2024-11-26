import requests
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)

def extract_ogp_metadata(url):
    """
    Extract Open Graph Protocol (OGP) metadata from a given URL.
    
    Args:
        url (str): The URL to extract metadata from
    
    Returns:
        dict: A dictionary containing OGP metadata (image, description)
    """
    try:
        # Add a user agent to mimic a browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Fetch the webpage
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract OGP metadata
        og_image = soup.find('meta', property='og:image')
        og_description = soup.find('meta', property='og:description')
        
        return {
            'image': og_image['content'] if og_image and 'content' in og_image.attrs else None,
            'description': og_description['content'] if og_description and 'content' in og_description.attrs else None
        }
    
    except requests.RequestException as e:
        logger.error(f"Error fetching OGP metadata for {url}: {e}")
        return {'image': None, 'description': None}
    except Exception as e:
        logger.error(f"Unexpected error extracting OGP metadata for {url}: {e}")
        return {'image': None, 'description': None}