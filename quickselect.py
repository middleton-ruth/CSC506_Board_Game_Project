"""
Quickselect Algorithm Implementation
Requirement #2: Create quickselect algorithm implementation that finds
the kth smallest element in a list.
"""

from typing import List, Callable, Any
from board_game import BoardGame
import random


class QuickSelect:
    """
    Quickselect algorithm for finding the kth smallest element.

    Uses the partition method from quicksort to efficiently find the kth
    smallest element without fully sorting the list.
    """

    def __init__(self, verbose: bool = True) -> None:
        """
        Initialize quickselect algorithm.

        Args:
            verbose: Whether to print detailed steps during execution

        Note:
            When verbose=True, prints partition details and search progress.
            When verbose=False, runs silently for performance testing.
        """
        self.verbose = verbose
        self.partition_count = 0

    def find_kth_smallest_integer(self, arr: List[int], k: int) -> int:
        """
        Find the kth smallest integer in a list using quickselect algorithm.

        Args:
            arr: List of integers
            k: The position to find (1-indexed, so k=1 finds the smallest)

        Returns:
            The kth smallest element

        Raises:
            TypeError: If arr is not a list or contains non-numeric values
            ValueError: If arr is None, empty, or k is out of range

        Examples:
            >>> qs = QuickSelect(verbose=False)
            >>> qs.find_kth_smallest_integer([3, 1, 4, 1, 5, 9, 2, 6], 3)
            2
            >>> qs.find_kth_smallest_integer([10, 20, 30], 1)
            10
        """
        # Edge case: Validate input
        if arr is None:
            raise ValueError("Input array cannot be None")
        if not isinstance(arr, list):
            raise TypeError(f"Expected list, got {type(arr).__name__}")

        # Edge case: Empty list
        if len(arr) == 0:
            raise ValueError("Cannot find kth element in empty list")

        # Edge case: Validate k range
        if not isinstance(k, int):
            raise TypeError(f"k must be an integer, got {type(k).__name__}")
        if k < 1 or k > len(arr):
            raise ValueError(f"k must be between 1 and {len(arr)}, got {k}")

        # Edge case: Single element
        if len(arr) == 1:
            if k == 1:
                return arr[0]
            else:
                raise ValueError(f"k={k} is out of range for single-element list")

        # Validate all elements are numeric
        for i, elem in enumerate(arr):
            if not isinstance(elem, (int, float)):
                raise ValueError(f"Element at index {i} is not numeric: {elem} (type: {type(elem).__name__})")

        # Create a copy to avoid modifying original
        arr_copy = arr.copy()
        self.partition_count = 0

        if self.verbose:
            print("=" * 80)
            print(f"QUICKSELECT - Finding {self._ordinal(k)} smallest element")
            print("=" * 80)
            print(f"Array: {arr_copy}")
            print(f"Array length: {len(arr_copy)}")
            print()

        result = self._quickselect(arr_copy, 0, len(arr_copy) - 1, k - 1)

        if self.verbose:
            print("=" * 80)
            print(f"RESULT: The {self._ordinal(k)} smallest element is {result}")
            print(f"Total partitions performed: {self.partition_count}")
            print("=" * 80)

        return result

    def find_kth_smallest_game(self, games: List[BoardGame], k: int,
                                key: Callable[[BoardGame], Any],
                                key_name: str = "value") -> BoardGame:
        """
        Find the kth smallest game by a given key using quickselect.

        Args:
            games: List of BoardGame objects
            k: The position to find (1-indexed)
            key: Function to extract the comparison key from each game
            key_name: Name of the key for display purposes

        Returns:
            The kth smallest BoardGame object according to the key

        Raises:
            TypeError: If games is not a list or key is not callable
            ValueError: If games is None, empty, or k is out of range
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
            raise ValueError("Cannot find kth element in empty games list")

        # Edge case: Validate k
        if not isinstance(k, int):
            raise TypeError(f"k must be an integer, got {type(k).__name__}")
        if k < 1 or k > len(games):
            raise ValueError(f"k must be between 1 and {len(games)}, got {k}")

        # Edge case: Single element
        if len(games) == 1:
            if k == 1:
                return games[0]
            else:
                raise ValueError(f"k={k} is out of range for single-element list")

        # Create list of (key_value, game) tuples for sorting
        keyed_games = [(key(game), game) for game in games]
        self.partition_count = 0

        if self.verbose:
            print("=" * 80)
            print(f"QUICKSELECT - Finding {self._ordinal(k)} smallest game by {key_name}")
            print("=" * 80)
            print(f"Total games: {len(games)}")
            print()

        result_tuple = self._quickselect(keyed_games, 0, len(keyed_games) - 1, k - 1)
        result_game = result_tuple[1]

        if self.verbose:
            print("=" * 80)
            print(f"RESULT: The {self._ordinal(k)} smallest game by {key_name}")
            print(f"  Title: {result_game.title}")
            print(f"  {key_name}: {key(result_game)}")
            print(f"  Location: {result_game.location}")
            print(f"Total partitions performed: {self.partition_count}")
            print("=" * 80)

        return result_game

    def find_median(self, arr: List[int]) -> float:
        """
        Find the median value using quickselect algorithm.

        Args:
            arr: List of integers

        Returns:
            Median value (average of two middle elements for even-length lists)

        Raises:
            TypeError: If arr is not a list
            ValueError: If arr is None or empty

        Examples:
            >>> qs = QuickSelect(verbose=False)
            >>> qs.find_median([1, 2, 3, 4, 5])
            3.0
            >>> qs.find_median([1, 2, 3, 4])
            2.5

        Note:
            For odd-length lists, returns the middle element.
            For even-length lists, returns the average of the two middle elements.
        """
        # Edge case: Validate input
        if arr is None:
            raise ValueError("Input array cannot be None")
        if not isinstance(arr, list):
            raise TypeError(f"Expected list, got {type(arr).__name__}")

        n = len(arr)

        # Edge case: Empty list
        if n == 0:
            raise ValueError("Cannot find median of empty list")

        # Edge case: Single element
        if n == 1:
            return float(arr[0])

        if n % 2 == 1:
            # Odd length - return middle element
            return float(self.find_kth_smallest_integer(arr, (n + 1) // 2))
        else:
            # Even length - return average of two middle elements
            mid1 = self.find_kth_smallest_integer(arr, n // 2)
            mid2 = self.find_kth_smallest_integer(arr, n // 2 + 1)
            return (mid1 + mid2) / 2.0

    def _quickselect(self, arr: List[Any], left: int, right: int, k: int) -> Any:
        """
        Internal quickselect implementation using partition method.

        Args:
            arr: List to search in
            left: Left boundary of current partition
            right: Right boundary of current partition
            k: Index to find (0-indexed)

        Returns:
            The kth smallest element
        """
        if left == right:
            return arr[left]

        # Choose random pivot to avoid worst-case performance
        pivot_index = random.randint(left, right)

        if self.verbose:
            print(f"Partition {self.partition_count + 1}: "
                  f"Searching in range [{left}..{right}], looking for index {k}")

        # Partition the array around the pivot
        pivot_index = self._partition(arr, left, right, pivot_index)

        if self.verbose:
            print(f"  Pivot moved to index {pivot_index}")

        # Check if we found the element
        if k == pivot_index:
            if self.verbose:
                print(f"  ✓ Found at index {k}!")
            return arr[k]
        elif k < pivot_index:
            if self.verbose:
                print(f"  → Search left partition")
            return self._quickselect(arr, left, pivot_index - 1, k)
        else:
            if self.verbose:
                print(f"  → Search right partition")
            return self._quickselect(arr, pivot_index + 1, right, k)

    def _partition(self, arr: List[Any], left: int, right: int, pivot_index: int) -> int:
        """
        Partition array around pivot element.

        Args:
            arr: Array to partition
            left: Left boundary
            right: Right boundary
            pivot_index: Index of pivot element

        Returns:
            Final position of pivot element
        """
        self.partition_count += 1

        pivot_value = arr[pivot_index]

        # Move pivot to end
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

        # Partition
        store_index = left
        for i in range(left, right):
            # Handle both simple values and tuples
            current_val = arr[i][0] if isinstance(arr[i], tuple) else arr[i]
            pivot_val = pivot_value[0] if isinstance(pivot_value, tuple) else pivot_value

            if current_val < pivot_val:
                arr[i], arr[store_index] = arr[store_index], arr[i]
                store_index += 1

        # Move pivot to final position
        arr[store_index], arr[right] = arr[right], arr[store_index]

        return store_index

    @staticmethod
    def _ordinal(n: int) -> str:
        """Convert number to ordinal string (1st, 2nd, 3rd, etc.)."""
        if 10 <= n % 100 <= 20:
            suffix = 'th'
        else:
            suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
        return f"{n}{suffix}"


def demo_integer_quickselect():
    """Demonstrate quickselect on integers."""
    print("\n" + "=" * 80)
    print("DEMO: Quickselect on Integers")
    print("=" * 80)

    test_list = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50]
    qs = QuickSelect(verbose=True)

    # Find 5th smallest
    result = qs.find_kth_smallest_integer(test_list, 5)

    # Find median
    print("\n")
    median = qs.find_median(test_list)
    print(f"\nMedian of {test_list} is {median}")


def demo_game_quickselect():
    """Demonstrate quickselect on board games."""
    from json_data_loader import JSONDataLoader

    print("\n" + "=" * 80)
    print("DEMO: Quickselect on Board Games")
    print("=" * 80)

    # Load games
    loader = JSONDataLoader()
    games = loader.load_games()

    # Filter to games with weight > 0
    games_with_weight = [g for g in games if g.weight > 0]

    # Find median complexity game
    qs = QuickSelect(verbose=True)
    median_game = qs.find_kth_smallest_game(
        games_with_weight,
        len(games_with_weight) // 2,
        key=lambda g: g.weight,
        key_name="Weight (Complexity)"
    )

    # Find 90th percentile (most complex games)
    print("\n")
    k_90th = int(len(games_with_weight) * 0.9)
    complex_game = qs.find_kth_smallest_game(
        games_with_weight,
        k_90th,
        key=lambda g: g.weight,
        key_name="Weight (Complexity)"
    )


if __name__ == "__main__":
    # Demo integer quickselect
    demo_integer_quickselect()

    # Demo game quickselect
    demo_game_quickselect()
