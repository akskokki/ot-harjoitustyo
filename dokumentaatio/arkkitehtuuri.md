# Arkkitehtuurikuvaus

## Käyttöliittymä

Sovelluksella on yksinkertainen käyttöliittymä, joka sisältää tällä hetkellä kaksi näkymää:

- Vaikeustasonvalinta
- Pelinäkymä

Pelin avautuessa käyttäjä näkee vaikeustasonvalintanäkymän, josta vaikeustason valinnan jälkeen siirrytään suoraan pelinäkymään.

## Sovelluslogiikka

Peli toimii pääosin käyttäen Level- ja Tile-luokkia. Level-luokalle annetaan käytettävä pelikenttä listamuodossa, jonka se toteuttaa käyttäen Tile-olioita miinaharavaruudukon luomiseen.

```mermaid
classDiagram
    direction TB
    class Level{
        level_map: list
    }
    class Tile{
        digit: int
        opened: bool
        flagged: bool
    }
    Level "1" -- "*" Tile
```

Kun käyttäjä klikkaa peliruudukon ruutua, Level-luokka etsii klikatuissa koordinaateissa sijaitsevan Tile-olion, ja merkitsee sen avatuksi:

```mermaid
sequenceDiagram
    actor User
    participant GameLoop
    participant Level
    participant Tile
    
    User ->>+ GameLoop: click unopened tile
    GameLoop ->>+ Level: click((x, y), "left")
    Level ->>+ Tile: rect.collidepoint((x, y))
    Tile -->>- Level: True
    Level ->>+ Tile: open()
    Tile -->>- Level: True
    Level -->>- GameLoop: 
    GameLoop -->>- User: 
```

Tile palauttaa arvon True avaamisen jälkeen osoittaakseen, että se on juuri tällä avaamisyrityksellä avattu ruutu. Tämä on tärkeää tyhjien ruutujen ympäristöjensä avaamisen toiminnan kannalta.
