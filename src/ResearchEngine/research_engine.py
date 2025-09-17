"""
Internet Research Engine
Performs web searches and research activities, saving results to files for monitoring
"""

import os
import time
import sys

# Ensure we're running from the project root directory
# Change to the project root directory (2 levels up from src/ResearchEngine)
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
os.chdir(project_root)
print(f"Research engine running in: {os.getcwd()}")

# File paths for communication - look in project root directory
RESEARCH_REQUEST_FILE = os.path.join(project_root, "research_request.txt")
RESEARCH_RESPONSE_FILE = os.path.join(project_root, "research_response.txt")

# Import the internet tool after setting the correct directory
from internet_tool import internet_tool

def read_request():
    """Read the research request from the file"""
    try:
        if os.path.exists(RESEARCH_REQUEST_FILE):
            with open(RESEARCH_REQUEST_FILE, 'r', encoding='utf-8') as f:
                return f.read().strip()
    except Exception as e:
        print(f"Error reading request file: {e}")
    return None

def write_response(response):
    """Write the research response to the file"""
    try:
        with open(RESEARCH_RESPONSE_FILE, 'w', encoding='utf-8') as f:
            f.write(response)
        return True
    except Exception as e:
        print(f"Error writing response file: {e}")
        return False

def perform_research(query):
    """Perform research based on the query"""
    try:
        # Search and fetch content
        results = internet_tool.search_and_fetch(query, 3)
        
        # Format results
        response_text = f"Research Results for: {query}\n\n"
        for i, result in enumerate(results, 1):
            response_text += f"{i}. {result.get('title', 'No title')}\n"
            response_text += f"   URL: {result.get('url', 'No URL')}\n"
            if 'snippet' in result:
                response_text += f"   Snippet: {result['snippet']}\n"
            if 'content' in result:
                response_text += f"   Content: {result['content'][:200]}...\n"
            if 'error' in result:
                response_text += f"   Error: {result['error']}\n"
            response_text += "\n"
        
        return response_text
    except Exception as e:
        return f"Error performing research: {str(e)}"

def main():
    """Main loop for the research engine"""
    print("Internet Research Engine started")
    print(f"Monitoring {RESEARCH_REQUEST_FILE} for research requests...")
    print(f"Writing responses to {RESEARCH_RESPONSE_FILE}")
    
    # Ensure the request file exists
    if not os.path.exists(RESEARCH_REQUEST_FILE):
        print(f"Creating initial research request file: {RESEARCH_REQUEST_FILE}")
        try:
            with open(RESEARCH_REQUEST_FILE, 'w', encoding='utf-8') as f:
                f.write("What is artificial intelligence?")
            print("Created initial research request file")
        except Exception as e:
            print(f"Error creating initial request file: {e}")
    
    last_request = ""
    
    while True:
        try:
            # Read the request
            request = read_request()
            
            # Print current request for debugging
            if request:
                print(f"Current request: '{request}'")
                print(f"Last request: '{last_request}'")
                print(f"Request changed: {request != last_request}")
            
            # If we have a new request, process it
            if request and request != last_request:
                print(f"New research request: {request}")
                last_request = request
                
                # Perform the research
                response = perform_research(request)
                print(f"Research completed, response length: {len(response)}")
                
                # Write the response
                if write_response(response):
                    print("Research response written successfully")
                    # Verify the response was written
                    try:
                        with open(RESEARCH_RESPONSE_FILE, 'r', encoding='utf-8') as f:
                            written_content = f.read()
                        print(f"Verified response file content length: {len(written_content)}")
                    except Exception as verify_ex:
                        print(f"Error verifying response file: {verify_ex}")
                else:
                    print("Failed to write research response")
            
            # Wait before checking again
            time.sleep(1)
            
        except KeyboardInterrupt:
            print("\nResearch engine stopped by user")
            break
        except Exception as e:
            print(f"Error in main loop: {e}")
            import traceback
            traceback.print_exc()
            time.sleep(5)  # Wait longer on error

if __name__ == "__main__":
    main()