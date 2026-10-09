"""
Board Game Collection Portfolio System
Requirement #4: Integrated portfolio system containing all course algorithms and data structures.

This system demonstrates mastery of:
- Bubble Sort (sorting with visualization)
- Quickselect (finding kth elements)
- Custom Set operations (union, intersection, difference, symmetric difference)
- Stack, Queue, Tree, Graph, Hash Table data structures
"""

from typing import List, Callable, Any
from json_data_loader import JSONDataLoader
from board_game import BoardGame
from bubble_sort import BubbleSort
from quickselect import QuickSelect
from custom_set import CustomSet, GameSet
from data_structures import Stack, Queue, BinarySearchTree, Graph, HashTable


class BoardGamePortfolio:
    """
    Comprehensive portfolio system for board game collection management.

    Integrates all algorithms and data structures to provide a complete
    collection management solution.
    """

    def __init__(self, data_file: str = "board_games_data.json", verbose: bool = False):
        """
        Initialize the portfolio system.

        Args:
            data_file: Path to JSON file containing game data
            verbose: Whether to show detailed progress messages
        """
        # Load data
        self.loader = JSONDataLoader(data_file, verbose=verbose)
        self.games: List[BoardGame] = []
        self.verbose = verbose

        # Data structures
        self.game_hash: HashTable = HashTable(size=500)  # Fast lookup by game number
        self.location_tree: BinarySearchTree = BinarySearchTree()  # Hierarchical locations
        self.similarity_graph: Graph = Graph(directed=False)  # Game relationships
        self.view_history: Stack = Stack()  # Recently viewed games
        self.paint_queue: Queue = Queue()  # Games to paint next

        # Algorithms
        self.bubble_sorter = BubbleSort(visualize=False)
        self.quickselector = QuickSelect(verbose=False)

    def load_data(self) -> None:
        """Load games from data file and populate data structures."""
        if self.verbose:
            print("\n" + "=" * 80)
            print("BOARD GAME COLLECTION PORTFOLIO SYSTEM")
            print("=" * 80)
            print("\n[1/6] Loading games from data file...")

        self.games = self.loader.load_games()

        if self.verbose:
            print("[2/6] Building hash table index...")
        self._build_hash_table()

        if self.verbose:
            print("[3/6] Building location tree...")
        self._build_location_tree()

        if self.verbose:
            print("[4/6] Building similarity graph...")
        self._build_similarity_graph()

        if self.verbose:
            print("[5/6] Initializing paint queue...")
        self._initialize_paint_queue()

        if self.verbose:
            print("[6/6] System ready!")
            print(f"\nLoaded {len(self.games)} games successfully!")

            # Print summary
            stats = self.loader.get_summary_stats()
            print(f"Painted: {stats['painted']} | Unpainted: {stats['unpainted']}")
            print(f"Locations: {stats['unique_locations']}")
            print(f"Average Complexity: {stats['average_weight']}")

    def _build_hash_table(self) -> None:
        """Build hash table for O(1) game lookup by game number."""
        for game in self.games:
            self.game_hash.insert(game.game_number, game)

    def _build_location_tree(self) -> None:
        """Build BST organized by location for hierarchical access."""
        for game in self.games:
            if game.location and game.location.strip() and game.location.strip() != 'nan':
                # Normalize location (strip whitespace)
                location = game.location.strip()
                # Use location as key, store list of games at that location
                existing = self.location_tree.search(location)
                if existing:
                    existing.append(game)
                else:
                    self.location_tree.insert(location, [game])

    def _build_similarity_graph(self) -> None:
        """Build graph of game similarities based on shared mechanisms."""
        # Sample: Connect games with similar weights (complexity)
        for i, game1 in enumerate(self.games[:100]):  # Sample for demo
            for game2 in self.games[i+1:i+10]:
                if game1.weight > 0 and game2.weight > 0:
                    # Connect if weights are within 0.5 of each other
                    if abs(game1.weight - game2.weight) <= 0.5:
                        self.similarity_graph.add_edge(game1.title, game2.title)

    def _initialize_paint_queue(self) -> None:
        """Initialize queue with unpainted games."""
        unpainted = [g for g in self.games if not g.painted]
        for game in unpainted[:20]:  # Add first 20 unpainted games
            self.paint_queue.enqueue(game)

    # ==================== SORTING OPERATIONS ====================

    def sort_by_weight(self, games: List[BoardGame] = None, visualize: bool = False) -> List[BoardGame]:
        """
        Sort games by complexity weight using bubble sort.

        Args:
            games: List of games to sort (defaults to all games)
            visualize: Whether to show visualization

        Returns:
            Sorted list of games
        """
        if games is None:
            games = [g for g in self.games if g.weight > 0]

        sorter = BubbleSort(visualize=visualize)
        return sorter.sort_games(games, key=lambda g: g.weight, key_name="Weight")

    def sort_by_title(self, games: List[BoardGame] = None, visualize: bool = False) -> List[BoardGame]:
        """Sort games alphabetically by title."""
        if games is None:
            games = self.games

        sorter = BubbleSort(visualize=visualize)
        return sorter.sort_games(games, key=lambda g: g.title, key_name="Title")

    # ==================== QUICKSELECT OPERATIONS ====================

    def find_median_complexity_game(self) -> BoardGame:
        """Find the game with median complexity using quickselect."""
        games_with_weight = [g for g in self.games if g.weight > 0]
        qs = QuickSelect(verbose=False)
        return qs.find_kth_smallest_game(
            games_with_weight,
            len(games_with_weight) // 2,
            key=lambda g: g.weight,
            key_name="Weight"
        )

    def find_kth_complexity_game(self, k: int) -> BoardGame:
        """
        Find the kth game by complexity (1=simplest, higher=more complex).

        Args:
            k: Position in complexity ranking (1-based, 1=simplest)

        Returns:
            The kth simplest game
        """
        games_with_weight = [g for g in self.games if g.weight > 0]
        qs = QuickSelect(verbose=False)
        return qs.find_kth_smallest_game(
            games_with_weight,
            k,
            key=lambda g: g.weight,
            key_name="Weight"
        )

    # ==================== SET OPERATIONS ====================

    def get_painted_games_set(self) -> GameSet:
        """Get set of painted games."""
        return GameSet.from_filter(self.games, lambda g: g.painted)

    def get_location_games_set(self, location: str) -> GameSet:
        """Get set of games at a specific location."""
        return GameSet.from_filter(self.games, lambda g: location in g.location)

    def get_complex_games_set(self, min_weight: float = 3.5) -> GameSet:
        """Get set of high complexity games."""
        return GameSet.from_filter(self.games, lambda g: g.weight >= min_weight)

    def find_painted_at_location(self, location: str) -> GameSet:
        """Find games that are painted AND at specific location (intersection)."""
        painted = self.get_painted_games_set()
        at_location = self.get_location_games_set(location)
        return painted.intersection(at_location)

    def find_painted_or_complex(self) -> GameSet:
        """Find games that are painted OR high complexity (union)."""
        painted = self.get_painted_games_set()
        complex_games = self.get_complex_games_set()
        return painted.union(complex_games)

    def find_complex_but_unpainted(self) -> GameSet:
        """Find high complexity games that are NOT painted (difference)."""
        complex_games = self.get_complex_games_set()
        painted = self.get_painted_games_set()
        return complex_games.difference(painted)

    # ==================== HASH TABLE OPERATIONS ====================

    def lookup_game_by_number(self, game_number: int) -> BoardGame:
        """Fast O(1) lookup of game by number."""
        return self.game_hash.get(game_number)

    # ==================== TREE OPERATIONS ====================

    def get_games_by_location(self, location: str) -> List[BoardGame]:
        """Get all games at a location using BST."""
        games = self.location_tree.search(location)
        return games if games else []

    def get_all_locations_sorted(self) -> List[str]:
        """Get all locations in sorted order using tree traversal."""
        traversal = self.location_tree.inorder_traversal()
        return [location for location, games in traversal]

    # ==================== GRAPH OPERATIONS ====================

    def get_similar_games(self, game_title: str) -> List[str]:
        """Get games similar to a given game using graph."""
        neighbors = self.similarity_graph.get_neighbors(game_title)
        return list(neighbors)

    # ==================== STACK OPERATIONS ====================

    def view_game(self, game: BoardGame) -> None:
        """Record viewing a game (add to history stack)."""
        self.view_history.push(game)

    def get_last_viewed(self) -> BoardGame:
        """Get last viewed game (peek at stack)."""
        if not self.view_history.is_empty():
            return self.view_history.peek()
        return None

    def undo_view(self) -> BoardGame:
        """Undo last view (pop from stack)."""
        if not self.view_history.is_empty():
            return self.view_history.pop()
        return None

    # ==================== QUEUE OPERATIONS ====================

    def get_next_to_paint(self) -> BoardGame:
        """Get next game to paint from queue."""
        if not self.paint_queue.is_empty():
            return self.paint_queue.dequeue()
        return None

    def add_to_paint_queue(self, game: BoardGame) -> None:
        """Add a game to the paint queue."""
        self.paint_queue.enqueue(game)

    # ==================== STATISTICS ====================

    def get_system_stats(self) -> dict:
        """Get comprehensive system statistics."""
        return {
            'total_games': len(self.games),
            'hash_table_items': self.game_hash.item_count(),
            'hash_table_load_factor': self.game_hash.load_factor(),
            'locations_in_tree': self.location_tree.size(),
            'graph_vertices': self.similarity_graph.vertex_count(),
            'graph_edges': self.similarity_graph.edge_count(),
            'view_history_size': self.view_history.size(),
            'paint_queue_size': self.paint_queue.size()
        }


