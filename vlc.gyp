{
  'targets': [
    {
      'target_name': 'vlc',
      'type': 'static_library',
      'defines': [
        'HAVE_CONFIG_H'
      ],
      'include_dirs': [
        'config/<(OS)/<(target_arch)',
        'src',
        'include',
        'include/vlc',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'include',
        ],
      },
      'sources': [
        'src/libvlc.c',
        'src/libvlc.h',
        'src/libvlc-module.c',
        'src/missing.c',
        'src/revision.c',
        'src/version.c',
        'src/interface/dialog.c',
        'src/interface/interface.c',
        'src/playlist/playlist_internal.h',
        'src/playlist/art.c',
        'src/playlist/art.h',
        'src/playlist/aout.c',
        'src/playlist/thread.c',
        'src/playlist/control.c',
        'src/playlist/engine.c',
        'src/playlist/fetcher.c',
        'src/playlist/fetcher.h',
        'src/playlist/sort.c',
        'src/playlist/loadsave.c',
        'src/playlist/preparser.c',
        'src/playlist/preparser.h',
        'src/playlist/tree.c',
        'src/playlist/item.c',
        'src/playlist/search.c',
        'src/playlist/services_discovery.c',
        'src/input/item.c',
        'src/input/access.c',
        'src/input/clock.c',
        'src/input/control.c',
        'src/input/decoder.c',
        'src/input/decoder_synchro.c',
        'src/input/demux.c',
        'src/input/es_out.c',
        'src/input/es_out_timeshift.c',
        'src/input/event.c',
        'src/input/input.c',
        'src/input/info.h',
        'src/input/meta.c',
        'src/input/access.h',
        'src/input/clock.h',
        'src/input/decoder.h',
        'src/input/demux.h',
        'src/input/es_out.h',
        'src/input/es_out_timeshift.h',
        'src/input/event.h',
        'src/input/item.h',
        'src/input/stream.h',
        'src/input/input_internal.h',
        'src/input/input_interface.h',
        'src/input/vlm_internal.h',
        'src/input/vlm_event.h',
        'src/input/vlm.c',
        'src/input/vlm_event.c',
        'src/input/vlmshell.c',
        'src/input/resource.h',
        'src/input/resource.c',
        'src/input/stats.c',
        'src/input/stream.c',
        'src/input/stream_demux.c',
        'src/input/stream_filter.c',
        'src/input/stream_memory.c',
        'src/input/subtitles.c',
        'src/input/var.c',
        'src/video_output/chrono.h',
        'src/video_output/control.c',
        'src/video_output/control.h',
        'src/video_output/display.c',
        'src/video_output/display.h',
        'src/video_output/event.h',
        'src/video_output/inhibit.c',
        'src/video_output/inhibit.h',
        'src/video_output/interlacing.c',
        'src/video_output/interlacing.h',
        'src/video_output/snapshot.c',
        'src/video_output/snapshot.h',
        'src/video_output/statistic.h',
        'src/video_output/video_output.c',
        'src/video_output/video_text.c',
        'src/video_output/video_epg.c',
        'src/video_output/video_widgets.c',
        'src/video_output/vout_subpictures.c',
        'src/video_output/window.c',
        'src/video_output/window.h',
        'src/video_output/opengl.c',
        'src/video_output/vout_intf.c',
        'src/video_output/vout_internal.h',
        'src/video_output/vout_control.h',
        'src/video_output/vout_wrapper.c',
        'src/audio_output/aout_internal.h',
        'src/audio_output/common.c',
        'src/audio_output/dec.c',
        'src/audio_output/filters.c',
        'src/audio_output/output.c',
        'src/audio_output/volume.c',
        'src/network/getaddrinfo.c',
        'src/network/io.c',
        'src/network/tcp.c',
        'src/network/udp.c',
        'src/network/rootbind.c',
        'src/network/tls.c',
        'src/text/charset.c',
        'src/text/strings.c',
        'src/text/unicode.c',
        'src/text/url.c',
        'src/text/filesystem.c',
        'src/text/iso_lang.c',
        'src/text/iso-639_def.h',
        'src/misc/md5.c',
        'src/misc/probe.c',
        'src/misc/rand.c',
        'src/misc/mtime.c',
        'src/misc/block.c',
        'src/misc/fifo.c',
        'src/misc/fourcc.c',
        'src/misc/es_format.c',
        'src/misc/picture.c',
        'src/misc/picture_fifo.c',
        'src/misc/picture_pool.c',
        'src/modules/modules.h',
        'src/modules/modules.c',
        'src/modules/bank.c',
        'src/modules/cache.c',
        'src/modules/entry.c',
        'src/modules/textdomain.c',
        'src/misc/threads.c',
        'src/misc/cpu.c',
        'src/misc/epg.c',
        'src/misc/exit.c',
        'src/config/configuration.h',
        'src/config/core.c',
        'src/config/chain.c',
        'src/config/file.c',
        'src/config/help.c',
        'src/config/intf.c',
        'src/config/keys.c',
        'src/config/cmdline.c',
        'src/config/getopt.c',
        'src/config/vlc_getopt.h',
        'src/misc/events.c',
        'src/misc/image.c',
        'src/misc/messages.c',
        'src/misc/mime.c',
        'src/misc/objects.c',
        'src/misc/variables.h',
        'src/misc/variables.c',
        'src/misc/error.c',
        'src/misc/update.h',
        'src/misc/update.c',
        'src/misc/update_crypto.c',
        'src/misc/xml.c',
        'src/extras/libc.c',
        'src/extras/tdestroy.c',
        'src/misc/addons.c',
        'src/misc/filter.c',
        'src/misc/filter_chain.c',
        'src/misc/http_auth.c',
        'src/misc/httpcookies.c',
        'src/misc/fingerprinter.c',
        'src/misc/text_style.c',
        'src/misc/subpicture.c',
        'src/misc/subpicture.h',
        'src/stream_output/stream_output.c',
        'src/stream_output/stream_output.h',
        'src/stream_output/sap.c',
        'src/stream_output/sdp.c',
        'compat/strlcpy.c',
      ],
      'conditions': [
        ['OS == "linux"', {
          'sources': [
            'posix/dirs.c',
            'posix/error.c',
            'posix/filesystem.c',
            'posix/netconf.c',
            'posix/plugin.c',
            'posix/thread.c',
            'posix/timer.c',
            'posix/linux_cpu.c',
            'posix/linux_specific.c',
            'posix/specific.c',
            'posix/rand.c',
          ],
          'link_settings': {
            'libraries': [
              '-lrt',
            ],
          },
        }],
        ['OS == "mac"', {
          'sources': [
            'darwin/dirs.c',
            'posix/filesystem.c',
            'posix/plugin.c',
            'darwin/thread.c',
            'posix/timer.c',
            'darwin/specific.c',
            'posix/rand.c',
            'darwin/error.c',
            'darwin/netconf.c',
          ],
        }],
        ['OS == "win"', {
          'sources': [
          	'win32/dirs.c',
            'win32/error.c',
            'win32/filesystem.c',
            'win32/netconf.c',
            'win32/plugin.c',
            'win32/thread.c',
            'win32/specific.c',
            'win32/winsock.c',
            'win32/rand.c',
          ],
        }],
      ],
    },
  ],
}