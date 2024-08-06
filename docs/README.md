# Readwise Analyzer

Readwise Analyzer is a Python application designed to help users manage their reading lists by fetching, analyzing, and categorizing articles from the Readwise Reader feed. It integrates with an AI tool called [Fabric](https://github.com/danielmiessler/fabric) to rate each article, making it easier to decide which articles to prioritize for reading.

## Features

- **Fetch Articles**: Retrieve articles from the Readwise Reader API.
- **Scrape Content**: Extract content from article URLs.
- **AI Analysis**: Use Fabric AI to analyze and rate articles.
- **Categorize Articles**: Automatically sort articles into categories based on their ratings:
  - **S Tier**: Shortlist
  - **A Tier**: Read This Week
  - **B & C Tier**: Weekend List
  - **D Tier**: Archive

## Project Structure

```plaintext
readwise-analyzer/
│
├── src/
│   ├── __init__.py
│   ├── readwise.py            # Interact with Readwise API
│   ├── scraper.py             # Scrape content from URLs
│   ├── fabric_integration.py  # Analyze content with Fabric
│   ├── analysis.py            # Main analysis logic
│   └── run.py                 # Entry point for the application
│
├── tests/                     # Unit tests
├── config/
│   ├── config.yml             # Configuration settings
│   └── secrets.json           # Example secrets file
│
├── docs/                      # Documentation
│   ├── README.md              # Project overview (this file)
│   ├── setup.md               # Setup instructions
│   └── usage.md               # Usage instructions
│
├── .gitignore                 # Git ignore file
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables file
└── setup.py                   # Package setup script
```

## Installation

### Prerequisites

- **Python 3.7+**: Ensure Python is installed on your system.
- **Fabric AI**: The Fabric application must be installed and accessible from your command line.

### Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/readwise-analyzer.git
   cd readwise-analyzer
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**

   Create a `.env` file in the project root directory with your Readwise API key:

   ```
   READWISE_API_KEY=your_readwise_api_key
   ```

5. **Configure Settings:**

   Edit the `config/config.yml` file to customize settings, if necessary.

## Usage

To run the application, execute the following command:

```bash
python src/run.py
```

The application will:
- Fetch articles from the Readwise Reader feed.
- Scrape and analyze each article using Fabric.
- Categorize articles based on their ratings into different reading lists.

## Testing

To run tests, use the following command:

```bash
pytest tests/
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For questions or feedback, please open an issue.