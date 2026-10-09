"""
BoardGame Data Model
Represents a single board game with all its attributes from the Excel file.
"""

from typing import Optional, List
from dataclasses import dataclass, field


@dataclass
class BoardGame:
    """
    Represents a board game with all tracked attributes.

    This class stores all information about a board game including its title,
    gameplay characteristics, location, and metadata.
    """
    # Core identification
    game_number: int
    title: str

    # Game characteristics
    category: str = ""
    mechanisms: str = ""
    description: str = ""

    # Gameplay information
    num_players: str = ""
    playing_time: str = ""
    weight: float = 0.0  # Complexity on scale 1-5

    # Collection management
    painted: bool = False
    location: str = ""  # For backward compatibility, stores comma-separated locations
    locations: List[str] = field(default_factory=list)  # Modern approach: list of locations
    can_travel: bool = False

    def __post_init__(self):
        """Initialize locations list from location string if needed"""
        if not self.locations and self.location:
            # Parse comma-separated locations from old format
            self.locations = [loc.strip() for loc in self.location.split(',') if loc.strip()]
        elif self.locations:
            # Sync location string from locations list
            self.location = ', '.join(self.locations)

    # Additional information
    expansions: str = ""
    links: str = ""
    notes: str = ""

    def __repr__(self):
        """String representation for debugging."""
        return f"BoardGame(#{self.game_number}: {self.title})"

    def __str__(self):
        """User-friendly string representation."""
        return f"{self.game_number}. {self.title} - {self.location}"

    def get_categories_list(self) -> List[str]:
        """
        Parse category string into list of individual categories.
        Categories are separated by newlines in the data.
        """
        if not self.category:
            return []
        return [cat.strip() for cat in self.category.split('\n') if cat.strip()]

    def get_mechanisms_list(self) -> List[str]:
        """
        Parse mechanisms string into list of individual mechanisms.
        Mechanisms are separated by newlines in the data.
        """
        if not self.mechanisms:
            return []
        return [mech.strip() for mech in self.mechanisms.split('\n') if mech.strip()]

    def get_playing_time_minutes(self) -> Optional[int]:
        """
        Extract numeric playing time in minutes.
        Handles formats like "60 - 120 Min", "120 Mins", etc.
        Returns the maximum time if range is given.
        """
        if not self.playing_time:
            return None

        # Remove common suffixes
        time_str = self.playing_time.replace("Min", "").replace("mins", "").replace("minutes", "").strip()

        # Handle ranges (take the maximum)
        if "-" in time_str:
            parts = time_str.split("-")
            try:
                return int(parts[-1].strip())
            except (ValueError, IndexError):
                return None

        # Handle single number
        try:
            return int(time_str.strip())
        except ValueError:
            return None

    def matches_category(self, category: str) -> bool:
        """Check if game has a specific category."""
        return category.lower() in [cat.lower() for cat in self.get_categories_list()]

    def matches_mechanism(self, mechanism: str) -> bool:
        """Check if game uses a specific mechanism."""
        return mechanism.lower() in [mech.lower() for mech in self.get_mechanisms_list()]

    def is_solo_playable(self) -> bool:
        """Check if game can be played solo."""
        return "solo" in self.num_players.lower() or "1" in self.num_players
