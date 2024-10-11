"""
This is the file that contains the relations between the different nodes in the graph.
The graph is a directed graph, and the relations are stored in the form of a dictionary.
The dictionary is of the form:
{
    "node1": ["node2", "node3", ...],
    "node2": ["node4", "node5", ...],
    ...
}
This means that node1 is connected to node2 and node3, and node2 is connected to node4 and node5, and so on.

Essentially, this was used for locking the users in their own path and not deviate from it
or go on scanning the QR codes of the other paths.
"""

main_relation = {
    "root": ["D0", "E0", "P0"],
    "D0": ["D1"],
    "D1": ["D2"],
    "D2": ["COMMON"],
    "COMMON": ["D3", "E3", "P3"],
    "D3": ["D4PRESENT", "D4PAST"],
    "D4PRESENT": ["D5PRESENT"],
    "D4PAST": ["D5PAST"],
    "D5PRESENT": ["D6PRESENT"],
    "D5PAST": ["D6PAST"],
    "D6PRESENT": ["D7A", "D7B"],
    "D6PAST": ["D7A", "D7B"],
    "D7A": ["D8A"],
    "D7B": ["D8B"],
    "D8A": ["D8A"],
    "D8B": ["D8B"],
    
    
    "E0": ["E1"],
    "E1": ["E2"],
    "E2": ["COMMON"],
    "E3": ["E4PRESENT", "E4PAST"],
    "E4PRESENT": ["E5PRESENT"],
    "E4PAST": ["E5PAST"],
    "E5PRESENT": ["E6PRESENT"],
    "E5PAST": ["E6PAST"],
    "E6PRESENT": ["E7A", "E7B"],
    "E6PAST": ["E7A", "E7B"],
    "E7A": ["E8A"],
    "E7B": ["E8B"],
    "E8A": ["E8A"],
    "E8B": ["E8B"],
    
    "P0": ["P1"],
    "P1": ["P2"],
    "P2": ["COMMON"],
    "P3": ["P4PRESENT", "P4PAST"],
    "P4PRESENT": ["P5PRESENT"],
    "P4PAST": ["P5PAST"],
    "P5PRESENT": ["P6PRESENT"],
    "P5PAST": ["P6PAST"],
    "P6PRESENT": ["P7A", "P7B"],
    "P6PAST": ["P7A", "P7B"],
    "P7A": ["P8A"],
    "P7B": ["P8B"],
    "P8A": ["P8A"],
    "P8B": ["P8B"],
}

all_possible = [
    "root",
    "end",
    "COMMON",
    "D0",
    "D1",
    "D2",
    "D3",
    "D4PRESENT",
    "D4PAST",
    "D5PRESENT",
    "D5PAST",
    "D6PRESENT",
    "D6PAST",
    "D7A",
    "D7B",
    "D8A",
    "D8B",
    
    "E0",
    "E1",
    "E2",
    "E3",
    "E4PRESENT",
    "E4PAST",
    "E5PRESENT",
    "E5PAST",
    "E6PRESENT",
    "E6PAST",
    "E7A",
    "E7B",
    "E8A",
    "E8B",
    
    "P0",
    "P1",
    "P2",
    "P3",
    "P4PRESENT",
    "P4PAST",
    "P5PRESENT",
    "P5PAST",
    "P6PRESENT",
    "P6PAST",
    "P7A",
    "P7B",
    "P8A",
    "P8B"
]

