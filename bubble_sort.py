"""
Bubble Sort Implementation with Step-by-Step Visualization
Requirement #1: Implement bubble sort algorithm for sorting lists of integers
with step-by-step visualization.
"""

from typing import List, Callable, Any
from board_game import BoardGame
import time


class BubbleSort:
    """
    Bubble sort implementation with visualization capabilities.

    This class provides bubble sort for both simple integer lists and
    complex objects like BoardGame instances.
    """

    def __init__(self, visualize: bool = True, delay: float = 0.0) -> None:
        """
        Initialize bubble sort.

        Args:
            visualize: Whether to print step-by-step visualization
            delay: Delay in seconds between steps (for animation effect)

        Raises:
            ValueError: If delay is negative
        """
        if delay < 0:
            raise ValueError(f"Delay must be non-negative, got {delay}")

        self.visualize = visualize
        self.delay = delay
        self.comparison_count = 0
        self.swap_count = 0
        self.steps = []

    def sort_integers(self, arr: List[int]) -> List[int]:
        """
        Sort a list of integers using bubble sort.

        Args:
            arr: List of integers to sort

        Returns:
            Sorted list of integers

        Raises:
            TypeError: If arr is not a list
            ValueError: If arr is None or contains non-integer values
        """
        # Edge case: Validate input
        if arr is None:
            raise ValueError("Input array cannot be None")
        if not isinstance(arr, list):
            raise TypeError(f"Expected list, got {type(arr).__name__}")

        # Edge case: Empty list
        if len(arr) == 0:
            return []

        # Edge case: Single element
        if len(arr) == 1:
            return arr.copy()

        # Validate all elements are integers
        for i, elem in enumerate(arr):
            if not isinstance(elem, (int, float)):
                raise ValueError(f"Element at index {i} is not a number: {elem} (type: {type(elem).__name__})")

        # Create a copy to avoid modifying original
        arr_copy = arr.copy()
        n = len(arr_copy)

        self.comparison_count = 0
        self.swap_count = 0
        self.steps = []

        if self.visualize:
            print("=" * 80)
            print("BUBBLE SORT - INTEGER LIST")
            print("=" * 80)
            print(f"Initial array: {arr_copy}\n")

        for i in range(n):
            swapped = False

            if self.visualize:
                print(f"--- Pass {i + 1} ---")

            for j in range(0, n - i - 1):
                self.comparison_count += 1

                if self.visualize:
                    print(f"Comparing {arr_copy[j]} and {arr_copy[j + 1]}", end="")

                if arr_copy[j] > arr_copy[j + 1]:
                    # Swap elements
                    arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                    self.swap_count += 1
                    swapped = True

                    if self.visualize:
                        print(f" → SWAP!")
                        print(f"  Array: {arr_copy}")
                        self.steps.append(arr_copy.copy())
                else:
                    if self.visualize:
                        print(f" → No swap")

                if self.delay > 0:
                    time.sleep(self.delay)

            if not swapped:
                if self.visualize:
                    print(f"\nNo swaps in pass {i + 1} - array is sorted!")
                break

            if self.visualize:
                print()

        if self.visualize:
            print("=" * 80)
            print(f"FINAL SORTED ARRAY: {arr_copy}")
            print(f"Total Comparisons: {self.comparison_count}")
            print(f"Total Swaps: {self.swap_count}")
            print("=" * 80)

        return arr_copy

    def sort_games(self, games: List[BoardGame], key: Callable[[BoardGame], Any],
                   key_name: str = "value") -> List[BoardGame]:
        """
        Sort a list of BoardGame objects using bubble sort.

        Args:
            games: List of BoardGame objects to sort
            key: Function to extract the sort key from each game
            key_name: Name of the key for display purposes

        Returns:
            Sorted list of BoardGame objects

        Raises:
            TypeError: If games is not a list or key is not callable
            ValueError: If games is None or empty
        """
        # Edge case: Validate input
        if games is None:
            raise ValueError("Games list cannot be None")
        if not isinstance(games, list):
            raise TypeError(f"Expected list, got {type(games).__name__}")
        if not callable(key):
            raise TypeError("Key must be a callable function")

        # Edge case: Empty list
        if len(games) == 0:
            raise ValueError("Cannot sort empty list of games")

        # Edge case: Single element
        if len(games) == 1:
            return games.copy()

        # Create a copy to avoid modifying original
        games_copy = games.copy()
        n = len(games_copy)

        self.comparison_count = 0
        self.swap_count = 0
        self.steps = []

        if self.visualize:
            print("=" * 80)
            print(f"BUBBLE SORT - BOARD GAMES (by {key_name})")
            print("=" * 80)
            print(f"Sorting {n} games...\n")

        for i in range(n):
            swapped = False

            if self.visualize:
                print(f"--- Pass {i + 1} ---")

            for j in range(0, n - i - 1):
                self.comparison_count += 1

                key1 = key(games_copy[j])
                key2 = key(games_copy[j + 1])

                if self.visualize:
                    print(f"Comparing: '{games_copy[j].title}' ({key1}) vs "
                          f"'{games_copy[j + 1].title}' ({key2})", end="")

                if key1 > key2:
                    # Swap elements
                    games_copy[j], games_copy[j + 1] = games_copy[j + 1], games_copy[j]
                    self.swap_count += 1
                    swapped = True

                    if self.visualize:
                        print(f" → SWAP!")
                else:
                    if self.visualize:
                        print(f" → No swap")

                if self.delay > 0:
                    time.sleep(self.delay)

            if not swapped:
                if self.visualize:
                    print(f"\nNo swaps in pass {i + 1} - list is sorted!")
                break

            if self.visualize:
                print()

        if self.visualize:
            print("=" * 80)
            print("SORTED GAMES:")
            print("=" * 80)
            for idx, game in enumerate(games_copy[:10], 1):  # Show first 10
                print(f"{idx}. {game.title} - {key_name}: {key(game)}")
            if len(games_copy) > 10:
                print(f"... and {len(games_copy) - 10} more games")
            print(f"\nTotal Comparisons: {self.comparison_count}")
            print(f"Total Swaps: {self.swap_count}")
            print("=" * 80)

        return games_copy

    def get_statistics(self) -> dict:
        """
        Get sorting statistics from the most recent sort operation.

        Returns:
            Dictionary with comparison and swap counts, including:
                - comparisons: Number of element comparisons
                - swaps: Number of element swaps
                - total_operations: Sum of comparisons and swaps

        Note:
            Returns statistics from the most recent sort operation.
            If no sort has been performed, all counts will be 0.
        """
        return {
            'comparisons': self.comparison_count,
            'swaps': self.swap_count,
            'total_operations': self.comparison_count + self.swap_count
        }


def demo_integer_sort():
    """Demonstrate bubble sort on integers."""
    print("\n" + "=" * 80)
    print("DEMO: Sorting Integers")
    print("=" * 80)

    test_list = [64, 34, 25, 12, 22, 11, 90]
    sorter = BubbleSort(visualize=True)
    sorted_list = sorter.sort_integers(test_list)

    print(f"\nOriginal: {test_list}")
    print(f"Sorted: {sorted_list}")


def demo_game_sort():
    """Demonstrate bubble sort on board games."""
    from json_data_loader import JSONDataLoader

    print("\n" + "=" * 80)
    print("DEMO: Sorting Board Games by Weight (Complexity)")
    print("=" * 80)

    # Load games
    loader = JSONDataLoader()
    games = loader.load_games()

    # Filter to games with weight > 0 and take first 10 for demo
    games_with_weight = [g for g in games if g.weight > 0][:10]

    # Sort by weight
    sorter = BubbleSort(visualize=True)
    sorted_games = sorter.sort_games(
        games_with_weight,
        key=lambda g: g.weight,
        key_name="Weight"
    )


if __name__ == "__main__":
    # Demo integer sorting
    demo_integer_sort()

    # Demo game sorting
    demo_game_sort()
