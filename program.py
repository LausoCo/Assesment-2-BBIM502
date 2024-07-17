"""
@Project Name: Hotel Management Application System for 'LANGHAM Hotels'
@Author: Laura Sofía Nieto Contreras
@Date: 13/07/2024
@Application Purpose: Develop software application for 'LANGHAM Hotels' to manage their day-to-day operations
    like the allocation of rooms, deallocation of rooms, displaying the status of rooms. Also .txt file is used as database
"""

# #### REQUIRED LIBRARIES ####
# Import the datetime module to get the current date and time
import datetime

# Import the os module to interact with the operating system
import os


# #### CREATION OF CLASSES ####
# Creation of a class for Room information
class Room:
    # Estrict the type of the variables in the constructor
    def __init__(
        self,
        roomNumber: int,
        isAllocated: bool,
        # Default values for the type and price of the room
        type: str = "Single",
        price: float = 0.0,
    ):
        """
        Constructor for Room class, where the room number and the status of the room are initialized.
        Also, additional information like the type and price as room features
        """
        self.roomNumber = roomNumber
        self.isAllocated = isAllocated
        self.type = type
        self.price = price

    # Methods to allocate and deallocate a room
    def allocateRoom(self):
        self.isAllocated = True

    def deallocateRoom(self):
        self.isAllocated = False


# Creation of a class for Customer information
class Customer:
    def __init__(self, customerNo: int, customerName: str):
        """
        Constructor for Customer class, where we get the customer ID and the customer name
        """
        self.customerNo = customerNo
        self.customerName = customerName


# Creation of a class for Room Allocation information
class RoomAllocation:

    def __init__(self, room: Room, customer: Customer):
        """
        Constructor for RoomAllocation class, where the room and the Customer are objects of the Room and Customer classes
        """
        self.allocatedRoom = room
        self.allocatedCustomer = customer


# VARIABLES USED IN THE PROGRAM

# Array of Room objects
listOfRooms = []

# List of Room Numbers already added
listOfRoomNumbers = []

# List of Customer numbers
listOfCustomerNumbers = []

# Quantity of rooms, initialized as 0
noOfRooms = 0

# List of RoomAllocation objects
listOfRoomAllocations = []

# Path to the file where the data is stored
filePath = os.path.join(os.getcwd(), "LHMS_764707603.txt")

# Today's date and time
date = datetime.datetime.now()
day = date.strftime("%m-%d-%Y")
time = date.strftime("%H.%M.%S")

# Path to the backup file using today's date and timea
filePathBackUp = os.path.join(os.getcwd(), f"LHMS_764707603_Backup_{day}_{time}.txt")


"""
        ### FUNCTIONS ###
Functions used in the program to perform different operations
"""


def addRooms():
    """
    Function to add rooms to the hotel, recieve the number of rooms the user wants to add, and store the room number, type and price for each room.
    Uses a loop to add the rooms to the hotel while checking if the room number already exists.
    """

    # Value Error exception handling
    try:
        # Display a message to the user
        print("\n ### ADD ROOMS ### \n")

        # Ask the user for the number of rooms they want to add and store it in the noOfRooms variable
        noOfRooms = int(input("Enter the number of rooms you want to add: "))

        # Loop to add the rooms to the hotel
        for i in range(noOfRooms):

            # Variable to check if the room number already exists
            success = False
            # Loop to check if the room number already exists
            while not success:
                # Ask the user for the room number and store it in the roomNo variable
                roomNo = int(input(f"Enter the room number {i+1}: "))
                # Check if the room number already exists
                if roomNo in listOfRoomNumbers:
                    print(
                        "Room number already exists. Please enter a different room number."
                    )
                # Check if the room number is negative
                elif roomNo < 0:
                    print("Please enter a valid room number.")
                # If the room number does not exist, add the room number to the list of rooms
                else:
                    # Variable to check if the room type is valid
                    roomType = ""
                    # Loop to check if the room type is valid
                    while roomType not in ["Single", "Double", "Suite"]:
                        # Ask the user for the type of room and store it in the roomType variable
                        roomType = input(
                            f"Enter the type of room {i+1} (Single, Double, Suite): "
                        )

                    price = 0.0
                    # Loop to check if the price is valid
                    while price <= 0:
                        # Ask the user for the price of the room and store it in the price variable
                        price = float(
                            input(f"Enter the price per night of the room {i+1}: ")
                        )
                    # Set the success variable to True to exit the loop
                    success = True
                    # Add the room number to the list of room numbers
                    listOfRoomNumbers.append(roomNo)

            try:
                # Create a Room object with the room number and the status of the room as False
                room = Room(roomNo, False, roomType, price)
                # Add the Room object to the list of rooms
                listOfRooms.append(room)
            except TypeError:
                print("Please enter a valid type.")
                addRooms()

    # An exception is raised if the user enters a value that is not a number
    except ValueError:
        print("Please enter a valid number.")
        addRooms()


