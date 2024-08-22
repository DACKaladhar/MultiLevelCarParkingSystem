
## Parking Management System

This Python project provides a simple parking management system for a multi-floor parking facility. It allows users to park and unpark vehicles, displays available parking slots, and maintains a record of parked vehicles. The system uses a 3D list to manage parking spaces and provides a command-line interface for user interactions.

### Features

- **Parking Allocation**: Park a vehicle in the first available slot and automatically update the slot status.
- **Unparking**: Remove a vehicle from the parking area by specifying its number and free up the slot.
- **Display Slots**: View the current status of all parking slots in a 3D-list format.
- **User-Friendly Interface**: Command-line interface to interact with the system.

### Instructions

1. **Run the Script**:
   ```bash
   python parking_management.py
   ```

2. **Commands**:
   - `in`: Park a new vehicle.
   - `out.vehicle<number>`: Unpark a specific vehicle.
   - `--display-slots`: Display the current parking status.
   - `close`: Terminate the program.

### Example Usage

- **Parking a Vehicle**: Enter `in` to park a new vehicle.
- **Unparking a Vehicle**: Enter `out.vehicle1` to unpark vehicle number 1.
- **Display Slots**: Enter `--display-slots` to view available slots.

### Implementation Details

- **Data Structure**: Utilizes a 3D list to represent parking floors, columns, and rows.
- **Vehicle Management**: Maintains a history of parked vehicles and checks availability for parking or unparking.
