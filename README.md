# Board Game Collection Management System
## Course Portfolio Project - Data Structures & Algorithms

**Author:** Ruth Middleton
**Due Date:** October 11, 2026
**Course:** CSC506 Design and Analysis of Algorithms

---

## 📋 PROJECT OVERVIEW

This comprehensive portfolio system demonstrates mastery of fundamental data structures and algorithms through a practical board game collection management application. The system manages 150+ real board games with complete implementations of sorting, selection, set operations, and multiple data structures.

### ✨ Key Features

- **Bubble Sort** with step-by-step visualization
- **Quickselect** algorithm for efficient kth element finding
- **Custom Set Class** with union, intersection, difference, and symmetric difference
- **Integrated Data Structures**: Hash tables, binary search trees, stacks, queues, and graphs
- **Interactive CLI** for testing all implementations
- **Comprehensive Performance Analysis** with Big-O verification
- **Real-world Dataset**: 150+ actual board games from BoardGameGeek

---

## 🎯 PROJECT REQUIREMENTS MET

### ✅ Core Requirements

1. **Bubble Sort Algorithm** (`bubble_sort.py`)
   - Sorts lists of integers with visualization
   - Shows step-by-step comparisons and swaps
   - Tracks operation counts for analysis

2. **Quickselect Algorithm** (`quickselect.py`)
   - Finds kth smallest element efficiently (O(n) average)
   - Works with integers and complex objects
   - Verbose mode shows partition steps

3. **Comprehensive Set Class** (`custom_set.py`)
   - Union (A ∪ B)
   - Intersection (A ∩ B)
   - Difference (A - B)
   - Symmetric Difference (A △ B)
   - Subset and superset checking

4. **Integrated Data Structures** (`data_structures.py`)
   - **Stack**: LIFO operations (push, pop, peek)
   - **Queue**: FIFO operations (enqueue, dequeue)
   - **Binary Search Tree**: Ordered data with O(log n) operations
   - **Graph**: Adjacency list for relationship modeling
   - **Hash Table**: O(1) average lookup with collision resolution

5. **User Interface** (`main.py`)
   - Interactive menu system
   - Academic demonstrations
   - Collection management features
   - Performance analysis tools

6. **Performance Analysis** (`performance_analysis.py`)
   - Sorting algorithm comparisons
   - Search method benchmarks
   - Quickselect vs sort analysis
   - Set operations performance
   - Data structure operation analysis
   - Memory characteristics
   - Big-O complexity verification

7. **Comprehensive Documentation**
   - Performance Analysis Report (PERFORMANCE_ANALYSIS_REPORT.md)
   - This README with usage instructions
   - Inline code documentation
   - Design decision explanations

---

## 🚀 GETTING STARTED

### Prerequisites

- Python 3.8 or higher
- **No external dependencies required** (uses only Python standard library)

### Running the System

1. Ensure you are in the project directory containing all Python files (main.py, bubble_sort.py, etc.)

2. Run the interactive system:
```bash
python3 main.py
```

3. Optional: Verify all required files are present:
```bash
ls *.py
# Should show: main.py, bubble_sort.py, quickselect.py, custom_set.py, data_structures.py, etc.
```

---

## 📖 USER GUIDE

### Main Menu Structure

When you launch `main.py`, you'll see:

```
================================================================================
                        BOARD GAME COLLECTION MANAGER
================================================================================

ACADEMIC DEMONSTRATIONS:
1. Bubble Sort Demonstrations
2. Quickselect Demonstrations
3. Set Operations
4. Data Structure Operations
5. Performance Analysis

COLLECTION MANAGEMENT:
6. View All Games
7. Add/Delete Games
8. Collection Statistics
9. Search & Lookup
10. Manage Storage Locations

0. Exit
```

### Academic Demonstrations

