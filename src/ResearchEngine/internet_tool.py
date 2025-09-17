"""
Internet Access Tool
Provides web search and content fetching capabilities for the research engine
"""

import requests
from bs4 import BeautifulSoup
from ddgs import DDGS
from googlesearch import search
from typing import List, Dict, Optional
import time

class InternetAccessTool:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def search_duckduckgo(self, query: str, max_results: int = 5) -> List[Dict[str, str]]:
        """Search using DuckDuckGo"""
        try:
            results = []
            with DDGS() as ddgs:
                search_results = ddgs.text(query, max_results=max_results)
                if search_results:
                    for result in search_results:
                        if len(results) >= max_results:
                            break
                        results.append({
                            'title': result.get('title', 'No title'),
                            'url': result.get('href', ''),
                            'snippet': result.get('body', 'No snippet available')
                        })
            return results
        except Exception as e:
            return [{'error': f'DuckDuckGo search failed: {str(e)}'}]
    
    def search_google(self, query: str, max_results: int = 5) -> List[Dict[str, str]]:
        """Search using Google"""
        try:
            results = []
            search_results = search(query, num_results=max_results, sleep_interval=1)
            # Handle both string and object results
            count = 0
            for item in search_results:
                if count >= max_results:
                    break
                if isinstance(item, dict) and 'url' in item:
                    results.append(item)
                elif isinstance(item, str):
                    results.append({'url': item, 'title': 'Search Result'})
                count += 1
            return results
        except Exception as e:
            return [{'error': f'Google search failed: {str(e)}'}]
    
    def fetch_webpage(self, url: str) -> Dict[str, str]:
        """Fetch and parse a webpage"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract title
            title = soup.title.string if soup.title else "No title found"
            
            # Extract text content
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            text = soup.get_text()
            # Clean up whitespace
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = ' '.join(chunk for chunk in chunks if chunk)
            
            return {
                'title': title,
                'url': url,
                'content': text[:2000],  # Limit content length
                'status': 'success'
            }
        except Exception as e:
            return {
                'url': url,
                'error': f'Failed to fetch webpage: {str(e)}',
                'status': 'error'
            }
    
    def search_and_fetch(self, query: str, max_results: int = 3) -> List[Dict[str, str]]:
        """Search and fetch content from results"""
        # Try DuckDuckGo first
        results = self.search_duckduckgo(query, max_results)
        
        # If DuckDuckGo fails or returns no results, try Google
        if not results or (len(results) == 1 and 'error' in results[0]):
            print("DuckDuckGo search failed or returned no results, trying Google...")
            results = self.search_google(query, max_results)
        
        # If both search engines fail, return an error
        if not results or (len(results) == 1 and 'error' in results[0]):
            return [{'error': 'Both search engines failed to return results'}]
        
        # Fetch content for each result
        detailed_results = []
        for result in results:
            if 'url' in result and result['url'] and 'error' not in result:
                # Add a small delay to be respectful to servers
                time.sleep(1)
                content = self.fetch_webpage(result['url'])
                detailed_results.append({
                    **result,
                    **content
                })
            else:
                detailed_results.append(result)
        
        return detailed_results

# Create an instance for use
internet_tool = InternetAccessTool()