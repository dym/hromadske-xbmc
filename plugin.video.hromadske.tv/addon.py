from xbmcswift2 import Plugin
from resources.lib.hromadske import scraper


plugin = Plugin()


@plugin.route('/')
def index():
    video_id = scraper.get_online_video_id()
    item = {
        'label': 'Online',
        'path': plugin.url_for('play_video', video_id=video_id),
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
