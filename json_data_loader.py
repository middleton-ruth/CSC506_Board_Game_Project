"""
JSON Data Loader Module
Handles importing board game data from JSON file and converting to BoardGame objects.
This is a cleaner alternative to Excel-based loading.
"""

import json
from typing import List
from board_game import BoardGame


class JSONDataLoader:
    """Loads and parses board game data from JSON file."""

    def __init__(self, file_path: str = "board_games_data.json", verbose: bool = True):
        """
        Initialize data loader.

        Args:
            file_path: Path to the JSON file containing board game data
            verbose: Whether to print loading messages
        """
        self.file_path = file_path
        self.games: List[BoardGame] = []
        self.verbose = verbose

    def load_games(self) -> List[BoardGame]:
        """
        Load games from JSON file.

        Returns:
            List of BoardGame objects
        """
        if self.verbose:
            print(f"Loading games from {self.file_path}...")

        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            games = []
            for game_data in data:
                try:
                    game = self._parse_game(game_data)
                    if game:
                        games.append(game)
                except Exception as e:
                    if self.verbose:
                        print(f"Warning: Could not parse game: {e}")
                    continue

            self.games = games
            if self.verbose:
                print(f"Successfully loaded {len(games)} games!")
            return games

        except FileNotFoundError:
            print(f"Error: File {self.file_path} not found!")
            return []
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format: {e}")
            return []

    def _parse_game(self, data: dict) -> BoardGame:
        """
        Parse a game dictionary into a BoardGame object.

        Args:
            data: Dictionary with game data

        Returns:
            BoardGame object or None if invalid
        """
        # Validate required fields
        game_num = data.get('game_number', 0)
        title = data.get('title', '').strip()

        if not game_num or not title:
            return None

        # Parse weight
        weight = 0.0
        try:
            weight = float(data.get('weight', 0))
        except (ValueError, TypeError):
            weight = 0.0

        # Parse boolean fields
        painted = data.get('painted', False)
        if isinstance(painted, str):
            painted = painted.lower() in ['true', 'yes', '1']

        can_travel = data.get('can_travel', False)
        if isinstance(can_travel, str):
            can_travel = can_travel.lower() in ['true', 'yes', '1']

        # Parse location
        location = str(data.get('location', '')).strip()

        # Create BoardGame object
        game = BoardGame(
            game_number=game_num,
            title=title,
            category=str(data.get('category', '')),
            mechanisms=str(data.get('mechanisms', '')),
            description=str(data.get('description', '')),
            num_players=str(data.get('num_players', '')),
            playing_time=str(data.get('playing_time', '')),
            weight=weight,
            painted=painted,
            location=location,
            can_travel=can_travel,
            expansions=str(data.get('expansions', '')),
            links=str(data.get('links', '')),
            notes=str(data.get('notes', ''))
        )

        return game

    def save_games(self, games: List[BoardGame] = None) -> bool:
        """
        Save games back to JSON file.

        Args:
            games: List of BoardGame objects (uses self.games if None)

        Returns:
            True if successful, False otherwise
        """
        if games is None:
            games = self.games

        if not games:
            print("No games to save!")
            return False

        try:
            data = []
            for game in games:
                game_dict = {
                    'game_number': game.game_number,
                    'title': game.title,
                    'category': game.category,
                    'mechanisms': game.mechanisms,
                    'description': game.description,
                    'num_players': game.num_players,
                    'playing_time': game.playing_time,
                    'weight': game.weight,
                    'painted': game.painted,
                    'location': game.location,
                    'can_travel': game.can_travel,
                    'expansions': game.expansions,
                    'links': game.links,
                    'notes': game.notes
                }
                data.append(game_dict)

            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            print(f"Successfully saved {len(games)} games to {self.file_path}")
            return True

        except Exception as e:
            print(f"Error saving games: {e}")
            return False

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
            'locations': sorted(locations) if locations else ['No locations set'],
            'average_weight': round(avg_weight, 2)
        }


def main():
    """Test the JSON data loader."""
    loader = JSONDataLoader()
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
        print(f"  Location: {game.location or 'Not set'}")
        print(f"  Painted: {game.painted}")
        print(f"  Weight: {game.weight}")
        print(f"  Players: {game.num_players}")
        print(f"  Time: {game.playing_time}")


if __name__ == "__main__":
    main()
