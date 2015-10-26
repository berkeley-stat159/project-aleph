from __future__ import absolute_import, division, print_function

import tempfile

from .. import data


def test_check_hashes():
    tf = tempfile.NamedTemporaryFile(delete=False)
    fname = tf.name
    with tempfile.NamedTemporaryFile() as temp:
        temp.write('Some data')
        temp.flush()
        fname = temp.name
        d = {fname: "fd733636ae8abe8f0ffbfadedd23896c"}
        data.check_hashes(d)
