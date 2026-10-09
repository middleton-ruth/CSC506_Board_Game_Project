"""
Data Structures Module
Requirement #4: Integrate all data structures from previous modules
(stacks, queues, trees, graphs, hash tables) into one unified system.
"""

from typing import Any, List, Optional, Dict, Set
from board_game import BoardGame


# ==================== STACK ====================

class Stack:
    """
    Stack implementation (LIFO - Last In, First Out).

    Use cases for board game collection:
    - Undo/redo operations
    - Recently viewed games
    - Browse history
    """

    def __init__(self):
        """Initialize empty stack."""
        self._items = []

    def push(self, item: Any) -> None:
        """
        Push an item onto the stack.

        Args:
            item: Item to push
        """
        self._items.append(item)

    def pop(self) -> Any:
        """
        Pop and return the top item.

        Returns:
            Top item from stack

        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> Any:
        """
        Return the top item without removing it.

        Returns:
            Top item from stack

        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        """Check if stack is empty."""
        return len(self._items) == 0

    def size(self) -> int:
        """Get number of items in stack."""
        return len(self._items)

    def clear(self) -> None:
        """Remove all items from stack."""
        self._items.clear()

    def __str__(self) -> str:
        return f"Stack({self._items})"


# ==================== QUEUE ====================

class Queue:
    """
    Queue implementation (FIFO - First In, First Out).

    Use cases for board game collection:
    - Games to play next
    - Games to paint queue
    - Priority game queue
    """

    def __init__(self):
        """Initialize empty queue."""
        self._items = []

    def enqueue(self, item: Any) -> None:
        """
        Add an item to the rear of the queue.

        Args:
            item: Item to add
        """
        self._items.append(item)

    def dequeue(self) -> Any:
        """
        Remove and return the front item.

        Returns:
            Front item from queue

        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)

    def front(self) -> Any:
        """
        Return the front item without removing it.

        Returns:
            Front item from queue

        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return len(self._items) == 0

    def size(self) -> int:
        """Get number of items in queue."""
        return len(self._items)

    def clear(self) -> None:
        """Remove all items from queue."""
        self._items.clear()

    def __str__(self) -> str:
        return f"Queue({self._items})"


# ==================== BINARY SEARCH TREE ====================

class TreeNode:
    """Node in a binary search tree."""

    def __init__(self, key: Any, value: Any):
        """
        Initialize tree node.

        Args:
            key: Sort key for the node
            value: Value stored in the node
        """
        self.key = key
        self.value = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class BinarySearchTree:
    """
    Binary Search Tree implementation.

    Use cases for board game collection:
    - Hierarchical organization (categories, locations)
    - Fast sorted access
    - Range queries (games with complexity 2.0-4.0)
    """

    def __init__(self):
        """Initialize empty tree."""
        self.root: Optional[TreeNode] = None
        self._size = 0

    def insert(self, key: Any, value: Any) -> None:
        """
        Insert a key-value pair into the tree.

        Args:
            key: Sort key
            value: Value to store
        """
        if self.root is None:
            self.root = TreeNode(key, value)
            self._size += 1
        else:
            self._insert_recursive(self.root, key, value)

    def _insert_recursive(self, node: TreeNode, key: Any, value: Any) -> None:
        """Helper method for recursive insertion."""
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key, value)
                self._size += 1
            else:
                self._insert_recursive(node.left, key, value)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key, value)
                self._size += 1
            else:
                self._insert_recursive(node.right, key, value)
        else:
            # Key already exists, update value
            node.value = value

    def search(self, key: Any) -> Optional[Any]:
        """
        Search for a value by key.

        Args:
            key: Key to search for

        Returns:
            Value if found, None otherwise
        """
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node: Optional[TreeNode], key: Any) -> Optional[Any]:
        """Helper method for recursive search."""
        if node is None:
            return None
        if key == node.key:
            return node.value
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def inorder_traversal(self) -> List[tuple]:
        """
        Return list of (key, value) tuples in sorted order.

        Returns:
            List of (key, value) tuples
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: Optional[TreeNode], result: List) -> None:
        """Helper method for inorder traversal."""
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append((node.key, node.value))
            self._inorder_recursive(node.right, result)

    def size(self) -> int:
        """Get number of nodes in tree."""
        return self._size

    def is_empty(self) -> bool:
        """Check if tree is empty."""
        return self.root is None


# ==================== GRAPH ====================

class Graph:
    """
    Graph implementation using adjacency list.

    Use cases for board game collection:
    - Game similarity network (games with similar mechanics)
    - Recommendation system (if you like A, try B)
    - Category relationships
    """

    def __init__(self, directed: bool = False):
        """
        Initialize empty graph.

        Args:
            directed: Whether graph is directed
        """
        self.directed = directed
        self.adjacency_list: Dict[Any, Set[Any]] = {}

    def add_vertex(self, vertex: Any) -> None:
        """
        Add a vertex to the graph.

        Args:
            vertex: Vertex to add
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = set()

    def add_edge(self, vertex1: Any, vertex2: Any) -> None:
        """
        Add an edge between two vertices.

        Args:
            vertex1: First vertex
            vertex2: Second vertex
        """
        # Ensure vertices exist
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        # Add edge
        self.adjacency_list[vertex1].add(vertex2)
        if not self.directed:
            self.adjacency_list[vertex2].add(vertex1)

    def get_neighbors(self, vertex: Any) -> Set[Any]:
        """
        Get all neighbors of a vertex.

        Args:
            vertex: Vertex to get neighbors for

        Returns:
            Set of neighboring vertices
        """
        return self.adjacency_list.get(vertex, set())

    def has_edge(self, vertex1: Any, vertex2: Any) -> bool:
        """
        Check if edge exists between two vertices.

        Args:
            vertex1: First vertex
            vertex2: Second vertex

        Returns:
            True if edge exists
        """
        return vertex2 in self.adjacency_list.get(vertex1, set())

    def get_vertices(self) -> List[Any]:
        """Get list of all vertices."""
        return list(self.adjacency_list.keys())

    def vertex_count(self) -> int:
        """Get number of vertices."""
        return len(self.adjacency_list)

    def edge_count(self) -> int:
        """Get number of edges."""
        count = sum(len(neighbors) for neighbors in self.adjacency_list.values())
        return count if self.directed else count // 2

    def __str__(self) -> str:
        lines = [f"Graph (directed={self.directed}):"]
        for vertex, neighbors in self.adjacency_list.items():
            lines.append(f"  {vertex} -> {neighbors}")
        return "\n".join(lines)


