import click
from rich.console import Console
from rich.panel import Panel
from .configs.config import get_api_key, save_api_key, delete_api_key, delete_all_config
from .core import get_word_definition, is_valid_word

console = Console()

@click.group()
def cli():
    pass

@cli.command()
@click.argument("words", nargs=-1, required=True)
def define(words):
    api_key = get_api_key()
    if not api_key:
        console.print(
            Panel.fit(
                "[bold red]API key not found![/]\n"
                "Please set your Gemini API key using the 'config' command:"
                "\n\n[bold]sollu config --key YOUR_API_KEY[/]"
            )
        )
        return

    for word in words:
        if not is_valid_word(word):
            console.print(
                Panel.fit(
                    f"[bold red]Error:[/] Invalid input\n"
                    f"Details: '{word}' is not a valid word.",
                    title=f"Error for '{word}'",
                    border_style="red"
                )
            )
            continue
        result = get_word_definition(word)
        if "error" in result:
            console.print(
                Panel.fit(
                    f"[bold red]Error:[/] {result['error']}\n"
                    f"Details: {result.get('details', 'No details provided')}",
                    title=f"Error for '{word}'",
                    border_style="red"
                )
            )
            continue

        definitions_text = "\n\n".join(
            f"[bold]Meaning {i+1}:[/] {item['definition']}\n[bold]Example:[/] {item['example']}"
            for i, item in enumerate(result.get("definitions", []))
        )

        console.print(
            Panel.fit(
                f"[bold underline]{result['word']}[/]\n\n{definitions_text}",
                title="Definitions",
                border_style="green"
            )
        )


@cli.group()
def config():
    pass

@config.command()
@click.option("--key", prompt="Enter your Gemini API key", help="Your Gemini API key")
def set(key):
    save_api_key(key)
    console.print("[bold green]API key configured successfully![/]")

@config.command()
def delete():
    if delete_api_key():
        console.print("[bold green]API key deleted successfully![/]")
    else:
        console.print("[bold yellow]No API key found to delete.[/]")

@config.command()
def reset():
    if delete_all_config():
        console.print("[bold green]All configuration deleted successfully![/]")
    else:
        console.print("[bold yellow]No configuration found to delete.[/]")
