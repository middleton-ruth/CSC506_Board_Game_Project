"""
Game Manager - Handles user modifications to board game collection.
Best practices: Data persistence, input validation, bulk operations.
"""

from typing import List, Optional
from board_game import BoardGame
from json_data_loader import JSONDataLoader


class GameManager:
    """
    Manages board game collection with user modifications.
    Provides save/load functionality and bulk operations.
    """

    def __init__(self, data_file: str = "board_games_data.json"):
        """Initialize game manager with data file."""
        self.loader = JSONDataLoader(data_file)
        self.games: List[BoardGame] = []
        self.modified = False

    def load_games(self) -> List[BoardGame]:
        """Load games from file."""
        self.games = self.loader.load_games()
        self.modified = False
        return self.games

    def save_games(self) -> bool:
        """Save current game state to file."""
        if self.loader.save_games(self.games):
            self.modified = False
            return True
        return False

    def update_game_location(self, game_number: int, location: str) -> bool:
        """
        Update location for a specific game.

        Args:
            game_number: Game number to update
            location: New location

        Returns:
            True if successful, False otherwise
        """
        for game in self.games:
            if game.game_number == game_number:
                game.location = location.strip()
                self.modified = True
                return True
        return False

    def update_game_painted(self, game_number: int, painted: bool) -> bool:
        """
        Update painted status for a specific game.

        Args:
            game_number: Game number to update
            painted: New painted status

        Returns:
            True if successful, False otherwise
        """
        for game in self.games:
            if game.game_number == game_number:
                game.painted = painted
                self.modified = True
                return True
        return False

    def bulk_update_location(self, game_numbers: List[int], location: str) -> int:
        """
        Update location for multiple games at once.

        Args:
            game_numbers: List of game numbers to update
            location: New location for all games

        Returns:
            Number of games updated
        """
        count = 0
        for game_num in game_numbers:
            if self.update_game_location(game_num, location):
                count += 1
        return count

    def search_by_title(self, query: str) -> List[BoardGame]:
        """
        Search games by title (case-insensitive partial match).

        Args:
            query: Search query

        Returns:
            List of matching games
        """
        query_lower = query.lower()
        return [g for g in self.games if query_lower in g.title.lower()]

    def filter_by_criteria(
        self,
        location: Optional[str] = None,
        painted: Optional[bool] = None,
        min_weight: Optional[float] = None,
        max_weight: Optional[float] = None,
        min_players: Optional[int] = None,
        max_players: Optional[int] = None
    ) -> List[BoardGame]:
        """
        Filter games by multiple criteria.

        Args:
            location: Filter by location
            painted: Filter by painted status
            min_weight: Minimum complexity
            max_weight: Maximum complexity
            min_players: Minimum player count
            max_players: Maximum player count

        Returns:
            List of games matching all criteria
        """
        results = self.games

        if location:
            results = [g for g in results if g.location == location]

        if painted is not None:
            results = [g for g in results if g.painted == painted]

        if min_weight is not None:
            results = [g for g in results if g.weight >= min_weight]

        if max_weight is not None:
            results = [g for g in results if g.weight <= max_weight]

        if min_players is not None:
            # Parse player count (e.g., "2-4" -> check if min >= min_players)
            results = [g for g in results if self._check_min_players(g, min_players)]

        if max_players is not None:
            results = [g for g in results if self._check_max_players(g, max_players)]

        return results

    def _check_min_players(self, game: BoardGame, min_count: int) -> bool:
        """Check if game supports at least min_count players."""
        try:
            player_range = game.num_players.split('-')
            min_p = int(player_range[0])
            return min_p <= min_count
        except (ValueError, IndexError):
            return True

    def _check_max_players(self, game: BoardGame, max_count: int) -> bool:
        """Check if game supports up to max_count players."""
        try:
            player_range = game.num_players.split('-')
            max_p = int(player_range[-1])
            return max_p >= max_count
        except (ValueError, IndexError):
            return True

    def get_statistics(self) -> dict:
        """Get comprehensive statistics about the collection."""
        stats = self.loader.get_summary_stats()

        # Add more detailed statistics
        if self.games:
            # Category distribution
            categories = {}
            for game in self.games:
                cat = game.category
                categories[cat] = categories.get(cat, 0) + 1

            # Top categories
            top_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)[:5]

            # Player count analysis
            solo_games = len([g for g in self.games if g.is_solo_playable()])
            two_player = len([g for g in self.games if '2' in g.num_players])

            stats['category_distribution'] = dict(top_categories)
            stats['solo_games'] = solo_games
            stats['two_player_games'] = two_player

        return stats

    def has_unsaved_changes(self) -> bool:
        """Check if there are unsaved changes."""
        return self.modified


def main():
    """Test game manager functionality."""
    print("=" * 80)
    print("GAME MANAGER TEST")
    print("=" * 80)

    manager = GameManager()
    manager.load_games()

    # Test search
    print("\n1. Search for 'Catan':")
    results = manager.search_by_title("Catan")
    for game in results[:5]:
        print(f"  - {game.title}")

    # Test filter
    print("\n2. Filter: Weight 3.5-4.5:")
    results = manager.filter_by_criteria(min_weight=3.5, max_weight=4.5)
    print(f"  Found {len(results)} games")
    for game in results[:5]:
        print(f"  - {game.title} (Weight: {game.weight})")

    # Test update
    print("\n3. Update game location:")
    if manager.update_game_location(1, "Game Room"):
        print("  ✓ Updated game #1 location to 'Game Room'")
        print(f"  Has unsaved changes: {manager.has_unsaved_changes()}")

    # Test statistics
    print("\n4. Collection Statistics:")
    stats = manager.get_statistics()
    print(f"  Total Games: {stats['total_games']}")
    print(f"  Solo Games: {stats.get('solo_games', 'N/A')}")
    print(f"  Average Complexity: {stats['average_weight']}")

    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()
