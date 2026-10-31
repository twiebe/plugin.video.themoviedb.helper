from jurialmunkey.ftools import cached_property


class TMDbImagePath:

    @cached_property
    def artwork_quality(self):
        from tmdbhelper.lib.addon.plugin import get_setting
        return get_setting('artwork_quality', 'int')

    @cached_property
    def poster_quality(self):
        from tmdbhelper.lib.addon.plugin import get_setting
        return get_setting('poster_quality', 'int')

    @cached_property
    def screen_height(self):
        from xbmcgui import getScreenHeight
        return getScreenHeight()

    @cached_property
    def artwork_quality_poster_artwork(self):
        from tmdbhelper.lib.addon.consts import IMAGEPATH_QUALITY_POSTER
        return IMAGEPATH_QUALITY_POSTER[self.artwork_quality]

    @cached_property
    def artwork_quality_poster_small(self):
        from tmdbhelper.lib.addon.consts import IMAGEPATH_SMALLPOSTER
        return IMAGEPATH_SMALLPOSTER

    @cached_property
    def artwork_quality_poster_auto(self):
        return self.get_artwork_quality_poster_auto()

    def get_artwork_quality_poster_auto(self):
        from tmdbhelper.lib.addon.consts import IMAGEPATH_SMALLPOSTER_MAXHEIGHT
        if self.screen_height > IMAGEPATH_SMALLPOSTER_MAXHEIGHT:
            return self.artwork_quality_poster_artwork
        return self.artwork_quality_poster_small

    poster_quality_attributes = (
        'artwork_quality_poster_auto',
        'artwork_quality_poster_small',
        'artwork_quality_poster_artwork',
    )

    @cached_property
    def artwork_quality_poster(self):
        return getattr(self, self.poster_quality_attributes[self.poster_quality])

    @cached_property
    def artwork_quality_fanart(self):
        from tmdbhelper.lib.addon.consts import IMAGEPATH_QUALITY_FANART
        return IMAGEPATH_QUALITY_FANART[self.artwork_quality]

    @cached_property
    def artwork_quality_thumbs(self):
        from tmdbhelper.lib.addon.consts import IMAGEPATH_QUALITY_THUMBS
        return IMAGEPATH_QUALITY_THUMBS[self.artwork_quality]

    @cached_property
    def artwork_quality_clogos(self):
        from tmdbhelper.lib.addon.consts import IMAGEPATH_QUALITY_CLOGOS
        return IMAGEPATH_QUALITY_CLOGOS[self.artwork_quality]

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
