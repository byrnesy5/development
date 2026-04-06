# Soccer ML Exploration

An exploratory codebase for applying different machine learning techniques to soccer data. Built as a personal reference — each notebook covers a distinct ML approach so you can revisit how each method works, what parameters matter, and how they compare.

## Data

All data comes from the [StatsBomb Open Data](https://github.com/statsbomb/open-data) — free, event-level match data covering select competitions including UEFA Euro 2020, Women's World Cup, La Liga, and more. No credentials required.

## Notebooks

| Notebook | Description |
|---|---|
| [00_data_exploration.ipynb](00_data_exploration.ipynb) | Documents available competitions, matches, lineups, events, and 360 freeze frame data |
| [01_la_liga_eda.ipynb](01_la_liga_eda.ipynb) | In-depth EDA of La Liga data — team/player aggregations, shot & xG analysis, pass stats, match tempo, home vs away |

More notebooks will be added as different ML techniques are applied to the dataset.

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync

# Launch Jupyter
uv run jupyter notebook
```

Then select the `.venv` interpreter as your kernel in VSCode or Jupyter.

## Dependencies

- `statsbombpy` — loads StatsBomb open data directly into pandas DataFrames
- `jupyter` — notebook environment
