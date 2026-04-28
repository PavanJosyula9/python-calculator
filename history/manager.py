history: list[str] = []

def add_entry(entry: str) -> None:
    history.append(entry)

def show_history() -> None:
    if not history:
        print('No history yet.')
        return
    
    print('\nCalculation History:')
    for i, entry in enumerate(history, start=1):
        print(f"{i}. {entry}")