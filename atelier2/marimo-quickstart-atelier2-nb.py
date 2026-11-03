import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import os

    import marimo as mo
    import sqlalchemy as sa
    from dotenv import load_dotenv
    from datetime import date

    return load_dotenv, mo, os, sa


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Connexion à la base OMOP
    """)
    return


@app.cell
def _(load_dotenv, mo, os, sa):
    # Paramètres de connexion lus dans le .env du dépôt Environnement-Hackathon-EDS
    load_dotenv(mo.notebook_dir() / "../../../Environnement-Hackathon-EDS/.env")

    engine = sa.create_engine(
        sa.URL.create(
            "postgresql+psycopg",
            host=os.environ["TARGET_PGHOST"],
            port=int(os.environ["TARGET_PGPORT"]),
            database=os.environ["TARGET_PGDATABASE"],
            username=os.environ["TARGET_PGUSER"],
            password=os.environ["TARGET_PGPASSWORD"],
        ),
        # Sessions en lecture seule : toute écriture est refusée par PostgreSQL
        connect_args={"options": "-c default_transaction_read_only=on"},
    )
    return (engine,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Test de la connexion
    """)
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT current_database() AS base,
               current_user AS utilisateur,
               version() AS version
        """,
        engine=engine
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Schémas
    """)
    return


@app.cell
def _(engine, mo):
    schemas = mo.sql(
        f"""
        SELECT schema_name, schema_owner
        FROM information_schema.schemata
        WHERE left(schema_name, 3) <> 'pg_'
          AND schema_name <> 'information_schema'
        ORDER BY schema_name
        """,
        engine=engine
    )
    return


if __name__ == "__main__":
    app.run()
