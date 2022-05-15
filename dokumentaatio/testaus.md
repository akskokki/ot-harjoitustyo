# Testausdokumentti

Ohjelmaa on testattu unittesteillä ja StubEventeillä.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Sovelluslogiikasta vastaavaa Level-luokkaa testataan luokalla [TestLevel](https://github.com/akskokki/ot-harjoitustyo/blob/master/src/tests/level_test.py). Testeissä suoritetaan erilaisia sovellustoimintoja, ja varmistetaan että ne tekevät oikeita asioita.

### Kentän luominen

Kenttää alustavan kartan luomisesta vastaavaa LevelGenerator-luokkaa testataan luokalla [TestLevelGenerator](https://github.com/akskokki/ot-harjoitustyo/blob/master/src/tests/level_generator_test.py). Testeissä luodaan uusi kenttä, ja varmistetaan että jokaisen solun arvo on sellainen kuin pitääkin.

### Pelisilmukka

Pelisilmukasta vastaavaa GameLoop-luokkaa testataan luokalla [TestGameLoop](https://github.com/akskokki/ot-harjoitustyo/blob/master/src/tests/game_loop_test.py). Testeissä silmukalle syötetään StubEvent-tapahtumia, ja tarkistetaan reagoiko silmukka niihin odotetulla tavalla.

### Testikattavuus

Käyttöliittymäluokat on jätetty testikattavuuden ulkopuolelle. Ilman niitä, testauksen haarautumakattavuus on 89%.

![](https://github.com/akskokki/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/coverage.png)

Testaamatta jäivät *utilities*-hakemiston alta löytyvät luokat, joiden päätarkoitus olikin se, että ne voidaan testeissä korvata helposti Stub-luokilla. Ehkä nekin olisi ollut järkevää jättää testikattavuuden ulkopuolelle, mutta kaikenkattavasti nämä testitulokset ovat varsin tyydyttäviä.

## Järjestelmätestaus

### Asennus

Sovellus on testattu toimivaksi sekä Linux- että Windows-ympäristöissä. Windowsilla tosin invoke-komennot eivät toimi, joten komennot pitää kirjoittaa kokonaisuudessaan.

### Toiminnallisuudet

Kaikki [määrittelydokumentin](https://github.com/akskokki/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md) listaamat toiminnallisuudet on käyty läpi ja niiden toimivuus testattu myös manuaalisesti.
