
"""
Board Game Collection Management System - Main Interactive Interface
Requirement #5: User interface allowing interactive testing of all implementations

This is the main entry point for the portfolio system.
Run this file to access all algorithms and data structures through an interactive menu.
"""

from portfolio_system import BoardGamePortfolio
from bubble_sort import BubbleSort
from quickselect import QuickSelect
from location_manager import LocationManager
from performance_analysis import PerformanceAnalyzer


class InteractiveUI:
    """Interactive command-line interface for the portfolio system."""

    def __init__(self):
        """Initialize the UI and portfolio system."""
        self.portfolio = None
        self.location_manager = LocationManager()
        print("\n" + "=" * 80)
        print(" " * 22 + "BOARD GAME COLLECTION MANAGER")
        print("=" * 80)
        print("\nThis system demonstrates advanced algorithms and data structures:")
        print("  • Sorting: Bubble Sort with visualization")
        print("  • Selection: Quickselect for kth element queries")
        print("  • Sets: Union, Intersection, Difference operations")
        print("  • Data Structures: Hash Tables, Trees, Graphs, Stacks, Queues")
        print("=" * 80)

    def _display_with_pagination(self, items, display_func, page_size=20):
        """
        Display a list with pagination for better readability.

        Args:
            items: List of items to display
            display_func: Function to format each item for display
            page_size: Number of items per page
        """
        total = len(items)
        if total == 0:
            print("No items to display.")
            return

        if total <= page_size:
            # Just display all if it fits on one page
            for i, item in enumerate(items, 1):
                print(display_func(i, item))
            return

        # Paginate for large lists
        page = 0
        while page * page_size < total:
            start = page * page_size
            end = min(start + page_size, total)

            print(f"\nShowing {start + 1}-{end} of {total}:")
            for i in range(start, end):
                print(display_func(i + 1, items[i]))

            if end < total:
                choice = input(f"\nPress Enter for next {page_size} (or 'q' to finish): ").strip().lower()
                if choice == 'q':
                    print(f"\nDisplayed {end} of {total} items.")
                    break
            page += 1

    def initialize_system(self):
        """Load data and initialize the portfolio system."""
        self.portfolio = BoardGamePortfolio(verbose=False)  # Clean output
        self.portfolio.load_data()

    def display_main_menu(self):
        """Display the main menu."""
        print("\n" + "=" * 80)
        print("MAIN MENU")
        print("=" * 80)
        print("\nACADEMIC DEMONSTRATIONS:")
        print("1. Bubble Sort Demonstrations")
        print("2. Quickselect Demonstrations")
        print("3. Set Operations")
        print("4. Data Structure Operations")
        print("5. Performance Analysis")
        print("\nCOLLECTION MANAGEMENT:")
        print("6. View All Games")
        print("7. Add/Delete Games")
        print("8. Collection Statistics")
        print("9. Search & Lookup")
        print("10. Manage Storage Locations")
        print("\n0. Exit")
        print("=" * 80)

    def bubble_sort_menu(self):
        """Menu for bubble sort operations."""
        while True:
            print("\n" + "-" * 80)
            print("BUBBLE SORT MENU")
            print("-" * 80)
            print("1. Sort games by complexity (Weight: 1=Light, 5=Heavy)")
            print("2. Sort games by title (Alphabetical)")
            print("3. Demo: Sort integers with visualization (shows algorithm steps)")
            print("4. Demo: Sort games with visualization (shows comparison steps)")
            print("0. Back to main menu")
            print("-" * 80)

            choice = input("\nEnter choice: ").strip()

            if choice == "1":
                try:
                    n_input = input("How many games to sort? (default 20): ").strip()
                    n = int(n_input or "20")
                    games = [g for g in self.portfolio.games if g.weight > 0][:n]
                    print(f"\nSorting {len(games)} games by complexity (Weight scale: 1=Light/Simple, 5=Heavy/Complex)...")
                    sorted_games = self.portfolio.sort_by_weight(games, visualize=False)

                    # Ask user preference for display
                    if len(sorted_games) > 50:
                        display_choice = input(f"\n{len(sorted_games)} games to show. Display (a)ll, (p)aginate 50 at a time, or (e)xport to file? [a/p/e]: ").strip().lower()

                        if display_choice == 'e':
                            filename = f"sorted_games_{len(sorted_games)}.txt"
                            with open(filename, 'w') as f:
                                f.write(f"Sorted by Complexity - {len(sorted_games)} Games\n")
                                f.write("=" * 80 + "\n\n")
                                for i, game in enumerate(sorted_games, 1):
                                    f.write(f"{i}. {game.title} - Weight: {game.weight}\n")
                            print(f"\nExported to {filename}")
                            continue
                        elif display_choice == 'p':
                            self._display_with_pagination(
                                sorted_games,
                                lambda i, g: f"{i}. {g.title} - Weight: {g.weight}",
                                page_size=50
                            )
                            continue

                    # Display all (for <= 50 or if user chose 'a')
                    print(f"\nAll {len(sorted_games)} Sorted Results:")
                    for i, game in enumerate(sorted_games, 1):
                        print(f"{i}. {game.title} - Weight: {game.weight}")
                except ValueError:
                    print("Invalid number entered. Using default/returning to menu.")

            elif choice == "2":
                try:
                    n_input = input("How many games to sort? (default 15): ").strip()
                    n = int(n_input or "15")
                    games = self.portfolio.games[:n]
                    sorted_games = self.portfolio.sort_by_title(games, visualize=False)

                    # Ask user preference for display
                    if len(sorted_games) > 50:
                        display_choice = input(f"\n{len(sorted_games)} games to show. Display (a)ll, (p)aginate 50 at a time, or (e)xport to file? [a/p/e]: ").strip().lower()

                        if display_choice == 'e':
                            filename = f"sorted_games_alphabetical_{len(sorted_games)}.txt"
                            with open(filename, 'w') as f:
                                f.write(f"Sorted Alphabetically - {len(sorted_games)} Games\n")
                                f.write("=" * 80 + "\n\n")
                                for i, game in enumerate(sorted_games, 1):
                                    f.write(f"{i}. {game.title}\n")
                            print(f"\nExported to {filename}")
                            continue
                        elif display_choice == 'p':
                            self._display_with_pagination(
                                sorted_games,
                                lambda i, g: f"{i}. {g.title}",
                                page_size=50
                            )
                            continue

                    # Display all (for <= 50 or if user chose 'a')
                    print("\nSorted Games:")
                    for i, game in enumerate(sorted_games, 1):
                        print(f"{i}. {game.title}")
                except ValueError:
                    print("Invalid number entered. Using default/returning to menu.")

            elif choice == "3":
                test_list = [64, 34, 25, 12, 22, 11, 90, 45]
                print(f"\nOriginal list: {test_list}")
                sorter = BubbleSort(visualize=True)
                sorted_list = sorter.sort_integers(test_list)
                print(f"\nFinal sorted list: {sorted_list}")

            elif choice == "4":
                try:
                    n_input = input("How many games to visualize? (5-10 recommended, default 7): ").strip()
                    n = int(n_input or "7")
                    games = [g for g in self.portfolio.games if g.weight > 0][:n]
                    self.portfolio.sort_by_weight(games, visualize=True)
                except ValueError:
                    print("Invalid number entered. Using default/returning to menu.")

            elif choice == "0":
                break

    def quickselect_menu(self):
        """Menu for quickselect operations."""
        while True:
            print("\n" + "=" * 80)
            print("QUICKSELECT ALGORITHM - Finding the Kth Element")
            print("=" * 80)
            print("\nWhat is the 'kth element'?")
            print("  The kth element is the item at position k in a sorted list.")
            print("  Example: In [3, 7, 1, 9, 5], the 2nd smallest element is 3")
            print("           (sorted: [1, 3, 5, 7, 9], position 2 = 3)")
            print()
            print("For board games, 'lightest/heaviest' refers to COMPLEXITY:")
            print("  • Lightest = Simplest rules (Weight 1-2: family games)")
            print("  • Heaviest = Most complex (Weight 4-5: strategic games)")
            print()
            print("Why Quickselect? It finds the kth element WITHOUT sorting everything!")
            print("  Sorting 150 games: O(n log n) - slower")
            print("  Quickselect: O(n) average - much faster!")
            print("-" * 80)
            print("PRACTICAL USE WITH BOARD GAMES:")
            print("  1. Find median complexity game (the middle-ranked game)")
            print("  2. Find game at specific rank (e.g., 10th simplest of 150)")
            print("  3. List games by complexity (lightest to heaviest)")
            print()
            print("EDUCATIONAL ALGORITHM DEMONSTRATIONS:")
            print("  (These use simple numbers to show HOW the algorithm works)")
            print("  4. Demo: Find median of a number list")
            print("  5. Demo: Find kth smallest in a number list")
            print()
            print("  0. Back to main menu")
            print("=" * 80)

            choice = input("\nEnter choice: ").strip()

            if choice == "1":
                median_game = self.portfolio.find_median_complexity_game()
                print(f"\nMedian Complexity Game:")
                print(f"  Title: {median_game.title}")
                print(f"  Weight: {median_game.weight}")
                print(f"  Location: {median_game.location}")

            elif choice == "2":
                total_games = len([g for g in self.portfolio.games if g.weight > 0])
                print(f"\n{'='*70}")
                print("UNDERSTANDING COMPLEXITY WEIGHT (BoardGameGeek 1-5 scale):")
                print(f"{'='*70}")
                print("  1.0-2.0: BEGINNER / Gateway Games")
                print("           Light rules, family-friendly, new gamer friendly")
                print("           Examples: Catan, Ticket to Ride, Kingdomino")
                print()
                print("  2.0-3.0: INTERMEDIATE / Medium Weight")
                print("           More strategic depth, some rules complexity")
                print("           Examples: Wingspan, 7 Wonders, Azul")
                print()
                print("  3.0-4.0: EXPERIENCED / Heavy Strategy")
                print("           Complex rules, significant strategy, longer playtime")
                print("           Examples: Terraforming Mars, Brass, Scythe")
                print()
                print("  4.0-5.0: EXPERT / Very Heavy")
                print("           Deep complexity, extensive rules, serious time investment")
                print("           Examples: Gloomhaven, 18xx series, Twilight Imperium")
                print(f"{'='*70}")
                print()
                print(f"You have {total_games} games in your collection.")
                print("The games are RANKED by their complexity weight:")
                print()
                print(f"  Rank 1       → The SIMPLEST game (lowest weight)")
                print(f"  Rank 10      → The 10th simplest game")
                print(f"  Rank 75      → The middle complexity game (median)")
                print(f"  Rank {total_games-9}     → The 10th most complex game")
                print(f"  Rank {total_games}     → The MOST COMPLEX game (highest weight)")
                print()
                print("What rank would you like to find?")

                k = int(input(f"Enter rank (1-{total_games}): "))

                if k < 1 or k > total_games:
                    print(f"  ✗ Please enter a number between 1 and {total_games}")
                    continue

                game = self.portfolio.find_kth_complexity_game(k)

                # Determine complexity category (gamer terminology)
                weight = game.weight
                if weight < 2.0:
                    category = "BEGINNER"
                    description = "gateway game - light rules, perfect for new gamers and families"
                elif weight < 3.0:
                    category = "INTERMEDIATE"
                    description = "medium weight - strategic depth with manageable complexity"
                elif weight < 4.0:
                    category = "EXPERIENCED"
                    description = "heavy strategy - complex rules, significant depth, longer sessions"
                else:
                    category = "EXPERT"
                    description = "very heavy - deep complexity, extensive rules, serious commitment"

                print(f"\n{'='*75}")
                print(f"YOU SELECTED: Rank #{k} of {total_games} games")
                print(f"{'='*75}")
                print(f"\n  Game: {game.title}")
                print(f"  Complexity Weight: {game.weight}/5.0")
                print(f"  Category: {category}")
                print(f"  Location: {game.location or 'Not set'}")
                print(f"\n{'─'*75}")
                print(f"EXPLANATION:")
                print(f"{'─'*75}")
                print(f"  Out of {total_games} games, this is ranked #{k} in complexity.")

                if k == 1:
                    print(f"  This is THE SIMPLEST game in your collection.")
                elif k <= 10:
                    print(f"  This is one of the {k} simplest games in your collection.")
                elif k == total_games:
                    print(f"  This is THE MOST COMPLEX game in your collection.")
                elif k >= total_games - 10:
                    print(f"  This is one of the 10 most complex games in your collection.")
                else:
                    print(f"  This is in the middle range of your collection's complexity.")

                print(f"\n  With a weight of {weight}, this is a {category.lower()} game,")
                print(f"  meaning it has {description}.")
                print(f"\n{'─'*75}")
                print(f"TECHNICAL NOTE: Found using Quickselect algorithm - O(n) average time")
                print(f"                Much faster than sorting all {total_games} games!")
                print(f"{'='*75}")

            elif choice == "3":
                # List games by complexity
                games_with_weight = [g for g in self.portfolio.games if g.weight > 0]
                total = len(games_with_weight)

                print(f"\n{'='*75}")
                print(f"LIST GAMES BY PLAYER EXPERIENCE LEVEL")
                print(f"{'='*75}")
                print(f"\nYou have {total} games with complexity ratings.")
                print("\nBrowse by gamer experience level:")
                print(f"  1. BEGINNER games (Weight 1.0-2.0) - Gateway & family games")
                print(f"  2. INTERMEDIATE games (Weight 2.0-3.0) - Medium strategy")
                print(f"  3. EXPERIENCED games (Weight 3.0-4.0) - Heavy strategy")
                print(f"  4. EXPERT games (Weight 4.0-5.0) - Very heavy")
                print()
                print("Or browse top/bottom games:")
                top_count = min(20, total)  # Show up to 20 for large collections
                print(f"  5. Top {top_count} lightest games (best for new gamers)")
                print(f"  6. Top {top_count} heaviest games (hardcore gaming night)")
                print(f"  7. ALL {total} games (lightest to heaviest)")
                print(f"  8. Custom number of games")

                list_choice = input("\nEnter choice (1-8): ").strip()

                # Sort all games first
                print(f"\nRetrieving games...")
                sorted_games = sorted(games_with_weight, key=lambda g: g.weight)

                # Filter by category
                if list_choice == "1":
                    # BEGINNER: 1.0-2.0
                    games_to_show = [g for g in sorted_games if g.weight < 2.0]
                    description = f"BEGINNER Games (Weight 1.0-2.0) - Gateway & Family Games - {len(games_to_show)} found"
                elif list_choice == "2":
                    # INTERMEDIATE: 2.0-3.0
                    games_to_show = [g for g in sorted_games if 2.0 <= g.weight < 3.0]
                    description = f"INTERMEDIATE Games (Weight 2.0-3.0) - Medium Strategy - {len(games_to_show)} found"
                elif list_choice == "3":
                    # EXPERIENCED: 3.0-4.0
                    games_to_show = [g for g in sorted_games if 3.0 <= g.weight < 4.0]
                    description = f"EXPERIENCED Games (Weight 3.0-4.0) - Heavy Strategy - {len(games_to_show)} found"
                elif list_choice == "4":
                    # EXPERT: 4.0-5.0
                    games_to_show = [g for g in sorted_games if g.weight >= 4.0]
                    description = f"EXPERT Games (Weight 4.0-5.0) - Very Heavy - {len(games_to_show)} found"
                elif list_choice == "5":
                    # Top N lightest (scales with collection size)
                    n = min(20, total)
                    games_to_show = sorted_games[:n]
                    description = f"Top {n} Lightest Games (Best for New Gamers)"
                elif list_choice == "6":
                    # Top N heaviest (scales with collection size)
                    n = min(20, total)
                    games_to_show = sorted_games[-n:]
                    games_to_show.reverse()  # Show heaviest first
                    description = f"Top {n} Heaviest Games (Hardcore Gaming Night)"
                elif list_choice == "7":
                    # All games
                    games_to_show = sorted_games
                    description = f"ALL {total} Games (Lightest to Heaviest)"
                elif list_choice == "8":
                    # Custom
                    n = int(input(f"How many games? (1-{total}): "))
                    games_to_show = sorted_games[:n]
                    description = f"Top {n} Games by Complexity"
                else:
                    print("Invalid choice")
                    continue

                if not games_to_show:
                    print("\nNo games found in this category.")
                    continue

                print(f"\n{'='*75}")
                print(f"{description}")
                print(f"{'='*75}")

                # Display with pagination for large lists
                if len(games_to_show) > 50:
                    display_choice = input(f"\n{len(games_to_show)} games to show. Display (a)ll, (p)aginate 50 at a time, or (e)xport to file? [a/p/e]: ").strip().lower()

                    if display_choice == 'e':
                        filename = f"games_by_complexity_{len(games_to_show)}.txt"
                        with open(filename, 'w') as f:
                            f.write(f"{description}\n")
                            f.write("=" * 80 + "\n\n")
                            for i, game in enumerate(games_to_show, 1):
                                # Use gamer-friendly categories
                                if game.weight < 2.0:
                                    category = "Beginner"
                                elif game.weight < 3.0:
                                    category = "Intermediate"
                                elif game.weight < 4.0:
                                    category = "Experienced"
                                else:
                                    category = "Expert"
                                f.write(f"{i}. {game.title}\n")
                                f.write(f"   Weight: {game.weight} ({category})\n")
                                f.write(f"   Location: {game.location or 'Not set'}\n\n")
                        print(f"\n✓ Exported to {filename}")
                        continue
                    elif display_choice == 'p':
                        page_size = 50
                        for page_start in range(0, len(games_to_show), page_size):
                            page_end = min(page_start + page_size, len(games_to_show))
                            print(f"\nShowing {page_start + 1}-{page_end} of {len(games_to_show)}:")
                            for i in range(page_start, page_end):
                                game = games_to_show[i]
                                # Use gamer-friendly categories
                                if game.weight < 2.0:
                                    category = "Beginner"
                                elif game.weight < 3.0:
                                    category = "Intermediate"
                                elif game.weight < 4.0:
                                    category = "Experienced"
                                else:
                                    category = "Expert"
                                print(f"{i+1}. {game.title} - Weight: {game.weight} ({category})")

                            if page_end < len(games_to_show):
                                cont = input(f"\nPress Enter for next {page_size} (or 'q' to finish): ").strip().lower()
                                if cont == 'q':
                                    break
                        continue

                # Display all
                print()
                for i, game in enumerate(games_to_show, 1):
                    # Use gamer-friendly categories
                    if game.weight < 2.0:
                        category = "Beginner"
                    elif game.weight < 3.0:
                        category = "Intermediate"
                    elif game.weight < 4.0:
                        category = "Experienced"
                    else:
                        category = "Expert"
                    print(f"{i}. {game.title} - Weight: {game.weight} ({category})")

                print(f"\n{'='*75}")
                print("NOTE: While this used standard sorting, Quickselect could be used")
                print("      to efficiently find specific games (e.g., top 10 lightest)")
                print("      without sorting the entire collection!")
                print(f"{'='*75}")

            elif choice == "4":
                print(f"\n{'='*75}")
                print("EDUCATIONAL DEMO: Finding the Median")
                print(f"{'='*75}")
                print("\nPURPOSE: This demonstrates the Quickselect algorithm on simple numbers")
                print("         to show how it works before applying it to board games.")
                print()
                test_list = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50]
                print(f"Sample list of numbers: {test_list}")
                print(f"Sorted version would be: {sorted(test_list)}")
                print()
                print("The MEDIAN is the middle value when sorted.")
                print(f"With {len(test_list)} numbers, the median is position {len(test_list)//2}")
                print()
                print("Watch how Quickselect finds it WITHOUT fully sorting:")
                print(f"{'─'*75}")

                qs = QuickSelect(verbose=True)
                median = qs.find_median(test_list)

                print(f"{'─'*75}")
                print(f"\nRESULT: The median is {median}")
                print()
                print("WHAT THIS MEANS FOR BOARD GAMES:")
                print("  This same algorithm finds the median complexity game in your")
                print("  collection without sorting all 150 games - much more efficient!")
                print(f"{'='*75}")

            elif choice == "5":
                print(f"\n{'='*75}")
                print("EDUCATIONAL DEMO: Finding the Kth Smallest Element")
                print(f"{'='*75}")
                print("\nPURPOSE: This demonstrates how Quickselect finds ANY position (not")
                print("         just the median) without sorting the entire list.")
                print()
                test_list = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50]
                print(f"Sample list of numbers: {test_list}")
                print(f"Sorted version would be: {sorted(test_list)}")
                print()
                print(f"This list has {len(test_list)} numbers.")
                print(f"You can find ANY position (k) in this list:")
                print(f"  k=1  → smallest number (11)")
                print(f"  k=5  → 5th smallest number (45)")
                print(f"  k={len(test_list)} → largest number (90)")
                print()

                k = int(input(f"Enter k (1-{len(test_list)}): "))

                if k < 1 or k > len(test_list):
                    print(f"  ✗ Please enter a number between 1 and {len(test_list)}")
                    continue

                print(f"\nWatch how Quickselect finds the {k}th smallest:")
                print(f"{'─'*75}")

                qs = QuickSelect(verbose=True)
                result = qs.find_kth_smallest_integer(test_list, k)

                print(f"{'─'*75}")
                print(f"\nRESULT: The {k}th smallest number is: {result}")
                print()
                print("WHAT THIS MEANS FOR BOARD GAMES:")
                print(f"  This same algorithm can find the {k}th simplest game in your")
                print("  collection. For example:")
                print(f"  - The 10th simplest game (good starter games)")
                print(f"  - The 100th game (medium complexity)")
                print(f"  - The 150th game (most complex)")
                print("  All without sorting the entire collection!")
                print(f"{'='*75}")

            elif choice == "0":
                break

    def set_operations_menu(self):
        """Menu for set operations."""
        while True:
            print("\n" + "-" * 80)
            print("SET OPERATIONS MENU")
            print("-" * 80)
            print("1. Find painted games in specific location (Intersection)")
            print("2. Find complex but unpainted games (Difference)")
            print("3. Find painted OR complex games (Union)")
            print("4. Custom set operation")
            print("0. Back to main menu")
            print("-" * 80)

            choice = input("\nEnter choice: ").strip()

            if choice == "1":
                location = input("Enter location (GR, LL, etc.): ").strip()
                result = self.portfolio.find_painted_at_location(location)
                print(f"\nPainted games in {location}: {result.size()} games")
                for game in result.to_list():
                    print(f"  - {game.title}")

            elif choice == "2":
                result = self.portfolio.find_complex_but_unpainted()
                print(f"\nComplex (≥3.5) but unpainted: {result.size()} games")
                for game in result.to_list():
                    print(f"  - {game.title} (weight: {game.weight})")

            elif choice == "3":
                result = self.portfolio.find_painted_or_complex()
                print(f"\nPainted OR Complex: {result.size()} games")

            elif choice == "4":
                print("\nAvailable filters:")
                print("  1. Painted")
                print("  2. Location")
                print("  3. High complexity (≥3.5)")
                filter1 = int(input("Choose first filter: "))
                filter2 = int(input("Choose second filter: "))
                operation = input("Operation (union/intersection/difference): ").lower()

                # Create sets based on choices
                sets_map = {
                    1: self.portfolio.get_painted_games_set(),
                    2: self.portfolio.get_location_games_set(input("Enter location: ")),
                    3: self.portfolio.get_complex_games_set()
                }

                set1 = sets_map[filter1]
                set2 = sets_map[filter2]

                if operation == "union":
                    result = set1.union(set2)
                elif operation == "intersection":
                    result = set1.intersection(set2)
                elif operation == "difference":
                    result = set1.difference(set2)
                else:
                    print("Invalid operation")
                    continue

                print(f"\nResult: {result.size()} games")
                for game in result.to_list():
                    print(f"  - {game.title}")

            elif choice == "0":
                break

    def data_structures_menu(self):
        """Menu for data structure operations."""
        while True:
            print("\n" + "-" * 80)
            print("DATA STRUCTURES MENU")
            print("-" * 80)
            print("1. Hash Table - Lookup game by number")
            print("2. Tree - View games by location")
            print("3. Graph - Find similar games")
            print("4. Stack - View history")
            print("5. Queue - Paint queue")
            print("0. Back to main menu")
            print("-" * 80)

            choice = input("\nEnter choice: ").strip()

            if choice == "1":
                game_num = int(input("Enter game number: "))
                game = self.portfolio.lookup_game_by_number(game_num)
                if game:
                    print(f"\nFound: {game.title}")
                    print(f"  Location: {game.location}")
                    print(f"  Painted: {game.painted}")
                    print(f"  Weight: {game.weight}")
                else:
                    print("Game not found")

            elif choice == "2":
                locations = self.portfolio.get_all_locations_sorted()
                print("\nAvailable locations:")
                for loc in locations:
                    print(f"  - {loc}")
                location = input("\nEnter location: ").strip()
                games = self.portfolio.get_games_by_location(location)
                print(f"\nGames at {location}: {len(games)} games")
                for game in games:
                    print(f"  - {game.title}")

            elif choice == "3":
                title = input("Enter game title: ").strip()
                similar = self.portfolio.get_similar_games(title)
                if similar:
                    print(f"\nSimilar games to '{title}' ({len(similar)} games):")
                    for game_title in list(similar):
                        print(f"  - {game_title}")
                else:
                    print("No similar games found or game not in graph")

            elif choice == "4":
                print(f"\nView history size: {self.portfolio.view_history.size()}")
                if not self.portfolio.view_history.is_empty():
                    last = self.portfolio.get_last_viewed()
                    print(f"Last viewed: {last.title}")

            elif choice == "5":
                print(f"\nPaint queue size: {self.portfolio.paint_queue.size()}")
                print("Next 5 games to paint:")
                for i in range(min(5, self.portfolio.paint_queue.size())):
                    game = self.portfolio.get_next_to_paint()
                    if game:
                        print(f"  {i+1}. {game.title}")

            elif choice == "0":
                break

    def performance_analysis_menu(self):
        """Menu for performance analysis."""
        while True:
            print("\n" + "-" * 80)
            print("PERFORMANCE ANALYSIS MENU")
            print("-" * 80)
            print("1. Run comprehensive analysis (all tests)")
            print("2. Sorting algorithm comparison")
            print("3. Search method comparison")
            print("4. Quickselect vs Sort comparison")
            print("5. Set operations comparison")
            print("6. Data structure operations analysis")
            print("7. Big-O complexity demonstration")
            print("8. Generate full report file (saves to disk)")
            print("0. Back to main menu")
            print("-" * 80)

            choice = input("\nEnter choice: ").strip()

            if choice == "1":
                analyzer = PerformanceAnalyzer()
                analyzer.run_comprehensive_analysis()
                input("\nPress Enter to continue...")

            elif choice == "2":
                analyzer = PerformanceAnalyzer()
                analyzer.compare_sorting_algorithms([10, 50, 100, 200, 500])
                input("\nPress Enter to continue...")

            elif choice == "3":
                analyzer = PerformanceAnalyzer()
                analyzer.compare_search_methods(self.portfolio.games)
                input("\nPress Enter to continue...")

            elif choice == "4":
                games_with_weight = [g for g in self.portfolio.games if g.weight > 0]
                analyzer = PerformanceAnalyzer()
                analyzer.compare_quickselect_vs_sort(games_with_weight)
                input("\nPress Enter to continue...")

            elif choice == "5":
                analyzer = PerformanceAnalyzer()
                analyzer.compare_set_operations(self.portfolio.games)
                input("\nPress Enter to continue...")

            elif choice == "6":
                analyzer = PerformanceAnalyzer()
                analyzer.analyze_data_structure_operations(self.portfolio.games)
                input("\nPress Enter to continue...")

            elif choice == "7":
                analyzer = PerformanceAnalyzer()
                analyzer.analyze_big_o_complexity()
                input("\nPress Enter to continue...")

            elif choice == "8":
                print("\nGenerating comprehensive performance analysis report...")
                analyzer = PerformanceAnalyzer()
                output_file = analyzer.generate_report_file()
                print(f"\n✓ Report saved to: {output_file}")
                print(f"  This report contains:")
                print(f"  - Sorting algorithm comparisons")
                print(f"  - Search method benchmarks")
                print(f"  - Quickselect vs sort analysis")
                print(f"  - Set operations performance")
                print(f"  - Data structure operations")
                print(f"  - Memory characteristics")
                print(f"  - Big-O complexity verification")
                input("\nPress Enter to continue...")

            elif choice == "0":
                break

    def statistics_menu(self):
        """Display collection statistics."""
        print("\n" + "=" * 80)
        print("COLLECTION STATISTICS")
        print("=" * 80)

        stats = self.portfolio.loader.get_summary_stats()
        print(f"\nTotal Games: {stats['total_games']}")
        print(f"Painted: {stats['painted']} ({stats['paint_percentage']:.1f}%)")
        print(f"Unpainted: {stats['unpainted']}")
        print(f"Can Travel: {stats['can_travel']}")
        print(f"Average Complexity: {stats['average_weight']}")
        print(f"\nUnique Locations: {stats['unique_locations']}")
        print("Locations:", ", ".join(stats['locations']))

        sys_stats = self.portfolio.get_system_stats()
        print(f"\nSystem Statistics:")
        print(f"  Hash Table Load Factor: {sys_stats['hash_table_load_factor']:.2f}")
        print(f"  Graph Vertices: {sys_stats['graph_vertices']}")
        print(f"  Graph Edges: {sys_stats['graph_edges']}")

        input("\nPress Enter to continue...")

    def location_management_menu(self):
        """Menu for managing storage locations."""
        while True:
            print("\n" + "-" * 80)
            print("LOCATION MANAGEMENT")
            print("-" * 80)
            print("1. View all storage locations")
            print("2. Add a new location")
            print("3. Remove a location")
            print("4. View games by location")
            print("5. Assign location(s) to a game")
            print("6. Change location of a game")
            print("0. Back to main menu")
            print("-" * 80)

            choice = input("\nEnter choice: ").strip()

            if choice == "1":
                self.location_manager.display_locations()
                if self.location_manager.locations:
                    print(f"\nTotal locations: {len(self.location_manager.locations)}")
                input("\nPress Enter to continue...")

            elif choice == "2":
                new_loc = input("\nEnter new location name: ").strip()
                if new_loc:
                    if self.location_manager.add_location(new_loc):
                        print(f"✓ Added location: {new_loc}")
                    else:
                        print("Location already exists or is invalid")
                else:
                    print("Location name cannot be empty")
                input("\nPress Enter to continue...")

            elif choice == "3":
                if not self.location_manager.locations:
                    print("\nNo locations to remove")
                    input("\nPress Enter to continue...")
                    continue

                self.location_manager.display_locations()
                loc_to_remove = input("\nEnter location name to remove: ").strip()
                if loc_to_remove:
                    # Check for affected games
                    affected_games = self.location_manager.get_games_at_location(
                        loc_to_remove, self.portfolio.games
                    )

                    if affected_games:
                        print(f"\n⚠ WARNING: This location is used by {len(affected_games)} game(s):")
                        for game in affected_games:
                            print(f"  - {game.title} (#{game.game_number})")
                        confirm = input("\nAre you sure you want to remove this location? (yes/no): ").strip().lower()
                        if confirm != 'yes':
                            print("Cancelled")
                            input("\nPress Enter to continue...")
                            continue

                    if self.location_manager.remove_location(loc_to_remove):
                        print(f"✓ Removed location: {loc_to_remove}")
                    else:
                        print("Location not found")
                else:
                    print("Invalid input")
                input("\nPress Enter to continue...")

            elif choice == "4":
                if not self.location_manager.locations:
                    print("\nNo locations defined yet")
                    input("\nPress Enter to continue...")
                    continue

                self.location_manager.display_locations()
                location = input("\nEnter location name to view games: ").strip()
                if location:
                    games = self.location_manager.get_games_at_location(location, self.portfolio.games)
                    if games:
                        print(f"\nGames at '{location}': {len(games)} game(s)")
                        print("=" * 50)
                        for game in games:
                            print(f"  #{game.game_number}: {game.title}")
                            print(f"     Weight: {game.weight}, Players: {game.num_players}")
                    else:
                        print(f"\nNo games found at '{location}'")
                input("\nPress Enter to continue...")

            elif choice == "5":
                try:
                    game_num = int(input("\nEnter game number: "))
                    game = self.portfolio.lookup_game_by_number(game_num)
                    if game:
                        print(f"\nGame: {game.title}")
                        current_loc = game.location if game.location else 'None'
                        print(f"Current location(s): {current_loc}")

                        # If game already has location(s), ask what to do
                        if game.location:
                            print(f"\nThis game is currently stored in: {game.location}")
                            print(f"\nWhat would you like to do with {game.title}'s location(s)?")
                            print("1. Replace with new location(s) (removes current, assigns new)")
                            print("2. Add more location(s) (keeps current, adds additional)")
                            print("3. Remove specific location(s) from this game")
                            print("4. Clear all locations from this game only")
                            print("0. Cancel (no changes)")

                            action = input("\nYour choice: ").strip()

                            if action == "1":
                                # Replace all locations
                                locations = self.location_manager.select_multiple_locations()
                                if locations:
                                    game.locations = locations
                                    game.location = ', '.join(locations)
                                    if hasattr(self.portfolio, 'loader') and hasattr(self.portfolio.loader, 'save_games'):
                                        self.portfolio.loader.save_games(self.portfolio.games)
                                    print(f"\n✓ Replaced location(s). Now stored in: {game.location}")
                                else:
                                    print("\nNo locations selected. Location unchanged.")

                            elif action == "2":
                                # Add more locations
                                print(f"\nCurrent: {game.location}")
                                print("Select additional location(s) to add:")
                                new_locs = self.location_manager.select_multiple_locations()
                                if new_locs:
                                    current = game.locations if game.locations else []
                                    combined = list(set(current + new_locs))
                                    game.locations = combined
                                    game.location = ', '.join(combined)
                                    if hasattr(self.portfolio, 'loader') and hasattr(self.portfolio.loader, 'save_games'):
                                        self.portfolio.loader.save_games(self.portfolio.games)
                                    print(f"\n✓ Added location(s). Now stored in: {game.location}")
                                else:
                                    print("\nNo locations selected. Location unchanged.")

                            elif action == "3":
                                # Remove specific location(s)
                                current_locs = game.locations if game.locations else []
                                if len(current_locs) == 0:
                                    print("\nNo locations to remove")
                                else:
                                    print(f"\nCurrent locations for {game.title}:")
                                    for i, loc in enumerate(current_locs, 1):
                                        print(f"  {i}. {loc}")

                                    remove_input = input("\nEnter location number(s) to remove (comma-separated) or 'all': ").strip()

                                    if remove_input.lower() == 'all':
                                        game.locations = []
                                        game.location = ""
                                    else:
                                        try:
                                            indices = [int(x.strip()) for x in remove_input.split(',')]
                                            to_remove = [current_locs[i-1] for i in indices if 1 <= i <= len(current_locs)]

                                            for loc in to_remove:
                                                if loc in game.locations:
                                                    game.locations.remove(loc)

                                            game.location = ', '.join(game.locations) if game.locations else ""
                                        except (ValueError, IndexError):
                                            print("\nInvalid input")
                                            continue

                                    if hasattr(self.portfolio, 'loader') and hasattr(self.portfolio.loader, 'save_games'):
                                        self.portfolio.loader.save_games(self.portfolio.games)

                                    if game.location:
                                        print(f"\n✓ Updated. Now stored in: {game.location}")
                                    else:
                                        print(f"\n✓ All locations removed from {game.title}")

                            elif action == "4":
                                # Clear all
                                confirm = input(f"\nAre you sure you want to clear all locations for {game.title}? (yes/no): ").strip().lower()
                                if confirm == 'yes':
                                    game.locations = []
                                    game.location = ""
                                    if hasattr(self.portfolio, 'loader') and hasattr(self.portfolio.loader, 'save_games'):
                                        self.portfolio.loader.save_games(self.portfolio.games)
                                    print(f"\n✓ Cleared all locations for {game.title}")
                                else:
                                    print("\nCancelled")
                            else:
                                print("\nCancelled")
                        else:
                            # No current location, just assign new one(s)
                            locations = self.location_manager.select_multiple_locations()
                            if locations:
                                game.locations = locations
                                game.location = ', '.join(locations)
                                if hasattr(self.portfolio, 'loader') and hasattr(self.portfolio.loader, 'save_games'):
                                    self.portfolio.loader.save_games(self.portfolio.games)
                                print(f"\n✓ Assigned location(s): {game.location}")
                            else:
                                print("\nNo locations selected")
                    else:
                        print("Game not found")
                except ValueError:
                    print("Invalid game number")
                input("\nPress Enter to continue...")

            elif choice == "6":
                try:
                    game_num = int(input("\nEnter game number: "))
                    game = self.portfolio.lookup_game_by_number(game_num)
                    if game:
                        print(f"\nGame: {game.title}")
                        print(f"Current location(s): {game.location if game.location else 'None'}")

                        print("\nWhat would you like to do?")
                        print("1. Replace all locations")
                        print("2. Add more locations")
                        print("3. Clear all locations")
                        sub_choice = input("Choice: ").strip()

                        if sub_choice == "1":
                            locations = self.location_manager.select_multiple_locations()
                            if locations:
                                game.locations = locations
                                game.location = ', '.join(locations)
                                # Save changes
                                if hasattr(self.portfolio, 'loader') and hasattr(self.portfolio.loader, 'save_games'):
                                    self.portfolio.loader.save_games(self.portfolio.games)
                                print(f"\n✓ Updated {game.title} location(s) to: {game.location}")

                        elif sub_choice == "2":
                            new_locs = self.location_manager.select_multiple_locations()
                            if new_locs:
                                current = game.locations if game.locations else []
                                combined = list(set(current + new_locs))
                                game.locations = combined
                                game.location = ', '.join(combined)
                                # Save changes
                                if hasattr(self.portfolio, 'loader') and hasattr(self.portfolio.loader, 'save_games'):
                                    self.portfolio.loader.save_games(self.portfolio.games)
                                print(f"\n✓ Updated {game.title} location(s) to: {game.location}")

                        elif sub_choice == "3":
                            game.locations = []
                            game.location = ""
                            # Save changes
                            if hasattr(self.portfolio, 'loader') and hasattr(self.portfolio.loader, 'save_games'):
                                self.portfolio.loader.save_games(self.portfolio.games)
                            print(f"\n✓ Cleared all locations for {game.title}")
                    else:
                        print("Game not found")
                except ValueError:
                    print("Invalid game number")
                input("\nPress Enter to continue...")

            elif choice == "0":
                break
            else:
                print("\nInvalid choice. Please try again.")

    def view_all_games(self):
        """Display all games in the collection."""
        print("\n" + "="*80)
        print(f"ALL GAMES IN COLLECTION ({len(self.portfolio.games)} total)")
        print("="*80)

        if not self.portfolio.games:
            print("\nNo games in collection yet.")
        else:
            # Sort by game number
            sorted_games = sorted(self.portfolio.games, key=lambda g: g.game_number)

            for game in sorted_games:
                location_str = f" | Location: {game.location}" if game.location else ""
                print(f"  #{game.game_number}: {game.title} (Weight: {game.weight}){location_str}")

        input("\nPress Enter to continue...")

    def add_delete_games_menu(self):
        """Menu for adding and deleting games."""
        while True:
            print("\n" + "-" * 80)
            print("ADD/DELETE GAMES")
            print("-" * 80)
            print("1. Add a new game")
            print("2. Delete a game")
            print("3. View all games (quick list)")
            print("0. Back to main menu")
            print("-" * 80)

            choice = input("\nEnter choice: ").strip()

            if choice == "1":
                # Add new game
                print("\n" + "="*50)
                print("ADD NEW GAME")
                print("="*50)

                try:
                    # Get next game number - find first available gap or use next sequential
                    existing_numbers = sorted([g.game_number for g in self.portfolio.games])
                    new_game_num = None

                    # Look for gaps in the sequence
                    for i, num in enumerate(existing_numbers, start=1):
                        if num != i:
                            new_game_num = i
                            break

                    # If no gaps, use next sequential number
                    if new_game_num is None:
                        new_game_num = len(existing_numbers) + 1 if existing_numbers else 1

                    print(f"New game will be assigned number: {new_game_num}")

                    # Get basic info
                    title = input("\nGame title: ").strip()
                    if not title:
                        print("Title cannot be empty")
                        input("\nPress Enter to continue...")
                        continue

                    category = input("Category (optional): ").strip()
                    mechanisms = input("Mechanisms (optional): ").strip()
                    description = input("Description (optional): ").strip()
                    num_players = input("Number of players (e.g., '2-4'): ").strip()
                    playing_time = input("Playing time (e.g., '60 min'): ").strip()

                    # Get weight with validation
                    while True:
                        weight_str = input("Complexity weight (1.0-5.0, 1=lightest, 5=heaviest): ").strip()
                        try:
                            weight = float(weight_str)
                            if 1.0 <= weight <= 5.0:
                                break
                            else:
                                print("Weight must be between 1.0 and 5.0")
                        except ValueError:
                            print("Please enter a valid number")

                    # Painted status
                    painted_str = input("Is it painted? (y/n): ").strip().lower()
                    painted = painted_str == 'y'

                    # Can travel
                    travel_str = input("Can it travel? (y/n): ").strip().lower()
                    can_travel = travel_str == 'y'

                    # Optional fields
                    expansions = input("Expansions (optional): ").strip()
                    links = input("Links (optional): ").strip()
                    notes = input("Notes (optional): ").strip()

                    # Location assignment
                    print("\nAssign location(s) to this game:")
                    locations = self.location_manager.select_multiple_locations()

                    # Create the game
                    from board_game import BoardGame
                    new_game = BoardGame(
                        game_number=new_game_num,
                        title=title,
                        category=category,
                        mechanisms=mechanisms,
                        description=description,
                        num_players=num_players,
                        playing_time=playing_time,
                        weight=weight,
                        painted=painted,
                        location=', '.join(locations) if locations else '',
                        locations=locations,
                        can_travel=can_travel,
                        expansions=expansions,
                        links=links,
                        notes=notes
                    )

                    # Add to portfolio
                    self.portfolio.games.append(new_game)

                    # Add to hash table for lookup
                    self.portfolio.game_hash.insert(new_game_num, new_game)

                    # Save to file
                    if hasattr(self.portfolio, 'loader') and hasattr(self.portfolio.loader, 'save_games'):
                        if self.portfolio.loader.save_games(self.portfolio.games):
                            print(f"\n✓ Successfully added '{title}' (#{new_game_num})")
                        else:
                            print("\n⚠ Game added but could not save to file")
                    else:
                        print(f"\n✓ Added '{title}' (#{new_game_num}) - Note: Save to file manually")

                except Exception as e:
                    print(f"\nError adding game: {e}")

                input("\nPress Enter to continue...")

            elif choice == "2":
                # Delete game
                print("\n" + "="*50)
                print("DELETE GAME")
                print("="*50)

                try:
                    game_num = int(input("\nEnter game number to delete: "))
                    game = self.portfolio.lookup_game_by_number(game_num)

                    if game:
                        print(f"\nGame: {game.title}")
                        print(f"  Number: {game.game_number}")
                        print(f"  Weight: {game.weight}")
                        print(f"  Location: {game.location if game.location else 'None'}")

                        confirm = input("\nAre you sure you want to delete this game? (yes/no): ").strip().lower()

                        if confirm == 'yes':
                            self.portfolio.games.remove(game)

                            # Remove from hash table
                            self.portfolio.game_hash.remove(game.game_number)

                            # Renumber all games to close gaps
                            sorted_games = sorted(self.portfolio.games, key=lambda g: g.game_number)
                            for i, g in enumerate(sorted_games, start=1):
                                old_num = g.game_number
                                if old_num != i:
                                    # Update game number
                                    g.game_number = i
                                    # Update hash table
                                    self.portfolio.game_hash.remove(old_num)
                                    self.portfolio.game_hash.insert(i, g)

                            # Save to file
                            if hasattr(self.portfolio, 'loader') and hasattr(self.portfolio.loader, 'save_games'):
                                if self.portfolio.loader.save_games(self.portfolio.games):
                                    print(f"\n✓ Successfully deleted '{game.title}'")
                                    print(f"✓ Renumbered games to close gaps")
                                else:
                                    print("\n⚠ Game deleted but could not save to file")
                            else:
                                print(f"\n✓ Deleted '{game.title}' - Note: Save to file manually")
                        else:
                            print("Cancelled")
                    else:
                        print(f"Game #{game_num} not found")

                except ValueError:
                    print("Invalid game number")
                except Exception as e:
                    print(f"Error deleting game: {e}")

                input("\nPress Enter to continue...")

            elif choice == "3":
                # Quick list of all games
                print("\n" + "="*50)
                print(f"ALL GAMES ({len(self.portfolio.games)} total)")
                print("="*50)

                # Sort by game number
                sorted_games = sorted(self.portfolio.games, key=lambda g: g.game_number)

                for game in sorted_games:
                    print(f"  #{game.game_number}: {game.title} (Weight: {game.weight})")

                input("\nPress Enter to continue...")
                # Loop continues back to menu

            elif choice == "0":
                break
            else:
                print("\nInvalid choice. Please try again.")

    def run(self):
        """Run the interactive interface."""
        self.initialize_system()

        while True:
            self.display_main_menu()
            choice = input("\nEnter choice: ").strip()

            # Academic Demonstrations (1-5)
            if choice == "1":
                self.bubble_sort_menu()
            elif choice == "2":
                self.quickselect_menu()
            elif choice == "3":
                self.set_operations_menu()
            elif choice == "4":
                self.data_structures_menu()
            elif choice == "5":
                self.performance_analysis_menu()

            # Collection Management (6-10)
            elif choice == "6":
                self.view_all_games()
            elif choice == "7":
                self.add_delete_games_menu()
            elif choice == "8":
                self.statistics_menu()
            elif choice == "9":
                # Search & Lookup
                try:
                    search_input = input("Enter game number to lookup: ").strip()
                    if search_input:
                        game_num = int(search_input)
                        game = self.portfolio.lookup_game_by_number(game_num)
                        if game:
                            print(f"\n{game.title}")
                            print(f"  Number: {game.game_number}")
                            print(f"  Location: {game.location}")
                            print(f"  Painted: {game.painted}")
                            print(f"  Weight: {game.weight}")
                            print(f"  Players: {game.num_players}")
                            print(f"  Time: {game.playing_time}")
                        else:
                            print("Game not found")
                    else:
                        print("Lookup cancelled")
                except ValueError:
                    print("Invalid input. Please enter a valid game number.")
                except Exception as e:
                    print(f"An error occurred: {e}")
                input("\nPress Enter to continue...")
            elif choice == "10":
                self.location_management_menu()
            elif choice == "0":
                print("\nThank you for using the Board Game Collection Manager!")
                print("=" * 80)
                break
            else:
                print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    ui = InteractiveUI()
    ui.run()
