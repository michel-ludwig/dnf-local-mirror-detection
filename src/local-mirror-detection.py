# DNF plugin for detecting the presence of a (local) package mirror
#
# Copyright (C) 2020 Michel Ludwig
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import dnf
import urllib.request
import json

class LocalMirrorDetection(dnf.Plugin):
    """DNF plugin for detecting the presence of a local mirror."""

    name = 'local-mirror-detection'
    LOCAL_URL_MIRROR_CONFIG_KEY = 'local_mirror_url'

    def __init__(self, base, cli):
        super(LocalMirrorDetection, self).__init__(base, cli)
        self.base = base

    def config(self):
        cp = self.read_config(self.base.conf)
        if not cp.has_section('main') or not cp.has_option('main', self.LOCAL_URL_MIRROR_CONFIG_KEY):
            return

        localmirrorurl = cp.get('main', self.LOCAL_URL_MIRROR_CONFIG_KEY)
        print('Local mirror url:', localmirrorurl)
        #basearch = self.base.conf.substitutions['arch']
        #releasever = self.base.conf.substitutions['releasever']

        iter_obj = self.base.repos.iter_enabled()
        repoDict = {};
        try:
            data = urllib.request.urlopen(localmirrorurl, None, 1).read()
            repoDict = json.loads(data.decode('utf-8'))
            print('Local mirror available')
        except:
            print('Local mirror not available')
            return

        while True:
            try:
                repo = next(iter_obj)
                if repo.id in repoDict:
                    repo.metalink = ''
                    repo.baseurl = [repoDict[repo.id]['url']]
            except StopIteration:
                break

#kate: space-indent on; indent-width 4; mixedindent off;
