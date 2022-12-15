# Käyttöohje

Lataa projektin viimeisimmän releasen lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

## Konfigurointi

Pysyväistallennukseen käytettävien tiedostojen nimiä voi halutessaan muuttaa TypingTest-hakemistossa _.env_-tiedostossa. Tiedostot luodaan automaattisesti _data_-hakeistoon, jos niitä ei siellä vielä ole. Tiedoston muoto on seuraava:

```
USER_DATABASE_FILENAME=users.sqlite
STATISTIC_DATABASE_FILENAME=statistics.sqlite
```

## Ohjelman käynnistäminen

Latauksen jälkeen, navigoi TypingTest-hakemistoon ja asenna riippuvuudet komennolla

```bash
poetry install
```

Jonka jälkeen projektin alustus hoituu komenolla:

```bash
poetry run invoke build
```

Tämän jälkeen voit käynnistää ohjelman komennolla:

```bash
poetry run invoke start
```

## Kirjautuminen

Ohjelman ensimmäinen näkymä on kirjautumisnäkymä. Kirjautuminen onnistuu kirjoittamalla olemassaoleva käyttäjätunnus ja salasana ja painamalla "login".

![kirjautumisnäkymä](kuvat/kirjautumisn%C3%A4kym%C3%A4.png)

## Uuden käyttäjän luominen

Kirjautumisnäkymästä on mahdollista siirtyä uuden käyttäjän luomiseen painamalla "create user". Uusi käyttäjä luodaan kirjoittamalla käyttäjätunnus ja salasana syötekenttiin ja painamalla "create user"-nappia.

![käyttäjän luominen](kuvat/k%C3%A4ytt%C3%A4j%C3%A4nluomisn%C3%A4kym%C3%A4.png)

Jos luominen onnnistuu, siirrytään takaisin kirjautumisnäkymään.

## Päävalikko

Kirjauduttuaan käyttäjä siirretään päävalikkonäkymään. Päävalikossa käyttäjä voi aloittaa uuden kirjoitusharjoituksen painamalla "Start a typing test", katsella tilastojaan painamalla "Statistics", tai kirjautua ulos painamalla "Logout".

![päävalikko](kuvat/p%C3%A4%C3%A4valikko.png)

## Kirjoitusharjoitus

Käyttäjä siirretään TypingTest-näkymään päävalikosta painettuaan "Start a typing test". Kirjoitusharjoitusnäkymä antaa käyttäjälle esimerkkilauseen joka käyttäjän tulee kirjoittaa syötekentälle. Käyttäjälle annetaan visuaalisia vihjeitä kirjoituksen oikeudesta, ja reaaliakaisia tilastoja. Käyttäjän voi siirtyä milloin vain takaisin päävalikkoon painamalla "Main menu"-nappia.

![kirjoitusharjoitus](kuvat/harjoitusn%C3%A4kym%C3%A4.png)

## Kirjoitusharjoituksen loppuminen

Kirjoitusharjoituksen loppuesssa käyttäjälle näytetään tilastoja suorituksesta, ja mahdollisuus aloittaa uusi harjoitus tai palata päävalikkoon

![harjoituksen loppu](kuvat/lopputilaston%C3%A4kym%C3%A4.png)

## Kokonaistilastojen katsominen

Käyttäjä voi tarkistella kokonaistilastojaan päävalikosta painamalla "Statistics"-nappia. Käyttäjä siirretään uuteen näkymään, jossa on listattu erinäisiä koottuja tilastoja aikasemmin suoritetuista kirjoitusharjoituksista. Käyttäjä voi palata päävalikkoon painamalla "Main menu"-painiketta.

![kokonaistilastot](kuvat/kokonaistilaston%C3%A4kym%C3%A4.png)