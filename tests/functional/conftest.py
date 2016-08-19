# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

VIEWPORT = {
    'desktop': {'width': 1280, 'height': 1024},
    'mobile': {'width': 320, 'height': 480}}

@pytest.fixture(scope='session')
def session_capabilities(session_capabilities):
    session_capabilities.setdefault('tags', []).append('kuma')
    return session_capabilities

@pytest.fixture
def selenium(request, selenium):
    viewport = VIEWPORT['desktop']
    if request.keywords.get('viewport') is not None:
        viewport = VIEWPORT[request.keywords.get('viewport').args[0]]
    selenium.set_window_size(viewport['width'], viewport['height'])
    return selenium
