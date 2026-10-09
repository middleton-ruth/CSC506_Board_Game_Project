"""
Location Manager for Board Game Collection
Allows users to define custom locations and reuse them across games
"""
import json
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from board_game import BoardGame


class LocationManager:
    """Manages custom storage locations for board games"""

    def __init__(self, locations_file: str = "locations.json"):
        self.locations_file = locations_file
        self.locations: List[str] = []
        self.load_locations()

    def load_locations(self) -> None:
        """Load locations from file"""
        try:
            with open(self.locations_file, 'r') as f:
                data = json.load(f)
                self.locations = data.get('locations', [])
        except FileNotFoundError:
            # Start with empty list if file doesn't exist
            self.locations = []
        except json.JSONDecodeError:
            print(f"Warning: Could not parse {self.locations_file}, starting fresh")
            self.locations = []

    def save_locations(self) -> bool:
        """Save locations to file"""
        try:
            with open(self.locations_file, 'w') as f:
                json.dump({'locations': self.locations}, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving locations: {e}")
            return False

    def add_location(self, location: str) -> bool:
        """Add a new location if it doesn't already exist"""
        location = location.strip()
        if not location:
            return False

        # Check if already exists (case-insensitive)
        if any(loc.lower() == location.lower() for loc in self.locations):
            print(f"Location '{location}' already exists")
            return False

        self.locations.append(location)
        self.save_locations()
        return True

    def remove_location(self, location: str, games: Optional[List] = None) -> bool:
        """
        Remove a location with optional warning about affected games

        Args:
            location: Location name to remove
            games: Optional list of all games to check for affected games

        Returns:
            True if removed, False if not found
        """
        location = location.strip()
        try:
            self.locations.remove(location)
            self.save_locations()
            return True
        except ValueError:
            return False

    def get_games_at_location(self, location: str, games: List) -> List:
        """Get all games stored at a specific location"""
        affected_games = []
        for game in games:
            # Check if location is in the game's locations list
            if hasattr(game, 'locations') and location in game.locations:
                affected_games.append(game)
            # Also check the location string for backward compatibility
            elif hasattr(game, 'location') and game.location:
                game_locs = [loc.strip() for loc in game.location.split(',')]
                if location in game_locs:
                    affected_games.append(game)
        return affected_games

    def get_locations(self) -> List[str]:
        """Get all locations"""
        return sorted(self.locations)

    def display_locations(self) -> None:
        """Display all locations with numbers"""
        if not self.locations:
            print("No locations defined yet")
            return

        print("\nYour storage locations:")
        for i, loc in enumerate(sorted(self.locations), 1):
            print(f"  {i}. {loc}")

    def select_location(self) -> Optional[str]:
        """Interactive location selection - user can pick existing or add new"""
        while True:
            print("\n" + "="*50)
            print("SELECT LOCATION")
            print("="*50)

            locations_sorted = sorted(self.locations)

            if locations_sorted:
                print("\nExisting locations:")
                for i, loc in enumerate(locations_sorted, 1):
                    print(f"  {i}. {loc}")
                print(f"\n  {len(locations_sorted) + 1}. Add a new location")
                print("  0. Skip (no location)")
            else:
                print("\nNo locations defined yet")
                print("  1. Add a new location")
                print("  0. Skip (no location)")

            choice = input("\nYour choice: ").strip()

            if choice == '0':
                return ''

            try:
                choice_num = int(choice)

                # Selecting existing location
                if 1 <= choice_num <= len(locations_sorted):
                    return locations_sorted[choice_num - 1]

                # Add new location
                elif choice_num == len(locations_sorted) + 1:
                    new_loc = input("Enter new location name: ").strip()
                    if new_loc:
                        self.add_location(new_loc)
                        print(f"Added location: {new_loc}")
                        return new_loc
                    else:
                        print("Location cannot be empty")
                else:
                    print("Invalid choice")
            except ValueError:
                print("Please enter a number")

    def select_multiple_locations(self) -> List[str]:
        """Allow user to select multiple locations for one game"""
        selected = []

        print("\n" + "="*50)
        print("SELECT LOCATION(S) FOR THIS GAME")
        print("="*50)
        print("Some games may be stored in multiple locations")
        print("(e.g., base game in one place, expansions in another)")

        while True:
            location = self.select_location()

            if location:
                selected.append(location)
                print(f"\nAdded: {location}")
                print(f"Current locations for this game: {', '.join(selected)}")

            if not selected:
                another = input("\nWould you like to add a location? (y/n): ").strip().lower()
                if another != 'y':
                    break
            else:
                another = input("\nAdd another location for this game? (y/n): ").strip().lower()
                if another != 'y':
                    break

        return selected
