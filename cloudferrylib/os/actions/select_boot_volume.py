from cloudferrylib.base.action import action
import utils


class SelectBootVolume(action.Action):

    def run(self, info=None, **kwargs):
        info_boot = utils.select_boot_volume(info)
        return {
            'info': info_boot
        }

