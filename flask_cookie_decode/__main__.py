import json
import click
from itsdangerous import URLSafeSerializer


@click.group()
def main():
    pass


@click.command()
@click.argument("cookie")
def decode(cookie):
    s = URLSafeSerializer("foo")
    click.echo(
        json.dumps(s.load_payload(cookie.encode("utf-8")), indent=2, sort_keys=True)
    )


main.add_command(decode)


if __name__ == "__main__":
    main()
