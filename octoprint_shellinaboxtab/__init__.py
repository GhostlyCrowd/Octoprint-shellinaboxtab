# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class shellinaboxtabPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin):
	def on_after_startup(self):
		self._logger.info("Shell In A Box TAB (more: %s)" % self._settings.get(["url"]))

	def get_settings_defaults(self):
		return dict(url="https://octoprint.local:4200")

	def get_template_configs(self):
		return [
			#dict(type="navbar", custom_bindings=False),
			dict(type="settings", custom_bindings=False)
		]

	def get_assets(self):
		return dict(
			js=["js/shellinaboxtab.js"],
			css=["css/shellinaboxtab.css"],
			less=["less/shellinaboxtab.less"]
		)

__plugin_name__ = "Shell In A Box TAB"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = shellinaboxtabPlugin()
