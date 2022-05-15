# Miinaharava

Klassikko miinaharava-peli. Jos peli ei ole ennestään tuttu, voi säännöt opetella vaikkapa täältä: [How to play Minesweeper](https://minesweepergame.com/strategy/how-to-play-minesweeper.php).

## Dokumentaatio

* [Käyttöohje](https://github.com/akskokki/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
* [Releases](https://github.com/akskokki/ot-harjoitustyo/releases)
* [Vaatimusmäärittely](https://github.com/akskokki/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
* [Tuntikirjanpito](https://github.com/akskokki/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
* [Changelog](https://github.com/akskokki/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
* [Arkkitehtuuri](https://github.com/akskokki/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
* [Testaus](https://github.com/akskokki/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```
poetry install
```

2. Käynnistä sovellus komennolla:

```
poetry run invoke start
```

## Testaaminen

Testit voi suorittaa komennolla:
```
poetry run invoke test
```

Testikattavuusraportin saa komennolla:
```
poetry run invoke coverage-report
```

Pylint-testit voi suorittaa komennolla:
```
poetry run invoke lint
```