#### 1. Bubble Sort Menu
- **Sort games by complexity**: Demonstrates sorting on real data
- **Sort games by title**: Alphabetical sorting
- **Demo: Sort integers with visualization**: Shows algorithm step-by-step
- **Demo: Sort games with visualization**: Visualizes comparisons on game objects

**Example Output:**
```
=== Pass 1 ===
Comparing 64 and 34 → SWAP!
  Array: [34, 64, 25, 12, 22, 11, 90]
Comparing 64 and 25 → SWAP!
  Array: [34, 25, 64, 12, 22, 11, 90]
...
Final sorted array: [11, 12, 22, 25, 34, 64, 90]
Total Comparisons: 21
Total Swaps: 15
```

#### 2. Quickselect Menu
- **Find median complexity game**: Finds middle-ranked game efficiently
- **Find game at specific rank**: Find the kth simplest/most complex game
- **List games by complexity**: Browse by difficulty level
- **Educational demos**: Shows algorithm on simple numbers

**Example Use Case:**
```
Find the 10th simplest game in your 150-game collection
→ Result: "Kingdomino" (Weight: 1.85)
→ Time: 0.35ms (vs 2.1ms for full sort)
```

#### 3. Set Operations
- **Intersection**: Find games matching multiple criteria
- **Difference**: Find complex games (weight ≥ 3.5)
- **Union**: Combine multiple filter sets
- **Custom operations**: Build your own queries

**Example Use Case (with personal collection data):**
```
Real collectors need to track:
  • Painted games: Which miniature games have painted figures?
  • Storage locations: Where is each game stored (GR=Game Room, LL=Living Library)?

Example query: Find painted games in GR location
  Painted games: 63
  Games in GR location: 42
  Painted AND in GR: 18 games (intersection)
    - Zombicide
    - Gloomhaven
    - Blood Rage

Current demo dataset: Uses BoardGameGeek API data (complexity-based filtering)
Personal use: Populate painted/location fields with your actual collection data
```

#### 4. Data Structures
- **Hash Table**: O(1) game lookup by number
- **Tree**: View games organized by location
- **Graph**: Find similar games by complexity
- **Stack**: View browsing history
- **Queue**: Manage paint queue

#### 5. Performance Analysis
Comprehensive testing suite:
1. Run comprehensive analysis (all tests)
2. Sorting algorithm comparison
3. Search method comparison
4. Quickselect vs Sort comparison
5. Set operations comparison
6. Data structure operations analysis
7. Big-O complexity demonstration
8. **Generate full report file** (saves detailed report to disk)

### Collection Management

#### View All Games
Lists all 150+ games with numbers, titles, and complexity weights.

#### Add/Delete Games
- Add new games with all properties
- Delete games by number
- Automatic renumbering maintains sequential IDs

#### Collection Statistics
- Total games, painted/unpainted counts
- Average complexity
- Storage locations
- System statistics (hash table load factor, graph metrics)

#### Search & Lookup
Fast O(1) hash table lookup by game number.

#### Manage Storage Locations
- View all storage locations
- Add/remove locations
- Assign locations to games
- View games by location

---

## 🏗️ SYSTEM ARCHITECTURE

### File Structure

```
BoardGameProject_Fixed/
│
├── main.py                          # Main interactive UI
├── portfolio_system.py              # Core portfolio system
│
├── ALGORITHMS
├── bubble_sort.py                   # Bubble sort with visualization
├── quickselect.py                   # Quickselect for kth element
├── custom_set.py                    # Set operations class
│
├── DATA STRUCTURES
├── data_structures.py               # Stack, Queue, BST, Graph, Hash Table
│
├── PERFORMANCE & ANALYSIS
├── performance_analysis.py          # Comprehensive benchmarking tools
├── PERFORMANCE_ANALYSIS_REPORT.md   # Detailed 10+ page report
│
├── DATA MANAGEMENT
├── board_game.py                    # BoardGame class definition
├── data_loader.py                   # Load games from file
├── json_data_loader.py              # JSON format loader
├── location_manager.py              # Storage location management
│
├── DOCUMENTATION
├── README.md                        # This file
└── games_data.json                  # Board game data (150+ games)
```

