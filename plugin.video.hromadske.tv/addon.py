from xbmcswift2 import Plugin


plugin = Plugin()


@plugin.route('/')
def index():
    item = {
        'label': 'Online',
        'path': plugin.url_for('play_video', video_id='iVGXapcHcMc'),
        'is_playable': True
    }
    return [item]


@plugin.route('/video/<video_id>/')
def play_video(video_id):
    url = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % video_id
    plugin.log.info('Playing url: %s' % url)
    plugin.set_resolved_url(url)


if __name__ == '__main__':
    plugin.run()