def deleteRooms():
    """
    Function to delete rooms from the hotel
    List the rooms available to delete and ask the user for the room number to delete
    Checks if the room number is valid and deletes the room from the list of rooms
    """
    # Check if there are rooms available to delete
    if len(listOfRooms) == 0:
        print("\nNo rooms available to delete.\n")
        return

    # Value Error exception handling
    try:
        print("\n ### DELETE ROOMS ### \n")
        print("List of Rooms already created: ")
        # Loop to display the list of rooms
        for room in listOfRooms:
            print(f"Room Number: {room.roomNumber}")

        # Variable to store the room number to delete
        roomNo = 0
        # List to store the rooms to delete
        roomsToDelete = []
        # Loop to delete the rooms from the hotel
        while roomNo != -1:
            # Ask the user for the room number to delete and store it in the roomNo variable
            roomNo = int(
                input("Enter the room number you want to delete (-1 to exit): ")
            )
            # Check if the room number is negative or if the room number is not in the list of room numbers
            if roomNo < 0 and roomNo != -1 or roomNo not in listOfRoomNumbers:
                print("Please enter a valid room number.")
            # If the room number is in the list of room numbers, add it to the list of rooms to delete
            else:
                roomsToDelete.append(roomNo)

        # Loop to delete the rooms from the list of rooms
        for room in listOfRooms:
            # Check if the room number is in the list of rooms to delete
            if room.roomNumber in roomsToDelete:
                # Remove the room from the list of rooms
                listOfRooms.remove(room)
                # Remove the room number from the list of room numbers
                listOfRoomNumbers.remove(room.roomNumber)

        print(f"\n {len(roomsToDelete)} Rooms deleted successfully.")
    except ValueError:
        print("Please enter a valid number.")
        deleteRooms()


def displayRoomDetails():
    """
    Function to display the details of the rooms, including the room number, type and price
    """
    print("\n ### ROOM DETAILS ### \n")
    print("List of Rooms: \n")

    # Loop to display the details of the rooms
    for room in listOfRooms:
        print(f"     Room Number: {room.roomNumber}")
        print(f"Room Type: {room.type}")
        print(f"Room Price: {room.price}")
        print("*" * 40)


def allocateRoom():
    """
    Function to allocate a room to a customer, updating the status of the room, and creating a new Customer
    """

    try:
        print(" ### ALLOCATE ROOM ### \n")

        # Create variable to store the quantity of allocated rooms
        quantityOfAllocatedRooms = 0
        # List to store the room numbers of the allocated rooms
        allocatedRooms = []

        print("List of not allocated Rooms: \n")
        # Loop to display the list of rooms that are not allocated
        for room in listOfRooms:
            # Check if the room is not allocated
            if not room.isAllocated:
                print(f"* Room Number: {room.roomNumber}")
                # Add the room number to the list of allocated rooms
                allocatedRooms.append(room.roomNumber)
                # Add 1 to the quantity of allocated rooms, to check if there are rooms available to allocate
                quantityOfAllocatedRooms += 1

        # Check if there are rooms available to allocate
        if quantityOfAllocatedRooms == 0:
            print("No rooms available to allocate.")
            return

        # Variable to store the room number selected by the user
        roomSelected = -1

        # Loop to check if the room number selected by the user is valid
        while roomSelected not in allocatedRooms:
            roomSelected = int(input("Enter the room number you want to allocate: "))

        # Variable to store the customer number
        customerNo = int(input("Enter the customer number: "))

        # Loop to check if the customer number is valid
        while customerNo in listOfCustomerNumbers:
            print(
                "\nCustomer number already exists. Please enter a different customer number."
            )
            customerNo = int(input("Enter the customer number: "))

        listOfCustomerNumbers.append(customerNo)

        # Variable to store the customer name
        customerName = input("Enter the customer name: ")

        # Create a Customer object with the customer number and the customer name
        customer = Customer(customerNo, customerName)

        # Loop to find the room object with the room number selected by the user
        for room in listOfRooms:
            if room.roomNumber == roomSelected:
                # Allocate the room
                room.allocateRoom()
                # Create a RoomAllocation object with the room and the customer information
                allocation = RoomAllocation(room, customer)
                # Add the RoomAllocation object to the list of room allocations
                listOfRoomAllocations.append(allocation)
                break

        print(f"\nRoom {roomSelected} allocated to {customerName} successfully.")

    except ValueError:
        print("Please enter a valid number.")
        allocateRoom()