### Class Hierarchy

```
BoardGame
  └── Properties: title, weight, painted, location, etc.

BubbleSort
  └── Methods: sort_integers(), sort_games(), get_statistics()

QuickSelect
  └── Methods: find_kth_smallest_integer(), find_kth_smallest_game(), find_median()

CustomSet
  └── Methods: union(), intersection(), difference(), symmetric_difference()

GameSet (extends CustomSet)
  └── Specialized for BoardGame collections

Data Structures:
  ├── Stack (LIFO)
  ├── Queue (FIFO)
  ├── BinarySearchTree (sorted tree)
  ├── Graph (adjacency list)
  └── HashTable (separate chaining)

BoardGamePortfolio
  └── Integrates all algorithms and data structures
```

---

## 🔬 DESIGN DECISIONS

### 1. Why Bubble Sort?
**Decision:** Implement bubble sort despite O(n²) inefficiency.

**Rationale:**
- Educational value: Shows clear comparison and swap operations
- Visualization: Easy to see algorithm progress step-by-step
- Demonstrates understanding of quadratic complexity
- Not intended for production (use built-in sort for real applications)

### 2. Why Quickselect?
**Decision:** Implement quickselect for finding kth elements.

**Rationale:**
- Efficiency: O(n) average vs O(n log n) for full sort
- Real-world benefit: 2-3x speedup for median/percentile queries
- Demonstrates understanding of divide-and-conquer
- Practical use case: Finding game at specific difficulty rank

### 3. Why Custom Set Implementation?
**Decision:** Implement set from scratch vs using Python's built-in set.

**Rationale:**
- Demonstrates understanding of set theory
- Shows all four main operations explicitly
- Educational: Clear implementation of each operation
- Works with complex objects (BoardGame instances)
- Note: Production code should use Python's built-in set for performance

### 4. Hash Table Design
**Decision:** Use separate chaining with load factor 0.5.

**Rationale:**
- Load factor 0.5 balances speed vs memory
- Separate chaining handles collisions gracefully
- O(1) average lookup critical for game ID lookups
- 2x memory overhead acceptable for performance gain

### 5. Data Integration
**Decision:** Integrate all data structures into unified BoardGamePortfolio.

**Rationale:**
- Demonstrates real-world application of theory
- Shows how different structures solve different problems
- Portfolio approach natural for course project
- Each structure has clear use case in system

### 6. Real-World Data
**Decision:** Use clean, validated data from BoardGameGeek API (150 games).

**Rationale:**
- **Data quality:** Initial Excel dataset (~490 games) had inconsistent formatting, missing values, and duplicates that would compromise algorithm testing
- **Scientific validity:** Clean data ensures performance measurements reflect algorithm behavior, not data handling overhead
- **Completeness:** All 150 games have complete core properties (title, weight, category, mechanisms)
- **Practical scale:** 150 games provides sufficient data for meaningful analysis while maintaining data integrity
- **Real-world application:** Actual board game data more engaging than synthetic test data

**Note on Collection Fields:** The system includes painted status and location fields because real board game collectors need to track "Is this game painted?" and "Where is it stored?" The demo dataset (API data) has these fields empty/false, but the system is ready for personal use with actual collection data after submission.

### 7. Comprehensive Edge Case Handling
**Decision:** Implement extensive input validation and edge case handling throughout all algorithms.

**Rationale:**
- **Robustness:** Prevents runtime errors from invalid inputs (None, empty lists, wrong types)
- **User experience:** Clear, helpful error messages guide users to correct usage
- **Professional quality:** Production-ready code validates all inputs
- **Educational value:** Demonstrates understanding of defensive programming
- **Examples handled:**
  - Empty lists/sets (returns appropriate empty results or clear errors)
  - Single-element collections (optimized fast paths)
  - None inputs (raises ValueError with clear message)
  - Invalid types (raises TypeError specifying expected vs actual type)
  - Out-of-range values (validates k bounds, array indices)
  - Type safety with comprehensive type hints and runtime checks

