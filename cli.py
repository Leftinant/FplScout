from utils import (
    load_fpl_data,
    preprocess_player_data,
    top_players,
    find_differentials,
    compare_players
)
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

console = Console()

def print_table(df, title=""):
    table = Table(title=title)
    for col in df.columns:
        table.add_column(col, justify="left")
    for _, row in df.iterrows():
        table.add_row(*map(str, row.values))
    console.print(table)

def run_cli():
    console.rule("[bold blue]FPL Scout Assistant [/bold blue]")

    # Load and preprocess data
    console.print("[green]Fetching data from FPL API...[/green]")
    elements, teams, positions = load_fpl_data()
    players = preprocess_player_data(elements, teams, positions)

    while True:
        console.print("\n[bold]Main Menu[/bold]")
        console.print("1. Show top players")
        console.print("2. Discover differentials")
        console.print("3. Compare players")
        console.print("4. Exit")

        choice = Prompt.ask("Select an option", choices=["1", "2", "3", "4"], default="1")

        if choice == "1":
            by = Prompt.ask("Sort by", choices=["total_points", "form", "value"], default="total_points")
            position = Prompt.ask("Filter by position (or leave blank)", default="")
            num = int(Prompt.ask("How many players to show?", default="10"))
            result = top_players(players, by=by, top_n=num, position=position or None)
            print_table(result, f"Top {num} players by {by}")

        elif choice == "2":
            max_ownership = float(Prompt.ask("Max ownership %", default="10"))
            min_form = float(Prompt.ask("Minimum form", default="5"))
            diffs = find_differentials(players, max_ownership, min_form)
            print_table(diffs, "Differentials")

        elif choice == "3":
            names = Prompt.ask("Enter player names (comma-separated)").split(",")
            names = [n.strip() for n in names]
            comparison = compare_players(players, names)
            print_table(comparison, "Player Comparison")

        elif choice == "4":
            console.print("[yellow]Goodbye![/yellow]")
            break