def main():
    """Demonstrate the portfolio system."""
    # Create and initialize system
    portfolio = BoardGamePortfolio()
    portfolio.load_data()

    print("\n" + "=" * 80)
    print("SYSTEM STATISTICS")
    print("=" * 80)
    stats = portfolio.get_system_stats()
    for key, value in stats.items():
        print(f"{key}: {value}")

    print("\n" + "=" * 80)
    print("DEMONSTRATION: All Algorithms and Data Structures")
    print("=" * 80)

    # Hash Table: Fast lookup
    print("\n[HASH TABLE] Looking up game #5:")
    game5 = portfolio.lookup_game_by_number(5)
    if game5:
        print(f"  Found: {game5.title}")

    # Quickselect: Find median
    print("\n[QUICKSELECT] Finding median complexity game:")
    median_game = portfolio.find_median_complexity_game()
    print(f"  {median_game.title} (weight: {median_game.weight})")

    # Set Operations
    print("\n[SET OPERATIONS] Finding painted games in GR location:")
    painted_gr = portfolio.find_painted_at_location("GR")
    print(f"  Found {painted_gr.size()} games")

    print("\n[SET OPERATIONS] Finding complex but unpainted games:")
    complex_unpainted = portfolio.find_complex_but_unpainted()
    print(f"  Found {complex_unpainted.size()} games")

    # Tree: Location lookup
    print("\n[TREE] Games in 'LL' location:")
    ll_games = portfolio.get_games_by_location("LL")
    print(f"  Found {len(ll_games)} games")

    # Queue: Paint queue
    print("\n[QUEUE] Next 3 games to paint:")
    for i in range(3):
        game = portfolio.get_next_to_paint()
        if game:
            print(f"  {i+1}. {game.title}")

    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()
