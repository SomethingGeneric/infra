module.exports = {
  "platform": "gitea",
  "endpoint": "https://git.goober.cloud/",
  "gitAuthor": "Renovate Bot <matt@get.bent.lol>",
  "autodiscover": true,
  "autodiscoverFilter": ["matt/*"],
  "onboardingConfig": {
  	"$schema": "https://docs.renovatebot.com/renovate-schema.json",
  	"extends": ["config:recommended"]
  },
  "optimizeForDisabled": true,
  "persistRepoData": true,
  "dependencyDashboard": true,
  "ignoreTests": false,
  "automerge": true,
  "automergeType": "branch",
  "platformAutomerge": true,
  "prCreation": "immediate",
  "stabilityDays": 0,
  "repositories": ["Ramon/nvim", "dizzybox/core", "dizzybox/website", "dizzybox/branding", "dizzybox/todo", "gort/website", "gort/suckless", "matt/ShushMonitor", "matt/emailbuddy", "matt/mediawiki-to-gfm", "matt/flaskforms", "matt/emailscript", "matt/pysubsonic", "matt/suckless", "matt/slstatus", "matt/forgejo-scripts", "matt/submarine", "matt/hpscoreboard", "matt/tumblrosint", "matt/goobot", "matt/OpenAssistant", "matt/nvim-dotfiles", "matt/yoink-nvim", "matt/mullvad-vpn-bin-fixed", "matt/ai-mealdelivery", "matt/pyrat", "matt/bankman", "matt/iss-tracker", "matt/autoaur", "matt/pqmgmt", "matt/gamerthemail", "matt/SYS320-01", "matt/sec335-scripts", "matt/forgejo-docker-stack", "matt/BetterMoneyPrinter", "dizzybox/core", "dizzybox/website", "dizzybox/branding", "dizzybox/todo", "goobercloud/website", "ikeda/pacbuild", "ikeda/pkgs", "larch/archiso", "larch/lt", "larch/iso"],
}
