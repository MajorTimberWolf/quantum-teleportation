import quantum_communication.quantum_data_teleporter as qc

def main():
    """
    Demonstrates the usage of the QuantumDataTeleporter class.

    Args:
        None
    """

    # Example usage with a file
    print("\n*** Example usage with a file ***")
    file_path = "data/text.txt"  # Path to the text file
    quantum_comm = qc.QuantumDataTeleporter(file_path=file_path, shots=1)  # Create a QuantumDataTeleporter object
    received_data, is_data_match = quantum_comm.run_simulation()  # Run the simulation

    print(f"Received Data: {received_data}")
    print(f"Sent Data == Received Data: {is_data_match}")  # Check if the sent and received data match

    # Example usage with a string
    print("\n*** Example usage with a string ***")
    text = "Hello, World!"  # Text to send
    quantum_comm = qc.QuantumDataTeleporter(text_to_send=text, shots=1)  # Create a QuantumDataTeleporter object
    received_data, is_data_match = quantum_comm.run_simulation()  # Run the simulation

    print(f"Received Data: {received_data}")
    print(f"Sent Data == Received Data: {is_data_match}")  # Check if the sent and received data match

if __name__ == "__main__":
    main()  # Run the main function if this script is executed directly