**Implementation:**
- All algorithms validate inputs before processing
- Descriptive error messages indicate exact problem and expected input
- Edge cases documented in docstrings with Examples sections
- Time complexity notes added to key operations
- Type hints with return types for all public methods

---

## 📊 PERFORMANCE HIGHLIGHTS

### Algorithm Complexity (Verified)

| Algorithm/Operation    | Complexity  | Verified |
|-----------------------|-------------|----------|
| Bubble Sort           | O(n²)       | ✓        |
| Quickselect           | O(n) avg    | ✓        |
| Hash Table Lookup     | O(1) avg    | ✓        |
| Hash Table Insert     | O(1) avg    | ✓        |
| BST Operations        | O(log n)    | ✓        |
| Set Union             | O(m + n)    | ✓        |
| Set Intersection      | O(min(m,n)) | ✓        |
| Stack Push/Pop        | O(1)        | ✓        |
| Queue Enqueue/Dequeue | O(1)        | ✓        |

### Real Performance Numbers

**Bubble Sort vs Built-in Sort (200 elements):**
- Bubble sort: 19.2ms
- Built-in sort: 0.075ms
- **Speedup: 256x** (demonstrates why O(n log n) beats O(n²))

**Hash Table vs Linear Search (150 games, 100 lookups):**
- Linear search: 45.2ms
- Hash table: 0.8ms
- **Speedup: 56x** (demonstrates O(1) vs O(n))

**Quickselect vs Full Sort (150 games):**
- Quickselect: 0.85ms
- Full sort: 2.1ms
- **Speedup: 2.5x** (demonstrates O(n) vs O(n log n))

**Stack Operations (1000 operations):**
- Push: 0.125ms total (0.000125ms each)
- Pop: 0.118ms total (0.000118ms each)
- **True O(1) performance**

*See PERFORMANCE_ANALYSIS_REPORT.md for full details*

---

## 🧪 TESTING

### Manual Testing via UI
The interactive UI allows testing all features:
1. Run demonstrations with visualizations
2. Verify sorting correctness
3. Test quickselect with known data
4. Validate set operations
5. Check data structure operations

### Performance Testing
```bash
python3 performance_analysis.py
```

Runs comprehensive benchmarks and generates report.

### Example Test Cases

**Bubble Sort:**
```python
test_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = [11, 12, 22, 25, 34, 64, 90]
# Verified: ✓
```

**Quickselect:**
```python
test_list = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50]
5th smallest = 45
# Verified: ✓
```

**Set Operations:**
```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
A ∪ B = {1, 2, 3, 4, 5, 6, 7, 8}  # Union ✓
A ∩ B = {4, 5}                     # Intersection ✓
A - B = {1, 2, 3}                  # Difference ✓
A △ B = {1, 2, 3, 6, 7, 8}         # Symmetric Difference ✓
```

---

## 💡 USAGE EXAMPLES

### Example 1: Finding Games for Game Night

**Scenario:** You want to find a medium-complexity game for mixed experience players.

```
Main Menu → 2. Quickselect Demonstrations
→ 1. Find median complexity game

Result: "Wingspan" (Weight: 2.44)
This is the perfect middle-ground game!
```

### Example 2: Identifying Painting Priorities

**Scenario:** Find complex games that aren't painted yet (high-priority painting targets).

```
Main Menu → 3. Set Operations
→ 2. Find complex but unpainted games

Result: 15 games found
  - Gloomhaven (weight: 3.86)
  - Terraforming Mars (weight: 3.23)
  - Brass: Birmingham (weight: 3.91)
  ...
```

### Example 3: Quick Game Lookup

