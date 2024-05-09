import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(
            gapminder[gapminder.continent == "Africa"],
            x="year",
            y="pop",
            color="gdpPercap",
        )
        .add(so.Line())
        .label(
            title="Expectativa",
            x="Año",
            y="Expectativa de vida",
            color="País",
        )
    )
    return dict(
        descripcion="El crecimiento de la poblacion de Africa a travéz de los años y donde también se puede observar el PBI",
        autor="Caterina Nagela",
        figura=figura,
    )