def displayRoomAllocationsDetails():
    """
    Function to display the details of the room allocations, including the room number, customer number and customer name
    """
    print("\n ### ROOM ALLOCATIONS ### \n")
    print("List of Rooms: \n")

    # Loop to display the details of the rooms
    for room in listOfRooms:
        print(f"     Room Number: {room.roomNumber}")
        # Check if the room is allocated
        if room.isAllocated:
            print(f"The room is allocated.\n")
            # Loop to display the details of the room allocations
            for allocation in listOfRoomAllocations:
                # Check if the room number is the same as the room number of the room allocation
                if allocation.allocatedRoom.roomNumber == room.roomNumber:
                    # Display the customer number and the customer name
                    print(f"Customer Number: {allocation.allocatedCustomer.customerNo}")
                    print(f"Customer Name: {allocation.allocatedCustomer.customerName}")
        else:
            print("The room is not allocated\n")
        print("*" * 40)


def billing():
    """
    Function to calculate the billing for the customer and deallocate the room
    """
    try:
        print(" ### BILLING & DEALLOCATION ### \n")

        # Check if there are rooms available to deallocate
        print("List of Rooms already allocated: \n")
        # Variable to store the quantity of allocated rooms
        quantityOfAllocatedRooms = 0
        # List to store the room numbers of the allocated rooms
        allocatedRooms = []
        # Loop to display the list of rooms that are allocated
        for room in listOfRooms:
            # Check if the room is allocated
            if room.isAllocated:
                print(f"* Room Number: {room.roomNumber}")
                # Add 1 to the quantity of allocated rooms, to check if there are rooms available to deallocate
                quantityOfAllocatedRooms += 1
                allocatedRooms.append(room.roomNumber)

        # Check if there are rooms available to deallocate
        if quantityOfAllocatedRooms == 0:
            print("No rooms available to deallocate.\n")
            return

        # Variable to store the customer number
        roomNo = int(input("Enter the room number: "))
        # Loop to check if the room number selected by the user is valid
        while roomNo not in allocatedRooms:
            print("Please enter a valid room number.")
            roomNo = int(input("Enter the room number: "))

        # Loop to find the room object with the room number selected by the user
        for room in listOfRooms:
            if room.roomNumber == roomNo:
                # Loop to find the RoomAllocation object with the room number selected by the user
                for allocation in listOfRoomAllocations:
                    if allocation.allocatedRoom.roomNumber == roomNo:

                        nights = int(input("Enter the number of nights: "))

                        # Calculate the billing for the customer
                        print(f"\nThe billing per night is: {room.price}")
                        print(f"The total billing is: {room.price * nights}")
                        # Deallocate the room
                        room.deallocateRoom()
                        # Remove the RoomAllocation object from the list of room allocations
                        listOfRoomAllocations.remove(allocation)

                        print(f"\nRoom {roomNo} deallocated successfully.")
                        break
                break

    except ValueError:
        print("Please enter a valid number.")
        billing()


