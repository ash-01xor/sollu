import click
from rich.console import Console
from rich.panel import Panel
from rich.text import Text 
from itertools import groupby 
from operator import itemgetter 
from .configs.config import get_api_key, save_api_key, delete_api_key, delete_all_config
from .core import get_word_definition

console = Console()

@click.group()
def cli():
    """Sollu - A command-line dictionary tool."""
    pass

@cli.command()
@click.argument("words", nargs=-1, required=True)
def define(words):
    """Look up definitions for one or more words."""
    api_key = get_api_key()
    if not api_key:
        console.print(
            Panel.fit(
                "[bold red]API key not found![/]\n"
                "Please set your Gemini API key using the 'config' command:"
                "\n\n[bold]sollu config set --key YOUR_API_KEY[/]" 
            )
        )
        return

    for word in words:
        result = get_word_definition(word)
        if "error" in result:
            console.print(
                Panel.fit(
                    f"[bold red]API Error:[/] {result['error']}\n" 
                    f"Details: {result.get('details', 'No details provided')}",
                    title=f"Processing Error for '{word}'",
                    border_style="red"
                )
            )
            continue

        if result.get("found") is False:
            word_returned = result.get("word", word)
            console.print(
                Panel.fit(
                    f"[bold yellow]Word not found:[/] The word '{word_returned}' could not be found in the dictionary.",
                    title=f"Not Found: '{word}'",
                    border_style="yellow"
                )
            )
            continue

        definitions = result.get("definitions", [])
        if result.get("found") is not True or not isinstance(definitions, list):
            console.print(
                Panel.fit(
                    f"[bold red]Unexpected API Response Format:[/]\n"
                    f"Details: Received unexpected data for '{word}' even though 'found' might be true. Response: {result}",
                    title=f"Format Error for '{word}'",
                    border_style="red"
                )
            )
            continue

        if not definitions:
            console.print(
                Panel.fit(
                    f"[bold yellow]No definitions found for:[/] '{word}'",
                    title=f"No Definitions: '{word}'",
                    border_style="yellow"
                )
            )
            continue

        definitions.sort(key=itemgetter('part_of_speech'))
        grouped_defs = {pos: list(defs) for pos, defs in groupby(definitions, key=itemgetter('part_of_speech'))}

        content = Text()
        word_returned = result.get("word", word)
        content.append(f"{word_returned}\n\n", style="bold underline")

        for pos, defs in grouped_defs.items():
            content.append(f"[{pos.upper()}]\n", style="bold blue")

            for i, item in enumerate(defs, 1):
                meaning = item.get('meaning', 'N/A')
                example = item.get('example', 'N/A')

                content.append(f"{i}. ", style="bold")
                content.append(f"{meaning}\n", style="")
                content.append(f"   Example: ", style="italic")
                content.append(f"{example}\n\n", style="italic dim")

        console.print(
            Panel.fit(
                content,
                title=f"Definitions for '{word_returned}'",
                border_style="green"
            )
        )

@cli.group()
def config():
    """Manage configuration settings."""
    pass

@config.command()
@click.option("--key", prompt="Enter your Gemini API key", help="Your Gemini API key")
def set(key):
    """Set your Gemini API key."""
    save_api_key(key)
    console.print("[bold green]API key configured successfully![/]")

@config.command()
def delete():
    """Delete your stored Gemini API key."""
    if delete_api_key():
        console.print("[bold green]API key deleted successfully![/]")
    else:
        console.print("[bold yellow]No API key found to delete.[/]")

@config.command()
def reset():
    """Delete all configuration data."""
    if delete_all_config():
        console.print("[bold green]All configuration deleted successfully![/]")
    else:
        console.print("[bold yellow]No configuration found to delete.[/]")
