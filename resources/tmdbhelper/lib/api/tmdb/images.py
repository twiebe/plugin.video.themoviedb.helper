from jurialmunkey.ftools import cached_property


class TMDbImagePath:

    @cached_property
    def artwork_quality(self):
        from tmdbhelper.lib.addon.plugin import get_setting
        return get_setting('artwork_quality', 'int')

    def get_artwork_quality(self, artwork_type):
        from tmdbhelper.lib.addon.plugin import get_setting
        quality = get_setting(f'artwork_quality_{artwork_type}', 'int')
        return self.artwork_quality if quality == -1 else quality

    @cached_property
    def screen_height(self):
        from xbmcgui import getScreenHeight
        return getScreenHeight()

    def get_artwork_quality_poster_auto(self):
        from tmdbhelper.lib.addon.consts import IMAGEPATH_QUALITY_POSTER, IMAGEPATH_SMALLPOSTER, IMAGEPATH_SMALLPOSTER_MAXHEIGHT
        if self.screen_height > IMAGEPATH_SMALLPOSTER_MAXHEIGHT:
            return IMAGEPATH_QUALITY_POSTER[self.artwork_quality]
        return IMAGEPATH_SMALLPOSTER

    def get_artwork_quality_poster(self):
        from tmdbhelper.lib.addon.consts import IMAGEPATH_QUALITY_POSTER, IMAGEPATH_QUALITY_POSTER_AUTO
        quality = self.get_artwork_quality('poster')
        if quality == IMAGEPATH_QUALITY_POSTER_AUTO:
            return self.get_artwork_quality_poster_auto()
        return IMAGEPATH_QUALITY_POSTER[quality]

    @cached_property
    def artwork_quality_poster(self):
        return self.get_artwork_quality_poster()

    @cached_property
    def artwork_quality_fanart(self):
        from tmdbhelper.lib.addon.consts import IMAGEPATH_QUALITY_FANART
        return IMAGEPATH_QUALITY_FANART[self.get_artwork_quality('fanart')]

    @cached_property
    def artwork_quality_thumbs(self):
        from tmdbhelper.lib.addon.consts import IMAGEPATH_QUALITY_THUMBS
        return IMAGEPATH_QUALITY_THUMBS[self.artwork_quality]

    @cached_property
    def artwork_quality_clogos(self):
        from tmdbhelper.lib.addon.consts import IMAGEPATH_QUALITY_CLOGOS
        return IMAGEPATH_QUALITY_CLOGOS[self.artwork_quality]

    @cached_property
    def profile_quality(self):
        from tmdbhelper.lib.addon.plugin import get_setting
        return get_setting('profile_quality', 'int')

    @cached_property
    def artwork_quality_profile_small(self):
        from tmdbhelper.lib.addon.consts import IMAGEPATH_SMALLPROFILE
        return IMAGEPATH_SMALLPROFILE

    @cached_property
    def artwork_quality_profile_auto(self):
        return self.get_artwork_quality_profile_auto()

    def get_artwork_quality_profile_auto(self):
        from tmdbhelper.lib.addon.consts import IMAGEPATH_SMALLPROFILE_MAXHEIGHT
        if self.screen_height > IMAGEPATH_SMALLPROFILE_MAXHEIGHT:
            return self.artwork_quality_poster
        return self.artwork_quality_profile_small

    profile_quality_attributes = (
        'artwork_quality_profile_auto',
        'artwork_quality_profile_small',
        'artwork_quality_poster',
    )

    @cached_property
    def artwork_quality_profile(self):
        return getattr(self, self.profile_quality_attributes[self.profile_quality])

    @cached_property
    def artwork_quality_origin(self):
        from tmdbhelper.lib.addon.consts import IMAGEPATH_ORIGINAL
        return IMAGEPATH_ORIGINAL

    @cached_property
    def artwork_quality_negate(self):
        from tmdbhelper.lib.addon.consts import IMAGEPATH_NEGATE
        return IMAGEPATH_NEGATE

    def get_imagepath_poster(self, v):
        if not v:
            return ''
        return f'{self.artwork_quality_poster}{v}'

    def get_imagepath_profile(self, v):
        if not v:
            return ''
        return f'{self.artwork_quality_profile}{v}'

    def get_imagepath_fanart(self, v):
        if not v:
            return ''
        return f'{self.artwork_quality_fanart}{v}'

    def get_imagepath_thumbs(self, v):
        if not v:
            return ''
        return f'{self.artwork_quality_thumbs}{v}'

    def get_imagepath_clogos(self, v):
        if not v:
            return ''
        return f'{self.artwork_quality_clogos}{v}'

    def get_imagepath_negate(self, v):
        if not v:
            return ''
        return f'{self.artwork_quality_negate}{v}'

    def get_imagepath_origin(self, v):
        if not v:
            return ''
        return f'{self.artwork_quality_origin}{v}'
