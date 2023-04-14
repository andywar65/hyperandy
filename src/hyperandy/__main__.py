"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Hyperandy."""


if __name__ == "__main__":
    main(prog_name="hyperandy")  # pragma: no cover
