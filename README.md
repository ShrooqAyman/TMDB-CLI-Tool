# <a href="https://roadmap.sh/projects/tmdb-cli">TMDB CLI Tool</a> 🎬

A simple command-line interface (CLI) app that fetches and displays movies from The Movie Database (TMDB) API.

## Features

- View popular, top-rated, upcoming, and now-playing movies
- Simple CLI interface using `argparse`
- Clean terminal output
- TMDB API integration

## Usage

```bash
python main.py --type [popular|top|upcoming|playing]
```
## Setup
1. Clone the repository:
```bash
git clone https://github.com/ShrooqAyman/TMDB-CLI-Tool.git
cd TMDB-CLI-Tool
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create a .env file:
```bash
TMDB_API_KEY=your_tmdb_bearer_token_here
```
4. Run the app using one of the command options listed above.
