
SHELL=/bin/bash

example:
	bashdash --dashboard example2

hub_update:
	@hub_ctrl ${HUB_MODE} ln "$(realpath ./src/bashdash)"