redirecturl = {
    "COMMON":"https://drive.google.com/file/d/1P66ELBqEsOg0hPRCvIF3eU-nasN1Pn09/view?usp=drive_link",

    "D0": "https://drive.google.com/file/d/1QvWsCsK8xl40nxJxbtlELxVE6R9149hK/view?usp=drive_link",
    "D1": "https://drive.google.com/file/d/1HfDr0nvFoKSI3ZkICo7jWQl2XbXK-X1_/view?usp=drive_link",
    "D2": "https://drive.google.com/file/d/1AO0MO_WuqnzaMVmkf5DFwYxbSKnMLIKh/view?usp=drive_link",
    "D3": "https://drive.google.com/file/d/1qVjRE6szQjjSYdJnjxxfgDBoyRGxbgAX/view?usp=drive_link",
    "D4PRESENT": "https://drive.google.com/file/d/1FC3TEko166l6wcNl9Q6kF2KjC05MajMo/view?usp=drive_link",
    "D4PAST": "https://drive.google.com/file/d/1616gigJtE8UJ3GlV6uvSidTYrZwWlo9w/view?usp=drive_link",
    "D5PAST": "https://drive.google.com/file/d/11nruGg7DWxmxx0ZoF6L-gVjytQTHgBTr/view?usp=drive_link",
    "D5PRESENT": "https://drive.google.com/file/d/16ss480BOGPA2IbutgBnfdtn_wJfD2uy6/view?usp=drive_link",
    "D6PAST": "https://drive.google.com/file/d/10-viq8HxAh8OLEK7X7cCaElauuOKBWer/view?usp=drive_link",
    "D6PRESENT": "https://drive.google.com/file/d/1tewjsO9arffO9kgqP9JaUz-4iPI1Tdbv/view?usp=drive_link",
    "D7A": "https://drive.google.com/file/d/1FxmuM-3ysF5foxNyCSddR-kCo9VR-NRp/view?usp=drive_link",
    "D7B": "https://drive.google.com/file/d/1JWafLYUxwBJCQBhWOE3B8sE2O7vpzTFB/view?usp=drive_link",
    "D8A": "https://drive.google.com/file/d/1jIyBHMX8k715tYkXC__q5n6o1BZK1y1P/view?usp=drive_link",
    "D8B": "https://drive.google.com/file/d/1np4iIrRIX4zXpBzSYNJSBExbbpdo84-w/view?usp=drive_link",

    "E0": "https://drive.google.com/file/d/1eosqEd41mNCDtbmQXgvDGqp_Py_LZWwE/view?usp=drive_link",
    "E1": "https://drive.google.com/file/d/1kim4J8iHglKb00IcXuj_bV7JQ_L_fml3/view?usp=drive_link",
    "E2": "https://drive.google.com/file/d/15K-Pl2E35iX04zC3wr_O3VQM89GaJgv2/view?usp=drive_link",
    "E3": "https://drive.google.com/file/d/1Lse9hCylS6EpcLa8G0fs85kmjnvWVeSC/view?usp=drive_link",
    "E4PAST": "https://drive.google.com/file/d/1auQVe77BaO1IJyZPWi3SUH2AR_J1RYKS/view?usp=drive_link",
    "E4PRESENT": "https://drive.google.com/file/d/1oMrogJMoSvfRnE-h-d0yTuQtqQpp7_hU/view?usp=drive_link",
    "E5PAST": "https://drive.google.com/file/d/1BUEQEdEkHug49zXnhkK6ZK4J27yfy1T9/view?usp=drive_link",
    "E5PRESENT": "https://drive.google.com/file/d/1KxmCQ8TazbWUoaxRkweuCzhH7wnfOqb3/view?usp=drive_link",
    "E6PAST": "https://drive.google.com/file/d/12MWHetxdzgEZLU3-JOj5I49F8OhtiIWA/view?usp=drive_link",
    "E6PRESENT": "https://drive.google.com/file/d/1rNSo36i2pKMD7n4Wabi2GBwFfwhTtE-Z/view?usp=drive_link",
    "E7A": "https://drive.google.com/file/d/1F9dWnENkNIj4XNdXt-GAqjDSI1x9ppSW/view?usp=drive_link",
    "E7B": "https://drive.google.com/file/d/10gy0zCdoUhDY5pm_FAz5MOWfVRHKLVkk/view?usp=drive_link",
    "E8A": "https://drive.google.com/file/d/1uLMqg-x1FhPc8R5V5m2e54hQ2W7qR7uQ/view?usp=drive_link",
    "E8B": "https://drive.google.com/file/d/15zk8pXAyFUczr1TjFgLiG0e65EaovakM/view?usp=drive_link",
    
    "P0": "https://drive.google.com/file/d/15wiuCFnvDZGTNE3U1M2QT2cGgo_tpK17/view?usp=drive_link",
    "P1": "https://drive.google.com/file/d/1NLV4WXPahH7nw0-vUqCFk6OhzTJvYGoD/view?usp=drive_link",
    "P2": "https://drive.google.com/file/d/1fS4NE1FtFnC0Sbu3QSUXuDzKC8zGYpA_/view?usp=drive_link",
    "P3": "https://drive.google.com/file/d/1VMPs5p9pN6WkPHwRDvdYDII_KintNIsP/view?usp=drive_link",
    "P4PAST": "https://drive.google.com/file/d/11Eqd7hI1DzkQijagIEEulONGLXbzQN_Y/view?usp=drive_link",
    "P4PRESENT": "https://drive.google.com/file/d/12u8cZIt_kOhayOVDnhv8STT6Goz5UtXC/view?usp=drive_link",
    "P5PAST": "https://drive.google.com/file/d/1m9XCXvzZc3HbXseJaVCrCd9qiFJ88Jeq/view?usp=drive_link",
    "P5PRESENT": "https://drive.google.com/file/d/1kE4HjLXQNaUKw_LMyhKzqRZJyrkuJOhI/view?usp=drive_link",
    "P6PAST": "https://drive.google.com/file/d/1iIqBvSwqGrpOoiM2ZCLnuurDJmUFjyeD/view?usp=drive_link",
    "P6PRESENT": "https://drive.google.com/file/d/1taj_UQNtl2ye6sFg_CwiY_WUsF6sBabI/view?usp=drive_link",
    "P7A": "https://drive.google.com/file/d/1TOpL3Z40iiDKhUpOdy4f8Hq7z5QxUjMr/view?usp=drive_link",
    "P7B": "https://drive.google.com/file/d/14Uv5oWnzN_NfCEVoiyLsoqT6f-FnxI7S/view?usp=drive_link",
    "P8A": "https://drive.google.com/file/d/1KnldhYopu55lpYGxFCUNlfiI0UpEur22/view?usp=drive_link",
    "P8B": "https://drive.google.com/file/d/1XXnqYGs-kPfe-ezR4BOvd0ih9t67nzmx/view?usp=drive_link"
}