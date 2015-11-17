#!/bin/env python3

# Copyright 2015 wink saville
#
# licensed under the apache license, version 2.0 (the "license");
# you may not use this file except in compliance with the license.
# you may obtain a copy of the license at
#
#     http://www.apache.org/licenses/license-2.0
#
# unless required by applicable law or agreed to in writing, software
# distributed under the license is distributed on an "as is" basis,
# without warranties or conditions of any kind, either express or implied.
# see the license for the specific language governing permissions and
# limitations under the license.

import subprocess
import sys

app = '../build/hello'

output = subprocess.check_output([app, '--version'],
                stderr=subprocess.STDOUT)

expected = b'Hello, World!\n'
if output != expected:
    print('Err:   output =', output)
    print('     expected =', expected)
    retVal = 1
else:
    print('OK')
    retVal = 0

sys.exit(retVal)
