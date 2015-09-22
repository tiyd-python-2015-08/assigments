import pytest
xfail = pytest.mark.xfail

import textminer.validator as v


@xfail
def test_binary_numbers():
    assert v.binary("0")
    assert v.binary("1")
    assert v.binary("01")
    assert v.binary("10")
    assert v.binary("1110100010")
    assert not v.binary("")
    assert not v.binary("911")


@xfail
def test_binary_even():
    """String must be a binary number and be even."""

    assert v.binary_even("10")
    assert v.binary_even("1110100010")
    assert not v.binary_even("1011")


@xfail
def test_hexadecimal():
    assert v.hex("CAFE")
    assert v.hex("9F9")
    assert v.hex("123")
    assert v.hex("6720EB3A9D1")
    assert not v.hex("")
    assert not v.hex("COFFEE")


@xfail
def test_word():
    assert v.word("hello")
    assert v.word("wonderful")
    assert v.word("zyggon")
    assert v.word("horse-dagger")
    assert v.word("18-wheeler")
    assert not v.word("")
    assert not v.word("12")
    assert not v.word("!!!")
    assert not v.word("bar*us")


@xfail
def test_words():
    """words can take an optional count argument. In case it exists, the text
    must match that number of words."""
    assert v.words("hello")
    assert v.words("hello world")
    assert v.words("raggggg hammer dog")
    assert v.words("18-wheeler tarbox")
    assert v.words("hello", count=1)
    assert v.words("hello world", count=2)
    assert v.words("raggggg hammer dog", count=3)
    assert v.words("18-wheeler tarbox", count=2)
    assert not v.words("")
    assert not v.words("12")
    assert not v.words("hey !!!", count=2)
    assert not v.words("bar*us w!zard", count=2)
    assert not v.words("hello", count=2)
    assert not v.words("hello world", count=3)
    assert not v.words("raggggg hammer dog", count=1)
    assert not v.words("18-wheeler tarbox", count=3)


@xfail
def test_phone_numbers():
    """US phone numbers only."""

    assert v.phone_number("919-555-1212")
    assert v.phone_number("(919) 555-1212")
    assert v.phone_number("9195551212")
    assert v.phone_number("919.555.1212")
    assert v.phone_number("919 555-1212")
    assert not v.phone_number("")
    assert not v.phone_number("555-121")
    assert not v.phone_number("1212")
    assert not v.phone_number("mobile")


@xfail
def test_money():
    """We are just concerned with dollars here."""

    assert v.money("$4")
    assert v.money("$19")
    assert v.money("$19.00")
    assert v.money("$3.58")
    assert v.money("$1000")
    assert v.money("$1000.00")
    assert v.money("$1,000")
    assert v.money("$1,000.00")
    assert v.money("$5,555,555")
    assert v.money("$5,555,555.55")
    assert v.money("$45,555,555.55")
    assert v.money("$456,555,555.55")
    assert v.money("$1234567.89")
    assert not v.money("")
    assert not v.money("$12,34")
    assert not v.money("$1234.9")
    assert not v.money("$1234.999")
    assert not v.money("$")
    assert not v.money("31")
    assert not v.money("$$31")


@xfail
def test_zip():
    assert v.zipcode("63936")
    assert v.zipcode("50583")
    assert v.zipcode("48418")
    assert v.zipcode("06399")
    assert v.zipcode("26433-3235")
    assert v.zipcode("64100-6308")
    assert not v.zipcode("")
    assert not v.zipcode("7952")
    assert not v.zipcode("115761")
    assert not v.zipcode("60377-331")
    assert not v.zipcode("8029-3924")


@xfail
def test_date():
    assert v.date("9/4/1976")
    assert v.date("1976-09-04")
    assert v.date("2015-01-01")
    assert v.date("02/15/2004")
    assert not v.date("9/4")
    assert not v.date("2015")


## HARD MODE BEGINS


@xfail
def test_hard_date():
    assert v.date("2014 Jan 01")
    assert v.date("2014 January 01")
    assert v.date("Jan. 1, 2015")
    assert not v.date("07/40/2015")
    assert not v.date("02/30/2015")


@xfail
def test_email():
    """Some of the emails listed as invalid are actually valid according to
    the email spec, but we will not accept them."""

    assert v.email("stroman.azariah@yahoo.com")
    assert v.email("viola91@gmail.com")
    assert v.email("eathel.west@example.org")
    assert v.email("dwehner@harley.us")
    assert v.email("malcolm.haley@hotmail.com")
    assert v.email("ezzard90@hotmail.com")
    assert v.email("legros.curley@gmail.com")
    assert v.email("leatha75@mertz.net")
    assert v.email("bonita43@yahoo.com")
    assert not v.email("")
    assert not v.email("legros.curley")
    assert not v.email("mertz.net")
    assert not v.email("bonita43@")


@xfail
def test_address():
    """This must be a full address with street number, street, city, state,
    and ZIP code. Again, US-only."""
    assert v.address("""368 Agness Harbor
    Port Mariah, MS 63293""")
    assert v.address("""96762 Juluis Road Suite 392
    Lake Imogenemouth, AK 20211""")
    assert v.address("""671 Tawnya Island Apt. 526
    Clementeburgh, AK 82652""")
    assert v.address("""568 Eunice Shoals
    Parishaven, AK 09922-2288""")
    assert v.address("8264 Schamberger Spring, Jordanside, MT 98833-0997")

    assert not v.address("")
    assert not v.address("99132 Kaylah Union Suite 301")
    assert not v.address("Lake Joellville, NH")
    assert not v.address("35981")
