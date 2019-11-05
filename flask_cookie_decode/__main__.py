import click


@click.group()
def main():
    pass


@click.command()
def decode():
    click.echo("decoding")


main.add_command(decode)


if __name__ == "__main__":
    main()
