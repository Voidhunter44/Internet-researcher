# Internet Research Viewer - Extending Qwen Code Capabilities

## Project Overview

This project is designed to extend the capabilities of Qwen Code, bringing back the powerful internet research functionality that was once a core feature. After the removal of Qwen's built-in search feature, finding accurate and up-to-date information became challenging. The directions for doing things became outdated, and some information was scattered or deprecated. This tool aims to restore that functionality by providing a real-time internet research viewer that works seamlessly with Qwen Code.

## What is Qwen Code?

Qwen Code is an interactive CLI agent developed by Alibaba Group, specializing in software engineering tasks. It helps users with coding tasks, project management, and problem-solving through an intelligent command-line interface. While it's incredibly powerful, the removal of its search feature made it difficult to access current information directly from the tool.

## Project Purpose

This project bridges that gap by providing a file-based communication system that allows Qwen Code to perform internet research and view results in real-time. It monitors research requests and responses as they happen, providing a seamless experience similar to the original search functionality.

## Features

- **Real-time Research Monitoring**: Watch as Qwen Code performs web searches and retrieves information
- **File-based Communication**: Uses a simple file-watching mechanism for communication between components
- **Multi-engine Search**: Leverages both DuckDuckGo and Google search engines for comprehensive results
- **Content Fetching**: Retrieves and processes web page content for detailed information
- **Windows Forms UI**: Graphical interface showing research requests and responses in a chat-like format
- **Logging**: All activities are logged for review and debugging

## Installation

For installation instructions, please refer to the official Qwen Code documentation:
[Qwen Code Installation Guide](https://github.com/qwen-code/qwen-code)

### Prerequisites

- .NET 9.0 SDK or later (for building the viewer)
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

### Running the Pre-built Application

1. Double-click `scripts\run-viewer.bat` to start the viewer application
2. Double-click `scripts\run-engine.bat` to start the research engine
3. Create or modify `research_request.txt` with your search query
4. Watch the results appear in the viewer window

### Testing the System

To verify that everything is working correctly:

1. Check that `research_request.txt` contains a search query
2. Run the research engine using `scripts\run-engine.bat`
3. Wait a few seconds for the research to complete
4. Check that `research_response.txt` now contains the results
5. Run the viewer using `scripts\run-viewer.bat` to see the results in the UI

### Building the Application

If you need to rebuild the application:

1. Double-click `scripts\build-viewer.bat` to build the Windows Forms application
2. The executable will be created in `src\ResearchViewer\bin\Release\net9.0-windows\`

## How It Works

The system consists of two main components:

1. **Research Viewer (Windows Forms Application)**: A graphical application that monitors research activities by watching files in real-time
2. **Research Engine (Python Script)**: Performs actual web searches and communicates with the viewer through files

Communication happens through two files in the project root directory:
- `research_request.txt`: Contains the search query
- `research_response.txt`: Contains the search results

## Troubleshooting

### Common Issues

1. **Research engine not working**: Make sure the research engine is running from the project root directory, not from the ResearchEngine directory. The batch script `scripts\run-engine.bat` handles this correctly.

2. **Viewer not showing updates**: Ensure that both the viewer and research engine are running, and that you're editing the `research_request.txt` file in the project root directory.

3. **Python packages missing**: If you get import errors, make sure you've installed all required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Permission errors**: If you get permission errors when writing files, make sure no other processes are locking the research files.

## Contributing

This project is organized to be easily shared and contributed to on GitHub. All source code is in the `src` directory, and all utility scripts are in the `scripts` directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.