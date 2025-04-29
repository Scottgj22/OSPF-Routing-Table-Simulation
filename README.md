# OSPF-Routing-Table-Simulation

This project simulates the behaviour of an OSPF (Open Shortest Path First) network, including:
- Router initialisation
- Neighbour relationship setup
- Link-State Advertisement (LSA) generation and flooding
- Shortest Path First (SPF) calculations (Dijkstra's algorithm)
- Full visualisation of the network topology

The simulation focuses on building routing tables based on OSPF principles, without routing actual packets.

Requirements
- Python 3.10 or newer (recommended)
- Visual Studio Code (optional, but helpful)
- Required Python packages:
---networkx
---matplotlib

Installation steps
1. Clone or download the project files into a folder on your computer
2. Open a terminal inside the project folder
3. Create a virtual environment (optional, but helpful)
---python -m venv .venv
4. Activate the virtual environment
---On Windows:

---On macOS/Linux:

5. Install the required Python packages:
---pip install -r requirements.txt

if there is no requirements.txt, you can install manually:
pip install networkx matplotlib

How to run the simulation
1. Open the project folder in Visual Studio Code (or your preferred editor)
2. Ensure the Python interpreter is set correctly to your environment
3. In the terminal, navigate to the src/ directory if needed
4. Run the simulation:
---python main.py
5. You will see:
- Terminal output showing each step of the OSPF simulation
- Routing tables for each router
- A graphical visualisation of the network topology (opens automatically)

Notes
- Every time you run the simulation, link costs are randomised unless you fix the random seed inside the code
- The simulation focuses on core OSPF concepts only - real-world OSPF features like areas, hello timers, and full packet forwarding are not implemented.
- If you want to change the network layout or structure, you can adjust the coordinates of the nodes in the pos array.