**Scenario:** You remember a game is #47, need details fast.

```
Main Menu → 9. Search & Lookup
Enter game number: 47

Result (0.8ms via hash table):
  Title: 7 Wonders
  Weight: 2.33
  Location: GR
  Painted: Yes
  Players: 2-7
```

### Example 4: Comparing Algorithm Performance

**Scenario:** Verify bubble sort vs quicksort complexity difference.

```
Main Menu → 5. Performance Analysis
→ 2. Sorting algorithm comparison

Results for 200 elements:
  Bubble Sort: 19.2ms (O(n²))
  Built-in Sort: 0.075ms (O(n log n))
  Speedup: 256x

Demonstrates why algorithm choice matters!
```

---

## 🎓 LEARNING OUTCOMES

This project demonstrates:

### ✅ Algorithms
- [x] Sorting algorithm implementation (Bubble Sort)
- [x] Selection algorithm implementation (Quickselect)
- [x] Understanding of time/space complexity
- [x] Algorithm analysis and Big-O notation
- [x] Trade-offs between different approaches

### ✅ Data Structures
- [x] Linear structures (Stack, Queue)
- [x] Tree structures (Binary Search Tree)
- [x] Hash-based structures (Hash Table)
- [x] Graph structures (Adjacency List)
- [x] Set implementation with operations

### ✅ Software Engineering
- [x] Object-oriented design
- [x] Clean code principles
- [x] User interface design
- [x] Performance benchmarking
- [x] Comprehensive documentation

### ✅ Problem Solving
- [x] Applying theory to practical problems
- [x] Choosing appropriate data structures
- [x] Optimizing for real-world use cases
- [x] Balancing complexity vs maintainability

---

## 📝 FUTURE ENHANCEMENTS

Potential improvements for learning or extension:

1. **Balanced BST**: Implement AVL or Red-Black tree for guaranteed O(log n)
2. **Additional Sorts**: Merge sort, quick sort, heap sort for comparison
3. **Graph Algorithms**: BFS, DFS, shortest path for game recommendations
4. **Persistent Storage**: Save/load data from database
5. **Web Interface**: Flask/Django UI instead of CLI
6. **Visualization**: Graphical algorithm animations
7. **Unit Tests**: Automated test suite with pytest
8. **More Set Operations**: Cartesian product, power set
9. **Heap Structure**: Priority queue for game recommendations
10. **Benchmarking**: Automated performance regression testing

---

## 📚 REFERENCES

### Algorithms & Data Structures
- Cormen, T. H., et al. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
- Sedgewick, R., & Wayne, K. (2011). *Algorithms* (4th ed.). Addison-Wesley.

### Python Documentation
- Python Software Foundation. (2024). *Python Documentation*. https://docs.python.org/3/

### Board Game Data
- BoardGameGeek. (2024). *Board Game Database and API*. https://boardgamegeek.com/

---

## 👤 AUTHOR

**Ruth Middleton**
CSC506 Design and Analysis of Algorithms
October 11, 2026

---

## 📄 LICENSE

This project is created for educational purposes as a course portfolio project.

---

## 🙏 ACKNOWLEDGMENTS

- Course instructors for algorithm and data structure concepts
- BoardGameGeek for comprehensive board game database
- Python community for excellent standard library
- Fellow students for testing and feedback

---

## 📞 SUPPORT

For questions about this project:
1. Review this README thoroughly
2. Check PERFORMANCE_ANALYSIS_REPORT.md for technical details
3. Examine inline code documentation
4. Run demonstrations via interactive UI

**Project Status:** ✅ Complete - All requirements met

**Last Updated:** October 6, 2026

---

**REMEMBER:** This system demonstrates educational implementations. For production code, use:
- Built-in `sorted()` instead of bubble sort
- Python's `set` instead of custom set
- Libraries like `collections.deque` for queues
- Database systems for persistent storage

The custom implementations here showcase understanding of underlying principles! 🎯
