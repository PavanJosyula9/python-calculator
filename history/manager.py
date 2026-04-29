from history.storage import save_history, load_history

history: list[str] = load_history()

def add_entry(entry: str) -> None:
    history.append(entry)
    save_history(history)

def show_history() -> None:
    if not history:
        print('No history yet.')
        return
    
    print('\nCalculation History:')
    for i, entry in enumerate(history, start=1):
        print(f"{i}. {entry}")

def clear_history() -> None:
    history.clear()
    save_history(history)
    print('History cleared')