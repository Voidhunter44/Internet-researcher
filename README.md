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

## Installation

For installation instructions, please refer to the official Qwen Code documentation:
[Qwen Code Installation Guide and Qwen Code Complete Introduction](https://github.com/QwenLM/qwen-code)

### Prerequisites

- Python 3.6 or later (for the research engine)
- Required Python packages: `requests`, `beautifulsoup4`, `ddgs`, `googlesearch-python`

### Install Python Packages

```bash
# Option 1: Install packages individually
pip install requests beautifulsoup4 ddgs googlesearch-python

# Option 2: Use the requirements.txt file
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

This project is organized to be easily shared and contributed to on GitHub. All source code is in the `src` directory, and all utility scripts are in the `scripts` directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.