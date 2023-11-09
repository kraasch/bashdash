
SHELL=/bin/bash

example:
	bashdash --dashboard example

hub_update:
	@hub_ctrl ${HUB_MODE} ln "$(realpath ./src/bashdash)"
