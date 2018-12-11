from flask.cli import FlaskGroup

from zamboni import api, db


cli = FlaskGroup(api)


@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()
