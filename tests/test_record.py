# coding=utf-8

import flarmnet


def test_record_decryption():
    line = '4637383339374c46205376e67665666c7976656b6c756220202020454b4d' \
           '422020202020202020202020202020202020484b33362053757065722044' \
           '696d6f6e61202020204f592d4d5842202020203133302e353735'

    record = flarmnet.Record(line)

    assert record.id == 'F78397'
    assert record.pilot == u'LF Svæveflyveklub'
    assert record.airfield == u'EKMB'
    assert record.plane_type == u'HK36 Super Dimona'
    assert record.registration == u'OY-MXB'
    assert record.competition_id is None
    assert record.radio_frequency == u'130.575'

