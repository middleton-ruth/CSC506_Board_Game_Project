"""
Custom Set Class Implementation
Requirement #3: Build a comprehensive Set class that supports union, intersection,
difference, and symmetric difference operations.
"""

from typing import List, Any, Callable, Optional
from board_game import BoardGame


class CustomSet:
    """
    Custom Set implementation supporting all standard set operations.

    This class demonstrates understanding of set theory and operations,
    implementing union, intersection, difference, and symmetric difference.
    """

    def __init__(self, elements: Optional[List[Any]] = None):
        """
        Initialize a set with optional elements.

        Args:
            elements: Initial elements for the set (duplicates will be removed)
        """
        self._elements = []
        if elements:
            for elem in elements:
                self.add(elem)

    def add(self, element: Any) -> None:
        """
        Add an element to the set (no duplicates).

        Args:
            element: Element to add
        """
        if element not in self._elements:
            self._elements.append(element)

    def remove(self, element: Any) -> None:
        """
        Remove an element from the set.

        Args:
            element: Element to remove

        Raises:
            ValueError: If element not in set
        """
        if element in self._elements:
            self._elements.remove(element)
        else:
            raise ValueError(f"Element {element} not in set")

    def contains(self, element: Any) -> bool:
        """
        Check if element is in set.

        Args:
            element: Element to check

        Returns:
            True if element is in set, False otherwise
        """
        return element in self._elements

    def size(self) -> int:
        """
        Get the number of elements in the set.

        Returns:
            Number of elements
        """
        return len(self._elements)

    def is_empty(self) -> bool:
        """
        Check if set is empty.

        Returns:
            True if set is empty
        """
        return len(self._elements) == 0

    def to_list(self) -> List[Any]:
        """
        Convert set to list.

        Returns:
            List of elements
        """
        return self._elements.copy()

    # ===== SET OPERATIONS =====

    def union(self, other: 'CustomSet') -> 'CustomSet':
        """
        Return a new set with elements from both sets (A ∪ B).

        Args:
            other: Another CustomSet

        Returns:
            New CustomSet containing all elements from both sets
        """
        result = CustomSet()
        # Add all elements from this set
        for elem in self._elements:
            result.add(elem)
        # Add all elements from other set
        for elem in other._elements:
            result.add(elem)
        return result

    def intersection(self, other: 'CustomSet') -> 'CustomSet':
        """
        Return a new set with elements common to both sets (A ∩ B).

        Args:
            other: Another CustomSet

        Returns:
            New CustomSet containing only common elements
        """
        result = CustomSet()
        for elem in self._elements:
            if other.contains(elem):
                result.add(elem)
        return result

    def difference(self, other: 'CustomSet') -> 'CustomSet':
        """
        Return a new set with elements in this set but not in other (A - B).

        Args:
            other: Another CustomSet

        Returns:
            New CustomSet containing elements only in this set
        """
        result = CustomSet()
        for elem in self._elements:
            if not other.contains(elem):
                result.add(elem)
        return result

    def symmetric_difference(self, other: 'CustomSet') -> 'CustomSet':
        """
        Return a new set with elements in either set but not both (A △ B).

        Args:
            other: Another CustomSet

        Returns:
            New CustomSet containing elements in exactly one of the sets
        """
        result = CustomSet()
        # Add elements in this set but not in other
        for elem in self._elements:
            if not other.contains(elem):
                result.add(elem)
        # Add elements in other set but not in this
        for elem in other._elements:
            if not self.contains(elem):
                result.add(elem)
        return result

    def is_subset(self, other: 'CustomSet') -> bool:
        """
        Check if this set is a subset of other (A ⊆ B).

        Args:
            other: Another CustomSet

        Returns:
            True if all elements of this set are in other
        """
        for elem in self._elements:
            if not other.contains(elem):
                return False
        return True

    def is_superset(self, other: 'CustomSet') -> bool:
        """
        Check if this set is a superset of other (A ⊇ B).

        Args:
            other: Another CustomSet

        Returns:
            True if all elements of other are in this set
        """
        return other.is_subset(self)

    def __str__(self) -> str:
        """String representation of set."""
        return "{" + ", ".join(str(e) for e in self._elements) + "}"

    def __repr__(self) -> str:
        """Official string representation."""
        return f"CustomSet({self._elements})"

    def __len__(self) -> int:
        """Support len() function."""
        return self.size()