def saveRoomAllocationsToFile():
    try:
        print(" ### SAVE ROOM ALLOCATIONS TO FILE ### \n")

        # Open the file in write mode and create it if it does not exist
        file = open(filePath, "w+")

        # Get the current date and time
        now = datetime.datetime.now()

        # Write the header of the file
        file.write(f"\t #### LANGHAM HOTEL MANAGEMENT SYSTEM ####\n")

        # Loop to write the details of the room allocations to the file
        for roomAllocation in listOfRoomAllocations:
            # Write the room number, customer number, customer name and the date to the file
            file.write(f"\nRoom Number: {roomAllocation.allocatedRoom.roomNumber}\n")
            file.write(
                f"Customer Number: {roomAllocation.allocatedCustomer.customerNo}\n"
            )
            file.write(
                f"Customer Name: {roomAllocation.allocatedCustomer.customerName}\n"
            )
            file.write(f"Date: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("*" * 40)

        # Close the file
        file.close()

        print("Room allocations saved as 'LHMS_1094' successfully.")

    # IOError exception handling
    except IOError:
        print("An error occurred while saving the file.")
        return
    # EOFError exception handling
    except EOFError:
        print("End of file.")
        return


def showRoomAllocationsFromFile():
    try:
        print(" ### SHOW ROOM ALLOCATIONS ### \n")

        # Open the file in read mode
        file = open(filePath, "r")

        # Read the content of the file
        content = file.read()

        # Print the content of the file
        print(content)
    except FileNotFoundError:
        print("File not found. Try saving the room allocations first.")
        return


def backupRoomAllocations():
    try:
        print(" ### BACKUP ### \n")

        # Open the file in read mode
        file = open(filePath, "r")
        # Read the content of the file
        content = file.read()
        # Close the file
        file.close()

        # Open the file in write mode to eliminate the content
        file = open(filePath, "w")
        # Write the header of the file
        file.write(f"\t #### LANGHAM HOTEL MANAGEMENT SYSTEM ####\n")
        file.close()

        # Open backup file in write mode
        fileBackup = open(filePathBackUp, "w+")  # Create the file if it does not exist
        # Write the content of the file to the backup file
        fileBackup.write(content)
        # Close the backup file
        fileBackup.close()

        print(f"Content of 'LHMS_1094' eliminated succesfully.")
        print(f"Backup created successfully as 'LHMS_1094_Backup_{day}_{time}'.")

    except FileNotFoundError:
        print("File not found. Try saving the room allocations first.")
        return


# #### MAIN PROGRAM ####
def main():
    """
    Main function of the program
    """

    # Name Error exception handling
    try:

        # Initialize the choice variable to -1, to enter the loop
        choice = -1

        # Loop to display the menu until the user chooses to exit
        while choice != 0:

            # Menu
            # Two blank lines are printed to separate the menu from the previous output
            print("\n")
            print("\n")
            print("*" * 70)
            print("                 LANGHAM HOTEL MANAGEMENT SYSTEM             ")
            print("                              MENU                        ")
            print("*" * 70)

            print("0. Exit")
            print("1. Add Rooms")
            print("2. Delete Rooms")
            print("3. Display Rooms Details")
            print("4. Allocate Rooms")
            print("5. Display Room Allocation Details")
            print("6. Billing & De-Allocation")
            print("7. Save the Room Allocations in the database")
            print("8. Load the Room Allocations from the database")
            print("9. Backup of Room Allocations")
            print("*" * 70)

            # Update choice variable with the user's choice
            choice = int(input("Enter your choice number here (0-9): "))

            # Check the user's choice and call the corresponding function
            if choice == 1:
                # Call the function to add rooms
                addRooms()
            elif choice == 2:
                # Call the function to display rooms
                deleteRooms()
            elif choice == 3:
                # Call the function to allocate rooms
                displayRoomDetails()
            elif choice == 4:
                # Call the function to deallocate rooms
                allocateRoom()
            elif choice == 5:
                # Call the function to display room allocation details
                displayRoomAllocationsDetails()
            elif choice == 6:
                # Call the function to calculate the billing
                billing()
            elif choice == 7:
                # Call the function to save the room allocations to a file
                saveRoomAllocationsToFile()
            elif choice == 8:
                # Call the function to show the room allocations from a file
                showRoomAllocationsFromFile()
            elif choice == 9:
                # Call the function to backup the room allocations
                backupRoomAllocations()
            elif choice == 0:
                # Exit the program
                print("Exiting the program...")
            else:
                # If the choice is not valid, display a message
                print("\nInvalid choice, please enter a number between 0 and 9\n")
                # If the choice is not valid, display the menu again
                main()

    # An exception is raised if the user enters a value that is not a number
    except ValueError:
        # Display a message to the user
        print("Please enter a valid number.")
        return


main()
