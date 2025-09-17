# Internet Research Engine - Extending Qwen Code Capabilities

## Project Overview

This project is designed to extend the capabilities of Qwen Code, bringing back the powerful internet research functionality that was once a core feature. After the removal of Qwen's built-in search feature, finding accurate and up-to-date information became challenging. The directions for doing things became outdated, and some information was scattered or deprecated. This tool aims to restore that functionality by providing a file-based internet research engine that works seamlessly with Qwen Code.

## What is Qwen Code?

Qwen Code is an interactive CLI agent developed by Alibaba Group, specializing in software engineering tasks. It helps users with coding tasks, project management, and problem-solving through an intelligent command-line interface. While it's incredibly powerful, the removal of its search feature made it difficult to access current information directly from the tool.

## Project Purpose

This project bridges that gap by providing a file-based communication system that allows Qwen Code to perform internet research. It monitors research requests and responses through files, providing a seamless experience similar to the original search functionality.

## Features

- **File-based Communication**: Uses a simple file-watching mechanism for communication
- **Multi-engine Search**: Leverages both DuckDuckGo and Google search engines for comprehensive results
- **Content Fetching**: Retrieves and processes web page content for detailed information
- **Logging**: All activities are logged for review and debugging

## Download & Installation

### Prerequisites

- Python 3.6 or later (for the research engine)
- Required Python packages: `requests`, `beautifulsoup4`, `ddgs`, `googlesearch-python`

### Download from GitHub

1. **Clone the repository** (requires Git):
   ```bash
   git clone https://github.com/Voidhunter44/internet-research-viewer.git
   ```

2. **Or download as ZIP**:
   - Click the green "Code" button at the top of this page
   - Select "Download ZIP"
   - Extract the ZIP file to your desired location

### Install Python Packages

```bash
# Navigate to the project directory
cd internet-research-viewer

# Option 1: Install packages individually
pip install requests beautifulsoup4 ddgs googlesearch-python

# Option 2: Use the requirements.txt file (recommended)
pip install -r requirements.txt
```

## Usage Instructions

### Running the Research Engine

1. Double-click `scripts\run-engine.bat` to start the research engine
2. Create or modify `research_request.txt` with your search query
3. Check `research_response.txt` for the results
4. View activities in `research.log`

### Testing the System

To verify that everything is working correctly:

1. Check that `research_request.txt` contains a search query
2. Run the research engine using `scripts\run-engine.bat`
3. Wait a few seconds for the research to complete
4. Check that `research_response.txt` now contains the results
5. Tell Qwen Code to look something up and tell Qwen where the downloaded repository is and it should understand and run the script.

### Integration with Qwen Code

To use this with Qwen Code:
1. Place the downloaded repository in a convenient location
2. Tell Qwen Code to perform research by creating/modifying the `research_request.txt` file
3. Qwen Code can monitor `research_response.txt` for results
4. The engine will automatically run in the background when started

## How It Works

The research engine monitors `research_request.txt` for search queries. When it detects a new query, it:

1. Performs web searches using DuckDuckGo (with Google as a fallback)
2. Fetches content from the top search results
3. Formats the results into a readable format
4. Writes the formatted results to `research_response.txt`

## Troubleshooting

### Common Issues

1. **Python packages missing**: If you get import errors, make sure you've installed all required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. **Permission errors**: If you get permission errors when writing files, make sure no other processes are locking the research files.

3. **No results in response file**: Check that:
   - The research engine is running
   - The request file contains a valid query
   - You wait a few seconds for processing to complete
   - Internet connection is working

## Contributing

Contributions are welcome! If you'd like to contribute to this project:

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a pull request

Please ⭐ Star this repository if you find it useful! It helps others discover the project and shows appreciation for the work done.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.