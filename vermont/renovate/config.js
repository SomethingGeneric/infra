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
  "repositories": ["matt/website", "matt/GamerbotAgain"],
}