# ==================== HASH TABLE ====================

class HashTable:
    """
    Hash Table implementation using separate chaining for collision resolution.

    Use cases for board game collection:
    - Fast game lookup by ID
    - Location index (find all games in a location)
    - Category index
    """

    def __init__(self, size: int = 100):
        """
        Initialize hash table.

        Args:
            size: Initial size of hash table
        """
        self.size = size
        self.table: List[List[tuple]] = [[] for _ in range(size)]
        self._item_count = 0

    def _hash(self, key: Any) -> int:
        """
        Hash function to compute index.

        Args:
            key: Key to hash

        Returns:
            Hash value (index)
        """
        return hash(key) % self.size

    def insert(self, key: Any, value: Any) -> None:
        """
        Insert a key-value pair.

        Args:
            key: Key
            value: Value
        """
        index = self._hash(key)
        bucket = self.table[index]

        # Check if key already exists and update
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Key doesn't exist, add new entry
        bucket.append((key, value))
        self._item_count += 1

    def get(self, key: Any) -> Optional[Any]:
        """
        Get value for a key.

        Args:
            key: Key to look up

        Returns:
            Value if found, None otherwise
        """
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v

        return None

    def remove(self, key: Any) -> bool:
        """
        Remove a key-value pair.

        Args:
            key: Key to remove

        Returns:
            True if removed, False if not found
        """
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._item_count -= 1
                return True

        return False

    def contains(self, key: Any) -> bool:
        """
        Check if key exists in hash table.

        Args:
            key: Key to check

        Returns:
            True if key exists
        """
        return self.get(key) is not None

    def item_count(self) -> int:
        """Get number of items in hash table."""
        return self._item_count

    def load_factor(self) -> float:
        """Get load factor (items / table size)."""
        return self._item_count / self.size

    def get_all_keys(self) -> List[Any]:
        """Get list of all keys."""
        keys = []
        for bucket in self.table:
            for k, v in bucket:
                keys.append(k)
        return keys

    def get_all_values(self) -> List[Any]:
        """Get list of all values."""
        values = []
        for bucket in self.table:
            for k, v in bucket:
                values.append(v)
        return values

    def __str__(self) -> str:
        return f"HashTable(size={self.size}, items={self._item_count}, load_factor={self.load_factor():.2f})"
