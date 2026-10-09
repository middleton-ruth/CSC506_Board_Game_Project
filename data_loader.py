"""
Data Loader Module
Handles importing board game data from Excel file and converting to BoardGame objects.
"""

import pandas as pd
from typing import List
from board_game import BoardGame


class DataLoader:
    """Loads and parses board game data from Excel file."""

    def __init__(self, file_path: str = "board_games.xlsx"):
        """
        Initialize data loader.

        Args:
            file_path: Path to the Excel file containing board game data
        """
        self.file_path = file_path
        self.games: List[BoardGame] = []

    def load_games(self, sheet_name: str = "Game List") -> List[BoardGame]:
        """
        Load games from Excel file.

        Args:
            sheet_name: Name of the sheet to load (default: "Game List")

        Returns:
            List of BoardGame objects
        """
        print(f"Loading games from {self.file_path}, sheet: {sheet_name}...")

        # Read Excel file
        df = pd.read_excel(self.file_path, sheet_name=sheet_name)

        # The actual headers are in row 1 (index 1)
        # Row 0 has some meta info, so we'll skip it
        headers = df.iloc[1].values
        data = df.iloc[2:]  # Start from row 2 (actual data)

        # Create new dataframe with proper headers
        df_clean = pd.DataFrame(data.values, columns=headers)

        # Parse each row into BoardGame object
        games = []
        for idx, row in df_clean.iterrows():
            try:
                game = self._parse_row(row)
                if game:
                    games.append(game)
            except Exception as e:
                print(f"Warning: Could not parse row {idx}: {e}")
                continue

        self.games = games
        print(f"Successfully loaded {len(games)} games!")
        return games

    def _parse_row(self, row) -> BoardGame:
        """
        Parse a single row into a BoardGame object.

        Args:
            row: Pandas Series representing one row

        Returns:
            BoardGame object or None if invalid
        """
        # Get game number - this is our primary key
        try:
            game_num = int(row.get('Game Number', 0))
            if game_num == 0:
                return None
        except (ValueError, TypeError):
            return None

        # Get title
        title = str(row.get('Title', '')).strip()
        if not title or title == 'nan':
            return None

        # Parse painted status
        painted_val = str(row.get('Painted', '')).strip().lower()
        painted = painted_val == 'yes' or painted_val == 'true'

        # Parse weight (complexity)
        weight = 0.0
        try:
            weight_str = str(row.get('Weight (Scale 1 - 5)', '0'))
            # Extract first number from string like "3.10 / 5"
            if '/' in weight_str:
                weight_str = weight_str.split('/')[0].strip()
            weight = float(weight_str)
        except (ValueError, TypeError):
            weight = 0.0

        # Parse can_travel
        can_travel_val = str(row.get('Can Travel', '')).strip().lower()
        can_travel = can_travel_val == 'yes' or can_travel_val == 'true'

        # Parse and normalize location
        location = str(row.get('Game Location', '')).strip()
        if location.lower() == 'nan' or not location:
            location = ''

        # Create BoardGame object
        game = BoardGame(
            game_number=game_num,
            title=title,
            category=str(row.get('Category', '')),
            mechanisms=str(row.get('Game Mechanisms', '')),
            description=str(row.get('Description', '')),
            num_players=str(row.get('# of Players', '')),
            playing_time=str(row.get('Playing Time', '')),
            weight=weight,
            painted=painted,
            location=location,
            can_travel=can_travel,
            expansions=str(row.get('Expansions', '')),
            links=str(row.get('Links', '')),
            notes=str(row.get('Notes', ''))
        )

        return game

    def _expand_location_name(self, location: str) -> str:
        """
        Expand location abbreviations to full names.

        Args:
            location: Location code/abbreviation

        Returns:
            Expanded location name
        """
        # Mapping of abbreviations to full names
        expansions = {
            'GR': 'Game Room',
            'LL': 'LL',  # Will be updated later
        }

        # Handle compound locations (e.g., "GR, GR Closet" or "LL/GR")
        result = location
        for abbrev, full_name in expansions.items():
            # Replace whole word matches
            result = result.replace(abbrev + ' ', full_name + ' ')
            result = result.replace(abbrev + ',', full_name + ',')
            result = result.replace(abbrev + '/', full_name + '/')
            # Handle if it's at the end
            if result.endswith(abbrev):
                result = result[:-len(abbrev)] + full_name
            # Handle if it's the entire string
            if result == abbrev:
                result = full_name

        return result

    def get_summary_stats(self) -> dict:
        """
        Get summary statistics about the loaded games.

        Returns:
            Dictionary with various statistics
        """
        if not self.games:
            return {}

        total = len(self.games)
        painted = sum(1 for g in self.games if g.painted)
        can_travel = sum(1 for g in self.games if g.can_travel)
        solo_playable = sum(1 for g in self.games if g.is_solo_playable())

        # Get unique locations (normalized)
        locations = set(g.location.strip() for g in self.games if g.location and g.location.strip())

        # Expand location abbreviations for display
        expanded_locations = sorted([self._expand_location_name(loc) for loc in locations])

        # Get average weight
        weights = [g.weight for g in self.games if g.weight > 0]
        avg_weight = sum(weights) / len(weights) if weights else 0

        return {
            'total_games': total,
            'painted': painted,
            'unpainted': total - painted,
            'paint_percentage': (painted / total * 100) if total > 0 else 0,
            'can_travel': can_travel,
            'solo_playable': solo_playable,
            'unique_locations': len(locations),
            'locations': expanded_locations,
            'average_weight': round(avg_weight, 2)
        }


def main():
    """Test the data loader."""
    loader = DataLoader()
    games = loader.load_games()

    print("\n" + "=" * 80)
    print("COLLECTION SUMMARY")
    print("=" * 80)

    stats = loader.get_summary_stats()
    for key, value in stats.items():
        print(f"{key}: {value}")

    print("\n" + "=" * 80)
    print("SAMPLE GAMES (First 5):")
    print("=" * 80)
    for game in games[:5]:
        print(f"\n{game}")
        print(f"  Location: {game.location}")
        print(f"  Painted: {game.painted}")
        print(f"  Weight: {game.weight}")
        print(f"  Players: {game.num_players}")
        print(f"  Time: {game.playing_time}")


if __name__ == "__main__":
    main()
