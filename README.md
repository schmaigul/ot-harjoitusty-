**Helsingin Yliopiston** kurssi ohjelmistotekniikka (5 ECTS)

# TypingTest

Sovelluksella voit testata kuinka nopea olet kirjoittamaan tietokoneen näppäimistöllä, antaen reaaliajassa tilastoja etenemisestäsi.

## Dokumentaatio

[Vaatimuusmäärittely](/dokumentaatio/vaatimusm%C3%A4%C3%A4rittely.md)

[Työaikakirjanpito](/dokumentaatio/ty%C3%B6aikakirjanpito.md)

[Changelog](/dokumentaatio/changelog.md)

[Arkkitehtuurikuvaus](/dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Asenna riippuvuudet komennolla:

``poetry install``

2. Käynnistä sovellus komennolla

``poetry run invoke start``

## Komentorivitoiminnot

# Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

``poetry run invoke start``

# Testaus

Testit suoritetaan komennolla

``poetry run invoke test``

# Testikattavuus

Testikattavuus generoidaan komennolla

``poetry run invoke coverage-report``

# Pylint

Tiedoston [.pylintrc](./TypingTest/.pylintrc) määritelmät tarkistukset onnistuu komennolla:

```poetry run invoke lint``