class GameSet:
    """
    Specialized set class for BoardGame collections with filtering capabilities.
    """

    def __init__(self, games: Optional[List[BoardGame]] = None):
        """
        Initialize a game set.

        Args:
            games: Initial list of games
        """
        self.games = CustomSet(games if games else [])

    @staticmethod
    def from_filter(all_games: List[BoardGame],
                    predicate: Callable[[BoardGame], bool]) -> 'GameSet':
        """
        Create a GameSet by filtering games based on a predicate.

        Args:
            all_games: List of all games to filter from
            predicate: Function that returns True for games to include

        Returns:
            New GameSet with filtered games
        """
        filtered = [g for g in all_games if predicate(g)]
        return GameSet(filtered)

    def union(self, other: 'GameSet') -> 'GameSet':
        """Union of two game sets."""
        result = GameSet()
        result.games = self.games.union(other.games)
        return result

    def intersection(self, other: 'GameSet') -> 'GameSet':
        """Intersection of two game sets."""
        result = GameSet()
        result.games = self.games.intersection(other.games)
        return result

    def difference(self, other: 'GameSet') -> 'GameSet':
        """Difference of two game sets."""
        result = GameSet()
        result.games = self.games.difference(other.games)
        return result

    def symmetric_difference(self, other: 'GameSet') -> 'GameSet':
        """Symmetric difference of two game sets."""
        result = GameSet()
        result.games = self.games.symmetric_difference(other.games)
        return result

    def to_list(self) -> List[BoardGame]:
        """Convert to list of games."""
        return self.games.to_list()

    def size(self) -> int:
        """Get number of games in set."""
        return self.games.size()

    def __str__(self) -> str:
        """String representation."""
        games_list = self.games.to_list()
        if len(games_list) == 0:
            return "GameSet(empty)"
        titles = [g.title for g in games_list[:5]]
        if len(games_list) > 5:
            titles.append(f"... and {len(games_list) - 5} more")
        return f"GameSet({len(games_list)} games: {', '.join(titles)})"


def demo_integer_sets():
    """Demonstrate set operations with integers."""
    print("=" * 80)
    print("DEMO: Set Operations with Integers")
    print("=" * 80)

    # Create sets
    set_a = CustomSet([1, 2, 3, 4, 5])
    set_b = CustomSet([4, 5, 6, 7, 8])

    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print()

    # Union
    union = set_a.union(set_b)
    print(f"A ∪ B (Union): {union}")

    # Intersection
    intersection = set_a.intersection(set_b)
    print(f"A ∩ B (Intersection): {intersection}")

    # Difference
    difference = set_a.difference(set_b)
    print(f"A - B (Difference): {difference}")

    # Symmetric Difference
    sym_diff = set_a.symmetric_difference(set_b)
    print(f"A △ B (Symmetric Difference): {sym_diff}")

    print()
    print(f"Is A subset of B? {set_a.is_subset(set_b)}")
    print(f"Is A superset of B? {set_a.is_superset(set_b)}")


def demo_game_sets():
    """Demonstrate set operations with board games."""
    from json_data_loader import JSONDataLoader

    print("\n" + "=" * 80)
    print("DEMO: Set Operations with Board Games")
    print("=" * 80)

    # Load games
    loader = JSONDataLoader()
    all_games = loader.load_games()

    # Create different game sets using filters
    painted_games = GameSet.from_filter(all_games, lambda g: g.painted)
    gr_location_games = GameSet.from_filter(all_games, lambda g: "GR" in g.location)
    high_complexity = GameSet.from_filter(all_games, lambda g: g.weight >= 3.5)

    print(f"\nPainted games: {painted_games.size()}")
    print(f"Games in GR location: {gr_location_games.size()}")
    print(f"High complexity games (≥3.5): {high_complexity.size()}")
    print()

    # Intersection: Painted AND in GR
    painted_and_gr = painted_games.intersection(gr_location_games)
    print(f"Painted AND in GR: {painted_and_gr.size()} games")
    for game in painted_and_gr.to_list()[:5]:
        print(f"  - {game.title}")
    print()

    # Union: Painted OR high complexity
    painted_or_complex = painted_games.union(high_complexity)
    print(f"Painted OR High Complexity: {painted_or_complex.size()} games")
    print()

    # Difference: High complexity but NOT painted
    complex_unpainted = high_complexity.difference(painted_games)
    print(f"High Complexity but NOT Painted: {complex_unpainted.size()} games")
    for game in complex_unpainted.to_list()[:5]:
        print(f"  - {game.title} (weight: {game.weight})")


if __name__ == "__main__":
    # Demo with integers
    demo_integer_sets()

    # Demo with games
    demo_game_sets()
