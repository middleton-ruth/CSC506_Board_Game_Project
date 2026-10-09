"""
Performance Analysis Module
Requirement #6: Develop performance analysis tools that compare different algorithms
and data structures across multiple metrics.

This module provides comprehensive performance testing and comparison.
"""

import time
import random
import sys
from typing import List, Callable, Any, Dict
from datetime import datetime
from json_data_loader import JSONDataLoader
from board_game import BoardGame
from bubble_sort import BubbleSort
from quickselect import QuickSelect
from custom_set import CustomSet, GameSet
from data_structures import HashTable, BinarySearchTree, Stack, Queue, Graph


class PerformanceAnalyzer:
    """
    Performance analyzer for comparing algorithms and data structures.
    """

    def __init__(self):
        """Initialize the performance analyzer."""
        self.results = []

    @staticmethod
    def time_function(func: Callable, *args, **kwargs) -> tuple:
        """
        Time the execution of a function.

        Args:
            func: Function to time
            *args: Function arguments
            **kwargs: Function keyword arguments

        Returns:
            Tuple of (result, elapsed_time_ms)
        """
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_ms = (end_time - start_time) * 1000
        return result, elapsed_ms

    def compare_sorting_algorithms(self, data_sizes: List[int]):
        """
        Compare bubble sort vs Python's built-in sort.

        Args:
            data_sizes: List of data sizes to test
        """
        print("=" * 80)
        print("SORTING ALGORITHM COMPARISON")
        print("=" * 80)
        print(f"Comparing Bubble Sort vs Built-in Sort")
        print(f"Data sizes: {data_sizes}\n")

        results = []

        for size in data_sizes:
            # Generate random data
            test_data = [random.randint(1, 1000) for _ in range(size)]

            # Test bubble sort
            sorter = BubbleSort(visualize=False)
            _, bubble_time = self.time_function(sorter.sort_integers, test_data.copy())
            bubble_comparisons = sorter.comparison_count
            bubble_swaps = sorter.swap_count

            # Test built-in sort
            _, builtin_time = self.time_function(sorted, test_data.copy())

            results.append({
                'size': size,
                'bubble_time': bubble_time,
                'builtin_time': builtin_time,
                'bubble_comparisons': bubble_comparisons,
                'bubble_swaps': bubble_swaps,
                'speedup': bubble_time / builtin_time if builtin_time > 0 else 0
            })

            print(f"Size: {size:4d} | Bubble Sort: {bubble_time:8.2f}ms | "
                  f"Built-in: {builtin_time:8.2f}ms | "
                  f"Speedup: {bubble_time / builtin_time:.1f}x")

        print("\n" + "=" * 80)
        print("DETAILED BUBBLE SORT METRICS")
        print("=" * 80)
        for r in results:
            print(f"Size {r['size']:4d}: {r['bubble_comparisons']:6d} comparisons, "
                  f"{r['bubble_swaps']:6d} swaps")

        return results

    def compare_search_methods(self, games: List[BoardGame]):
        """
        Compare different search methods: Linear vs Hash Table vs BST.

        Args:
            games: List of games to index
        """
        print("\n" + "=" * 80)
        print("SEARCH METHOD COMPARISON")
        print("=" * 80)
        print(f"Indexing {len(games)} games\n")

        # Build hash table
        print("Building hash table...")
        hash_table = HashTable(size=len(games) * 2)
        start = time.time()
        for game in games:
            hash_table.insert(game.game_number, game)
        hash_build_time = (time.time() - start) * 1000

        # Build BST
        print("Building binary search tree...")
        bst = BinarySearchTree()
        start = time.time()
        for game in games:
            bst.insert(game.game_number, game)
        bst_build_time = (time.time() - start) * 1000

        print(f"\nBuild Times:")
        print(f"  Hash Table: {hash_build_time:.2f}ms")
        print(f"  BST: {bst_build_time:.2f}ms")

        # Test lookups
        print(f"\nLookup Performance (100 random lookups):")
        test_numbers = [random.choice(games).game_number for _ in range(100)]

        # Linear search
        start = time.time()
        for num in test_numbers:
            found = next((g for g in games if g.game_number == num), None)
        linear_time = (time.time() - start) * 1000

        # Hash table search
        start = time.time()
        for num in test_numbers:
            found = hash_table.get(num)
        hash_time = (time.time() - start) * 1000

        # BST search
        start = time.time()
        for num in test_numbers:
            found = bst.search(num)
        bst_time = (time.time() - start) * 1000

        print(f"  Linear Search: {linear_time:.2f}ms")
        print(f"  Hash Table: {hash_time:.2f}ms (Speedup: {linear_time/hash_time:.1f}x)")
        print(f"  BST: {bst_time:.2f}ms (Speedup: {linear_time/bst_time:.1f}x)")

        return {
            'linear_time': linear_time,
            'hash_time': hash_time,
            'bst_time': bst_time,
            'hash_speedup': linear_time / hash_time,
            'bst_speedup': linear_time / bst_time
        }

    def compare_quickselect_vs_sort(self, games: List[BoardGame]):
        """
        Compare quickselect vs full sort for finding kth element.

        Args:
            games: List of games
        """
        print("\n" + "=" * 80)
        print("QUICKSELECT VS FULL SORT COMPARISON")
        print("=" * 80)
        print(f"Finding median in {len(games)} games\n")

        # Using quickselect
        qs = QuickSelect(verbose=False)
        _, quickselect_time = self.time_function(
            qs.find_kth_smallest_game,
            games,
            len(games) // 2,
            lambda g: g.weight,
            "Weight"
        )

        # Using full sort
        def find_median_by_sort():
            sorted_games = sorted(games, key=lambda g: g.weight)
            return sorted_games[len(sorted_games) // 2]

        _, sort_time = self.time_function(find_median_by_sort)

        print(f"Quickselect: {quickselect_time:.2f}ms")
        print(f"Full Sort: {sort_time:.2f}ms")
        print(f"Quickselect Speedup: {sort_time/quickselect_time:.2f}x faster")

        return {
            'quickselect_time': quickselect_time,
            'sort_time': sort_time,
            'speedup': sort_time / quickselect_time
        }

    def compare_set_operations(self, games: List[BoardGame]):
        """
        Compare set operations vs manual iteration.

        Args:
            games: List of games
        """
        print("\n" + "=" * 80)
        print("SET OPERATIONS COMPARISON")
        print("=" * 80)

        # Create sets
        painted_set = GameSet.from_filter(games, lambda g: g.painted)
        complex_set = GameSet.from_filter(games, lambda g: g.weight >= 3.5)

        # Test intersection using set operations
        _, set_time = self.time_function(
            painted_set.intersection,
            complex_set
        )

        # Test intersection using manual loops
        def manual_intersection():
            painted = [g for g in games if g.painted]
            complex_games = [g for g in games if g.weight >= 3.5]
            result = [g for g in painted if g in complex_games]
            return result

        _, manual_time = self.time_function(manual_intersection)

        print(f"Finding intersection of painted and complex games:")
        print(f"  Custom Set Operations: {set_time:.2f}ms")
        print(f"  Manual Iteration: {manual_time:.2f}ms")
        print(f"  Difference: {abs(set_time - manual_time):.2f}ms")

        # Test union
        _, set_union_time = self.time_function(
            painted_set.union,
            complex_set
        )

        def manual_union():
            painted = [g for g in games if g.painted]
            complex_games = [g for g in games if g.weight >= 3.5]
            # Manual deduplication
            result = painted.copy()
            for game in complex_games:
                if game not in result:
                    result.append(game)
            return result

        _, manual_union_time = self.time_function(manual_union)

        print(f"\nFinding union of painted and complex games:")
        print(f"  Custom Set Operations: {set_union_time:.2f}ms")
        print(f"  Manual Iteration: {manual_union_time:.2f}ms")

        return {
            'set_intersection_time': set_time,
            'manual_intersection_time': manual_time,
            'set_union_time': set_union_time,
            'manual_union_time': manual_union_time
        }

    def analyze_data_structure_operations(self, games: List[BoardGame]):
        """
        Analyze stack, queue, and graph operations.

        Args:
            games: List of games
        """
        print("\n" + "=" * 80)
        print("DATA STRUCTURE OPERATIONS ANALYSIS")
        print("=" * 80)

        # Stack operations
        print("\nSTACK Performance (Recently Viewed Games):")
        stack = Stack()
        start = time.time()
        for i in range(1000):
            stack.push(games[i % len(games)])
        push_time = (time.time() - start) * 1000

        start = time.time()
        for i in range(1000):
            if not stack.is_empty():
                stack.pop()
        pop_time = (time.time() - start) * 1000

        print(f"  1000 Push operations: {push_time:.3f}ms ({push_time/1000:.4f}ms per operation)")
        print(f"  1000 Pop operations: {pop_time:.3f}ms ({pop_time/1000:.4f}ms per operation)")

        # Queue operations
        print("\nQUEUE Performance (Paint Queue):")
        queue = Queue()
        start = time.time()
        for i in range(1000):
            queue.enqueue(games[i % len(games)])
        enqueue_time = (time.time() - start) * 1000

        start = time.time()
        for i in range(1000):
            if not queue.is_empty():
                queue.dequeue()
        dequeue_time = (time.time() - start) * 1000

        print(f"  1000 Enqueue operations: {enqueue_time:.3f}ms ({enqueue_time/1000:.4f}ms per operation)")
        print(f"  1000 Dequeue operations: {dequeue_time:.3f}ms ({dequeue_time/1000:.4f}ms per operation)")

        # Graph operations
        print("\nGRAPH Performance (Game Similarity Network):")
        graph = Graph()
        start = time.time()
        # Add vertices
        for game in games[:100]:
            graph.add_vertex(game.title)
        # Add edges (games with similar weight are connected)
        edge_count = 0
        for i, game1 in enumerate(games[:100]):
            for game2 in games[i+1:100]:
                if abs(game1.weight - game2.weight) < 0.5:
                    graph.add_edge(game1.title, game2.title)
                    edge_count += 1
        graph_build_time = (time.time() - start) * 1000

        print(f"  Built graph with {graph.vertex_count()} vertices and {graph.edge_count()} edges")
        print(f"  Build time: {graph_build_time:.2f}ms")

        # Test neighbor lookups
        start = time.time()
        for game in games[:100]:
            neighbors = graph.get_neighbors(game.title)
        neighbor_time = (time.time() - start) * 1000
        print(f"  100 neighbor lookups: {neighbor_time:.3f}ms ({neighbor_time/100:.4f}ms per lookup)")

        return {
            'stack_push_time': push_time,
            'stack_pop_time': pop_time,
            'queue_enqueue_time': enqueue_time,
            'queue_dequeue_time': dequeue_time,
            'graph_build_time': graph_build_time,
            'graph_neighbor_time': neighbor_time
        }

    def analyze_memory_usage(self, games: List[BoardGame]):
        """
        Analyze memory characteristics of different data structures.

        Args:
            games: List of games
        """
        print("\n" + "=" * 80)
        print("MEMORY CHARACTERISTICS ANALYSIS")
        print("=" * 80)

        # Hash table
        hash_table = HashTable(size=len(games) * 2)
        for game in games:
            hash_table.insert(game.game_number, game)

        print(f"\nHASH TABLE:")
        print(f"  Table size: {hash_table.size} slots")
        print(f"  Items stored: {hash_table.item_count()}")
        print(f"  Load factor: {hash_table.load_factor():.3f}")
        print(f"  Optimal load factor: 0.5-0.75 (lower = faster, higher = memory efficient)")

        # BST
        bst = BinarySearchTree()
        for game in games:
            bst.insert(game.game_number, game)

        print(f"\nBINARY SEARCH TREE:")
        print(f"  Nodes: {bst.size()}")
        print(f"  Memory overhead: ~3 pointers per node (parent, left, right)")

        # Custom Set
        game_set = GameSet(games)
        print(f"\nCUSTOM SET:")
        print(f"  Elements: {game_set.size()}")
        print(f"  Memory: List-based, minimal overhead")

        return {
            'hash_load_factor': hash_table.load_factor(),
            'bst_size': bst.size(),
            'set_size': game_set.size()
        }

    def analyze_big_o_complexity(self):
        """
        Demonstrate Big-O complexity with increasing data sizes.
        """
        print("\n" + "=" * 80)
        print("BIG-O COMPLEXITY ANALYSIS")
        print("=" * 80)
        print("\nTesting algorithms with increasing data sizes to verify time complexity\n")

        sizes = [50, 100, 200, 400, 800]

        # Bubble Sort - O(n²)
        print("BUBBLE SORT - Expected: O(n²)")
        print("Size\tTime(ms)\tOperations\tTime Ratio\tOps Ratio")
        print("-" * 70)
        prev_time = None
        prev_ops = None
        prev_size = None

        for size in sizes:
            test_data = [random.randint(1, 1000) for _ in range(size)]
            sorter = BubbleSort(visualize=False)
            _, elapsed = self.time_function(sorter.sort_integers, test_data)
            ops = sorter.comparison_count + sorter.swap_count

            time_ratio = elapsed / prev_time if prev_time else 1.0
            ops_ratio = ops / prev_ops if prev_ops else 1.0
            size_ratio = size / prev_size if prev_size else 1.0

            print(f"{size}\t{elapsed:.2f}\t\t{ops}\t\t{time_ratio:.2f}x\t\t{ops_ratio:.2f}x")

            prev_time = elapsed
            prev_ops = ops
            prev_size = size

        print("\nNote: For O(n²), doubling input size should ~4x operations")

        # Hash Table Lookup - O(1)
        print("\n\nHASH TABLE LOOKUP - Expected: O(1) average")
        print("Size\tTime(ms)\tTime Ratio")
        print("-" * 50)
        prev_time = None

        for size in sizes:
            hash_table = HashTable(size=size * 2)
            for i in range(size):
                hash_table.insert(i, f"value_{i}")

            # Perform 100 lookups
            start = time.time()
            for _ in range(100):
                key = random.randint(0, size - 1)
                hash_table.get(key)
            elapsed = (time.time() - start) * 1000

            time_ratio = elapsed / prev_time if prev_time else 1.0
            print(f"{size}\t{elapsed:.2f}\t\t{time_ratio:.2f}x")
            prev_time = elapsed

        print("\nNote: For O(1), time should remain relatively constant as size increases")

        # Quickselect - O(n) average
        print("\n\nQUICKSELECT - Expected: O(n) average")
        print("Size\tTime(ms)\tTime Ratio\tSize Ratio")
        print("-" * 60)
        prev_time = None
        prev_size = None

        for size in sizes:
            test_data = [random.randint(1, 1000) for _ in range(size)]
            qs = QuickSelect(verbose=False)
            _, elapsed = self.time_function(qs.find_kth_smallest_integer, test_data, size // 2)

            time_ratio = elapsed / prev_time if prev_time else 1.0
            size_ratio = size / prev_size if prev_size else 1.0

            print(f"{size}\t{elapsed:.2f}\t\t{time_ratio:.2f}x\t\t{size_ratio:.2f}x")
            prev_time = elapsed
            prev_size = size

        print("\nNote: For O(n), doubling input size should ~2x time")

    def run_comprehensive_analysis(self):
        """Run all performance comparisons and generate report."""
        print("\n" + "=" * 80)
        print("COMPREHENSIVE PERFORMANCE ANALYSIS")
        print("Board Game Collection Management System")
        print("=" * 80)
        print(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Load data
        print("\nLoading data...")
        loader = JSONDataLoader()
        games = loader.load_games()
        games_with_weight = [g for g in games if g.weight > 0]

        print(f"Loaded {len(games)} games ({len(games_with_weight)} with weight data)\n")

        # Run all comparisons
        print("\n[1/7] Sorting Algorithm Comparison")
        sort_results = self.compare_sorting_algorithms([10, 50, 100, 200])

        print("\n[2/7] Search Method Comparison")
        search_results = self.compare_search_methods(games)

        print("\n[3/7] Quickselect vs Sort Comparison")
        quickselect_results = self.compare_quickselect_vs_sort(games_with_weight)

        print("\n[4/7] Set Operations Comparison")
        set_results = self.compare_set_operations(games)

        print("\n[5/7] Data Structure Operations Analysis")
        ds_results = self.analyze_data_structure_operations(games)

        print("\n[6/7] Memory Characteristics Analysis")
        memory_results = self.analyze_memory_usage(games)

        print("\n[7/7] Big-O Complexity Analysis")
        self.analyze_big_o_complexity()

        # Summary
        print("\n" + "=" * 80)
        print("ANALYSIS SUMMARY")
        print("=" * 80)
        print("\nKey Findings:")
        print(f"1. Hash table provides {search_results['hash_speedup']:.1f}x speedup over linear search")
        print(f"2. Quickselect is {quickselect_results['speedup']:.2f}x faster than full sort for finding median")
        print(f"3. Custom set operations provide clean, reusable code for complex queries")
        print(f"4. Bubble sort has O(n²) complexity vs built-in O(n log n)")
        print(f"5. Stack/Queue operations are O(1) - extremely fast ({ds_results['stack_push_time']/1000:.4f}ms per op)")
        print(f"6. Hash table load factor: {memory_results['hash_load_factor']:.3f} (optimal: 0.5-0.75)")

        print("\nAlgorithm Complexity Summary:")
        print("  Bubble Sort:        O(n²) time, O(1) space")
        print("  Quickselect:        O(n) average time, O(log n) space")
        print("  Hash Table Insert:  O(1) average time")
        print("  Hash Table Lookup:  O(1) average time")
        print("  BST Insert:         O(log n) average, O(n) worst")
        print("  BST Search:         O(log n) average, O(n) worst")
        print("  Set Union:          O(m + n) time")
        print("  Set Intersection:   O(min(m,n)) time")

        print("\nRecommendations:")
        print("- Use hash tables for frequent lookups by ID (O(1) vs O(n))")
        print("- Use quickselect when only kth element is needed (O(n) vs O(n log n))")
        print("- Use set operations for complex filtering logic (cleaner code)")
        print("- Use built-in sort for production (bubble sort for learning only)")
        print("- Use stacks for undo/history (LIFO operations)")
        print("- Use queues for processing orders (FIFO operations)")
        print("- Use graphs for relationship modeling (game similarities)")

        print("\n" + "=" * 80)

        return {
            'sort_results': sort_results,
            'search_results': search_results,
            'quickselect_results': quickselect_results,
            'set_results': set_results,
            'ds_results': ds_results,
            'memory_results': memory_results
        }

    def generate_report_file(self, output_file: str = "PERFORMANCE_ANALYSIS_REPORT.txt"):
        """
        Generate a comprehensive written report file.

        Args:
            output_file: Output filename
        """
        original_stdout = sys.stdout

        with open(output_file, 'w') as f:
            sys.stdout = f

            # Run comprehensive analysis (output goes to file)
            results = self.run_comprehensive_analysis()

        sys.stdout = original_stdout

        print(f"\n✓ Performance analysis report saved to: {output_file}")
        return output_file


def main():
    """Run performance analysis."""
    analyzer = PerformanceAnalyzer()
    analyzer.run_comprehensive_analysis()


if __name__ == "__main__":
    main()
