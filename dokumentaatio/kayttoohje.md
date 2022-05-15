# Käyttöohje

Lataa projektin viimeisin releasen lähdekoodi [täältä](https://github.com/akskokki/ot-harjoitustyo/releases).

## Ohjelman käynnistäminen

Asenna ohjelman riippuvuudet komennolla:

```
poetry install
```

Nyt ohjelman voi käynnistää komennolla:

```
poetry run invoke start
```

## Ohjelman testaaminen

Testit voi suorittaa komennolla
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

## Vaikeustason valinta

Ohjelma käynnistyy vaikeustasonvalintaruutuun, josta voi valita joko helpon, keskitasoisen tai vaikean pelin. Mahdollisuutena on myös custom-peli, jolloin ruudukon voi luoda halutun kokoiseksi.

## Pelaaminen

Peli toimii tavallisilla [miinaharava-säännöillä](https://minesweepergame.com/strategy/how-to-play-minesweeper.php). Hiiren vasemmalla näppäimellä voi avata ruudun, ja sen oikealla näppäimellä sijoittaa ruutuun miinan sijaintia osoittavan lipun.

Peli loppuu, kun pelaaja joko räjäyttää miinan sitä napsauttamalla, tai saa avattua kaikki miinattomat ruudut.

## Pelin loppuruutu

Pelin loppuruudulta pelaaja näkee motivaationaalisen viestin sekä voiton yhteydessä peliin käytetyn ajan. 

Loppuruudulta voi joko pelata uuden pelin samalla vaikeustasolla, tai valita täysin uuden vaikeustason.
