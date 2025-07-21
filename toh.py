# Tower of Hanoi

# Function to move disks
def tower(disk, source, auxi, dest):
    if disk == 1:
        print(f"Move disk 1 from {source} to {dest}")
        return
    # Move n-1 disks from source to auxiliary
    tower(disk - 1, source, dest, auxi)
    # Move nth disk from source to destination
    print(f"Move disk {disk} from {source} to {dest}")
    # Move n-1 disks from auxiliary to destination
    tower(disk - 1, auxi, source, dest)

# Input from user
disk = int(input("Enter the number of disks: "))

# Call the function with A as source, B as auxiliary, and C as destination
tower(disk, 'A', 'B', 'C')
