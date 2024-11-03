import click


@click.group()
@click.option('--config_file',
              default="README.md",
              type=click.File(mode='r'),
              help='help')
@click.pass_context
def cli(ctx, config_file):
    import json
    config = json.load(config_file)
    ctx.obj['config'] = config


@cli.command()
@click.pass_context
def hello(ctx) -> None:
    print("Hello, world!")


@cli.command()
@click.pass_context
def world(ctx) -> None:
    print("Foobar!")


def main():
    cli(obj={})


if __name__ == '__main__':
    main()
